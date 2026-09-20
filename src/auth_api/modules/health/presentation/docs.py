from fastapi import status
from ....shared.presentation.response_wrapper import ResponseWrapper
from ....shared.presentation.schemas import BaseResponse

router_docs = {
    'prefix': '',
    'tags': ['health'],
    'route_class': ResponseWrapper
}

healthcheck_docs = {
    'summary': 'Checks the current health of the application.',
    'description': 'This endpoint should be used to verify the current disponibility of the application. It verifies the disponibility verifying the database, cache server, or external services.',
    'status_code': status.HTTP_200_OK,
    'responses': {
        200: {
            'model': BaseResponse,
            'description': 'Successful Response',
            'content': {
                'application/json': {
                    'example': {
                        'code': 200,
                        'method': 'GET',
                        'path': '/healthcheck',
                        'details': {
                            'message': 'Successfull request.',
                            'data': {
                                'status': 'ok'
                            }
                        }
                    }
                }
            }
        }
    }
}