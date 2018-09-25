from rest_framework import serializers

class RoundResults(serializers.Serializer):
    team = serializers.CharField()
    score = serializers.IntegerField()    