from django.contrib import admin
from .models import Merchants,Product,Costomer,Status,Order,Admin,Help,Delivery_status

admin.site.register(Merchants),
admin.site.register(Product),
admin.site.register(Costomer),
admin.site.register(Status),
admin.site.register(Order),
admin.site.register(Admin),
admin.site.register(Help),
admin.site.register(Delivery_status),

# Register your models here.
