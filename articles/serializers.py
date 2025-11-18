from rest_framework import serializers

from articles.models import NewSource, Article, Digest, DigestArticle


class NewSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewSource
        fields = ['id', 'name', 'rss_url', 'active']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'source', 'title', 'link', 'published', 'summary']


class DigestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digest
        fields = ['id', 'name', 'created_at']


class DigestArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigestArticle
        fields = ['id', 'digest', 'article']
