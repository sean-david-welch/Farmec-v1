from django.db import models
import uuid

# Create your models here.
class PaymentProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True) #cents
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']
