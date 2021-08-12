from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        Fields = ["title","slug,author","body","publish","status","created","updated"]
 