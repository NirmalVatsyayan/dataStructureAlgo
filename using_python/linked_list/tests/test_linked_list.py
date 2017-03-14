import sys
import os.path

#sys.path.append(os.path.join(os.path.abspath(os.pardir), "linked_list"))
sys.path.append(os.path.abspath(os.pardir))

from singly_linked_list import SinglyLinkList
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkList()

    def tearDown(self):
        self.list = None

    
    def test_insert(self):
        self.list.insertAtBeginning("Nirmal")

        self.assertTrue(self.list.head.getData() == "Nirmal")
        self.assertTrue(self.list.head.getNext() is None)

    
    def test_insert_two(self):
        self.list.insertAtBeginning("Nirmal")
        self.list.insertAtBeginning("Vatsyayan")

        self.assertTrue(self.list.head.getData() == "Vatsyayan")

        head_next = self.list.head.getNext()
        self.assertTrue(head_next.getData() == "Nirmal")
    
    
    def test_nextNode(self):
        self.list.insertAtBeginning("1")
        self.list.insertAtBeginning("2")
        self.list.insertAtBeginning("3")

        self.assertTrue(self.list.head.getData() == "3")

        head_next = self.list.head.getNext()
        self.assertTrue(head_next.getData() == "2")

        last = head_next.getNext()
        self.assertTrue(last.getData() == "1")

    
    def test_positive_search(self):
        self.list.insertAtBeginning("1")
        self.list.insertAtEnd("2")
        self.list.insertAtEnd("3")

        found = self.list.search_list("1")
        self.assertTrue(found.getData() == "1")

        found = self.list.search_list("2")
        self.assertTrue(found.getData() == "2")

        found = self.list.search_list("3")
        self.assertTrue(found.getData() == "3")
    
    
    def test_searchNone(self):
        self.list.insertAtBeginning("1")
        self.list.insertAtEnd("2")

        # make sure reg search works
        found = self.list.search_list("1")

        self.assertTrue(found.getData() == "1")

        #with self.assertRaises(ValueError):
        #    self.list.search_list("2")

    
    def test_delete(self):
        self.list.insertAtBeginning("Nirmal")
        self.list.insertAtEnd("Vatsyayan")

        # Delete the list head
        self.list.delete("Nirmal")
        self.assertTrue(self.list.head.getData() == "Vatsyayan")

        # Delete the list tail
        self.list.delete("Vatsyayan")
        
        self.assertTrue(self.list.head is None)

#unittest.main()
#python -m unittest test_linked_list.TestLinkedList
