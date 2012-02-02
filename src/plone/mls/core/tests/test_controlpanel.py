# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2012 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS AND ANY EXPRESSED OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
