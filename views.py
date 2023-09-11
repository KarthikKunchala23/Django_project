
from signal import CTRL_BREAK_EVENT
from turtle import bgcolor
from django.shortcuts import redirect, render,HttpResponse
from . import models 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required 
from . import forms
from rest_framework.response import Response
from .serializer import studentSerializer
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin 
# from rest_framework.serializers import Serializer


class studentlist(GenericAPIView,ListModelMixin):
    queryset=models.student.objects.all()
    serializer_class=studentSerializer
    def get(self,request):
        return self.list(request)


class studentretrieve(GenericAPIView,RetrieveModelMixin):
    queryset=models.student.objects.all()
    serializer_class= studentSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request, **kwargs)


class studentCreate(GenericAPIView,CreateModelMixin):
    queryset=models.student.objects.all()
    serializer_class=studentSerializer
    def post(self,request,**kwargs):
        return self.create(request,**kwargs)

class studentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=models.student.objects.all()
    serializer_class=studentSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)

class studentDelete(GenericAPIView,DestroyModelMixin):
    queryset=models.student.objects.all()
    serializer_class=studentSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)


# Create your views here.
#@api_view(['GET'])
def home(request):
    #   objs=models.student.objects.all()
    #   serial= studentSerializer(objs,many=True)
    #   print(serial.data)
    #   return Response(serial.data) 
    
    # for obj in objs:
    #     print(obj.id,obj.name,obj.mobile,obj.address,obj.email)
    d={
       'bgcolor':'lightblue',
    }
    return render(request,'home.html',d)
  
    
def about(request):
    d={'name':'karthik'}
    return render(request,'about.html',d)
def contact(request):
    d={
        'address':{
            'address1':{
            'HNO':'13-12/A',
            'Colony':'Gopal Nagar',
            'PIN':523101,
            'CONTACT':8074497946,
            },
            'address2':{
                'HNO':'65/B',
                'Colony':'sri ram nagar',
                'PIN':523101,
                'CONTACT':7659960744,
            }
            }
        }
    
    return render(request,'contact.html',d)

def showdata(request):
    d={
        'body_color':'white',
        'table_data':{
            'data1':{
                'name':'Karthik','mobile':8074497946,
                'address':'singarayakonda','email':'karthikkunchala2307@gmail.com',
            },
            'data2':{
                'name':'Raju','mobile':7659960744,
                'address':'hyderabad','email':'karthikkunchala170@gmail.com',
            },
            'data3':{
                'name':'Rishi','mobile':9959978174,
                'address':'kerala','email':'karthikkunchala2398@gmail.com',
            },
        }
    }
    return render(request,'showdata.html',d)

# @login_required(login_url='loggin')
# def insertdata(request):
#   if request.method == 'POST':
#       obj=models.student()
#       obj.name='karthik' #request.POST['name']
#       obj.mobile='7659960744' #request.POST['mobile']
#       obj.address='singarayakonda523101' #request.POST['address']
#       obj.email='karthikkunchala2307@gmail.com' #request.POST['email']
#       obj.save()
#       return HttpResponse('{},record inserted'.format(obj.name))
#   else:
#       return HttpResponse('record not inserted')


# @login_required(login_url='loggin')
@api_view(['POST'])
def insert(request):
    ser=studentSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)


@api_view(['PUT'])
def update(request,id):
    obj=models.student.objects.get(id=id)
    serial=studentSerializer(instance=obj,data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

    # if request.method == 'POST':
    #   obj= models.student()
    #   obj.name='Apoorva' #request.POST['name']
    #   obj.mobile='7659960744' #request.POST['mobile']
    #   obj.address='hyderabad' #request.POST['address']
    #   obj.email='apoorva2307@gmail.com' #request.POST['email']
    #   obj.save()
    #   return HttpResponse('{},record inserted'.format(obj.name))
    # # else:
    # #   return HttpResponse('record not inserted')
    # d={
    #     'bgcolor1':'indianRed',
    #     'bgcolor2':'LightCoral',
    # }
    # return render(request,'insert.html',d)


@login_required(login_url='loggin')
def showdata2(request):
    obj=models.student.objects.all()
    d={
        'data':obj,
        'bgcolor':'Salmon',

    }
    return render(request,'showdata2.html',d) 


@login_required(login_url='loggin')
def delete(request,id):
    obj=models.student.objects.get(id=id)
    obj.delete()
    return HttpResponse('object deleted')


# @login_required(login_url='loggin')
# def update(request,id):
#     obj=models.student.objects.get(id=id)
#     d={
#         'data':obj,
#         'bgcolor':'indianRed'
#     }
#     return render(request,'update.html',d)


@login_required(login_url='loggin')
def modify(request):
    if request.method == 'POST':
        obj=models.student.objects.get(id=request.POST['id'])
        obj.name=request.POST['name']
        obj.mobile=request.POST['mobile']
        obj.address=request.POST['address']
        obj.email=request.POST['email']
        obj.save()
        return HttpResponse('record updated')
    return HttpResponse('record not updated')

def loggin(request):
    return render(request,'login.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password,sep='##')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(home)
        return redirect(loggin)

def loggout(request):
    logout(request)
    return redirect(home)


def form(request):
       if request.method == 'POST':
          myform = forms.studentform(request.POST)
          if myform.is_valid():
             myform.save()
          return redirect(showdata2)
       else:
            myform = forms.studentform
            d = {
            'form':myform,
              }
            return render(request,'form.html',d)
