from django.shortcuts import render
import numpy as n
from django import forms
def index(request):
    return render(request,'index.html')
def root(request):
    return render(request,'root.html')
def quadratic(request):
      class quadform(forms.Form):
           x2=forms.IntegerField(label='Co-eff of  X^2 ')
           print(end='/n')
           x=forms.IntegerField(label='Co-eff of  X ')
           const=forms.IntegerField(label='Constant term')
      if request.method=='POST':
            form=quadform(request.POST)
            if form.is_valid():
                 x=form.cleaned_data['x2']
                 y=form.cleaned_data['x']
                 z=form.cleaned_data['const']
                 res=n.roots([x,y,z])
                 return render(request,'result2.html',{'res':res})

      return render(request,'quad.html',{'form':quadform()})
def cubic(request):
      class cubicform(forms.Form):
             x3=forms.IntegerField(label='Co-eff of X^3')
             x2=forms.IntegerField(label='Co-eff of X^2')
             x=forms.IntegerField(label='Co-eff of X')
             Const=forms.IntegerField(label='Constant term')
      if request.method=="POST":
            form=cubicform(request.POST)
            if form.is_valid():
                 a=form.cleaned_data['x3']
                 b=form.cleaned_data['x2']
                 c=form.cleaned_data['x']
                 d=form.cleaned_data['Const']
                 res=n.roots([a,b,c,d])
                 return render(request,'result3.html',{'res':res.real})
      return render(request,'cubic.html',{'form':cubicform()})
# Create your views here.
