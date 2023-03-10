from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video, Supplier
from .views import get_video_details

@receiver(post_save, sender=Video)
def update_video_details(sender, instance, created, **kwargs):
    if created or kwargs.get('update_fields') == {'web_url'}:
        get_video_details(instance.web_url, instance.supplier.pk)
