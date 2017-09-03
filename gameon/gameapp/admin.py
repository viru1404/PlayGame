from django.contrib import admin



from .models import Profile, Questions, Activeusers

admin.site.register(Profile)
admin.site.register(Questions)
admin.site.register(Activeusers)
