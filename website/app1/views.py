from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app1/index.html', None)


def process_form(request):

	data = {}
	input1 = request.POST.get('input2')
	input2  = request.POST.get('input1')

	data['input1'] = input1
	data['input2'] = input2

	return render(request, 'app1/response.html', data)



