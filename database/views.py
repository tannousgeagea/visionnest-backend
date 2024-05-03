from django.shortcuts import render
from django.http import JsonResponse
from .models import Dataset, Workspace
# Create your views here.


def read_data(reqeues):
    data = []
    images = Dataset.objects.all()
    
    for image in images:
        data.append(
            {
                'created_at': image.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'image_id': image.image_id,
                'image_url': image.image_file.url,
            }
        )
        
        
    return JsonResponse(data=data, safe=False)