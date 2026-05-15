from rest_framework import serializers
from .models import Todo

#Here we define our serialiser for our Todo model
#We also validate the incoming data to ensure the string has no blank spaces..

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value
    
    def validate_description(self, value):
        if value and len(value) < 5:
            raise serializers.ValidationError("Description too short")
        return value