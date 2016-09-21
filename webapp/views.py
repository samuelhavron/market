from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import User
from django.forms import ModelForm
from webapp.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import json
import os

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email_address']

def inspect_user(request):
	user = int(os.path.basename(os.path.normpath(request.path)))
	print(user)
	print(type(user))
	for u in User.objects.all():
		print(u)
	try: 
		obj= User.objects.get(pk=user)
		
		print(obj)
		
	except ObjectDoesNotExist as e:
		return HttpResponse('user does not exist')
	

	print(obj)
	if request.method == 'GET':
		print(request.GET)
		return HttpResponse('way to GET it')
	else: 
		return HttpReponse('go GET em tiger')

def create_user(request):
    dictionary = {}
    if request.method == 'POST':
        #print(request.POST)
        #create a form to add an article
        form = UserForm(request.POST)
        
        
        #print(request.POST)
        for key in request.POST:

          #print(key)
          #print (1)
          v = request.POST[key]
          #print(v)
        if form.is_valid():
            print ("VALID!")
            try:
                new_user = form.save(commit='false')

                print (new_user)
                #new_user.username = 'bob'
                new_user.save()
                users = User.objects.all().order_by('username')
                print (users)
                for u in User.objects.all():
                  u.delete()
                print (users)



         #       print(type(new_user))

         #       print("form looks like:")
        #        print(form)
                
                dictionary = form

                #u = models.User(username=request.POST['username'],
                #         password=request.POST['password'],
                #         email_address=request.POST['email_address'])
                #u.save()
                # return JsonResponse()
                return HttpResponse(json.dumps(new_user.to_json()), content_type="application/json")

            except IntegrityError as e:
                return HttpResponse("problem saving data")
        else:
            for u in User.objects.all():
              u.delete()
            print ("NOOOOOOOOOOOOOOOOOOO VALID!")
            #print (form)
            # print (form.errors)
            return HttpResponse(form.errors)
    else:
        return HttpResponse("not working")
