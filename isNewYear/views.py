from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.
def index(request, name, num):
   return render(request, 'isNewYear/index.html',{
      'isNewYear': datetime.now().month == 1 and datetime.now().day == 1,
      'name': name,
      'num': num
   })
