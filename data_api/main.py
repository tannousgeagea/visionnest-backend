import uvicorn
import uuid
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.image_gallery import fetch_images


def create_app() -> FastAPI:
    tags_meta = [
        {
            'name': "VisionNest Data API",
            'description': "VisionNest a place where visual data are nurtured and analyzed"
        }
    ]
    
    app = FastAPI(
        openapi_tags=tags_meta,
        debug=True,
        title='VisionNest: Data API',
        description="VisionNest a place where visual data are nurtured and analyzed",
        version="0.0.1",
        contact={
            'name': 'Tannous Geagea',
            'url': 'http://localhost:3000/',
            'email': 'tannousgeagea@hotmail.com'
        },
        openapi_url="/openapi.json"
    )
    
    origins = ['http://localhost:3000', 'http://localhost:8000']  # Assuming the frontend might be at :3000 and :8000
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["X-Requested-With", "Content-Type"],
        expose_headers=["X-Request-ID"],
    )

    # Here you would add your routes
    app.include_router(fetch_images.router)

    return app


app = create_app()
