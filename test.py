import unittest
from bloom_filter import BloomFilter
from hashtable_chaining import HashTable as hashtable_chaining
from hashtable_linear_probing import HashTable as hashtable_linear_probing


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bf = BloomFilter()

    def test_basic_add(self):
        self.bf.add_elem("example_elem")
        self.assertTrue(self.bf.check_membership("example_elem"))

    def test_basic_empty(self):
        self.assertFalse(self.bf.check_membership("bad"))

    def test_bad_membership_with_elements(self):
        self.assertFalse(self.bf.check_membership("test"))
        self.bf.add_elem("test")
        self.assertTrue(self.bf.check_membership("test"))

    def test_bad_with_one_element(self):
        self.bf.add_elem("test1")
        self.assertFalse(self.bf.check_membership("test2"))

class TestHashtableChaining(unittest.TestCase):

    def setUp(self):
        self.ht = hashtable_chaining()

    def test_empty_ht(self):
        self.assertEqual(self.ht.size(), 0)

    def test_one_insert(self):
        self.ht.insert("test", "val")
        self.assertEqual(self.ht.size(), 1)
        self.assertEqual(self.ht.get("test"), "val")

    def test_insert_remove(self):
        self.ht.insert("test", "val")
        self.ht.remove("test")
        self.assertEqual(self.ht.size(), 0)
        self.assertIsNone(self.ht.get("test"))

    def test_array_size(self):
        for i in xrange(7):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 10)
        self.ht.insert("test8", "val")
        self.assertEqual(self.ht.array_size, 20)

    def test_array_size2(self):
        for i in xrange(14):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 20)
        self.ht.insert("test15", "val")
        self.assertEqual(self.ht.array_size, 40)

    def test_array_size3(self):
        for i in xrange(14):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 20)
        self.ht.insert("test14", "val")
        self.assertEqual(self.ht.array_size, 40)
        for i in xrange(15):
            self.ht.remove("test" + str(i))
        self.assertEqual(self.ht.size(), 0)
        self.assertEqual(self.ht.array_size, 40)

    def test_adding_new_values(self):
        self.ht.insert("test", "value 1")
        self.ht.insert("test", "value 2")
        self.assertEqual(self.ht.get("test"), "value 2")
        self.assertEqual(self.ht.size(), 1)

    def test_remove_empty(self):
        rem_val = self.ht.remove("nothing")
        self.assertIsNone(rem_val)

    def test_remove_has_right_value(self):
        self.ht.insert("test", "val")
        rem_val = self.ht.remove("test")
        self.assertEqual(rem_val, "val")

    def test_100(self):
        full_list = [(str(i), "temp" + str(i)) for i in xrange(100)]
        in_list = []
        out_list = []

        for k,v in full_list:
            self.ht.insert(k,v)
            in_list.append((k,v))
            self.assertEqual(self.ht.size(), len(in_list))
            self.assertEqual(self.ht.get(k), v)

        for k,v in full_list:
            rem_val = self.ht.remove(k)
            out_list.append((k,v))
            self.assertEqual(self.ht.size(), 100-len(out_list))
            self.assertEqual(rem_val, v)

    def test_1000(self):
        full_list = [(str(i), "temp" + str(i)) for i in xrange(1000)]
        in_list = []
        out_list = []

        for k,v in full_list:
            self.ht.insert(k,v)
            in_list.append((k,v))
            self.assertEqual(self.ht.size(), len(in_list))
            self.assertEqual(self.ht.get(k), v)

        for k,v in full_list:
            rem_val = self.ht.remove(k)
            out_list.append((k,v))
            self.assertEqual(self.ht.size(), 1000-len(out_list))
            self.assertEqual(rem_val, v)

    def test_10000(self):
        full_list = [(str(i), "temp" + str(i)) for i in xrange(10000)]
        in_list = []
        out_list = []

        for k,v in full_list:
            self.ht.insert(k,v)
            in_list.append((k,v))
            self.assertEqual(self.ht.size(), len(in_list))
            self.assertEqual(self.ht.get(k), v)

        for k,v in full_list:
            rem_val = self.ht.remove(k)
            out_list.append((k,v))
            self.assertEqual(self.ht.size(), 10000-len(out_list))
            self.assertEqual(rem_val, v)

    def test_load_factor_1(self):
        self.ht = hashtable_chaining(10, 1)
        for i in xrange(11):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 20)

    def test_insert_exception1(self):
        self.assertRaises(Exception, self.ht.insert, None, 'val')

    def test_insert_exception2(self):
        self.assertRaises(Exception, self.ht.insert, 'val', None)

    def test_get_exception1(self):
        self.assertRaises(Exception, self.ht.get, None)

    def test_remove_exception(self):
        self.assertRaises(Exception, self.ht.remove, None)

