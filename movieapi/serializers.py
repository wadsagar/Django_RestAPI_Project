from myapp.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):  # Converting a Database file format data into json file format data
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Movie
        fields = ('name', 'description', 'rating', 'image')