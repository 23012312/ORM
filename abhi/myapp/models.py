from django.db import models
from django.contrib import admin
class Library(models.Model):
    bookauthor=models.CharField(max_length=20);
    bookname=models.CharField(max_length=25);
    bookid=models.IntegerField(primary_key=True);
    published_date=models.DateField();
    bookcost=models.IntegerField();

class LibraryAdmin(admin.ModelAdmin):
    list_display=("bookauthor","bookname","bookid","published_date","bookcost");a