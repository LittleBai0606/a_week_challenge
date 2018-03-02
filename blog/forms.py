#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: forms.py
@time: 2018/3/2 下午2:45
"""
from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': '名字',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': '邮箱',
            }),
            'url': forms.TextInput(attrs={
                'placeholder': '网址',
            }),
        }


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()