from django.db.models.signals import pre_save
from django.dispatch import receiver
from . models import PaymentProduct

@receiver(pre_save, sender=PaymentProduct)
def multiply_price(sender, instance, **kwargs):
    instance.price *= 100