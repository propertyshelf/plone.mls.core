# -*- coding: utf-8 -*-

##############################################################################
#
# Copyright (c) 2011 Propertyshelf, LLC and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""Propertyshelf MLS utils."""

# python imports
from jsonpickle import decode
from urllib import urlencode
import httplib2
import simplejson
import urllib2
# import json

# zope imports
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

# local imports
from plone.mls.core.interfaces import IMLSSettings


TIMEOUT = 10


class MLSError:
    """General MLS Error."""
    def __init__(self, code=None, reason=None):
        self.code = code
        self.reason = reason


class MLSConnectionError(MLSError):
    """No Conncetion to the MLS."""

class MLSDataError(MLSError):
    """Data returned from the MLS contains errors."""


def authenticate():
    """Authenticate the Plone Website."""
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IMLSSettings)
#    test_json()

    if settings.mls_site is None and settings.agency_id is None:
        return False

    url = '%(site)s/agencies/%(agency_id)s' % dict(
        site=settings.mls_site,
        agency_id=settings.agency_id,
    )
    url = urllib2.unquote(url)
    
    try:
        urllib2.urlopen(url)
    except IOError:
        return False

    return True


def get_listing(lid, summary=False):
    """Get the data for a single listing."""
    kwargs = {}
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IMLSSettings)

    if settings.mls_site is None or len(settings.mls_site) == 0:
        raise MLSConnectionError(code=503)

    if settings.agency_id is None or len(settings.agency_id) == 0:
        raise MLSConnectionError(code=503)

    URL_BASE = '%(site)s/agencies/%(agency_id)s/listings/%(listing_id)s/json' % dict(
        site=settings.mls_site,
        agency_id=settings.agency_id,
        listing_id=lid,
    )

    kwargs.update({
        'apikey': settings.mls_key,
        'agency': settings.agency_id,
        'listing': lid,
    })

    if summary:
        kwargs.update({'summary': 1})

    url = URL_BASE + '?' + urlencode(kwargs)

    h = httplib2.Http(".cache")
#     h = httplib2.Http()
    resp, content = h.request(url)

#     try:
#         data = urllib2.urlopen(url)
#     except urllib2.URLError, e:
#         if isinstance(e, urllib2.HTTPError):
#             raise MLSConnectionError(code=e.code, reason=e.msg)
#         else:
#             print("MLSConnectionError")
#             # No connection to the server possible
#             raise MLSConnectionError(code=503, reason=e.reason)
# 
#     try:
#         result = simplejson.load(data)
    try:
        result = simplejson.loads(content)
    except simplejson.JSONDecodeError, e:
        raise MLSDataError(code=401)

    if result.get('status', 'error') != 'ok':
        raise MLSDataError
    return result.get('result', None)


# def test_json():
#     url = 'http://localhost:8060/mls/agencies/lep/listings/rl1000009/'
#     data = json.dumps({'id': 1, 'method': 'listing', 'params': {'lang': 'en'}})
#     req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
#     f = urllib2.urlopen(req)
#     result = f.read()
#     print(result)
#     print "Done"
