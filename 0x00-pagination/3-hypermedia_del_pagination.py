#!/usr/bin/env python3
"""This File Contains Server Class and Its Two Methods Defined Below"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Method to perform deletion-resilient hypermedia pagination.

        Arguments:
        index -- The current start index of the return page. If None, default is 0.
        page_size -- The current page size. Default is 10.

        Returns:
        A dictionary containing the following key-value pairs:
        'index': The current start index of the return page.
        'next_index': The next index to query with.
        'page_size': The current page size.
        'data': The actual page of the dataset.
        """
        if index is None:
            index = 0

        assert isinstance(
            index, int) and index >= 0, "Invalid index. Must be a non-negative integer."
        assert isinstance(
            page_size, int) and page_size > 0, "Invalid page_size. Must be a positive integer."

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        total_pages = math.ceil(total_items / page_size)

        if index >= total_items:
            raise AssertionError("Index out of range.")

        data = []
        next_index = index
        for _ in range(page_size):
            row = indexed_dataset.get(next_index)
            if row is None:
                break
            data.append(row)
            next_index += 1

        metadata = {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }

        return metadata
