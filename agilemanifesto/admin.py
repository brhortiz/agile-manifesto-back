from django.contrib import admin
from agilemanifesto.models import AgilePrinciple
from agilemanifesto.models import AgileValue

# Register your models here.
admin.site.register(AgilePrinciple)
admin.site.register(AgileValue)