from rest_framework import serializers
from blogs.models import Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, allow_null=False)
    owner = serializers.CharField(min_length=1, max_length=100, allow_null=False)
    description = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        blog = Blog(**validated_data)
        blog.save()
        return blog

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

