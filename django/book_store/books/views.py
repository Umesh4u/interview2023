from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)
from django.db.models import Avg, Max,Min, Sum, Count
from .serializers import BookSerializer
from .models import Book,Author,Store
from exception import HousingException
import os
import sys


def all_queries(request):
	author = Author(name="J.K. Rowling")
	author.save()

	book = Book(title='Harry Potter and the Philosopher\'s Stone', publication_date='1997-06-26', author=author, price=19)
	book.save()

	# Get all Authors
	authors =author.objects.all()

	#Get a single author by id
	author = Author.objects.get(id=1)

	# Get all books by a specific author
	books = Book.objects.filter(author=author)

	# Get books with a specific title
	books = Book.objects.filter(title='Harry Potter and the Philosopher\'s Stone')

	# Get the first book in the queryset
	firstbook=Book.objects.first()

	# Get the last book in the queryset
	lastbook = Book.objects.last()

	# Get book orderd by publication date
	book_orderd_by_date = Book.objects.order_by(publication_date)

	#update a single's book title
	book = Book.objects.get(id=1)
	book.title="Vikram bettal"
	book.save()

	#bulk update
	Book.objects.filter(author=author).update(price=90)


	#delete a single book

	book= Book.objects,get(id=1)
	book.delete()

	#Bulk delete
	Books.objects.filter(author=author).delete()

	# Filter book published after a certain date
	books_published_after= Book.object.filter(publication_date__gt='2001-01-01')


	#Filter books with price less then or equal to 20
	affordable_book = Book.objects.filter(price__lte=20)

	# Filter book with titles containing a sub-string(case-sensitive)
	book_title= Book.objects.filter(title__icontains="Vikram")

	# Filter book published in  a specific year
	book_published = Book.objects.filter(publication_date__year=1997)

	# Exclude books by a specific author
	books_not_by author = Book.objects.exclude(author=author)

	#Exclude books which price greater then 30
	cheaper_book = Book.objects.exclude(price__gt=30)

	#Get the average price of all books
	avg_price = Book.objects.aggregate(Avg("price"))

	#Get the maximum price of books
	max_price = Book.objects.aggregate(Max("price"))

	#Get the minimum price of books
	min_price = Book.objects.aggregate(Min("price"))

	# Get the total number of books
	total_books = Book.objects.aggregate(Count("id"))

	#Get the sum of all books
	books_sum = Book.objects.aggregate(Sum("price"))
	
def store_detail(request):
	obj = Store.objects.annotate('book')
	print(obj)
	context={'data':obj}
	return render(request,"books.html",context)

def Booklist(ListAPIView):
	serializer_class = BookSerializer

	def list(self,request, *args, **kwargs):
		try:
			queryset = Book.objects.filter(active_status=True)
			return Response({"data":1})
		except exception as e:
			raise HousingException(e,sys) from e 
