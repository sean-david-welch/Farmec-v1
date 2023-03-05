from django.db.models.signals import pre_save
from django.dispatch import receiver
from . models import PaymentProduct

@receiver(pre_save, sender=PaymentProduct)
def multiply_price(sender, instance, **kwargs):
    for instance in PaymentProduct.objects.all():
        instance.price *= 100
        print(instance.price + 'singal fired') 