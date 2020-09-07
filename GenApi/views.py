from .serializers import GenSerializer, DiseaseSerializer, VarianSerializer
from .models import Gen, Disease, Variant
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


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


class VariantsOfGen(APIView):

    def get(self, request, id):
        gen = Gen.objects.filter(symbol=id)[0]
        variants_of_gen = Variant.objects.select_related().filter(gen_symbol = gen.id)
        serializer_context = {
            'request': request,
        }
        serializer = VarianSerializer(variants_of_gen, many=True, context=serializer_context)
        return Response(serializer.data)


class GenesOfVariant(APIView):

    def get(self, request, reference):
        variant = Variant.objects.filter(reference=reference)[0]
        gen = Gen.objects.filter(symbol=variant.gen_symbol)[0]
        serializer_context = {
            'request': request,
        }
        serializer = GenSerializer(gen, context=serializer_context)
        return Response(serializer.data)


class GenBySymbol(APIView):
    def get(self, request, symbol):
        gen = Gen.objects.filter(symbol=symbol)[0]
        serializer_context = {
            'request': request,
        }
        serializer = GenSerializer(gen, context=serializer_context)
        return Response(serializer.data)


class DiseasByName(APIView):
    def get(self, request, name):
        d = Disease.objects.filter(name=name)[0]
        serializer_context = {
            'request': request,
        }
        serializer = DiseaseSerializer(d, context=serializer_context)
        return Response(serializer.data)