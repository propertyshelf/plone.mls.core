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
"""Interface definitions."""

# zope imports
from zope import schema
from zope.interface import Interface

# local imports
from plone.mls.core import _


class IMLSSettings(Interface):
    """Global Propertyshelf MLS settings.

    This describes records stored in the configuration registry and obtainable
    via plone.registry.
    """

    mls_key = schema.TextLine(
        default=u"",
        description=_(
            u"help_mls_key",
            default=u"",
        ),
        required=False,
        title=_(
            u"label_mls_key",
            default=u"MLS API Key",
        )
    )

    mls_site = schema.TextLine(
        default=u"",
        description=_(
            u"help_mls_site",
            default=u"",
        ),
        required=True,
        title=_(
            u"label_mls_site",
            default=u"MLS URL",
        )
    )

    agency_id = schema.TextLine(
        default=u"",
        description=_(
            u"help_agency_id",
            default=u"",
        ),
        required=True,
        title=_(
            u"label_agency_id",
            default=u"Agency ID",
        )
    )
