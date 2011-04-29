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
"""Test the control panel for plone.mls.core."""

# python imports
import unittest

# zope imports
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase
from plone.registry import Registry
from zope.component import getMultiAdapter
from zope.interface import directlyProvides

# local imports
from plone.mls.core.browser.interfaces import IMLSSpecific
from plone.mls.core.interfaces import IMLSSettings
from plone.mls.core.tests.layer import MLSCoreLayer


class RegistryTest(PloneTestCase):

    layer = MLSCoreLayer

    def afterSetUp(self):
        directlyProvides(self.portal.REQUEST, IMLSSpecific)
        self.loginAsPortalOwner()
        self.registry = Registry()
        self.registry.registerInterface(IMLSSettings)

    def test_mls_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
            name="mls-controlpanel")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_mls_controlpanel_view_protected(self):
        # Test that the MLS setting control panel view can not be accessed
        # by anonymous users.
        from AccessControl import Unauthorized
        self.logout()
        self.assertRaises(Unauthorized, self.portal.restrictedTraverse,
            '@@mls-controlpanel')

    def test_mls_in_controlpanel(self):
        # Check that there is an MLS entry in the control panel.
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless('propertyshelf_mls' in [a.getAction(self)['id']
            for a in self.controlpanel.listActions()])

    def test_record_mls_key(self):
        # Test that the mls_key record is in the control panel.
        record_mls_key = self.registry.records[
            'plone.mls.core.interfaces.IMLSSettings.mls_key']
        self.failUnless('mls_key' in IMLSSettings)
        self.assertEquals(record_mls_key.value, u"")

    def test_record_mls_site(self):
        # Test that the mls_site record is in the control panel.
        record_mls_site = self.registry.records[
            'plone.mls.core.interfaces.IMLSSettings.mls_site']
        self.failUnless('mls_site' in IMLSSettings)
        self.assertEquals(record_mls_site.value, u"")


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
