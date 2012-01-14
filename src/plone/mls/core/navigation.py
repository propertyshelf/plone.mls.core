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
"""Custom Batch Provider for listing results."""

# zope imports
from Products.CMFPlone.PloneBatch import Batch, LazyNextBatch, LazyPrevBatch


class LazyListingPrevBatch(LazyPrevBatch):
    """Previous listing result batch."""

    def __of__(self, parent):
        return ListingBatch(parent._sequence, parent._size,
                            parent.first - parent._size + parent.overlap, 0,
                            parent.orphan, parent.overlap,
                            batch_data=parent.batch_data)


class LazyListingNextBatch(LazyNextBatch):
    """Next listing result batch."""

    def __of__(self, parent):
        if parent.end >= (parent.last + parent.size):
            return None
        return ListingBatch(parent._sequence, parent._size,
                            parent.end - parent.overlap, 0,
                            parent.orphan, parent.overlap,
                            batch_data=parent.batch_data)


class ListingBatch(Batch):
    """Listing result batch."""
    __allow_access_to_unprotected_subobjects__ = 1

    previous = LazyListingPrevBatch()
    next = LazyListingNextBatch()

    def __init__(self, sequence, size, start=0, end=0, orphan=0, overlap=0,
                 pagerange=7, quantumleap=0, b_start_str='b_start',
                 batch_data=None):
        self.batch_data = batch_data
        if self.batch_data is not None:
            length = 0
            if sequence is not None:
                length = len(sequence)
            self.sequence_length = self.batch_data.get('results', length)

        if sequence is None:
            sequence = []

        super(ListingBatch, self).__init__(sequence, size, start, end, orphan,
                                           overlap, pagerange, quantumleap,
                                           b_start_str)

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError(index)
        return self._sequence[index]
