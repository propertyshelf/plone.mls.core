# -*- coding: utf-8 -*-
"""Migration steps for plone.mls.listing."""

from plone import api
from plone.mls.core.interfaces import IMLSSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


PROFILE_ID = 'profile-plone.mls.core:default'


def migrate_to_1001(context):
    """Migrate from 1000 to 1001.

    * Activate portal actions.
    * Register JS resources.
    """
    setup = api.portal.get_tool(name='portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'actions')
    setup.runImportStepFromProfile(PROFILE_ID, 'jsregistry')


def migrate_to_1002(context):
    """Migrate from 1001 to 1002.

    * Add new registry settings for MLS.
    """
    registry = getUtility(IRegistry)
    registry.registerInterface(IMLSSettings)


def migrate_to_1003(context):
    """Migrate from 1002 to 1003.

    * Register new exclude_agency_id field in MLS settings registry.
    """
    registry = getUtility(IRegistry)
    registry.registerInterface(IMLSSettings)


def migrate_to_1004(context):
    """Migrate from 1003 to 1004.

    * Register new show_listing_attribution field in MLS settings registry.
    """
    registry = getUtility(IRegistry)
    registry.registerInterface(IMLSSettings)
