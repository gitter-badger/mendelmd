
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
	# print "Hello"
	#if user is logged redirect
	if request.user.is_authenticated():
		return redirect('dashboard')

	return render(request, 'index.html')