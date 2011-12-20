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
"""Test Control Panel for plone.mls.core."""

# python imports
import unittest2 as unittest

# zope imports
from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_ID, logout, setRoles
from plone.registry import Registry
from zope.component import getMultiAdapter
from zope.interface import directlyProvides

# local imports
from plone.mls.core.browser.interfaces import IMLSSpecific
from plone.mls.core.interfaces import IMLSSettings
from plone.mls.core.testing import PLONE_MLS_CORE_INTEGRATION_TESTING


class TestMLSControlPanel(unittest.TestCase):
    """Control Panel Test Case for plone.mls.core."""
    layer = PLONE_MLS_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']
        directlyProvides(self.portal.REQUEST, IMLSSpecific)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.registry = Registry()
        self.registry.registerInterface(IMLSSettings)

    def test_mls_controlpanel_view(self):
        """Test that the MLS configuration view is available."""
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='mls-controlpanel')
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_mls_controlpanel_view_protected(self):
        """Test that the MLS configuration view needs authentication."""
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized, self.portal.restrictedTraverse,
                          '@@mls-controlpanel')

    def test_mls_in_controlpanel(self):
        """Check that there is an MLS entry in the control panel."""
        self.controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        self.assertTrue('propertyshelf_mls' in [a.getAction(self)['id']
            for a in self.controlpanel.listActions()])
