from rest_framework import serializers
from .models import News
from django import forms


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        # 通过model做映射，下面fields的字段可以直接再Goods的model中找到对应的字段类型
        model = News
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        # __all__代表取所有字段，其中外键会序列化成键id，
        fields = '__all__'


# class EntrySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         # 通过model做映射，下面fields的字段可以直接再Goods的model中找到对应的字段类型
#         model = Test
#         # fields = ('name', 'click_num', 'market_price', 'add_time')
#         # __all__代表取所有字段，其中外键会序列化成键id，
#         fields = '__all__'


# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = '__all__'
