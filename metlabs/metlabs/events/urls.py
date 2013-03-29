from django.conf.urls import url, patterns

from metlabs.events.views import (EventView, EventListView,
                                  SessionDetailView, ProposalSubmissionView,
                                  ProposalSubmissionView)


urlpatterns = patterns(
    '',

    url(r'^$', EventListView.as_view(), name="events"),
    url(r'^(?P<slug>[-\w]+)/$', EventView.as_view(),
        name="events_detail"),

    url(r'^(?P<slug>[-\w]+)/sessions/(?P<pk>\d+)/$',
        SessionDetailView.as_view(),
        name="events_session_detail"),

    url(r'^(?P<slug>[-\w]+)/sessions/(?P<pk>\d+)/proposals$',
        ProposalSubmissionView.as_view(),
        name="events_send_proposal"),
)
