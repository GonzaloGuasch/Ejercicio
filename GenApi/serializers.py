from rest_framework import serializers
from .models import Gen, Disease, Variant


class GenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gen
        fields = ('chromosome_number',
                  'chromosome_initial_position',
                  'chromosome_last_position',
                  'symbol',
                  'related_disease')


class VarianSerializer(serializers.ModelSerializer):
    gen_symbol = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Variant
        fields = ('chromosome_number',
                  'position',
                  'id',
                  'reference',
                  'alternative',
                  'gen_symbol')


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'
