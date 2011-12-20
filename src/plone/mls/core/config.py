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
"""Package configuration."""

ERROR_404 = u"""
<p>The listing does not exist in the MLS.</p>
"""

ERROR_503 = u"""
<p>The MLS is currently not available. If the error persists, please contact <a
href="mailto:support@propertyshelf.com">support@propertyshelf.com</a>.</p>
<p>Please also double check your <a href="%(portal_url)s/@@mls-controlpanel">MLS settings</a>.</p>
"""
