from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import StudentSerializer
from .models import Student

# Create your views here.

# {
# "name":"Kusum Kumari",
# "mobile":"9643661724",
# "address":"om garden"
# }
class StudentData(APIView):
	# permissions_class =[IsAuthenticated]

	def get_object(self,pk):
		try:
			return Student.objects.get(id=pk)
		except Student.DoesNotExist:
			raise Http404


	def get(self,request):
		stu = Student.objects.all()
		stu_serialize = StudentSerializer(stu,many=True)
		return Response(stu_serialize.data,status=200)

	def post(self,request):
		data=request.data
		stu_data = StudentSerializer(data=data)
		if stu_data.is_valid():
			stu_data.save()
			return Response(stu_data.data,status=201)
		return Response(stu_data.errors,status=400)


	def put(self, request,pk):
		obj = self.get_object(self,request.query_params.get("id"))
		stu_data = StudentSerializer(obj,data=request.data)
		if stu_data.is_valid():
			stu_data.save()
			return Response(stu_data.data)
		return Response(stu_data.errors,status=400)

	def delete(self,request):
		obj = self.get_object(self,request.query_params.get("id"))
		obj.delete()
		return Response(status=204)



