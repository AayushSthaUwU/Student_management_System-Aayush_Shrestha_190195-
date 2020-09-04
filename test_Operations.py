from unittest import TestCase
from Operations import operation
from Mainpg import *


class Testoperation(TestCase):

    def test_add_student(self):
        b = Add_Student()
        result = b.add_student("test_fname", "test_lname", "test_course","test_mobile","test_email","test_gender","test_dob","test_address","test_country")
        self.assertTrue(result)

    def test_add_student2(self):
        b = Add_Student()
        result = b.add_student("", "", "", "", "", "","", "", "")
        self.assertFalse(result)

    def test_show_all_student(self):
        b = Update_Student()
        result = b.all_student()
        actual_result= len(result)
        expected_result = 4
        self.assertEqual(actual_result,expected_result)

    def test_search(self):
        b = Update_Student()
        result = b.search(1)
        self.assertTrue(result)

    def test_remove_student(self):
        b = Update_Student()
        result = b.remove_student(12)
        self.assertTrue(result)



