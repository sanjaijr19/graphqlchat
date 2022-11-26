from django.contrib import admin
from .models import GroupDetails,GroupName,Message
from django.apps import apps
# Register your models here.


app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
# Register your models here.
admin.site.register(GroupDetails)
admin.site.register(GroupName)
admin.site.register(Message)



