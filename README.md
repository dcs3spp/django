# Quickstart

Packages install
- django
- djangorestframework
- djangorestframework_jsonapi
- django-filter
- pytest-django
-

```bash
mkdir proj_root
cd proj_root
django-admin startproject main .;
django-admin startapp api .;
```

In main/settings.py there is an *INSTALLED_APPS* section.
In this the apps need to be registered and the django rest
framework and django rest framework jsonapi:

```bash
INSTALLED_APPS = [
  'app.apps.MyConfig',
  'rest_framework',
  'rest_framework_json_api',
]
```

Now create a superuser:

```bash
python manage.py createsuperuser
```

Visit *http://localhost:8080/admin/*

# Models

Every model has a base of `models.Model`.

It should have a nested class Meta if need to define field ordering.
It should also define __str__ method.
It should have a get_absolute_url method
Check out the models in API folder for example fields and relationships

A model can be saved to db using `my_model_instance.save()`
A model can be searched using *objects* property on the model class:

```python
all_books = Book.objects.all()
wild_books = Book.objects.filter(title__contains='wild')
number_wild_books = wild_books.count()

books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
```

Make and apply the migrations to the underlying database after modifying models:

``` bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Register the models for use in the admin site.
Every django app has an admin.py that can be configured to register model
classes for maintaining and entering data.

```python
#admin.py
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
```

## Views
The *djangorestframework* package provides a *ModelViewSet* class that
should be inherited to provide paths/endpoints for list, delete etc.

This should include a *queryset* attribute used to retrieve the data
and a serializer_class for JSON serialization from/to the underlying model.

```python
from django.shortcuts import render
from rest_framework import viewsets

from .models import Genre
from .serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
```


## Serializers
Import from *from rest_framework_json_api import serializers*

Each serializer class serializes from a model to JSON:API spec.
Each class has a *model* and *fields* attributes specific in 
nested *Meta* class as listed below.

```python
class GenreSerializer(serializers.HyperlinkedModelSerializer): 
      class Meta:
          model = Genre
          fields = ('name',)
```

## Map Views To Url's

In each application create a *SimpleRouter* and register paths and url patterns.

```python
from django.conf.urls import include, url
from rest_framework import routers

from .views import GenreViewSet

api_router = routers.SimpleRouter()
api_router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
  url(r'', include(api_router.urls))
]
```

Then in the main project url include the url patterns from all apps.

```python
urlpatterns = [
      path('admin/', admin.site.urls),
      url('', include('local.api.urls')),
]
```

## Testing
When testing models test the field attributes, no need to test the model properties
We need to test the views further status codes, responses....but this is 
integration. Do we need unit tests without this....
