from functools import wraps
from http import HTTPStatus

from fastapi.responses import JSONResponse
from core import exceptions


def exception_handler(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:

            result = await func(*args, **kwargs)

            return result

        except exceptions.BadRequestException as e:

            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content={
                    "error": e.code,
                    "message": e.message,
                    "extra_information": e.extra_information,
                },
            )
        except Exception as e:
            return JSONResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content={
                    "error": "Undefined error",
                    "extra_information": e.args,
                },
            )

    return inner
