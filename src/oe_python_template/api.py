"""Webservice API of OE Python Template.

- Provides a versioned API
- Automatically registers APIs of modules and mounts them to the main API.
"""

import os

from fastapi import FastAPI

from .constants import API_VERSIONS
from .utils import (
    VersionedAPIRouter,
    __author_email__,
    __author_name__,
    __base__url__,
    __documentation__url__,
    __repository_url__,
    locate_implementations,
)

TITLE = "OE Python Template"
UVICORN_HOST = os.environ.get("UVICORN_HOST", "127.0.0.1")
UVICORN_PORT = os.environ.get("UVICORN_PORT", "8000")
CONTACT_NAME = __author_name__
CONTACT_EMAIL = __author_email__
CONTACT_URL = __repository_url__
TERMS_OF_SERVICE_URL = __documentation__url__

API_BASE_URL = __base__url__
if not API_BASE_URL:
    API_BASE_URL = f"http://{UVICORN_HOST}:{UVICORN_PORT}"

app = FastAPI(
    root_path="/api",
    title=TITLE,
    contact={
        "name": CONTACT_NAME,
        "email": CONTACT_EMAIL,
        "url": CONTACT_URL,
    },
    terms_of_service=TERMS_OF_SERVICE_URL,
    openapi_tags=[
        {
            "name": version,
            "description": f"API version {version.lstrip('v')}, check link on the right",
            "externalDocs": {
                "description": "sub-docs",
                "url": f"{API_BASE_URL}/api/{version}/docs",
            },
        }
        for version, _ in API_VERSIONS.items()
    ],
)

# Create API instances for each version
api_instances: dict["str", FastAPI] = {}
for version, semver in API_VERSIONS.items():
    api_instances[version] = FastAPI(
        version=semver,
        title=TITLE,
        contact={
            "name": CONTACT_NAME,
            "email": CONTACT_EMAIL,
            "url": CONTACT_URL,
        },
        terms_of_service=TERMS_OF_SERVICE_URL,
    )

# Register routers with appropriate API versions
for router in locate_implementations(VersionedAPIRouter):
    router_instance: VersionedAPIRouter = router
    version = router_instance.version
    if version in API_VERSIONS:
        api_instances[version].include_router(router_instance)

# Mount all API versions to the main app
for version in API_VERSIONS:
    app.mount(f"/{version}", api_instances[version])
