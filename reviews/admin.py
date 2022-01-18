from django.contrib import admin
from .models import ProductReview


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'product',
        'user',
        'rating',
        'review_date'
    )

admin.site.register(ProductReview)