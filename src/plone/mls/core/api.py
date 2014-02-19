# -*- coding: utf-8 -*-
"""plone.mls.core API."""

# zope imports
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

# local imports
from plone.mls.core.interfaces import IMLSSettings


def get_settings():
    """Get the MLS settings."""
    settings = {}
    # Get the global configuration.
    registry = getUtility(IRegistry)
    if registry is not None:
        try:
            registry_settings = registry.forInterface(IMLSSettings)
        except:
            pass
        else:
            settings = {
                'agency_id': registry_settings.agency_id,
                'mls_key': registry_settings.mls_key,
                'mls_site': registry_settings.mls_site,
            }
    return settings
