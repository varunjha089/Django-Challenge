from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

# Trying to change the class dynamically from the list in views.py https://www.youtube.com/watch?v=wkTE2QvzSmc
# class list_of_class(models.Model):
#     class_name = models.CharField(max_length=20, null=False, blank=False)

#     def __str__(self):
#         return self.class_name

class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description