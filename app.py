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

    # database_url = app.config.get('DATABASE_URL')
    # database_url_read = app.config.get('REPLICA_DATABASE_URL')
    #
    # if not database_url:
    #     raise Exception("Environment Exception: DATABASE_URL not set.")

    # db.init_app(app)
    # session = get_session(database_url)
    # read_session = get_read_session(database_url_read)

    # config_logger(app)
    create_restful_api(app)

    # def close_session(response_or_exc):
    #     session.remove()
    #     read_session.remove()
    #     return response_or_exc

    # app.teardown_request(close_session)
    # app.teardown_appcontext(close_session)
    return app


def create_test_app():
    """
    Create flask app, configure the app, configure database session
    :returns: instance of flask
    """

    app = Flask("FLASK_TEST_APP_NAME")
    app.config.from_object(FLASK_CONFIG_MODULE)

    # database_url = app.config.get('DATABASE_URL')
    #
    # if not database_url:
    #     raise Exception("Environment Exception: DATABASE_URL not set.")

    # session = get_session(database_url)

    # config_logger(app)

    # create_restful_api(app)

    # def close_session(response_or_exc):
    #     session.remove()
    #     return response_or_exc
    #
    # app.teardown_request(close_session)
    # app.teardown_appcontext(close_session)
    return app


main_app = create_app()

if __name__ == '__main__':
    main_app.run('0.0.0.0', port=5012, debug=True)
