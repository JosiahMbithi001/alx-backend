#!/usr/bin/env python3
"""This File Contains A
Class Server
Function index_range"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This Function Returns Dataset"""
        try:
            assert (page > 0 and page_size > 0)
            assert (type(page) is int and type(page_size) is int)
            pages = index_range(page, page_size)
            dataset = self.dataset()[pages[0]: pages[1]]
            return dataset
        except:
            return []


def index_range(page: int, page_size: int) -> tuple:
    """This Function returns Start and End Index i.e Index Range"""

    if page < 1 or page_size < 1:
        raise ValueError("Page and Page Size must be Positive Integer")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index

def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict :
    """This Function returns page sie, page and data """

    data_page = self.get_page(page, page_size)
    total_items = len(self.dataset())
    total_pages = 

    dict = {
        "page_size": len(data_page)
        "page": get_page
    }