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
"""MLS Settings Control Panel."""

# zope imports
from plone.app.registry.browser import controlpanel

# local imports
from plone.mls.core import _
from plone.mls.core.browser.interfaces import IMLSSettings


class MLSSettingsEditForm(controlpanel.RegistryEditForm):
    """MLS Settings Form"""

    schema = IMLSSettings
    label = _(u"heading_mls_settings", u"Propertyshelf MLS Settings")
    description = _(u"help_mls_settings", default=u"")

    def updateFields(self):
        super(MLSSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(MLSSettingsEditForm, self).updateWidgets()


class MLSSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """MLS Settings Control Panel"""

    form = MLSSettingsEditForm
