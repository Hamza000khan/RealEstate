from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Realtor
from django.utils import timezone


#@login_required(login_url="/accounts/login")
# def create(request):
# 	if request.method == 'POST':
# 		if request.POST['name'] and request.FILES['photo'] and request.POST['description'] and request.POST['email'] and request.POST['hire_date']:
# 			realtor = Realtor()
# 			realtor.name = request.POST['title']
# 			realtor.photo = request.FILES['photo']
# 			realtor.description = request.POST['description']
# 			realtor.email = request.POST['email']
# 			realtor.hire_date = timezone.datetime.now()
# 			realtor.save()
# 			return redirect('/listings/'+ str(realtor.id))
# 		else:
# 			return render(request, '/listings/', {'error': 'All Fields are required'})
# 	else:
# 		return render(request, '/listings/')

def detail(request, realtor_id):
	realtor = get_object_or_404(Realtor, pk=realtor_id)
	return render(request, 'listings/detail/', {'realtor':realtor})