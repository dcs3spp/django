from django.conf.urls import include, url
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view, SchemaGenerator


from .views import AuthorViewSet, GenreViewSet, index, pages


api_router = routers.SimpleRouter()
api_router.register(r'authors', AuthorViewSet, basename='author')
api_router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    url(r'api/', include(api_router.urls)),
    path('', index, name='home'),
    re_path(r'^.*\.*', pages, name='pages'),
    path('v1/openapi', get_schema_view(generator_class=SchemaGenerator, public=True), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema', 'title': 'LibraryAPI'}
    ), name='swagger-ui'),
]

