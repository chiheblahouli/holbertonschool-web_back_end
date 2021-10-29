#!/usr/bin/env python3
"""
Server class
"""


import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


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
        """get page"""
        assert(type(page) == type(page_size) == int)
        assert (page > 0 and page_size > 0)
        t = index_range(page, page_size)
        listd = self.dataset()
        return listd[t[0]:t[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """hyper_v:P"""

        self.page_size = len(self.get_page(page, page_size))
        self.page = page
        self.total_pages = math.ceil(len(self.__dataset) / page_size)
        self.data = self.get_page(page, page_size)
        self.next_page = page + 1 if page < self.total_pages else None
        self.prev_page = page - 1 if page > 1 else None
        return {k: self.__dict__[k]
                for k in self.__dict__ if k != "_Server__dataset"}
