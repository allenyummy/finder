# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Check type of input text

import logging

logger = logging.getLogger(__name__)


def is_string(text):
    if isinstance(text, str):
        return True
    return False


def is_list_of_string(text):
    if isinstance(text, list) and all(isinstance(i, str) for i in text):
        return True
    return False


def is_nested_list_of_string(text):
    if isinstance(text, list):
        for i in text:
            if not isinstance(i, list):
                return False
            for j in i:
                if not isinstance(j, str):
                    return False
        return True
    return False