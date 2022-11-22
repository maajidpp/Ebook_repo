from dataclasses import fields
from .models import Ebooks
from rest_framework import serializers

class EbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ebooks
        fields = '__all__'
    
    def validate(self, attrs):
        print('welcome')
        Author = attrs.get('Author',None)
        Title = attrs.get('Title',None)
        Genre = attrs.get('Genre',None)
        Review = attrs.get('Review',None)
        print(Author,Title,Genre,Review)
        if Author == None or Title == None or Genre == None or Review == None:
            serializers.ValidationError('missing fields')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Ebooks.objects.create(**validated_data)



