# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2011 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
###############################################################################
"""Interface definitions."""

# zope imports
from zope import schema
from zope.interface import Interface

# local imports
from plone.mls.core.i18n import _


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
