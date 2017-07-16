from django import forms

from .models import Student, Parent

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email_id",
            "address",
            "dob",
            "mobile_ph",
            "doj",
            "parent",
        ]

class ParentCreateForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = [
            "pfirst_name",
            "plast_name",
            "pemail",
            "mobile_ph",
            "paddress",
            "job",
            "office_addr",
        ]