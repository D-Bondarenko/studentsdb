# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse

def groups_list(request):
	return render(request, 'students/groups_list.html', {})

def groups_add(request):
	return HttpResponse('Group Add Form')

def groups_edit(request, gid):
	return HttpResponse('Edit group %s' % gid)

def groups_delete(request, gid):
	return HttpResponse('Delete group %s' % gid)
