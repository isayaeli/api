from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *


class BeatView(viewsets.ModelViewSet):
	queryset = Beat.objects.all()
	serializer_class = BeatSerializer


class UserView(viewsets.ModelViewSet):
	queryset = Beat.objects.all()
	serializer_class = BeatSerializer


class InstrumentView(viewsets.ModelViewSet):
	queryset = Instrument.objects.all()
	serializer_class = InstrumentSerializer



class GuitarView(viewsets.ModelViewSet):
	queryset = Guitar.objects.all()
	serializer_class = GuitarSerializer



class PianoView(viewsets.ModelViewSet):
	queryset =Piano.objects.all()
	serializer_class = PianoSerializer



class MarimbaView(viewsets.ModelViewSet):
	queryset = Marimba.objects.all()
	serializer_class = MarimbaSerializer


class TrumpetsView(viewsets.ModelViewSet):
	queryset = Trumpets.objects.all()
	serializer_class = TrumpetsSerializer


