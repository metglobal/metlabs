from metlabs.events.models import Event


def next_event(context):
    events = Event.objects.all()

    try:
        next_event = events[0]
    except IndexError:
        next_event = None

    return {
        "next_event": next_event
    }