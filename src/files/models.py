from django.conf import settings
from django.db import models

from cfehome.aws.utils import AWS

User = settings.AUTH_USER_MODEL

def user_directory_path(instance, filename):
    # file will be uploaded to bucket/user_<id>/<filename>
    return 's3files/user_{0}/{1}'.format(instance.user.id, filename)


class S3File(models.Model):
    user        = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name        = models.CharField(max_length=220, blank=True, null=True)
    #thumbnail   = models.FileField(upload_to=user_directory_path, blank=True, null=True) # ImageField
    key         = models.TextField() # key path in aws "path"
    filetype    = models.CharField(max_length=120, default='video/mp4')
    uploaded    = models.BooleanField(default=False) # true / false
    active      = models.BooleanField(default=True)  # show in resuls
    size        = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True) # size of file
    duration    = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)# any changes
    timestamp   = models.DateTimeField(auto_now_add=True)# when added
    

    def get_download_url(self):
        key = self.key
        botocfe = AWS()
        return botocfe.get_download_url(key=key, force_download=True, filename='abc.png') #, expires_in=10)









