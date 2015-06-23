from django.core.urlresolvers import reverse
from django.db import models
from taggit.managers import TaggableManager
from django.forms import ModelForm
# Create your models here.


class Reason(models.Model):
    """
    Main reason
    """

    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    tags = TaggableManager()


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('reason_item', args=[self.id])


class ReasonForm(ModelForm):
    class Meta:
        model = Reason
        fields = ['title','description','tags']