from typing import TypeVar, Generic, Tuple, Any, Type
from abc import ABC, abstractmethod
from data_structures.linkedlist import LinkedList

S = TypeVar('S', str, int)
T = TypeVar('T')


class HashFunction(ABC, Generic[S]):
  @staticmethod
  @abstractmethod
  def hash(key: S) -> int:
    """
    Returns the index at which the value for the key is stored at
    """
    pass


class HashTable(Generic[S, T]):
  def __init__(self, hash_function: Type[HashFunction[S]], bucket_count: int = 10):
    self._buckets = LinkedList[LinkedList[Tuple[S, T]]]([])
    for _ in range(bucket_count):
      self._buckets.append(LinkedList([]))
    self._hash_function = hash_function

  def insert(self, key: S, value: T):
    index = self._hash_function.hash(key)
    ll = self._buckets[index]
    ll.append((key, value))
    return self

  def search(self, key: S, default: Any = None):
    index = self._hash_function.hash(key)
    for k, v in self._buckets[index]:
      if key == k:
        return v
    return default

  def delete(self, key: S):
    index = self._hash_function.hash(key)
    ind = 0
    for k, v in self._buckets[index]:
      if key == k:
        self._buckets[index].pop(ind)
        break
      ind += 1
    return self

  def update(self, key: S, item: T):
    found = False
    index = self._hash_function.hash(key)
    for i in range(len(self._buckets[index])):
      if self._buckets[index][i][0] == key:
        self._buckets[index][i] = (key, item)
        found = True
        break
    if not found:
      raise KeyError
    return self

  def keys(self):
    # TODO: Make these views
    return [k for bucket in self._buckets for k, v in bucket]

  def values(self):
    return [v for bucket in self._buckets for k, v in bucket]

  def items(self):
    return [(k, v) for bucket in self._buckets for k, v in bucket]

  def __setitem__(self, key: S, item: T):
    if self.search(key, None) is None:
      self.insert(key, item)
      return self
    self.update(key, item)
    return self

  def __getitem__(self, key: S):
    return self.search(key, None)

  def __delitem__(self, key: S):
    self.delete(key)
    return self

  def __contains__(self, item: T):
    for bucket in self._buckets:
      for k, v in bucket:
        if v == item:
          return True
    return False

  def __iter__(self):
    for bucket in self._buckets:
      for k, v in bucket:
        yield (k, v)

  def __str__(self) -> str:
    return "{ " + ", ".join([f"{k}: {v}" for k, v in self.items()]) + " }"
