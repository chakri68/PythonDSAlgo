from __future__ import annotations
from typing import TypeVar, Generic, Optional, overload, TYPE_CHECKING, Iterable, cast


T = TypeVar('T')


class Node(Generic[T]):
  def __init__(self, val: T, next: Optional[Node[T]] = None):
    self._val = val
    self._next = next

  def val(self):
    return self._val

  def next(self):
    return self._next

  def set_next(self, next: Optional[Node[T]]):
    self._next = next
    return self

  def set_val(self, val: T):
    self._val = val
    return self

  def __str__(self) -> str:
    return f"{{ value: {self._val}, next: {self._next.__repr__()} }}"

  def __eq__(self, other: Node[T]):
    if not isinstance(other, Node):
      return NotImplemented
    return self._val == other._val


class LinkedList(Generic[T]):
  def __init__(self, iterable: Iterable = []):
    self._head: Optional[Node[T]] = None
    self._length = 0
    curr_node = self._head
    for val in iterable:
      if self._head is None:
        self._head = Node(val)
        curr_node = self._head
        self._length += 1
        continue
      curr_node = cast(Node[T], curr_node)
      curr_node.set_next(Node(val))
      curr_node = curr_node.next()
      self._length += 1

  def append(self, val: T):
    """
    Appends `val` at the end of the linked-list
    """
    if self._head is None:
      self._head = Node(val)
    else:
      curr_node = self._head
      for _ in range(self._length - 1):
        if curr_node is None:
          raise Exception("Iteration Error")
        curr_node = curr_node.next()
      if curr_node is None:
        raise Exception("Iteration Error")
      curr_node.set_next(Node(val))
    self._length += 1
    return self

  def insert(self, index: int, val: T):
    """
    Appends `val` at the index `index`
    Raises IndexError if the index is out of bounds
    """
    if index > self._length or index < 0 - self._length or self._head is None:
      raise IndexError
    ind = index
    if ind < 0:
      ind = self._length + ind
    if ind == 0:
      next_node = self._head
      self._head = Node(val, next=next_node)
    else:
      curr_node = self._head
      for _ in range(ind - 1):
        if curr_node is None:
          raise Exception("Iteration Error")
        curr_node = curr_node.next()
      if curr_node is None:
        raise Exception("Iteration Error")
      curr_node.set_next(Node(val, next=curr_node.next()))
    self._length += 1
    return self

  def extend(self, iterable: Iterable[T]):
    """
    Appends all the elements in the iterable at the end of the LinkedList
    """
    last_node = None
    try:
      last_node = self._get_node(-1)
    except:
      pass
    for i in iterable:
      if last_node is None:
        self._head = Node(i)
        last_node = self._head
        self._length += 1
        continue
      last_node.set_next(Node(i))
      last_node = last_node.next()
      self._length += 1
    return self

  def pop(self, index: int = -1):
    if not self._index_exists(index):
      raise IndexError
    ind = index
    if ind < 0:
      ind = self._length + ind
    if self._length == 1:
      self._head = None
    elif ind == 0:
      self._head = cast(Node[T], self._head).next()
    else:
      prev_node = self._get_node(ind - 1)
      node = prev_node.next()
      next_node = node.next() if node is not None else None
      prev_node.set_next(next_node)
      del node
    self._length -= 1
    return self

  def remove(self, val: T):
    ind = 0
    for i in self:
      if i == val:
        self.pop(ind)
        break
      ind += 1
    return self

  def _index_exists(self, index: int):
    return not (index > self._length or index < 0 - self._length or self._head is None)

  def _get_node(self, index: int):
    if not self._index_exists(index):
      raise IndexError
    ind = index
    if ind < 0:
      ind = self._length + ind
    curr_node = self._head
    for _ in range(ind):
      if curr_node is None:
        raise Exception(f"Accessing None at index {_}")
      curr_node = curr_node.next()
    if curr_node is None:
      raise Exception(f"Accessing None at index {ind}")
    return curr_node

  def __iter__(self):
    curr_node = self._head
    while curr_node is not None:
      yield curr_node.val()
      curr_node = curr_node.next()

  def __getitem__(self, index: int):
    req_node = self._get_node(index)
    return req_node.val()

  def __setitem__(self, index: int, val: T):
    req_node = self._get_node(index)
    req_node.set_val(val)
    return self

  def __len__(self):
    return self._length

  def __str__(self) -> str:
    return " -> ".join([str(x) for x in self])


if __name__ == "__main__":
  my_arr: LinkedList[int] = LinkedList([1, 2, 3])
  print(f"List: {my_arr}")
  print(f"Length: {len(my_arr)}")
  for i in my_arr:
    print(i)
  print(list(my_arr))
