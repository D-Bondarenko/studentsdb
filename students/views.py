# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse

#Views for Students

def students_list(request):
	students = (
		{'id': 1,
		'first_name': u'Віталій',
		'last_name': u'Подоба',
		'ticket': 235,
		'image': 'img/me.jpeg'},

		{'id': 2,
		'first_name': u'Корост',
		'last_name': u'Андрій',
		'ticket': 2123,
		'image': 'img/piv.png'},
		)
		
	return render (request, 'students/students_list.html', {'students':students})

def students_add(request):
	return HttpResponse('Student Add Form')

def students_edit(request, sid):
	return HttpResponse('Edit Student %s' % sid)

def students_delete(request, sid):
	return HttpResponse('Delete Student %s' % sid)


# views for Groups

def groups_list(request):
	return HttpResponse('Groups listing')

def groups_add(request):
	return HttpResponse('Group Add Form')

def groups_edit(request, gid):
	return HttpResponse('Edit group %s' % gid)

def groups_delete(request, gid):
	return HttpResponse('Delete group %s' % gid)




