# encoding=utf-8
# Author: Yu-Lun Chiang
# Description:

import logging
import os
import sys

sys.path.append(os.getcwd())
import re
import itertools
from typing import List, Union
from src.struct import Struct
from src.check import is_string, is_list_of_string, is_nested_list_of_string

logger = logging.getLogger(__name__)


class Finder:
    def __init__(self):
        pass

    def find(
        self,
        text: Union[str, List[str]],
        target: Union[str, List[str], List[List[str]]],
        is_split_into_words: bool = False,
    ) -> List[Struct]:

        out = list()
        if is_split_into_words:
            if is_list_of_string(text) and is_list_of_string(target):
                out = self.find_target_from_list_of_string(text, target)
            elif is_list_of_string(text) and is_nested_list_of_string(target):
                out = self.find_targets_from_list_of_string(text, target)
        else:
            if is_string(text) and is_string(target):
                out = self.find_target_from_text(text, target)
            elif is_string(text) and is_list_of_string(target):
                out = self.find_targets_from_text(text, target)
        return out

    def find_target_from_text(self, text: str, target: str) -> List[Struct]:

        out = list()
        matched_iter = re.finditer(target, text)
        try:
            first_match = next(matched_iter)
        except StopIteration:
            struct = Struct(target, -1, -1)
            out.append(struct)
        else:
            for match in itertools.chain([first_match], matched_iter):
                struct = Struct(target, match.start(), match.end())
                out.append(struct)
        out = self.sort(out)
        return out

    def find_targets_from_text(self, text: str, targets: List[str]) -> List[Struct]:

        out = list()
        for target in targets:
            tmp_out = self.find_target_from_text(text, target)
            out.extend(tmp_out)
        out = self.sort(out)
        return out

    def find_target_from_list_of_string(
        self, text: List[str], target: List[str]
    ) -> List[Struct]:

        out = list()
        cursor = 0
        for i, token in enumerate(text):
            if token == target[cursor]:
                cursor += 1
                if cursor == len(target):
                    end_pos = i + 1
                    start_pos = end_pos - len(target)
                    struct = Struct(target, start_pos, end_pos)
                    out.append(struct)
                    cursor = 0
            else:
                cursor = 0
        out = self.sort(out)
        return out

    def find_targets_from_list_of_string(
        self, text: List[str], targets: List[List[str]]
    ) -> List[Struct]:

        out = list()
        for target in targets:
            tmp_out = self.find_target_from_list_of_string(text, target)
            out.extend(tmp_out)
        out = self.sort(out)
        return out

    @staticmethod
    def sort(out: List[Struct]) -> List[Struct]:
        return sorted(out, key=lambda x: (x.start_pos, x.end_pos))
