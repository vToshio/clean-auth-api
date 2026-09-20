from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import cast

async def http_exception_handler(
    request: Request,
    error: Exception
) -> JSONResponse:
    err = cast(HTTPException, error)
    if hasattr(err, 'message') and hasattr(err, 'data'):
        message = getattr(err, 'message')
        data = getattr(err, 'data')
    else:
        match(err.status_code):
            case status.HTTP_401_UNAUTHORIZED:
                message = 'Authentication error'
            case status.HTTP_403_FORBIDDEN:
                message = 'Authorization error'
            case status.HTTP_404_NOT_FOUND:
                message = 'Not found error'
            case status.HTTP_405_METHOD_NOT_ALLOWED:
                message = 'Method not allowed error'
            case status.HTTP_422_UNPROCESSABLE_CONTENT:
                message = 'Form validation error'
            case _:
                message = 'Internal Server Error'
        data = { 'error': str(err.detail) }
    
    return JSONResponse(
        status_code=err.status_code,
        content={
            'code': err.status_code,
            'method': request.method,
            'path': request.url.path,
            'details': {
                'message': message,
                'data': data
            }
        }
    )

async def internal_exception_handler(
    request: Request,
    exception: Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 500,
            'method': request.method,
            'path': request.url.path,
            'details': {
                'message': 'Internal Server Error',
                'data': { 'errors': [ 'An unexpected error occurred.' ]}
            }
        }
    )