from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('genes', views.GenesView)
router.register('variant', views.VariantView)
router.register('disease', views.DiseaseView)


urlpatterns = [
    path('', include(router.urls)),
    path('diseasOf/<str:id>/', views.DiseasesOfGenView.as_view(), name="genesOf"),
    path('genOf/<str:name>/', views.GenesOfDiseas.as_view(), name="diseasOf"),
    path('genVariant/<str:name>', views.GenVariant.as_view(), name="genVariant")

]