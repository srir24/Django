from django import forms
from crud_op.models import stud

class stdform(forms.ModelForm):
    class Meta:
        model=stud
        fields="__all__"
