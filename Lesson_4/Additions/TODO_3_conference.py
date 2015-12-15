@endpoints.method(message_types.VoidMessage, ConferenceForms,
        path='getConferencesCreated',
        http_method='POST', name='getConferencesCreated')
def getConferencesCreated(self, request):
    """Return conferences created by user."""
    # make sure user is authed
    user = endpoints.get_current_user()
    if not user:
        raise endpoints.UnauthorizedException('Authorization required')

    # make profile key
    p_key = ndb.Key(Profile, getUserId(user))
    # create ancestor query for this user
    conferences = Conference.query(ancestor=p_key)
    # get the user profile and display name
    prof = p_key.get()
    displayName = getattr(prof, 'displayName')
    # return set of ConferenceForm objects per Conference
    return ConferenceForms(
        items=[self._copyConferenceToForm(conf, displayName) for conf in conferences]
    )
    

    @endpoints.method(CONF_GET_REQUEST, ConferenceForm,
            path='conference/{websafeConferenceKey}',
            http_method='GET', name='getConference')
    def getConference(self, request):
        """Return requested conference (by websafeConferenceKey)."""
        # get Conference object from request; bail if not found
        conf = ndb.Key(urlsafe=request.websafeConferenceKey).get()
        if not conf:
            raise endpoints.NotFoundException(
                'No conference found with key: %s' % request.websafeConferenceKey)
        prof = conf.key.parent().get()
        # return ConferenceForm
        return self._copyConferenceToForm(conf, getattr(prof, 'displayName'))
     
