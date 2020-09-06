from rest_framework import serializers
from .models import Gen, Disease, Variant


class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class VarianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variant
        fields = ('id',
                  'chromosome_number',
                  'position',
                  'id_variant',
                  'reference',
                  'alternative',
                  'gen_symbol')



class GenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gen
        fields = ['id',
                  'chromosome_number',
                  'chromosome_initial_position',
                  'chromosome_last_position',
                  'symbol',
                  'diseases']