from django.db import models

from profiles.models import UserProfile
from products.models import Product


class ProductReview(models.Model):
    """
    Creates a review model to allow user to perform
    CRUD operations on product reviews
    """

    class Meta:
        ordering = ['-review_date']

    RATE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField()
    rating = models.IntegerField(choices=RATE, default=5)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review_date)

