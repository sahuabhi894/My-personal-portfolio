from django.contrib import admin

from .models import Job
from .models import Contact

admin.site.register(Job)


# Register your models here.
admin.site.register(Contact)
