import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


STATIC_URL = '/static/'

# Production Storage for CSS, JavaScript, Images (aka post-collectstatic)
STATIC_ROOT = os.path.join(
                os.path.dirname(BASE_DIR), 
                'static_cdn', 
                'static'
             )

# Local Storage for CSS, JavaScript, Images (aka pre-collectstatic)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')] 

#URL ROOT for Serving Uploaded Meida (ie ImageField or FileField)
MEDIA_URL = '/media/'

# Storage Location for Uploaded Media (live or local; ImageField and/or FileField)
MEDIA_ROOT = os.path.join(
                os.path.dirname(BASE_DIR), 
                'static_cdn', 
                'media'
                )