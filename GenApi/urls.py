from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('genes/', views.GenGetAndPost.as_view()),
    path('genes/delete/<str:symbol>/', views.GenesDelete.as_view()),
    path('disease/', views.DiseaseDetail.as_view()),
    path('disease/delete/<str:name>/', views.DiseaseDelete.as_view()),
    path('variant/', views.VariantDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)