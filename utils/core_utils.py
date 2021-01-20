#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Basic utilities used throughout the project
"""

__author__ = "Simandhar Sahuji"
__date__ = "17th Jan 2021"

import logging
import logging.config
import os
from functools import wraps
from importlib import import_module


from flask import current_app as app
from flask_cors import CORS
from flask_restful import Api
from url_list import URL_LIST
from marshmallow import validate


def create_restful_api(app):
    CORS(app, resources={r"/*": {"origins": "*"}})
    # added cors as it was only giving pre-flight request
    api = Api(app, prefix="/")
    for url_obj in URL_LIST:
        resource_name = url_obj.resource
        rsplit = resource_name.split('.')
        module, resource = '.'.join(rsplit[:-1]), rsplit[-1]
        try:
            imported_module = getattr(
                import_module(module),
                resource
            )
        except ImportError as e:
            msg = "Resource '{}' could not be found".format(resource)
            app.logger.error(msg)
            raise e

        else:
            api.add_resource(
                imported_module,
                url_obj.url,
                endpoint=url_obj.name,
                strict_slashes=False
            )


def config_logger(app):
    logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))
    logger = logging.getLogger(app.config.get("DEFAULT_LOGGER_NAME"))
    app.logger.handlers = app.logger.handlers[1:]
    app.logger.addHandler(logger)
    # log = logging.getLogger('werkzeug')
    # log.setLevel(logging.ERROR)
    app.logger.info("logger configured")


def os_environ(key, default=None):
    try:
        return os.environ[key]
    except KeyError:
        if default is not None:
            return default

        raise Exception(
            "Enviroment-Variable '{}' "
            "is required and was not found".format(key))


def is_ascii(string):
    try:
        string.decode('ascii')
        return True
    except UnicodeEncodeError:
        return False


def check_credit_card_number():
    return validate.Length(equal=16, error="Invalid Credit Card Number")


def check_security_code():
    # return validate.Range
    return validate.Length(equal=3, error="Invalid security code")
