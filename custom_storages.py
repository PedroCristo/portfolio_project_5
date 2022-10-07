from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Tells Django that in production mode use S3 to store the static files
    """

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Tells Django that in production mode use S3 to store the media files
    """

    location = settings.MEDIAFILES_LOCATION
