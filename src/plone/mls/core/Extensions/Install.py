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
"""Install/Uninstall methods."""

# python imports
from logging import getLogger

# zope imports
from Products.CMFCore.utils import getToolByName


UNINSTALL_PROFILE = 'profile-plone.mls.core:uninstall'
logger = getLogger('plone.mls.core')


def uninstall(portal):
    portal_setup = getToolByName(portal, 'portal_setup')
    portal_setup.runAllImportStepsFromProfile(UNINSTALL_PROFILE)
    logger.info('Ran all uninstall steps.')
