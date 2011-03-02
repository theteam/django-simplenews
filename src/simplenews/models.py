from django.db import models
from django.utils.translation import ugettext as _

from djqmgr import QManager
from django_extensions.db.fields import CreationDateTimeField,\
     ModificationDateTimeField, AutoSlugField

class Article(models.Model):
    """News articles"""
    LIVE = 1
    HIDDEN = 2
    REMOVED = 3
    STATUS_CHOICES = ((LIVE, _('Live')),
                      (HIDDEN, _('Hidden')),
                      (REMOVED, _('Removed')),
                      )
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(blank=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=LIVE)
    is_featured = models.BooleanField(default=False)
    url = models.URLField(verify_exists=False, blank=True)

    # managers
    objects = models.Manager()
    live = QManager(status=LIVE)

    def __unicode__(self):
        return u'Article: %s ' % self.title
