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
