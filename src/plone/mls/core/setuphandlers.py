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
"""Additional setup steps."""

# python imports
from logging import getLogger

# zope imports
from plone.browserlayer import utils as layerutils

# local imports
from plone.mls.core.browser.interfaces import IMLSSpecific

logger = getLogger('plone.mls.core')


def resetLayers(context):
    """Remove custom browser layer on uninstall."""

    if context.readDataFile('plone.mls.core_uninstall.txt') is None:
        return

    if IMLSSpecific in layerutils.registered_layers():
        layerutils.unregister_layer(name='plone.mls.core')
        logger.info('Browser layer "plone.mls.core" uninstalled.')
