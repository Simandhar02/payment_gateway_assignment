import json

import requests
from flask import current_app as app
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from constants.common_constants import PAYMENT_GATEWAY_BASE_URL, CHEAP_GATEWAY, EXPENSIVE_GATEWAY, PREMIUM_GATEWAY


def payment_processor(**request_params):
    if request_params.get('request_params').get('amount') < 20:
        response = make_request(PAYMENT_GATEWAY_BASE_URL, CHEAP_GATEWAY, request_params)
        app.logger.info("response from cheap gateway {}".format(response.__dict__))
        return check_status_code(response.status_code)
    elif request_params.get('request_params').get('amount') in range(21, 501):
        response = make_request(PAYMENT_GATEWAY_BASE_URL, EXPENSIVE_GATEWAY, request_params)
        app.logger.info("response from cheap gateway {}".format(response.__dict__))
        if response.status_code != 200:
            response = make_request(PAYMENT_GATEWAY_BASE_URL, CHEAP_GATEWAY, request_params)
        return check_status_code(response.status_code)
    elif request_params.get('request_params').get('amount') > 500:
        response = make_request(PAYMENT_GATEWAY_BASE_URL, PREMIUM_GATEWAY, request_params, retry=True)
        app.logger.info("response from cheap gateway {}".format(response.__dict__))
        return check_status_code(response.status_code)


def check_status_code(status_code):
    if status_code == 200:
        return "Payment is processed"
    else:
        raise Exception("INTERNAL SERVER ERROR")


def make_request(payment_url, gateway, request_params, retry=False):
    try:
        if retry:
            s = requests.Session()
            retries = Retry(total=3, backoff_factor=1, method_whitelist=frozenset(['POST']),
                            status_forcelist=[502, 503, 504, 500, 400, 404])
            s.mount(payment_url + gateway, HTTPAdapter(max_retries=retries))
            response = s.post(payment_url + gateway,
                              json=json.dumps(request_params, default=str))
        else:
            response = requests.post(payment_url + gateway,
                                     json=json.dumps(request_params, default=str))
        return response
    except Exception as e:
        app.logger.error(str(e))
        raise Exception("INTERNAL SERVER ERROR")
