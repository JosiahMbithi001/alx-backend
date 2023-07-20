#!/usr/bin/env python3
"""This File Contains A Function index_range"""

def index_range(page: int, page_size: int) -> tuple:
    """This Function returns Start and End Index i.e Index Range"""

    if page < 1 or page_size <1:
        raise ValueError("Page and Page Size must be Positive Integer")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index