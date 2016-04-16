import json

import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from instadjango import settings
from .forms import HashtagForm
from .models import Photo, HashTag

def search(request):
    if request.method == 'GET':
        form = HashtagForm()
        return render(request, 'instagram/search.html', {'form': form})
    elif request.method == 'POST':
        form = HashtagForm(request.POST)
        if form.is_valid():
            hashtag = form.cleaned_data['search_box']
            hashtag_clean = hashtag.replace('#', '')
            return HttpResponseRedirect("/instagram/results?search=" + hashtag_clean)
        else:
            return form.errors


def results(request):
    hashtag = request.GET.getlist('search')[0]
    params = {"client_id": settings.product_client_id, "count": "9"}
    try:
        max_tag_id = request.GET.getlist('max_tag_id')[0]
        if max_tag_id is not False:
            params['max_tag_id'] = max_tag_id
    except:
        pass

    hashtag_url = 'https://api.instagram.com/v1/tags/' + hashtag + "/media/recent"

    req = requests.get(hashtag_url, params=params)
    body_unicode = req.text
    json_data = json.loads(body_unicode)
    next_url = json_data.get('pagination', False).get('next_max_tag_id', False)
    next_url = '/instagram/results?search=' + hashtag + '&max_tag_id=' + next_url
    data = json_data['data']
    try:
        hashtag_object = HashTag.objects.get(hashtag=hashtag)
        hashtag_object.increment_counter()
    except:
        hashtag_object = HashTag.objects.create(hashtag=hashtag)

    photo_template = []

    for photo in data:
        if photo["type"] == "image":
            photo_dict = {"username": photo['user']['username'], "profile_picture": photo['user']['profile_picture'],
                          "full_name": photo['user']['full_name'],
                          "picture_url": photo['images']['standard_resolution']['url'],
                          "tags": photo['tags'], "post_id": photo['id']}
            try:
                object = Photo.objects.get(post_id=photo_dict['post_id'])
                object.increment_counter()
            except:
                object = Photo.objects.create(**photo_dict)

            hashtag_object.add_related_tags(photo_dict['tags'])
            photo_template.append(object)
            # do something with object.
        else:
            pass

    return render(request, 'instagram/results.html',
                  context={"photos": photo_template, "next_url": next_url,
                           "previous_hashtags": HashTag.objects.all().order_by('-search_count')[:10], "related_tag": hashtag_object.related_tag.all().order_by('-count')[:20]})

