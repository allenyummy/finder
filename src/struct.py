# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Structure

import logging
from typing import NamedTuple

logging.getLogger(__name__)


class Struct(NamedTuple):
    """
    An internal data structure of a target in a given string.

    Args:
        `text`: A text of target.
        `start_pos`: A start position of `text` in given string.
        `end_pos`: A end position of `text` in given string. (Notice: exact_end or exact_end+1)
    Type:
        `text`: string
        `start_pos`: integer
        `end_pos`: integer
    """

    text: str
    start_pos: int
    end_pos: int

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.start_pos == other.start_pos
            and self.end_pos == other.end_pos
        )

    def __repr__(self):
        return f"({self.text}, {self.start_pos}, {self.end_pos})"
