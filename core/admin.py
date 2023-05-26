from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Customer
# Register your models here.


class CustomerInLine(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Customer'
    fk_name = 'user'
    fields = ('user', 'date_of_birth', 'street', 'post_code', 'city', 'country')


class UserAdmin(UserAdmin):
    inlines = (CustomerInLine, )
    list_display = ('username', 'email', 'get_date_of_birth')

    def get_inline_instances(self, request, obj = None):
        if not obj:
            return list()
        return super(UserAdmin,self).get_inline_instances(request,obj)

    def get_date_of_birth(self,obj):
        return Customer.objects.get(user=obj).date_of_birth


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
