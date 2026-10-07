from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        movie = get_object_or_404(Movie, pk=instance.pk)
        movie.save(**validated_data)
