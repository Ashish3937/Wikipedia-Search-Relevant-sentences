from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .test4django import main

# Create your views here.
def index(request):
    query="wikipedia"
    number=int(4)
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():

            query=form.cleaned_data['query']
            number=form.cleaned_data['number']
    result=main(query,number)
    form=ContactForm()
    return render(request,'first_app/index.html',{'form':form,'result':result})    

