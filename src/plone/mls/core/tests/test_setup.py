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
"""Test Setup of plone.mls.core."""

# python imports
import unittest2 as unittest

# zope imports
from plone.browserlayer import utils as layerutils

# local imports
from plone.mls.core.browser.interfaces import IMLSSpecific
from plone.mls.core.testing import PLONE_MLS_CORE_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):
    """Setup Test Case for plone.mls.core."""
    layer = PLONE_MLS_CORE_INTEGRATION_TESTING

    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual('Plone site', portal.getProperty('title'))

    def test_plone_app_registry_installed(self):
        portal = self.layer['portal']
        qi = portal.portal_quickinstaller
        if qi.isProductAvailable('plone.app.registry'):
            self.assertTrue(qi.isProductInstalled('plone.app.registry'))
        else:
            self.assertTrue('plone.app.registry' in \
                            qi.listInstallableProfiles())

    def test_browserlayer_installed(self):
        self.assertTrue(IMLSSpecific in layerutils.registered_layers())
