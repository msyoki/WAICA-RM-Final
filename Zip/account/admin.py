from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django import forms
from django.contrib import admin
from account.models import User,UserActivityLog
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models

# from .models import Profile


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name',)
    list_filter = ('country', 'email', 'is_active', 'is_admin', 'start_date')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name', 'last_name', 'country', 'language',
                    'is_active', 'is_admin', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'country', 'language')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),

    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = ((None,
                      {'classes': ('wide',
                                   ),
                       'fields': ('email',
                                  'first_name',
                                  'last_name',
                                  'country',
                                  'language',
                                  'password1',
                                  'password2',
                                  'is_active',
                                  'is_admin')}),
                     )


admin.site.register(User, UserAdminConfig)


User = get_user_model()


class UserLogConfig(admin.ModelAdmin):
    model = UserActivityLog
    list_display = ('date','time','activity','ip_address', 'user_email', 'user_name','country')
    list_filter = ('date','time', 'country', 'user_email')
    ordering = ('-date','-time')
admin.site.register(UserActivityLog, UserLogConfig)

# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.


class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)