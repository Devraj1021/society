from django.contrib import admin
from .models import Member, MaintenanceRecord, Complaint
# Register your models here.
admin.site.register(Member)
admin.site.register(MaintenanceRecord)
admin.site.register(Complaint)

