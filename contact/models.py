from django.db import models
from django.utils import timezone

SUBJECT_MENU = (
    ('general_question', 'GENERAL QUESTION'),
    ('update_my_order', 'UPDATE MY ORDER'),
    ('account_issue', 'ACCOUNT ISSUE'),
    ('offer_your_products', 'OFFER YOUR PRODUCTS'),
)

class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=100, choices=SUBJECT_MENU,default='general_question', null=False, blank=False)
    message = models.TextField(max_length=2000, blank=False, null=False)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
