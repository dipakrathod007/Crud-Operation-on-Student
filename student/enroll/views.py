from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']        # This is used for add the data or save the data one by one
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm=StudentRegistration()     #    This is used for when you have to take input in form after add button the form will be claer or blank form
    else:
        fm = StudentRegistration()
    stud = User.objects.all()    # This is used for all the data are show to the front end 
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})




def delete_data(request,id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')



def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        print(pi)
        fm=StudentRegistration(request.POST, instance=pi)
        print(fm)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request, 'enroll/updatefile.html',{'form':fm})
    
