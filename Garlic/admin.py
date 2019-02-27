from django.contrib import admin
from .models import Billing
from .models import Deliveryboydetails
from .models import Orderdetails
from .models import Promo
from .models import Restaurants
from .models import Users
# Register your models here.
admin.site.register(Billing)
admin.site.register(Deliveryboydetails)
admin.site.register(Orderdetails)
admin.site.register(Promo)
admin.site.register(Restaurants)
admin.site.register(Users)