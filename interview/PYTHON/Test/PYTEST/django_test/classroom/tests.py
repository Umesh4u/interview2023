# from django.test import TestCase
# from classroom.models import Student
# from mixer.backend.django import mixer

# class TestStudentModel(TestCase):
# 	# def setUp(self):
# 	# 	self.student1 = Student.objects.create(
# 	# 				first_name='Tom', 
# 	# 				last_name='Mooya',
# 	# 				admission_number=123
# 	# 				)
# 	def test_add_a_plus_b(self):
# 		a = 1
# 		b = 2
# 		c = a + b
# 		#self.assertEqual(c,3)

# 		assert c == 3

# 	def test_student_can_be_created(self):
# 		# student1 = Student.objects.create(
# 		# 			first_name='Tom', 
# 		# 			last_name='Mooya',
# 		# 			admission_number=1234
# 		# 			)

# 		#student1 = mixer.blend(Student)
# 		student1 = mixer.blend(Student,first_name = "Tom")
# 		student_result = Student.objects.last()
# 		#self.assertEqual(student_result.first_name,"Tom")
# 		assert student_result.first_name == "Tom"

# 	def test_str_return(self):
# 		student1 = Student.objects.create(
# 					first_name='Tom', 
# 					last_name='Mooya',
# 					admission_number=1234
# 					)
# 		student_result = Student.objects.last()
# 		self.assertEqual(str(student_result),"Tom")


# 	# def test_grade_fail(self):
# 	# 	student1 = Student.objects.create(
# 	# 				first_name='Tom', 
# 	# 				last_name='Mooya',
# 	# 				admission_number=124,
# 	# 				average_score = 10
# 	# 				)
# 	# 	student_result = Student.objects.last()
# 	# 	self.assertEqual(student_result.get_grade(),"Fail")


# 	def test_grade_excellent(self):
# 		student1 = mixer.blend(Student,average_score=90)
# 		student_result = Student.objects.last()
# 		self.assertEqual(student_result.get_grade(),"Excellent")

# 	def test_grade_excellent(self):
# 		student1 = mixer.blend(Student,average_score=60)
# 		student_result = Student.objects.last()
# 		self.assertEqual(student_result.get_grade(),"Pass")



import pytest
from classroom.models import Product
pytestmark = pytest.mark.django_db

class TestProductModel:
    def test_save(self):
        product = Product.objects.create(
            name="Sample product",
            price=500
        )
        assert product.name == "Sample product"
        assert product.price == 500
