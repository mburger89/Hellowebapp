from django.shortcuts import render

# Create your views here.
def index(request):
	# definig the variable
	number = 6
	#this is your new view
	return render(request, 'index.html', {
		'number': number,
	})