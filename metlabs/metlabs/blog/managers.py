from django.db import models


class PublishedManager(models.Manager):
    """
    Returns published blog posts.
    """
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set() \
            .filter(is_published=True)
