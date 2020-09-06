from .serializers import GenSerializer, DiseaseSerializer, VarianSerializer
from .models import Gen, Disease, Variant
from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GenesView(viewsets.ModelViewSet):
    queryset = Gen.objects.all()
    serializer_class = GenSerializer


class VariantView(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VarianSerializer


class DiseaseView(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class DiseasesOfGenView(APIView):

    def get(self, request, id):
        genes = Gen.objects.filter(symbol=id)
        gen_with_id = genes.first()
        diseases = gen_with_id.diseases.all()
        serializer_context = {
            'request': request,
        }
        serializer = DiseaseSerializer(diseases, many=True, context=serializer_context)
        return Response(serializer.data)


class GenesOfDiseas(APIView):

    def get(self, request, name):
        disease = Disease.objects.filter(name=name)
        disease_with_name = disease.first()
        genes = disease_with_name.gen_set.all()
        serializer_context = {
            'request': request,
        }

        serializer = GenSerializer(genes, many=True, context=serializer_context)
        return Response(serializer.data)


class GenVariant(APIView):

    def get(self, request, id):
        genes = Gen.objects.filter(symbol=id)
        gen_with_id = genes.first()
        diseases = gen_with_id.diseases.all()
        serializer_context = {
            'request': request,
        }
        serializer = DiseaseSerializer(diseases, many=True, context=serializer_context)
        return Response(serializer.data)
