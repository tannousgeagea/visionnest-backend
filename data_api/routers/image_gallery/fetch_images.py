import os
import time
import django
django.setup()
from typing import Callable, Coroutine, Any
from datetime import datetime
from fastapi import HTTPException
from fastapi.routing import APIRoute
from fastapi.routing import APIRouter
from starlette.requests import Request
from starlette.responses import Response
from fastapi.responses import JSONResponse

from database.models import Dataset

class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request:Request) -> Response:
            before = time.time()
            response:Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers['X-Response-Time'] = str(duration)
            print(f'route duration: {duration}')
            print(f'route response: {response}')
            print(f'route response header: {response.headers}')
            
            return response
        
        return custom_route_handler
    
    
    
router = APIRouter(
    prefix="/api/v1",
    tags=['Images'],
    route_class=TimedRoute,
    responses={404:{"description": "Not Found"}},
)

@router.api_route("/images", methods=["GET"], tags=['Images'])
def read_data():
    try:
        data = []
        images = Dataset.objects.all()
        
        for image in images:
            data.append(
                {
                    'created_at': image.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'image_id': image.image_id,
                    'image_url': "http://127.0.0.1:8000" + image.image_file.url,
                }
            )
        
        return JSONResponse(content=data, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))