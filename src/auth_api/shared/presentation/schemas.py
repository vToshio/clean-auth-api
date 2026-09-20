from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class DetailResponse(BaseModel, Generic[T]):
    message: str = Field(
        title='Response message',
        description='A summary of the response of the actual request.',
        examples=['Successful request.', 'Unable to process your request.']
    )
    data: Optional[T] = Field(
        title='Additional data (optional)',
        description='A JSON Object containing processed data from the API.',
        examples=[
            { 'field': 'value' }, 
            { 
                'items': [ 
                    { 'id': 1, 'name': 'example.' },
                    { 'id': 2, 'name': 'other example.' }
                ]
            },
            {}
        ]
    )   

    model_config = ConfigDict(
        title='DetailResponse',
        extra='forbid',
        validate_default=True,
        validate_assignment=True,
        validate_return=True
    )


class BaseResponse(BaseModel, Generic[T]):
    code: int = Field(
        title='Status code',
        description='Represents de HTTP status code of the actual request.',
        examples=[200, 201, 404, 422, 500]
    )
    method: str = Field(
        title='HTTP Method',
        description='Represents the HTTP Method of the request (GET, POST, PUT, PATCH or DELETE).',
        pattern=r'^(GET|POST|PUT|PATCH|DELETE)$',
        examples=['DELETE', 'POST', 'GET']
    )
    path: str = Field(
        title='Resource path',
        description='URI path for the requested endpoint.',
        pattern=r'^/.*$',
        examples=['/api/products', '/healthcheck']
    )
    details: DetailResponse[T] = Field(
        title='Response details (optional)',
        description='Detailed payload for success responses.',
        default_factory=lambda: DetailResponse[T](
            message='Successful request.',
            data={}
        ),
        examples=[
            {
                'message': 'Successful request.',
                'data': { 'key': 'value' }
            }
        ]
    )

    model_config = ConfigDict(
        title='BaseResponse',
        extra='forbid',
        validate_default=True,
        validate_assignment=True,
        validate_return=True
    )
    