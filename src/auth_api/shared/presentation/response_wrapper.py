from collections.abc import Callable
from fastapi import Request, Response
from fastapi.routing import APIRoute
import json

class ResponseWrapper(APIRoute):
    def get_route_handler(self) -> Callable:
        original_handler = super().get_route_handler()

        async def custom_handler(request: Request) -> Response:
            response: Response = await original_handler(request)
            body = json.loads(response.body)

            data = {
                'code': response.status_code,
                'method': request.method,
                'path': request.url.path,
                'details': { 
                    'message': 'Successfull request.', 
                    'data': body
                }
            }

            return Response(
                content=json.dumps(data),
                status_code=response.status_code,
                media_type='application/json'
            )

        return custom_handler
