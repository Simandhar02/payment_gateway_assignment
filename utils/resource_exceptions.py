from functools import wraps

from flask import current_app as app
from marshmallow.exceptions import ValidationError


def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValidationError as err:
            app.logger.error(err)
            return str(err), 400, 'failed'
        except ValueError as err:
            app.logger.error(err)
            return str(err), 400, 'failed'
        except Exception as exc:
            app.logger.exception(exc)
            return str(exc), 500, 'failed'

    return wrapper
