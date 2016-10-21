from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Revolver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return self.user.get_full_name()
    
    def __unicode__(self):
        return u'%s' % self.user.get_full_name()
    
class Project(models.Model):
    owner = models.ForeignKey(Revolver)
    author = models.CharField(max_length=255,default="Anonymous")
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
def create_revolver(instance, created, raw, **kwargs):
    # Ignore fixtures and saves
    # if not created or raw:
    #     return

    if not hasattr(instance, 'revolver'):
        revolver, _ = Revolver.objects.get_or_create(user=instance)
    #     instance.revolver = revolver
    # 
    # instance.save()

models.signals.post_save.connect(create_revolver, sender=User, dispatch_uid='create_revolver')