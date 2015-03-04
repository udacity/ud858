@endpoints.method(message_types.VoidMessage, ConferenceForms,
        path='filterPlayground',
        http_method='GET', name='filterPlayground')
def filterPlayground(self, request):
    q = Conference.query()
    # simple filter usage:
    # q = q.filter(Conference.city == "Paris")

    # advanced filter building and usage
    # field = "city"
    # operator = "="
    # value = "London"
    # f = ndb.query.FilterNode(field, operator, value)
    # q = q.filter(f)

    # TODO
    # add 2 filters:
    # 1: city equals to London
    # 2: topic equals "Medical Innovations"

    return ConferenceForms(
        items=[self._copyConferenceToForm(conf, "") for conf in q]
    )