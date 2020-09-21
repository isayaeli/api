from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class BeatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beat
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class InstrumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instrument
		fields = '__all__'



class GuitarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Guitar
		fields = '__all__'




class PianoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Piano
		fields = '__all__'




class MarimbaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Marimba
		fields = '__all__'




class TrumpetsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trumpets
		fields = '__all__'


