from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField

from metlabs.blog.managers import PublishedManager


CONTENT_SEPARATOR = "<!-- split -->"


class Author(models.Model):
    full_name = models.CharField(_("Name"), max_length=255)
    short_bio = models.TextField(blank=True, null=True)
    github_username = models.CharField(max_length=255, blank=True)
    twitter_username = models.CharField(max_length=255, blank=True)
    blog_url = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="files", blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.full_name)


class Post(models.Model):
    """
    Holds blog post data.
    """
    title = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    content = MarkupField(_("Content"))
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_published = models.BooleanField(_("Published"), default=True)
    author = models.ForeignKey(Author, blank=True, null=True)

    objects = models.Manager()
    published_objects = PublishedManager()

    class Meta:
        ordering = ("-date_created", )

    def __unicode__(self):
        return smart_unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return "blog_detail", [self.slug]

    def get_description(self, separator=CONTENT_SEPARATOR):
        """Returns the description part of a full text"""
        return mark_safe(self.content.rendered.split(separator)[0])
