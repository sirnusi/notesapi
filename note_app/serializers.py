from rest_framework import serializers
from .models import Note, Category

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Note
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    category = NoteSerializer(read_only=True, many=True)#all the notes under that category.
    class Meta:
        model = Category
        fields = "__all__"
    

