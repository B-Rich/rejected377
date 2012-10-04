#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests WithContextSkip"""

from . import WithContextSkip

StatementSkipped = WithContextSkip.StatementSkipped


# helper methods

@WithContextSkip.conditionalcontextmanager
def wanneer(condition):
    """Runs the controlled block if the condition is True
    Otherwise skips it"""

    if condition:
        yield
    else:
        raise WithContextSkip.SkipStatement()


@WithContextSkip.conditionalcontextmanager
def if_positive(value):
    """Runs the controlled block if the value is greater than 0
    Otherwise skips it. The value is returned for assignment to a variable"""

    if value > 0:
        yield value
    else:
        raise WithContextSkip.SkipStatement()


@WithContextSkip.conditionalcontextmanager
def ignorant_peasant():
    """Never yields - doesn't even raise a valid exception"""

    if True is False:
        yield value


# basic tests illustrating the principles

def test_no_value_condition_avoided():
    """The generator not yielding means the governed code block is not run,
    with no value being assigned by the with statement"""

    code_run = False
    with wanneer(False) as StatementSkipped.detector:
        code_run = True
    assert not code_run


def test_no_value_condition_passed():
    """The generator yielding means the governed code block is run,
    with no value being assigned by the with statement"""

    code_run = False
    with wanneer(True) as StatementSkipped.detector:
        code_run = True
    assert code_run


def test_ignored_value_condition_passed():
    """The generator yielding means the governed code block is run,
    with a value being yielded by the generator but ignored"""

    code_run = False
    with if_positive(37) as StatementSkipped.detector:
        code_run = True
    assert code_run


def test_ignored_value_condition_avoided():
    """The generator not yielding means the governed code block is not run,
    with a value being yielded by the generator but ignored"""

    code_run = False
    with if_positive(-37) as StatementSkipped.detector:
        code_run = True
    assert not code_run


def test_received_value_condition_passed():
    """The generator yielding means the governed code block is run,
    with a value being yielded by the generator and received"""

    code_run = False
    with if_positive(37) as (value, StatementSkipped.detector):
        code_run = True
        assert value == 37
    assert value == 37
    assert code_run


def test_received_value_condition_avoided():
    """The generator not yielding means the governed code block is not run,
    with StatementSkipped being received by the target value variable"""

    code_run = False
    with if_positive(-37) as (value, StatementSkipped.detector):
        code_run = True
    assert not code_run
    assert value is StatementSkipped


def test_never_yields():
    """If the generator completes without yielding, a RuntimeError is raised"""

    raised = False
    code_run = False
    try:
        with ignorant_peasant() as StatementSkipped.detector:
            code_run = True
    except RuntimeError, e:
        raised = True
        assert 'SkipStatement' in e.message
    assert raised and not code_run
