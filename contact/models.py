from django.db import models

SUBJECT_MENU = (
    ('general_query', 'GENERAL QUERY'),
    ('update_cancel_my_order', 'UPDATE OR CANCEL MY ORDER'),
    ('sign_in_or_sign_up_issue', 'SIGN IN OR SIGN UP ISSUE'),
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
    subject = models.CharField(max_length=100, choices=SUBJECT_MENU,default='general_query', null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name