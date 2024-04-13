from django.contrib import admin
# from .models import Tracking, Officer
from .models import *

admin.site.register(Tracking)
admin.site.register(Officer)
admin.site.register(AskQA)