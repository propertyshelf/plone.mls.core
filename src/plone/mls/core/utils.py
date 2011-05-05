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
import urllib2
import json

# zope imports
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

# local imports
from plone.mls.core.interfaces import IMLSSettings


TIMEOUT = 10


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
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IMLSSettings)

    if settings.mls_site is None and settings.agency_id is None:
        return False

    url = '%(site)s/agencies/%(agency_id)s/listings/%(listing_id)s/json' % dict(
        site=settings.mls_site,
        agency_id=settings.agency_id,
        listing_id=lid,
    )
    if summary:
        url = url + '?summary'

    url = urllib2.unquote(url)

    try:
        print("Getting listing...")
        raw = urllib2.urlopen(url, timeout=TIMEOUT)
    except IOError:
        print("Timeout?")
        return False
    raw = '\n'.join(raw.readlines())

    try:
        data = decode(raw)
    except ValueError:
        return False

    return data


def test_json():
    url = 'http://localhost:8060/mls/agencies/lep/listings/rl1000009/'
    data = json.dumps({'id': 1, 'method': 'listing', 'params': {'lang': 'en'}})
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    result = f.read()
    print(result)
    print "Done"
