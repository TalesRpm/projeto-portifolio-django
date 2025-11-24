from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
  class Meta: #metadados
    model = Livro
    fields = ['id','titulo','autor','ano_publicacao']