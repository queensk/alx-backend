#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start index and
    an end index corresponding to the range
    """
    return ((page - 1) * page_size, page * page_size)
