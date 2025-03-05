from django.contrib import admin
from .models import Listing, Bid, Comment, User

# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'starting_bid', 'created_date', 'category', 'user', 'is_active')



admin.site.register(Listing, AuctionAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(User)
