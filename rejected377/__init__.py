#!/usr/bin/env python

"""Implementation of with block context managers that allow
clearly defined skipping of the controlled block ala PEP 377

PEP 377 (rejected) proposed making this a standard language feature,
and was rejected primarily because it alters the logical control flow
of the with block.

This implementation uses the fact that variable assignments in the
with ... as ...: syntax are considered part of the with block
Exceptions raised in these assignments are passed to the __exit__
function of the context manager, and can be used to skip the block.
"""

from WithContextSkip import SkipStatement, \
        StatementSkipped, StatementNotSkipped, \
        ConditionalContextManager, conditionalcontextmanager
from ThreadWeave import only_thread, only_thread_blocking
