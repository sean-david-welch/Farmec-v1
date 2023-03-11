from django.conf import settings
from .models import Video, Supplier

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from urllib.parse import urlparse, parse_qs

def get_video_info(pk):
    print('get_video_info called')
    video = Video.objects.get(id=pk)
    web_url = video.web_url

    # Parse the video ID from the URL
    parsed_url = urlparse(web_url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params["v"][0]

    # Create a YouTube Data API client
    api_key = settings.YOUTUBE_API_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Call the YouTube API to get the video details
    video_response = youtube.videos().list(
        part='id, snippet',
        id=video_id,
        maxResults=1
    ).execute()

    # Extract the video details from the API response
    video_snippet = video_response['items'][0]['snippet']
    thumbnail_url = video_snippet['thumbnails']['medium']['url']
    title = video_snippet['title']

    return {
        'video_id': video_id,
        'thumbnail_url': thumbnail_url,
        'title': title,
    }