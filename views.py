from urllib import quote_plus
from urllib import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post

def post_home(request, id=None):
	#(a = get_object_or_404(Post, id=id)
	#context = {
	#	"title" : a.title,
	#	"instance" : a
	#})
	
	return render(request, "index.html")

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	share_string = quote_plus(instance.title)
	context = {
		"title" : instance.title,
		"instance" : instance,
		"share_string" : share_string,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list= Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(difficulty__icontains=query)|
			Q(duration__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 200) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	
	context = {
		"object_list": queryset,
		"title" : "List"
	}
	return render(request, "base.html", context)


def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")
# Create your views here.

