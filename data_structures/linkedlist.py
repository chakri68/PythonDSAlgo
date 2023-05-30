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
    curr_node = self._head
    for _ in range(self._length - 1):
      if curr_node is None:
        raise Exception("Iteration Error")
      curr_node = curr_node.next()
    for i in iterable:
      if curr_node is None:
        self._head = Node(i)
        curr_node = self._head
        self._length += 1
        continue
      curr_node.set_next(Node(i))
      curr_node = curr_node.next()
      self._length += 1
    return self

  def pop(self, index: int = -1):
    if index > self._length or index < 0 - self._length or self._head is None:
      raise IndexError
    ind = index
    if ind < 0:
      ind = self._length + ind
    if self._length == 1:
      self._head = None
    elif ind == 0:
      self._head = self._head.next()
    else:
      curr_node = self._head
      for _ in range(ind - 1):
        if curr_node is None:
          raise Exception("Iteration Error")
        curr_node = curr_node.next()
      if curr_node is None or curr_node.next() is None:
        raise Exception("Iteration Error")
      node = curr_node.next()
      prev_node = curr_node
      next_node = node.next() if node is not None else None
      prev_node.set_next(next_node)
      del node
    self._length -= 1
    return self

  def _check_index(self, index: int):
    return not (index > self._length or index < 0 - self._length or self._head is None)

  def __iter__(self):
    curr_node = self._head
    while curr_node is not None:
      yield curr_node.val()
      curr_node = curr_node.next()

  def __getitem__(self, index: int):
    if index > self._length or index < 0 - self._length or self._head is None:
      raise IndexError
    curr_ind = 0
    curr_node = self._head
    ind = index
    if index < 0:
      ind = self._length + index
    while curr_ind < ind:
      if curr_node is None:
        raise Exception(f"Accessing None at index {curr_ind}")
      curr_node = curr_node.next()
      curr_ind += 1
    if curr_node is None:
      raise Exception(f"Accessing None at index {curr_ind}")
    return curr_node.val()

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
