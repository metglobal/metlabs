# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField

from metlabs.events.managers import EventManager
from metlabs.events.constants import SESSION_TYPES, SESSION_TYPE_PRESENTATION, SESSION_TYPE_PLANNING


class Event(models.Model):
    """
    Holds events data
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"))
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    content = MarkupField(_("Content"), blank=True, null=True)
    max_participants = models.IntegerField(_("Max Participants"), default=30)
    address = models.TextField(max_length=255, blank=True, null=True)
    coordinates = models.CharField(max_length=255, blank=True, null=True)

    objects = EventManager()

    class Meta:
        ordering = ["-date"]

    def __unicode__(self):
        return smart_unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return "events_detail", [self.slug]

    def speakers(self):
        return [session.speaker
                for session in
                self.sessions.filter(speaker__isnull=False)]


class Session(models.Model):
    """
    Holds schedule of an event
    """
    event = models.ForeignKey(Event, related_name="sessions")
    start_time = models.TimeField()
    end_time = models.TimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    content = MarkupField(_("Content"), blank=True, null=True)
    session_type = models.IntegerField(choices=SESSION_TYPES,
                                       default=SESSION_TYPE_PRESENTATION)
    speaker = models.ForeignKey('blog.Author', blank=True, null=True,
                                related_name="sessions")

    class Meta:
        ordering = ["start_time"]

    def __unicode__(self):
        return smart_unicode("%s - %s - %s" % (
            self.start_time, self.end_time, self.title))

    @models.permalink
    def get_absolute_url(self):
        return "events_session_detail", [self.event.slug, self.pk]

    def is_planning(self):
        return self.session_type == SESSION_TYPE_PLANNING


class Attendee(models.Model):
    """
    Holds attendees for events
    """
    event = models.ForeignKey(Event, related_name="attendees")
    email = models.EmailField(_("Email"), max_length=255)
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    telephone = models.CharField(_("Telephone"), max_length=255,
                                 blank=True, null=True)

    class Meta:
        unique_together = ("event", "email")

    def __unicode__(self):
        return smart_unicode(self.full_name)

    @property
    def full_name(self):
        return "%(first_name)s %(last_name)s" % {
            "first_name": self.first_name,
            "last_name": self.last_name
        }


class Proposal(models.Model):
    """
    Holds the user-submitted proposals
    """
    session = models.ForeignKey(Session, related_name="proposals")
    email = models.EmailField(_("Email"), max_length=255)
    full_name = models.CharField(_("Ad & Soyad"), max_length=255)
    telephone = models.CharField(_("Telefon"), max_length=255)
    subject = models.CharField(_("Konu"), max_length=255)
    content = models.TextField(_(u"Detaylı Açıklama"), blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.email)
