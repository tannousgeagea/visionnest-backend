from django.contrib import admin
from .models import Workspace
from .models import Dataset

class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['workspace_name', 'workspace_description', 'created_at']
    list_filter = ['workspace_name']
    
class DatasetAdmin(admin.ModelAdmin):
    list_display = ['workspace', 'image_id', 'image_file', 'created_at', 'annotated', 'annotation', 'processed', 'mode']
    list_filter = ['workspace', 'annotated', 'mode']
    
# Register your models here.
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Dataset, DatasetAdmin)