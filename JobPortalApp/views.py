from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from JobPortalApp.forms import UserRegisterForm, UserLoginForm, JobForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from JobPortalApp.models import Job
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = 'home.html'

class UserHome(ListView):
    model = Job
    template_name = 'userhome.html'
    context_object_name = "datakey"

class UserRegister(View):
    
    def get(self,request):
        form = UserRegisterForm()
        return render(request,'register.html',{'form':form})
    
    def post(self,request):
        data = UserRegisterForm(request.POST)
        if data.is_valid():
            User.objects.create_user(**data.cleaned_data)
            return redirect('Login')
        else:
            return HttpResponse("Invalid Credentials")
        
class UserLogin(View):
    
    def get(self,request):
        form = UserLoginForm()
        return render(request,'login.html',{'formkey':form})
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect('UserHome')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('Login')

        
class UserLogout(View):

    def get(self,request):
        logout(request)
        return redirect('Home')
    
class CreateJob(CreateView):
    form_class = JobForm
    template_name = 'create_job.html'
    model = Job 
    success_url = reverse_lazy('List')

class ListJob(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = "datakey"

class EditJob(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job_edit.html'
    success_url = reverse_lazy('List')
    pk_url_kwarg = 'id'

class DeleteJob(DeleteView):
    model = Job
    template_name = 'job_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('List')