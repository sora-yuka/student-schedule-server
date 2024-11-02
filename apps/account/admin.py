from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.exceptions import AlreadyRegistered
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from apps.profiles.models import StudentProfileModel

# Register your models here.

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        
    def save(self, commit=True) -> models.Model:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        profile = StudentProfileModel.objects.create(owner=user)
        
        if commit:
            user.save()
        return user
    
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserAdmin(DefaultUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_staff"]})
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "password"]
            }
        )
    ]
    search_fields = ["username"]
    

def admin_register(model: models.Model, admin_class: admin.ModelAdmin = None) -> None:
    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass
    
admin_register(model=User, admin_class=UserAdmin)