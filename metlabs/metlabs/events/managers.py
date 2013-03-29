from django.db import models
from django.utils import timezone


class EventManager(models.Manager):

    def future(self, date=None):
        events = self.get_query_set()
        return events.filter(date__gt=date or timezone.now())
