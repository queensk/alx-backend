# 0x00. Pagination
## Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resistant manner
# Tasks
## 0. Simple helper function
Write a function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
```
def index_range(page, page_size):
    # Your code here
```
## 1. Simple pagination
Copy index_range from the previous task and the following class into your code:
```
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    def __init__(self):
        self.__dataset = None
        self.dataset_filename = "Popular_Baby_Names.csv"

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.dataset_filename) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10."""
        # Your code here
```
Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. return the correct list of rows).

If the input arguments are out of range for the dataset, an empty list should be returned.

## 2. Hypermedia pagination
Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page (equivalent to return from previous task)
- `next_page`: number of the next page, None if no next page
- `prev_page`: number of the previous page, None if no previous page
- `total_pages`: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

## 3. Deletion-resistant pagination
Copy code from previous tasks.

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

For example, if we have a dataset of size 1000 split into pages of size 100 and we’re on page 3, and then we delete rows 200 to 300 from the dataset; if we refresh we’ll still be on page 3 but we’ll have missed rows 100 to 200.

To fix this, we’re going to use a query parameter instead of using page numbers: index .

Implement a method named get_hyper_index that takes two integer arguments: index with a None default value and page_size with default value of 10.

The method should return a dictionary with the following key-value pairs:

- `index`: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data - was removed from the dataset, the current index should be 60.
- `next_index`: index of the next page, None if no next page
- `prev_index`: index of the previous page, None if no previous page
- `page_size`: see above
- `data`: see above
Use code from previous tasks as base - but now you have to use index instead of pages.
