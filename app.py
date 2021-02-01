#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Flask app creation with standard configuration
"""

__author__ = "Simandhar Sahuji"

from flask import Flask
from utils.core_utils import config_logger

from constants.common_constants import FLASK_APP_NAME, FLASK_CONFIG_MODULE
# from database import get_read_session, get_session
from utils.core_utils import create_restful_api


def create_app():
    """
    Create flask app, configure the app, configure database session
    :returns: instance of flask
    """
    app = Flask(FLASK_APP_NAME)
    app.config.from_object(FLASK_CONFIG_MODULE)

    create_restful_api(app)

    return app


def create_test_app():
    """
    Create flask app, configure the app, configure database session
    :returns: instance of flask
    """

    app = Flask("FLASK_TEST_APP_NAME")
    app.config.from_object(FLASK_CONFIG_MODULE)

    return app


main_app = create_app()

if __name__ == '__main__':
    main_app.run('0.0.0.0', port=5012, debug=True)
