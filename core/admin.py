from django.contrib import admin
from core.models import Project, Revolver
from core.forms import ProjectForm

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    #fields display on change list
    list_display = ['title','owner','author','created','published']
    #fields to filter the change list with
    list_filter = ['published','created']
    #fields to search in change list
    search_fields = ['title','content']
    #enable the date drill down on change list
    date_hierarchy = 'created'
    #enable the save buttons on top of change form
    save_on_top = True
    # #prepopulate the slug from the title
    # prepopulated_fields = {"slug":("title",)}
    
class RevolverAdmin(admin.ModelAdmin):
    list_display = ['user']
    save_on_top = True

admin.site.register(Project,ProjectAdmin)
admin.site.register(Revolver,RevolverAdmin)
