# from django.shortcuts import render

# Create your views here.

from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


# FilterSetを継承したフィルタセット(設定クラス)を作る
# class EntryFilter(filters.FilterSet):

    # フィルタの定義
#    author = filters.CharFilter(name="author", lookup_expr='exact')
#    status = filters.CharFilter(name="status", lookup_expr='exact')

#    class Meta:
#        model = Entry
        # フィルタを列挙する。
        # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
#        fields = ['author', 'status'] 


class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class EntryViewSet(viewsets.ModelViewSet):
     queryset = Entry.objects.all()
     serializer_class = EntrySerializer
     filter_fields = ('author', 'status')
     
     
     

