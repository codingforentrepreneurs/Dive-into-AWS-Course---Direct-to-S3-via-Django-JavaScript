from storages.backends.s3boto3 import S3Boto3Storage


# static/
StaticS3Storage = lambda: S3Boto3Storage(location='static')

# media/
MediaS3Storage = lambda: S3Boto3Storage(location='media')