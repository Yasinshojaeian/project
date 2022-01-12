from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class ArticleSerialiser(serializers.ModelSerializer):
    # author = 
    class Meta:
        model = Article
        fields ="__all__"
    def validate_title(self, value):
        filter_list = ["javascript","laravel","php"]
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("dont use bad word ! :{}".format(i))

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields ="__all__"