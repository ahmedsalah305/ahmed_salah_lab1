from django                 import forms
from .models                import Movie , Category
# from django.core.exceptions import ValidationError

# not_allowed_names = ["ahmed" , "mahmoud" , "salah"]

# class customLoginForm(forms.Form):
#     name    = forms.CharField(max_length=255)
#     content = forms.CharField(widget=forms.PasswordInput)
    
#     def clean(self):
#         super(customLoginForm , self).clean()
#         name = self.cleaned_data.get("name")
#         if name in not_allowed_names:
#             return ValidationError("name is forbidden")


class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"

