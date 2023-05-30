import unittest
from data_structures.linkedlist import LinkedList


class LinkedListTests(unittest.TestCase):
  def test_append(self):
    # Arrange
    linked_list = LinkedList()

    # Act
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Assert
    self.assertEqual(list(linked_list), [1, 2, 3])
    self.assertEqual(len(linked_list), 3)

  def test_insert(self):
    # Arrange
    linked_list = LinkedList([1, 3, 4])

    # Act
    linked_list.insert(1, 2)

    # Assert
    self.assertEqual(list(linked_list), [1, 2, 3, 4])
    self.assertEqual(len(linked_list), 4)

  def test_extend(self):
    # Arrange
    linked_list = LinkedList([1, 2])

    # Act
    linked_list.extend([3, 4, 5])

    # Assert
    self.assertEqual(list(linked_list), [1, 2, 3, 4, 5])
    self.assertEqual(len(linked_list), 5)

  def test_pop(self):
    # Arrange
    linked_list = LinkedList([1, 2, 3])

    # Act
    linked_list.pop(1)

    # Assert
    self.assertEqual(list(linked_list), [1, 3])
    self.assertEqual(len(linked_list), 2)

  def test_getitem(self):
    # Arrange
    linked_list = LinkedList([1, 2, 3])

    # Act
    item = linked_list[1]

    # Assert
    self.assertEqual(item, 2)

  def test_len(self):
    # Arrange
    linked_list = LinkedList([1, 2, 3, 4, 5])

    # Act
    length = len(linked_list)

    # Assert
    self.assertEqual(length, 5)

  def test_insert_at_index_0(self):
    linked_list = LinkedList([1, 2, 3])
    linked_list.insert(0, 0)
    self.assertEqual(list(linked_list), [0, 1, 2, 3])
    self.assertEqual(len(linked_list), 4)

  def test_insert_at_index_negative_1(self):
    linked_list = LinkedList([1, 2, 4])
    linked_list.insert(-1, 3)
    self.assertEqual(list(linked_list), [1, 2, 3, 4])
    self.assertEqual(len(linked_list), 4)

  def test_pop_at_index_0(self):
    linked_list = LinkedList([1, 2, 3])
    linked_list.pop(0)
    self.assertEqual(list(linked_list), [2, 3])
    self.assertEqual(len(linked_list), 2)

  def test_pop_at_index_negative_1(self):
    linked_list = LinkedList([1, 2, 3])
    linked_list.pop(-1)
    self.assertEqual(list(linked_list), [1, 2])
    self.assertEqual(len(linked_list), 2)


if __name__ == "__main__":
  unittest.main()
