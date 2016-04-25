#!/usr/bin/env python
# coding: utf-8

from django import forms



class registerForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(required=True)
