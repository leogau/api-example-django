from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.shortcuts import redirect, render
from django.core.mail import mail_admins
from django.conf import settings

import api.client

import logging
log = logging.getLogger("apidemo")

def view(request):
    # FIXME check session for OAuth token
    if api.client.OAUTH_KEY in request.session.keys():
        access_token = request.session[api.client.OAUTH_KEY]
        log.debug("user has oauth access token: %s" % access_token)
        return render(request, 'demo.html')
    else:
        log.debug("user doesn't have a token yet, redirect to login...")
        return redirect(api.client.LOGIN_URL)

