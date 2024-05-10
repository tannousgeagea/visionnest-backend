import os
import django
import shutil
django.setup()

from django.conf import settings
from database.models import Dataset

media = settings.MEDIA_ROOT

def save_images_in_database(files):
    pass
            