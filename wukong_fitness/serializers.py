from rest_framework import serializers
from wukong_fitness.models import Coach 


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('id','First', 'Last', 'Age', 'Email')
