from django.db import models

SUBJECT_MENU = (
    ('general_question', 'GENERAL QUESTION'),
    ('update_my_order', 'UPDATE MY ORDER'),
    ('account_issue', 'ACCOUNT ISSUE'),
    ('offer_your_products', 'OFFER YOUR PRODUCTS'),
)


class Contact(models.Model):
    """
    A Contact model for admin to view users queries
    """
    class Meta:
        """Set field to store information in DB"""
        verbose_name_plural = 'Queries'

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    subject = models.CharField(max_length=100, choices=SUBJECT_MENU,default='general_question', null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name