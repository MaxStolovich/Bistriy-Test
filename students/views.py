# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students_list(request):
	students = (
	   {'id': 1,
		'first_name': u'Вадим',
		'last_name' : u'Сидур',
		'ticket' : 2123,
		'image': 'image/dog.jpg'},
		{'id': 2,
		'first_name': u'Александр',
		'last_name' : u'Романов',
		'ticket' : 254,
		'image': 'image/dog2.jpg'},
		{'id': 3,
		'first_name': u'Хрущ',
		'last_name' : u'Артем',
		'ticket' : 5332,
		'image': 'image/sepia.jpg'},
		{'id': 4,
		'first_name': u'Виктор',
		'last_name' : u'Невик',
		'ticket' : 3312,
		'image': 'image/bird.jpg'},
		{'id': 5,
		'first_name': u'Екатерина',
		'last_name' : u'Кудрик',
		'ticket' : 303,
		'image': 'image/cat.jpg'},
		
	)
	return render(request,
	 'students/students_list.html', 
	 {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid) 
	
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid) 
		
# Views for Groups
		
def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>') 	
	
def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
	
