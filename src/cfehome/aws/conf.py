import datetime
import os

# IAM User
AWS_USER_NAME = 'GrowthFromZero'
AWS_IAM_GROUP = 'GrowthFromZero_S3_Group'

AWS_ACCESS_KEY_ID = str(os.environ.get(
        'CFEHOME_AWS_ACCESS_ID', 
        'AKIAJROCVCEOOHLZUFWA'
        ))

AWS_SECRET_ACCESS_KEY = str(os.environ.get(
        'CFEHOME_AWS_SECRET_ID', 
        '+3uALqERwjeHZjy/RMqguAUgZZeRRjSUjx4FKPHB'
        ))

## Django-storages
# Media ROOT # to media/ -> static.growthfromzero.com/media/
DEFAULT_FILE_STORAGE = 'cfehome.aws.storages.MediaS3Storage'
# Static Root # static/ -> # static.growthfromzero.com/static/
STATICFILES_STORAGE = 'cfehome.aws.storages.StaticS3Storage'
AWS_STORAGE_BUCKET_NAME = 'static.growthfromzero.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_BUCKET_ACL = None
AWS_AUTO_CREATE_BUCKET = False

days_expires = 61
two_months = datetime.timedelta(days=days_expires)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()))
}

AWS_QUERYSTRING_AUTH = False # sign the url for a static file

AWS_QUERYSTRING_EXPIRE  = 3600
AWS_S3_FILE_OVERWRITE = True
AWS_S3_REGION_NAME = 'us-east-1'

# CDN
AWS_S3_CUSTOM_DOMAIN = 'static.growthfromzero.com'


