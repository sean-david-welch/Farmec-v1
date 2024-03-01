from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Video
from .utils import get_video_info

@receiver(post_save, sender=Video)
def update_video_info(sender, instance, **kwargs):
    print('post_save signal called')
    if kwargs.get('created', False): # if the instance is being created
        video_id, thumbnail_url, title = get_video_info(instance.pk).values()
        instance.video_id = video_id
        instance.thumbnail_url = thumbnail_url
        instance.title = title
        instance.save(update_fields=['video_id', 'thumbnail_url', 'title'])
    else: # if the instance is being updated
        video_info = get_video_info(instance.pk)
        if instance.video_id != video_info['video_id']:
            instance.video_id = video_info['video_id']
            instance.save(update_fields=['video_id'])
        if instance.thumbnail_url != video_info['thumbnail_url']:
            instance.thumbnail_url = video_info['thumbnail_url']
            instance.save(update_fields=['thumbnail_url'])
        if instance.title != video_info['title']:
            instance.title = video_info['title']
            instance.save(update_fields=['title'])

