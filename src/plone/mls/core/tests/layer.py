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
"""Test layer for plone.mls.core."""

# zope imports
from Products.Five import fiveconfigure, zcml
from Products.PloneTestCase import layer, ptc
from Testing import ZopeTestCase as ztc


ptc.setupPloneSite(
    extension_profiles=('plone.mls.core:default', )
)


class MLSCoreLayer(layer.PloneSite):
    """Configure plone.mls.core."""

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import plone.mls.core
        zcml.load_config("configure.zcml", plone.mls.core)
        fiveconfigure.debug_mode = False
        ztc.installPackage("plone.mls.core")

    @classmethod
    def tearDown(cls):
        pass
