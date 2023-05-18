# 0x01. Caching

This project is about implementing caching algorithms in Python. Caching is a technique that improves the performance and efficiency of a system by storing frequently accessed data in a temporary storage location, called a cache. A caching algorithm is a method or algorithm that decides what data to store in the cache, how long to keep it, and what data to evict when the cache is full.

## Learning Objectives

- What is caching and why is it important
- What are caching levels
- What are caching policies
- How to implement FIFO caching
- How to implement LIFO caching
- How to implement LRU caching
- How to implement MRU caching
- How to use redis for caching

## Requirements

- Python 3.7 or higher
- Redis 5.0.7 or higher
- PEP8 style

## Files

- `0-basic_cache.py`: A class `BasicCache` that inherits from `BaseCaching` and is a caching system. It has methods `put` and `get` that store and retrieve data from the cache respectively.
- `1-fifo_cache.py`: A class `FIFOCache` that inherits from `BaseCaching` and is a caching system. It implements the FIFO caching policy (first in, first out). It has methods `put` and `get` that store and retrieve data from the cache respectively.
- `2-lifo_cache.py`: A class `LIFOCache` that inherits from `BaseCaching` and is a caching system. It implements the LIFO caching policy (last in, first out). It has methods `put` and `get` that store and retrieve data from the cache respectively.
- `3-lru_cache.py`: A class `LRUCache` that inherits from `BaseCaching` and is a caching system. It implements the LRU caching policy (least recently used). It has methods `put` and `get` that store and retrieve data from the cache respectively.
- `4-mru_cache.py`: A class `MRUCache` that inherits from `BaseCaching` and is a caching system. It implements the MRU caching policy (most recently used). It has methods `put` and `get` that store and retrieve data from the cache respectively.
- `100-lfu_cache.py`: A class `LFUCache` that inherits from `BaseCaching` and is a caching system. It implements the LFU caching policy (least frequently used). It has methods `put` and `get` that store and retrieve data from the cache respectively.
- `101-redis_cache.py`: A class `RedisCache` that uses redis as a backend for storing and retrieving data. It has methods `store`, `get`, `get_str`, and `get_int` that perform different operations on the redis database.

## Usage

To use any of the classes, import them from their respective files. For example:

```python
from 0-basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("foo", "bar")
print(my_cache.get("foo"))
# Output: bar
```

To use the redis class, make sure you have redis installed and running on your machine. For example:

```bash
$ sudo apt-get install redis-server
$ sudo service redis-server start
$ redis-cli ping
PONG
```

Then, import the class from the file and use it as follows:

```python
from 101-redis_cache import RedisCache

rc = RedisCache()
rc.store("foo", "bar")
print(rc.get("foo"))
# Output: b'bar'
print(rc.get_str("foo"))
# Output: bar
```