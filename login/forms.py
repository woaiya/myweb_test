#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class UserAccountForm(forms.Form):

    username = forms.CharField(
        required=True,
        min_length=3,
        max_length=20,
        error_messages={
            "required": "用户名不能为空",
            "min_length": "用户名不能小于3位",
            "max_length": "用户名不能超过20位",
        }
    )
    password = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
        error_messages={
            "required": "密码不能为空",
            "min_length": "用户名不能小于3位",
            "max_length": "用户名不能超过50位",
        }
    )


def userForm(username, password):
    if username is None or password is None:
        print("账号密码不能为空")