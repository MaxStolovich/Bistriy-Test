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
		'image': 'images/dog.jpeg'},
		{'id': 2,
		'first_name': u'Александр',
		'last_name' : u'Романов',
		'ticket' : 254,
		'image': 'images/dog2.jpeg'},
		{'id': 3,
		'first_name': u'Хрущ',
		'last_name' : u'Артем',
		'ticket' : 5332,
		'image': 'images/sepia.jpeg'},
		{'id': 4,
		'first_name': u'Виктор',
		'last_name' : u'Невик',
		'ticket' : 3312,
		'image': 'images/bird.jpeg'},
		{'id': 5,
		'first_name': u'Екатерина',
		'last_name' : u'Кудрик',
		'ticket' : 303,
		'image': 'images/cat.jpeg'},
		
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
	groups = (
	   {'id': 1,
		'group_name': u'МТМ-21',
		'lead' : u'Сидур',},
		{'id': 2,
		'group_name': u'МТМ-22',
		'lead' : u'Хрущ',},
		{'id': 3,
		'group_name': u'МТМ-23',
		'lead' : u'Невик',},
		
	)
	return render(request,
	 'students/groups_list.html', 
	 {'groups': groups})
	
def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
	
