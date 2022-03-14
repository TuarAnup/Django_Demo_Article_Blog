from artical.models import Article
from rest_framework.serializers import ModelSerializer
from artical.models import Article
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'