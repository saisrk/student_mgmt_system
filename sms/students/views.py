from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (ListView,
                                  DeleteView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  )

from .models import Student, Parent
from .forms import StudentCreateForm, ParentCreateForm

# Creating Student and Parent
class StudentCreateView(CreateView):
    form_class = StudentCreateForm
    template_name = "students/student_form.html"

class ParentCreateView(CreateView):
    form_class = ParentCreateForm
    template_name = "students/parent_form.html"

# Modify Student / Parent details
class StudentUpdateView(UpdateView):
    pass
# List Student details
class StudentListView(ListView):
    model = Student

# Student Detail
class StudentDetailView(DetailView):
    model = Student

# Delete Student and Parent details

def under_contruction(request):
    return HttpResponse("Under construction")
