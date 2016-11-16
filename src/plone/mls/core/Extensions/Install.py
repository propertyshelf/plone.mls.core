# -*- coding: utf-8 -*-
"""Install/Uninstall methods."""

# python imports
from logging import getLogger

# zope imports
from plone import api


UNINSTALL_PROFILE = 'profile-plone.mls.core:uninstall'
logger = getLogger('plone.mls.core')


def uninstall(portal):
    portal_setup = api.portal.get_tool(name='portal_setup')
    portal_setup.runAllImportStepsFromProfile(UNINSTALL_PROFILE)
    logger.info('Ran all uninstall steps.')
