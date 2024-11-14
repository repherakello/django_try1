from django.db import models

# Create your models here.

#ForeignKey Relationship
class category(models.Model):
    call = models.CharField(max_length=100)

class Production(models.Model):
    call = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='products')


#OneToOneField Relationship
class User(models.Model):
    username = models.CharField(max_length=100)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

#ManyToManyField Relationships
class Student(models.Model):
    name = models.CharField(max_length=100)


class course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')


#Handling Related Object Deletion

class Author(models.Model):
    identity = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


#Performance Consideration

class Categorize(models.Model):
    naming = models.CharField(max_length=100)

class Product(models.Model):
    naming = models.CharField(max_length=100)
    categorize = models.ForeignKey(Categorize, on_delete=models.CASCADE, related_name='products')

  #optimizing queries with prefetching
products = Product.objects.prefetch_related('category')

