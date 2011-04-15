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
    summary = models.TextField(blank=True)
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

    @models.permalink
    def get_absolute_url(self):
        return ('simplenews:news_detail', [self.slug,])

    @property
    def image(self):
        """Added property to keep backwards compatibility"""
        if hasattr(self, '_image_cached'):
            return self._image_cached
        try:
            image = self.articleimage_set.filter(
                position=ArticleImage.TOP)[0]
            self._image_cached = image.image
            return self._image_cached
        except IndexError:
            pass
        return None

    @property
    def image_top(self):
        """Top image on this article"""
        if hasattr(self, '_image_top'):
            return self._image_top
        try:
            image_top = self.articleimage_set.filter(
                position=ArticleImage.TOP)[0]
            self._image_top = image_top
            return self._image_top
        except IndexError:
            pass
        return None

    @property
    def image_bottom(self):
        """Bottom image on this article"""
        if hasattr(self, '_image_bottom'):
            return self._image_bottom
        try:
            image = self.articleimage_set.filter(
                position=ArticleImage.BOTTOM)[0]
            self._image_bottom = image
            return self._image_bottom
        except IndexError:
            pass
        return None


class ArticleImage(models.Model):
    """Images to be displayed with the Article"""
    TOP = 1
    BOTTOM = 2
    POSITION_CHOICES = ((TOP, _('top')),
                        (BOTTOM, _('bottom')),)
    LANDSCAPE = 1
    PORTRAIT = 2
    ORIENTATION_CHOICES = ((LANDSCAPE, _('landscape')),
                           (PORTRAIT, _('portrait')))
    image = models.ImageField(upload_to="news", blank=True)
    title = models.CharField(blank=True, max_length=255)
    article = models.ForeignKey('simplenews.Article')
    position = models.IntegerField(choices=POSITION_CHOICES)
    orientation = models.IntegerField(choices=ORIENTATION_CHOICES,
                                      editable=False)

    def __unicode__(self):
        return 'Image for %s' % self.article.title

    def save(self, *args, **kwargs):
        if self.image.width > self.image.height:
            self.orientation = self.LANDSCAPE
        else:
            self.orientation = self.PORTRAIT
        super(ArticleImage, self).save(*args, **kwargs)

    @property
    def is_landscape(self):
        return self.orientation == self.LANDSCAPE

    @property
    def is_portrait(self):
        return self.orientation == self.PORTRAIT