class TestHashtableProbing(unittest.TestCase):
    
    def setUp(self):
        self.ht = hashtable_linear_probing()

    def test_empty_ht(self):
        self.assertEqual(self.ht.size(), 0)

    def test_one_insert(self):
        self.ht.insert("test", "val")
        self.assertEqual(self.ht.size(), 1)
        self.assertEqual(self.ht.get("test"), "val")

    def test_insert_remove(self):
        self.ht.insert("test", "val")
        self.ht.remove("test")
        self.assertEqual(self.ht.size(), 0)
        self.assertIsNone(self.ht.get("test"))

    def test_array_size(self):
        for i in xrange(7):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 10)
        self.ht.insert("test8", "val")
        self.assertEqual(self.ht.array_size, 20)

    def test_array_size2(self):
        for i in xrange(14):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 20)
        self.ht.insert("test14", "val")
        self.assertEqual(self.ht.array_size, 40)

    def test_array_size3(self):
        for i in xrange(14):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 20)
        self.ht.insert("test14", "val")
        self.assertEqual(self.ht.array_size, 40)
        for i in xrange(15):
            self.ht.remove("test" + str(i))
        self.assertEqual(self.ht.size(), 0)
        self.assertEqual(self.ht.array_size, 40)

    def test_adding_new_values(self):
        self.ht.insert("test", "value 1")
        self.ht.insert("test", "value 2")
        self.assertEqual(self.ht.get("test"), "value 2")
        self.assertEqual(self.ht.size(), 1)

    def test_remove_empty(self):
        rem_val = self.ht.remove("nothing")
        self.assertIsNone(rem_val)

    def test_remove_has_right_value(self):
        self.ht.insert("test", "val")
        rem_val = self.ht.remove("test")
        self.assertEqual(rem_val, "val")

    def test_100(self):
        full_list = [(str(i), "temp" + str(i)) for i in xrange(100)]
        in_list = []
        out_list = []

        for k,v in full_list:
            self.ht.insert(k,v)
            in_list.append((k,v))
            self.assertEqual(self.ht.size(), len(in_list))
            self.assertEqual(self.ht.get(k), v)

        for k,v in full_list:
            rem_val = self.ht.remove(k)
            out_list.append((k,v))
            self.assertEqual(self.ht.size(), 100-len(out_list))
            self.assertEqual(rem_val, v)

    def test_1000(self):
        full_list = [(str(i), "temp" + str(i)) for i in xrange(1000)]
        in_list = []
        out_list = []

        for k,v in full_list:
            self.ht.insert(k,v)
            in_list.append((k,v))
            self.assertEqual(self.ht.size(), len(in_list))
            self.assertEqual(self.ht.get(k), v)

        for k,v in full_list:
            rem_val = self.ht.remove(k)
            out_list.append((k,v))
            self.assertEqual(self.ht.size(), 1000-len(out_list))
            self.assertEqual(rem_val, v)

    def test_10000(self):
        full_list = [(str(i), "temp" + str(i)) for i in xrange(10000)]
        in_list = []
        out_list = []

        for k,v in full_list:
            self.ht.insert(k,v)
            in_list.append((k,v))
            self.assertEqual(self.ht.size(), len(in_list))
            self.assertEqual(self.ht.get(k), v)

        for k,v in full_list:
            rem_val = self.ht.remove(k)
            out_list.append((k,v))
            self.assertEqual(self.ht.size(), 10000-len(out_list))
            self.assertEqual(rem_val, v)

    def test_load_factor_1(self):
        self.ht = hashtable_linear_probing(10, 1)
        for i in xrange(11):
            self.ht.insert("test" + str(i), "val")
        self.assertEqual(self.ht.array_size, 20)

    def test_insert_exception1(self):
        self.assertRaises(Exception, self.ht.insert, None, 'val')

    def test_insert_exception2(self):
        self.assertRaises(Exception, self.ht.insert, 'val', None)

    def test_get_exception1(self):
        self.assertRaises(Exception, self.ht.get, None)

    def test_remove_exception(self):
        self.assertRaises(Exception, self.ht.remove, None)

if __name__ == '__main__':
    unittest.main()
