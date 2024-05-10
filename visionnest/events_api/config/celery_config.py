import os
import celery
from functools import lru_cache
from kombu import Queue

def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(':')
        return {"queue":  queue}
    
    return {"queue": "celery"}


class BaseConfig:
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@localhost:18046//")
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")

    CELERY_TASK_QUEUES: list = (
        # default queue
        Queue("celery"),
        # custom queue
    )

    CELERY_TASK_ROUTES = (route_task,)
    ACCEPT_CONTENT = ['json', 'pickle']
    TASK_SERIALIZE = 'pickle'
    RESULT_SERIALIZE = 'pickle'
    TIMEZONE = 'UTC'
    ENABLE_UTC = True
    
class DevelopmentConfig(BaseConfig):
    pass

@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()