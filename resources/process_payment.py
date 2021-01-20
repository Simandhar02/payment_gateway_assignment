import datetime
from datetime import timedelta

from flask import current_app as app
from flask_restful import Resource
from marshmallow import Schema, fields as field

from functionality.process_payment import payment_processor
from utils.core_utils import check_credit_card_number, check_security_code
from utils.formatter import io_formatter
from utils.resource_exceptions import handle_exceptions


class PaymentProcessSchema(Schema):
    credit_card_number = field.Str(required=True, validate=check_credit_card_number(), load_from='CreditCardNumber')
    card_holder = field.Str(required=True, load_from='CardHolder')
    expiry_date = field.DateTime(required=True, allow_none=False,
                                 validate=lambda x: x > datetime.datetime.now() + timedelta(hours=1),
                                 load_from='ExpirationDate')
    security_code = field.Str(required=False, validate=check_security_code(), load_from='SecurityCode')
    amount = field.Decimal(required=True, validate=lambda x: x > 0, load_from='Amount')

    class Meta:
        strict = True


class PaymentProcess(Resource):
    method_decorators = [handle_exceptions, io_formatter(PaymentProcessSchema)]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self, **request):
        return payment_processor(**request)
