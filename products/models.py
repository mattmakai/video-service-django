from django.db import models


class SupportTicket(models.Model):
    """
        Represents a single support ticket in the customer service system.
    """
    endpoint = models.CharField(max_length=512)
    product_url = models.CharField(max_length=2048)
