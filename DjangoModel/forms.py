from django import forms
from DjangoModel.models import Toshiba


class wanafunziform(forms.ModelForm):
    class Meta:
        model = Toshiba
        fields = "__all__"
