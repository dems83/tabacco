from django.shortcuts import render


def index(request):
	context = {

	}
	return render(request, "tabacco/index.html", context)



def about(request):
	context = {

	}
	return render(request, 'tabacco/about.html', context)


def accessories(request):
	context = {

	}
	return render(request, 'tabacco/accessories.html', context)


def catalog(request):
	context = {
	
	}
	return render(request, 'tabacco/catalog.html', context)


def contact(request):
	context = {
	
	}
	return render(request, 'tabacco/contact.html', context)
