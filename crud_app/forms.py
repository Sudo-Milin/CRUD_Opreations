from django import forms
from django import forms
from django.db import models
from django.forms import fields
from .models import CRUD

class CreateModelform(forms.ModelForm):
    class Meta:
      model = CRUD
      fields = ("text",)