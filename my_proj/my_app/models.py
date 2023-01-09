from django.db import models


"""
BOOK STORE

//
Position

id              PK int
name            char
wage            int
//

//
Employee

id              PK int
first_name      Char
last_name       Char
recruit_date    DateTime
birth_date      DateTime
posit           Position
//

//
Author

id              PK int
first_name      Char
last_name       Char
birth_date      Date
death_date      DateTime || null
photo           "path/to/file"
//  

//
Book

id              PK int
title           Char
author          Author
price           float
photo           "path/to/file"
//

//
Client

id              PK int
first_name      Char
last_name       Char
//

//
Buy

id              PK int
client          Client
employee        Employee
date            DateTime
books           Book
payment         Float
//
"""

class Position(models.Model):
    name = models.CharField(null=False, max_length=40)
    wage = models.IntegerField(null=False)
    
class Employee(models.Model):
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    recruit_date = models.DateField(null=False, auto_now_add=True)
    birth_date = models.DateField(null=False)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    
class Author(models.Model):
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    birth_date = models.DateField(null=False)
    death_date = models.DateField(blank=True)
    photo = models.ImageField(upload_to="photo/%Authors")
    
class Book(models.Model):
    title = models.CharField(null=False, max_length=30)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    price = models.IntegerField(null=False)
    photo = models.ImageField(upload_to="%photo/%Author/%TitleBook")
  
class Client(models.Model):
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    
class Buy(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date = models.DateTimeField(null=False, auto_now_add=True)
    books = models.ForeignKey(Book, on_delete=models.PROTECT)
    