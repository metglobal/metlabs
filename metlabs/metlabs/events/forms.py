from django import forms
from django.utils.translation import ugettext_lazy as _

from metlabs.events.models import Attendee, Proposal


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Attendee
        exclude = ("event", )

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop("event", None)
        super(EventRegistrationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        if self.event.attendees.filter(email=email).exists():
            raise forms.ValidationError(_('A registration with that email '
                                          'already exists'))
        return self.cleaned_data

    def save(self, commit=True):
        self.instance.event = self.event
        return super(EventRegistrationForm, self).save(commit)


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ('session', )
