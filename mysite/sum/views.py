from django.shortcuts import render
from .forms import SumForm

def index(request):
	if request.method == 'POST':
		intsum = None
		form = SumForm(request.POST)
		if form.is_valid():
			x = form.cleaned_data['x']
			y = form.cleaned_data['y']
			intsum = x + y

		return render(request, 'sum/home.html', {'content':intsum})


	else:
		return render(request, 'sum/home.html')
    
