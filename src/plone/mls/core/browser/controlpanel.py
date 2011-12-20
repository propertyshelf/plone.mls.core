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
"""MLS Settings Control Panel."""

# zope imports
from plone.app.registry.browser import controlpanel

# local imports
from plone.mls.core import _
from plone.mls.core.interfaces import IMLSSettings


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
