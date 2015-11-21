from django.shortcuts import render

from django.http import HttpResponse

#Views for Students

def students_list(request):
	return render (request, 'students/students_list.html', {})

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




