from django.http import HttpResponse
from django.template import loader
from .models import Album
import json

def index(request):
	all_albums = Album.objects.all()
	template = loader.get_template('music/index.html')
	context = {
		'all_albums' : all_albums,
	}
	return HttpResponse(template.render(context, request))


def detail(request, album_id):
	return HttpResponse("<h2>Details for Album id: "+ str(album_id) + "</h2>")


def mapdemo(request):
	template = loader.get_template('music/amenities-manager.html')
	lines = []
	with open('music/coors.json', encoding='utf8') as f:
		json_data = json.load(f)

	context = {
		'coordinates_var' : json_data["features"],
	}
	return HttpResponse(template.render(context, request))

def mapdemo2(request):
	template = loader.get_template('music/Analysis.html')
	lines = []
	with open('music/coors.json', encoding='utf8') as f:
		json_data = json.load(f)

	context = {
		'coordinates_var' : json_data["features"],
	}
	return HttpResponse(template.render(context, request))

def mapdemo3(request):
	template = loader.get_template('music/File-Manager.html')
	lines = []
	with open('music/coors.json', encoding='utf8') as f:
		json_data = json.load(f)

	context = {
		'coordinates_var' : json_data["features"],
	}
	return HttpResponse(template.render(context, request))
