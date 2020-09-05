from .serializers import GenSerializer, DiseaseSerializer, VarianSerializer
from .models import Gen, Disease, Variant
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GenGetAndPost(APIView):
    def get(self, request, format=None):
        genes = Gen.objects.all()
        serializer_class = GenSerializer(genes, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = GenSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.error_messages, status=status.HTTP_400_BAD_REQUEST)


class GenesDelete(APIView):
    def get_object(self, symbol):
        try:
            g = Gen.objects.get(symbol=symbol)
            return g
        except Gen.DoesNotExist:
            raise Http404

    def delete(self, request, symbol):
        gen = self.get_object(symbol)
        gen.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DiseaseDetail(APIView):
    def get(self, request, format=None):
        diseases = Disease.objects.all()
        serializer_class = DiseaseSerializer(diseases, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = DiseaseSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.error_messages, status=status.HTTP_400_BAD_REQUEST)


class DiseaseDelete(APIView):
    def get_object(self, name):
        try:
            d = Disease.objects.get(name=name)
            return d
        except Disease.DoesNotExist:
            raise Http404

    def delete(self, request, name):
        disease = self.get_object(name)
        disease.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class VariantDetail(APIView):
    def get(self, request, format=None):
        diseases = Variant.objects.all()
        serializer_class = VarianSerializer(diseases, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = VarianSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.error_messages, status=status.HTTP_400_BAD_REQUEST)