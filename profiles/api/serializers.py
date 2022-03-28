from rest_framework import serializers
from profiles.models import Profile, ProfileStatus

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
    
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileStatusSerializerv(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        models = ProfileStatus
        fields = '__all__'
