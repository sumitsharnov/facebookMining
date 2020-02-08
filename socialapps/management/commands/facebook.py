import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand
from socialapps.models import Item
from socialapps.models import MyPosts



class Fb():
    def fb(self, graph):
        profile = graph.get_object('me', fields='name,location{location}, gender, id, photos')
        photos = graph.get_object('me', fields='photos{images}')
        listofPhotos = photos['photos']['data']
        posts_fullPictures = graph.get_object('me', fields='posts{full_picture}')
        listofPictures = posts_fullPictures['posts']['data']
        # print(listofPhotos)
        # for listofPictures_ID in posts_fullPictures:
        #     item = Item()
        #     item.image_id = listofPictures_ID.get('id')
        #     item.save()
        try:
            shutil.rmtree('images')
        except:
            print("Images folder doesn't exist")
        Item.objects.all().delete()
        for pictures in listofPictures:
            item = Item()
            if not pictures.get("full_picture") == None:
                item.image_url = pictures.get("full_picture")
                item.save()
                item.cache()
                item.save()
        print(json.dumps(profile, indent=4))

        #Importing Posts data
        MyPosts.objects.all().delete()
        posts = graph.get_object('me', fields='posts{permalink_url,caption,created_time,name,type,status_type}')
        postsData = posts['posts']['data']
        for post in postsData:
            myPosts = MyPosts()
            if not post.get('permalink_url') == None:
                myPosts.post_url = post.get('permalink_url')
            if not post.get('type') == None:
                myPosts.status_type = post.get('type')
            if not post.get('status_type') == None:
                myPosts.status_source=post.get('status_type')
            if not post.get('caption') == None:
                myPosts.caption= post.get('caption')
            else:
                myPosts.caption="N/A"
            if not post.get('created_time') == None:
                myPosts.post_time = post.get('created_time')
            myPosts.save()
