from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Parent(models.Model):
    pfirst_name = models.CharField(max_length=50, verbose_name="First Name")
    plast_name = models.CharField(max_length=50, verbose_name="Last Name")
    pemail = models.EmailField(verbose_name="Email Address")
    mobile_ph = models.CharField(max_length=10, verbose_name="Mobile Phone")
    paddress = models.TextField(verbose_name="Address")
    job = models.CharField(max_length=50, verbose_name="Job")
    office_addr = models.TextField(verbose_name="Office Address")

    def __unicode__(self):
        return "%s %s" % (self.pfirst_name, self.plast_name)

    def get_absolute_url(self):
        return reverse("student:list")

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    middle_name = models.CharField(max_length=50, verbose_name="Middle Name", blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email_id = models.EmailField(blank=True, null=True)
    address = models.TextField(verbose_name="Address")
    dob = models.DateField(verbose_name="Date of Birth")
    mobile_ph = models.CharField(max_length=10, verbose_name="Mobile Phone", blank=True, null=True)
    doj = models.DateField(verbose_name="Date of Joining")
    parent = models.ForeignKey(Parent)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("student:detail", kwargs={'pk': self.pk})

