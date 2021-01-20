from flask import current_app as app
from flask_restful import Resource

from utils.resource_exceptions import handle_exceptions


class CheapPayment(Resource):
    method_decorators = [handle_exceptions]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self, **request):
        app.logger.info("Processing payment with cheap premium gateway")
        app.logger.debug("Request params {}".format(request))
        return True


class ExpensivePayment(Resource):
    method_decorators = [handle_exceptions]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self, **request):
        app.logger.info("Processing payment with expensive premium gateway")
        return True


class PremiumPayment(Resource):
    method_decorators = [handle_exceptions]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self, **request):
        app.logger.info("Processing payment with premium premium gateway")
        return True
