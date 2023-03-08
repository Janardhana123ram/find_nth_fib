from rest_framework import serializers
from fib.models import Fibonacci


class FibonacciSerializer(serializers.Serializer):
    n = serializers.IntegerField(default=0)
    nth = serializers.IntegerField(default=0)
    status = serializers.CharField(max_length=100, default="pending")

    
    def create(self, validated_data):
        return Fibonacci.objects.create(**validated_data)

