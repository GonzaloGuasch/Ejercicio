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
    path('variantsOfGen/<str:id>', views.VariantsOfGen.as_view(), name="variantOfGen"),
    path('genOfVarian/<str:reference>', views.GenesOfVariant.as_view(), name="genVariant"),

    path('genBySymbol/<str:symbol>', views.GenBySymbol.as_view()),
    path('diseaseByName/<str:name>', views.DiseasByName.as_view())

]