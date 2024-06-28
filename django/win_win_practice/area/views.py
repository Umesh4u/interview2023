from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Area,City,State
# Create your views here.

@api_view(['GET'])
def areas_list(request):
	result=[] # for Final json

	# Fetch area data
	area_data = Area.objects.all().values()
	for data in area_data:
		new_dict={}
		new_dict['area_name']=data['name']
		new_dict['id']=data['id']
		new_dict['priority']=data['priority']

		# Fetch and manipulate state data
		state_list=[]
		state_data = State.objects.filter(area=data['id']).values()
		for state in state_data:
			new_state_dict={}
			new_state_dict['state_name']=state['name']
			new_state_dict['id']=state['id']
			new_state_dict['area_id']=state['area_id']
			state_list.append(new_state_dict)

			#Fetch and manipulate city data
			city_data = City.objects.filter(state=state['id']).values()
			city_list=[]
			for city in city_data:
				new_city_dict={}
				new_city_dict['city_name']=city['name']
				new_city_dict['id']=city['id']
				city_list.append(new_city_dict)
				new_state_dict['city']=city_list

			new_dict['state']=state_list
		result.append(new_dict)

	return Response(result)
