#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# gen_secret.py
#
# generate a secret key for use in environment variable
from django.core.management import utils


secret_key = utils.get_random_secret_key()

print(f"secret key generated := {secret_key}")

