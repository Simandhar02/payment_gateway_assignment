#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Config settings for flask project
"""

import sys
from utils.core_utils import os_environ

DEBUG = os_environ("DEBUG", False)
FLASK_DEBUG = DEBUG
ERROR_404_HELP = False
