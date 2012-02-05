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
"""Interface definitions."""

# zope imports
from zope import schema
from zope.interface import Interface

# local imports
from plone.mls.core.i18n import _


class IMLSSettings(Interface):
    """Global Propertyshelf MLS settings.

    This describes records stored in the configuration registry and obtainable
    via plone.registry.
    """

    mls_key = schema.TextLine(
        default=u"",
        required=False,
        title=_(
            u"label_mls_key",
            default=u"MLS API Key",
        )
    )

    mls_site = schema.TextLine(
        default=u"",
        required=True,
        title=_(
            u"label_mls_site",
            default=u"MLS URL",
        )
    )

    agency_id = schema.TextLine(
        default=u"",
        required=True,
        title=_(
            u"label_agency_id",
            default=u"Agency ID",
        )
    )
