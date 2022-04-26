import json

from fastapi.openapi.utils import get_openapi
from main import app


def generate_openapi_spec(app):
    with open("./docs/openapi.json", "w") as f:
        json.dump(
            get_openapi(
                title=app.title,
                version=app.version,
                openapi_version=app.openapi_version,
                description=app.description,
                routes=app.routes,
            ),
            f,
        )


generate_openapi_spec(app=app)
