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
from Products.CMFPlone.PloneBatch import Batch


class ListingBatch(Batch):
    """Listing result batch."""

    def __init__(self, sequence, size, start=0, end=0, orphan=0, overlap=0,
                 pagerange=7, quantumleap=0, b_start_str='b_start',
                 batch_data=None):
        self.batch_data = batch_data

        if sequence is None:
            sequence = []

        super(ListingBatch, self).__init__(
            sequence, size, start, end, orphan, overlap, pagerange,
            quantumleap, b_start_str,
        )

    @property
    def sequence_length(self):
        """Effective length of sequence."""
        if self.batch_data is not None:
            length = getattr(self, 'pagesize', 0)
            return self.batch_data.get('results', length)
        return super(ListingBatch, self).sequence_length

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError(index)
        return self._sequence[index]

    @property
    def next(self):
        """Next batch page."""
        if self.end >= (self.last + self.pagesize):
            return None
        return ListingBatch(
            self._sequence, self._size, self.end - self.overlap, 0,
            self.orphan, self.overlap, batch_data=self.batch_data,
        )

    @property
    def previous(self):
        """Previous batch page."""
        if not self.first:
            return None
        return ListingBatch(
            self._sequence, self._size, self.first - self._size + self.overlap,
            0, self.orphan, self.overlap, batch_data=self.batch_data,
        )
