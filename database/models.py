from django.db import models

# Create your models here.
class Workspace(models.Model):
    workspace_name = models.CharField(max_length=255)
    workspace_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workspace'
        verbose_name_plural = 'Workspace'
        
    def __str__(self) -> str:
        return self.workspace_name
    
class Dataset(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    image_id = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    annotated = models.BooleanField(default=False)
    annotation = models.FileField(upload_to='labels/')
    processed = models.BooleanField(default=False)
    mode = models.CharField(max_length=255, default='N/A')
    
    class Meta:
        db_table = 'dataset'
        verbose_name_plural = 'Dataset'
        
    def __str__(self) -> str:
        return self.image_file.url
    
    