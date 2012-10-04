rejected377
===========

Implementation of with block context managers that allow clearly defined skipping of the controlled block ala PEP 377 (which was rightly rejected)

[PEP 377](http://www.python.org/dev/peps/pep-0377/) (rejected) proposed making this a standard language feature...
and was rejected primarily because it alters the logical control flow of the `with` block.
The full text of this PEP is included for instructional purposes with this module.

This implementation uses the fact that variable assignments in the `with ... as ...:` syntax are considered part of the `with` block
Exceptions raised in these assignments are passed to the `__exit__` function of the context manager, and can be used to skip the block.

Of course, nobody should actually *use* this; this is mainly published because it was the subject of a Lightning Talk at [PyConZA 2012](http://za.pycon.org/).

The example of usage is in writing testing code around different threads - see the `ThreadWeave` module. `test_ThreadWeave` illustrates the different approach to testing that this provides, but a basic example is:

    import rejected377
    
    with rejected377.only_thread('main') as rejected377.StatementSkipped.detector:
        print True

For convenience, there's a `Singleton` module as well; the tests for this are of the highland variety.

