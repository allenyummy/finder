# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test for finder.py

import logging
import os
import sys

sys.path.append(os.getcwd())
import pytest
from src.finder import Finder

logger = logging.getLogger(__name__)

#######################
##### Test Finder #####
#######################

test_data = [
    (
        "TEST-GENIA-MEDLINE:93136418-abstract-4",
        "When cells were treated with IL-4 for 5 hours before LPS activation , both the c-fos and the c-jun mRNA expression was decreased .",
        "IL-4",
        False,
        [(29, 33)],
    ),
    (
        "TEST-GENIA-MEDLINE:93136418-abstract-4",
        "When cells were treated with IL-4 for 5 hours before LPS activation , both the c-fos and the c-jun mRNA expression was decreased .",
        "il-4",
        False,
        [(-1, -1)],
    ),
    (
        "TEST-GENIA-MEDLINE:93136418-abstract-4",
        "When cells were treated with IL-4 for 5 hours before LPS activation , both the c-fos and the c-jun mRNA expression was decreased .",
        ["IL-4"],
        False,
        [(29, 33)],
    ),
    (
        "TEST-FakeData-1",
        ["A", "B", "C", "D", "B", "C"],
        ["B", "C"],
        True,
        [(1, 3), (4, 6)],
    ),
    (
        "TEST-FakeData-1",
        ["A", "B", "C", "D", "B", "C"],
        [["B"], ["B", "C"], ["B", "C", "D"]],
        True,
        [(1, 2), (1, 3), (1, 4), (4, 5), (4, 6)],
    ),
]


@pytest.fixture(scope="function")
def finder():
    return Finder()


@pytest.mark.parametrize(
    argnames=("name, text, target, is_split_into_words, expected_ans"),
    argvalues=test_data,
    ids=[f"{i[0]}" for i in test_data],
)
def test_finder(finder, name, text, target, is_split_into_words, expected_ans):

    a = finder.find(text, target, is_split_into_words)
    logger.warning(a)
    for a_element, ans in zip(a, expected_ans):
        assert a_element.start_pos == ans[0]
        assert a_element.end_pos == ans[1]
