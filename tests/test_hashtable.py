import unittest
from typing import TypeVar, Tuple
from data_structures.hashtable import HashTable, HashFunction

S = TypeVar('S', str, int)
T = TypeVar('T')


class SimpleHashFunction(HashFunction[S]):
  @staticmethod
  def hash(key: S) -> int:
    return len(str(key)) % 10


class HashTableTests(unittest.TestCase):
  def test_insert_and_search(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    self.assertEqual(hash_table.search("key1"), "value1")
    self.assertEqual(hash_table.search("key2"), "value2")
    self.assertEqual(hash_table.search("key3"), "value3")

  def test_search_nonexistent_key(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")

    self.assertIsNone(hash_table.search("nonexistent_key"))

  def test_delete(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    hash_table.delete("key2")

    self.assertIsNone(hash_table.search("key2"))
    self.assertEqual(hash_table.search("key1"), "value1")
    self.assertEqual(hash_table.search("key3"), "value3")

  def test_update(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value")

    hash_table.update("key1", "new_value1")
    hash_table.update("key3", "value3")

    self.assertEqual(hash_table.search("key1"), "new_value1")
    self.assertEqual(hash_table.search("key2"), "value2")
    self.assertEqual(hash_table.search("key3"), "value3")

  def test_keys(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    self.assertEqual(sorted(hash_table.keys()), ["key1", "key2", "key3"])

  def test_values(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    self.assertEqual(sorted(hash_table.values()), [
                     "value1", "value2", "value3"])

  def test_items(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    expected_items = [("key1", "value1"),
                      ("key2", "value2"), ("key3", "value3")]
    self.assertEqual(sorted(hash_table.items()), sorted(expected_items))

  def test_setitem_and_getitem(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table["key1"] = "value1"
    hash_table["key2"] = "value2"

    self.assertEqual(hash_table["key1"], "value1")
    self.assertEqual(hash_table["key2"], "value2")

  def test_delitem(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")

    del hash_table["key1"]

    self.assertIsNone(hash_table.search("key1"))
    self.assertEqual(hash_table.search("key2"), "value2")

  def test_contains(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")

    self.assertTrue("value1" in hash_table)
    self.assertTrue("value2" in hash_table)
    self.assertFalse("value3" in hash_table)

  def test_iteration(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    expected_items = [("key1", "value1"),
                      ("key2", "value2"), ("key3", "value3")]
    self.assertEqual(sorted(list(hash_table)), sorted(expected_items))

  def test_str(self):
    hash_table = HashTable(SimpleHashFunction)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")

    expected_string = "{ key1: value1, key2: value2 }"
    self.assertEqual(str(hash_table), expected_string)


if __name__ == '__main__':
  unittest.main()
