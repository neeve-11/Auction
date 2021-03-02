from django.contrib import admin

from .models import user,comment,bidding,wishlist
# Register your models here.


admin.site.register(user)
admin.site.register(comment)
admin.site.register(bidding)
admin.site.register(wishlist)
