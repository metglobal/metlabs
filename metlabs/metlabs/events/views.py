from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin

from metlabs.events.models import Event, Session
from metlabs.events.forms import EventRegistrationForm, ProposalForm


class EventView(FormView, SingleObjectMixin):
    model = Event
    template_name = "events/detail.html"
    form_class = EventRegistrationForm

    def get_context_data(self, **kwargs):
        """
        Adds the current object into context data
        """
        self.object = self.get_object()
        return super(EventView, self).get_context_data(
            object=self.object,
            proposal_form=ProposalForm(),
            **kwargs)

    def get_form(self, form_class):
        event = self.get_object()
        return form_class(event=event, **self.get_form_kwargs())

    def form_valid(self, form):
        """
        Populates the current object as event
        """
        form.save()
        messages.success(self.request, _('Registration completed '
                                         'successfully'))
        return redirect(form.event)


class SessionDetailView(DetailView):
    model = Session
    context_object_name = "session"


class EventListView(ListView):
    model = Event
    template_name = "events/list.html"
    context_object_name = "events"


class ProposalSubmissionView(CreateView, SingleObjectMixin):
    template_name = "events/proposals.html"
    form_class = ProposalForm
    model = Session
    context_object_name = "session"

    def get_context_data(self, **kwargs):
        return super(ProposalSubmissionView, self).get_context_data(
            session=self.get_object(),
            **kwargs)

    def form_valid(self, form):
        session = self.get_object()
        form.instance.session = session
        form.save()
        messages.success(self.request, _('Thanks for your proposal.'))
        return redirect(session.event)
