from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

class NewTaskFrom(forms.Form):
   task = forms.CharField(label="Task")
   priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
   if 'tasks' not in request.session:
      request.session['tasks'] = []
   return render(request, 'todo/index.html', {
      'tasks': request.session['tasks']
   })

def add(request):
   if request.method == 'POST':
      form = NewTaskFrom(request.POST)
      if form.is_valid():
         task = form.cleaned_data['task']
         request.session['tasks'] += [task]
         return HttpResponseRedirect(reverse("todo:index"))
      else:
         return render(request, 'todo/add.html', {
            'newTaskForm': form
         })
   return render(request, 'todo/add.html', {
      'newTaskForm': NewTaskFrom
   })