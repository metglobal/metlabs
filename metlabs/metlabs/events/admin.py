from django import forms
from django.contrib import admin

from metlabs.events.models import Event, Attendee, Session, Proposal


class EventForm(forms.ModelForm):
    class Meta:
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 3
            })
        }


class SessionInline(admin.StackedInline):
    model = Session
    extra = 0


class EventAdmin(admin.ModelAdmin):
    save_on_top = True
    form = EventForm
    inlines = [SessionInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee)
admin.site.register(Proposal)
