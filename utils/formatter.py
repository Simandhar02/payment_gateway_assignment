from functools import wraps

from flask import request, Response
import urllib
import json

from utils.resource_exceptions import handle_exceptions


class IO(object):
    """
    Input Output formatter class
    """

    @staticmethod
    @handle_exceptions
    def input_formatter(**kwargs):
        """
        input formatter method
        """
        if request.content_type == 'application/json':
            # JSON payload
            payload = request.get_json()
        else:
            raise ValueError("NOT SUPPORTED")
            # payload = request.form.to_dict()
        # payload.update(request.args.to_dict())
        return payload

    @staticmethod
    def output_formatter(response, status='success', resp_status=200, **kwargs):
        """
        Output formatter method
        """
        if type(response) == tuple:
            response, resp_status, status = response

        response_dict = dict(vstatus=status, responseText=response)

        if request.content_type in ['application/json']:
            return Response(response=json_response(response_dict, 'response'),
                            status=resp_status,
                            content_type='application/json')
        else:
            return response


@handle_exceptions
def marshal_data(data, schema):
    """
    creating schema format for request/response
    """
    if not schema:
        return data

    # Initialize marshal schema
    schema_obj = schema()

    # Load the request input and marshal.
    # It will raise exception if data is invalid according to the schema.
    marshal = schema_obj.load(data)

    # Return marshalled data
    data = marshal.data

    return data


def io_formatter(request_schema=None, response_schema=None,
                 post_load=None, xml_schema=False, root_values=0, **params):
    """
    Decorator for input output formatting
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get data from request
            data = IO.input_formatter(**params)

            # Validate and marshal input data
            if post_load:
                data = post_load(data)
            data = marshal_data(data, request_schema)

            # Perform the function for handling the API
            if type(data) == tuple:
                response = data
            else:
                response = func(request_params=data, *args, **kwargs)

            # Validate and marshal response
            if type(response) == tuple:
                response = marshal_data(response, None)
            else:
                response = marshal_data(response, response_schema)

            # Format response as per the content-type
            response = IO.output_formatter(response, xml_schema=xml_schema, root_values=root_values, **params)
            return response

        return wrapper

    return decorator


def json_response(response_dict, root='response'):
    """
    method to send json response
    """
    response = json.dumps({root: response_dict})
    return response
