import random

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from markdown2 import Markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
	page = util.get_entry(title)
	if page is None:
		return render(request, "encyclopedia/error.html",{'message': "ERROR! NO SUCH PAGE...."})
	else:
		return HttpResponse(page)

def show_page(request,name):
	page = util.get_entry(name)
	markdowner=Markdown()
	if page is None:
		return render(request,"encyclopedia/error.html",{'message': "ERROR! NO SUCH PAGE...."})
	return HttpResponse(markdowner.convert(page)+'<a href="edit/'+ name +'">EDIT</a>')

def edit_entry(request,entry):
	previous=util.get_entry(entry)
	return render(request,"encyclopedia/edit.html",{'title': entry,'previous': previous})

def search(request):
	if request.method == "POST":
		title=request.POST.get("q")
	entries = util.list_entries()
	markdowner=Markdown()
	if title in entries:
		page = util.get_entry(title)
		if page is None:
			return render(request, "encyclopedia/error.html",{'message': "ERROR! the requested page was not found..."})
		else:
			return HttpResponse(markdowner.convert(page)+'<a href="edit/'+ title +'">EDIT</a>')
	else:
		matches = [i for i in entries if title in i]
		return render(request, "encyclopedia/results.html", {
        "matches": matches
    })

def new_page(request):
    return render(request, "encyclopedia/new_entry.html")

def adding(request):
	if request.method == "POST":
		title=request.POST.get("title")
		contents=request.POST.get("contents")
		if title in util.list_entries():
			return render(request, "encyclopedia/error.html",{'message': "ERROR! the title already exists..."}) 
		util.save_entry(title,contents)
		return HttpResponseRedirect(reverse("show_page", args=[title]))

def editing(request):
	if request.method =='POST':
		title=request.POST.get("title")
		contents=request.POST.get("contents")
		util.save_entry(title,contents)
		return HttpResponseRedirect(reverse("show_page", args=[title]))

def random_page(request):
	entries = util.list_entries()
	entry = random.choice(entries)
	page = util.get_entry(entry)
	markdowner=Markdown()
	hello=markdowner.convert(page)
	# world='<form><input type="text"><form>'
	# return render(request, "encyclopedia/display.html",{'hello': hello+world.encode("utf-8")}) 
	return HttpResponse(markdowner.convert(page)+'<a href="edit/'+ entry +'">EDIT</a>')