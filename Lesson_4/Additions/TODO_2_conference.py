from models import ConferenceForms
from models import ConferenceQueryForm
from models import ConferenceQueryForms


@endpoints.method(ConferenceQueryForms, ConferenceForms,
            path='queryConferences',
            http_method='POST',
            name='queryConferences')
def queryConferences(self, request):
    """Query for conferences."""
    conferences = Conference.query()

     # return individual ConferenceForm object per Conference
    return ConferenceForms(
        items=[self._copyConferenceToForm(conf, "") \
        for conf in conferences]
    )
