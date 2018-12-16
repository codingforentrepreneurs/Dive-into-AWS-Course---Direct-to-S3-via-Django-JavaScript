import boto3
import datetime
from django.conf import settings
# import from elsewhere
# Django "settings" module

AWS_ACCESS_KEY_ID       = getattr(settings, 'AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY   = getattr(settings, 'AWS_SECRET_ACCESS_KEY', None)
AWS_S3_REGION_NAME      = getattr(settings, 'AWS_S3_REGION_NAME', None)
AWS_STORAGE_BUCKET_NAME = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', None)
AWS_OBJECT_DOWNLOAD_HOURS = getattr(settings, 'AWS_OBJECT_DOWNLOAD_HOURS', 1)

if AWS_ACCESS_KEY_ID == None:
    raise NotImplementedError("AWS_ACCESS_KEY_ID must be set in settings")

if AWS_SECRET_ACCESS_KEY == None:
    raise NotImplementedError("AWS_SECRET_ACCESS_KEY must be set in settings")

if AWS_S3_REGION_NAME == None:
    raise NotImplementedError("AWS_S3_REGION_NAME must be set in settings")

if AWS_STORAGE_BUCKET_NAME == None:
    raise NotImplementedError("AWS_STORAGE_BUCKET_NAME must be set in settings")


class AWS:
    access_key      = AWS_ACCESS_KEY_ID
    secret_key      = AWS_SECRET_ACCESS_KEY
    region          = AWS_S3_REGION_NAME
    bucket          = AWS_STORAGE_BUCKET_NAME
    s3_client       = None
    client          = None
    session         = None
    s3_session      = None


    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_session(self):
        if self.session == None:
            session = boto3.Session(
                    aws_access_key_id=self.access_key,
                    aws_secret_access_key=self.secret_key,
                    region_name = self.region
                )
            self.session = session
        return self.session

    def get_client(self, service='s3'):
        if self.client == None:
            client = boto3.client(service,
                    aws_access_key_id=self.access_key,
                    aws_secret_access_key=self.secret_key,
                    region_name = self.region
                )
            self.client = client
        return self.client


    def get_s3_client(self):
        if self.s3_client == None:
            s3_client = self.get_client(service='s3')
            if s3_client is None:
                return None
            self.s3_client = s3_client
        return self.s3_client

    def get_s3_session(self):
        if self.s3_session == None:
            session = self.get_session()
            if session is None:
                return None # Raise some error
            s3_session = session.resource("s3")
            self.s3_session = s3_session
        return self.s3_session

    def get_download_url(self, key=None, force_download=True, filename=None, expires_in=AWS_OBJECT_DOWNLOAD_HOURS):
        '''
        For any key, grab a signed url, that expires
        '''
        if key is None:
            return ""
        s3_client = self.get_s3_client()
        if s3_client is None:
            return ""

        download_args = {}
        if force_download:
            download_args = {
                'ResponseContentType': 'application/force-download'
            }
            if filename is not None:
                download_args['ResponseContentDisposition'] = f'attachment; filename="{filename}"'
        url = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params = {
                    'Bucket': self.bucket,
                    'Key': key,
                    **download_args
                },
                ExpiresIn=datetime.timedelta(hours=expires_in).total_seconds()
                )
        return url

    def presign_post_url(self, key=None, is_public=False):
        acl = 'private'
        if is_public:
            acl = 'public-read'
        fields = {"acl": acl}
        conditions = [
            {"acl": acl}
        ]
        if key is None:
            return ""
        s3_client = self.get_s3_client()
        if s3_client is None:
            return ""
        data = s3_client.generate_presigned_post(
                Bucket = self.bucket,
                Key = key,
                Fields= fields,
                Conditions = conditions
            )
        return data