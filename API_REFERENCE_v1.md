# API v1 Reference
---
title:       - system
language_tabs:
toc_footers: []
includes: []
search: true
highlight_theme: darkula
---


                             (pid 60791)                                                                                                                                                                        
components:
  schemas:
    Echo:
      description: Response model for echo endpoint.
      properties:
        text:
          description: The echo
          examples:
          - HELLO, WORLD!
          minLength: 1
          title: Text
          type: string
      required:
      - text
      title: Echo
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    Health:
      description: "Represents the health status of a service with optional components\
        \ and failure reasons.\n\n- A health object can have child components, i.e.\
        \ health forms a tree.\n- Any node in the tree can set itself to DOWN. In\
        \ this case the node is required\n    to set the reason attribute. If reason\
        \ is not set when DOWN,\n    automatic model validation of the tree will fail.\n\
        - DOWN'ness is propagated to parent health objects. I.e. the health of a parent\n\
        \    node is automatically set to DOWN if any of its child components are\
        \ DOWN. The\n    child components leading to this will be listed in the reason.\n\
        - The root of the health tree is computed in the system module. The health\
        \ of other\n    modules is automatically picked up by the system module."
      properties:
        components:
          additionalProperties:
            $ref: '#/components/schemas/Health'
          title: Components
          type: object
        reason:
          anyOf:
          - type: string
          - type: 'null'
          title: Reason
        status:
          $ref: '#/components/schemas/_HealthStatus'
      required:
      - status
      title: Health
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
            - type: string
            - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
      - loc
      - msg
      - type
      title: ValidationError
      type: object
    _HealthStatus:
      enum:
      - UP
      - DOWN
      title: _HealthStatus
      type: string
    _HelloWorldResponse:
      description: Response model for hello-world endpoint.
      properties:
        message:
          description: The hello world message
          examples:
          - Hello, world!
          title: Message
          type: string
      required:
      - message
      title: _HelloWorldResponse
      type: object
info:
  contact:
    email: helmuthva@gmail.com
    name: Helmut Hoffer von Ankershoffen
    url: https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template
  termsOfService: https://oe-python-template.readthedocs.io/en/latest/
  title: OE Python Template
  version: 1.0.0
openapi: 3.1.0
paths:
  /healthz:
    get:
      description: "Determine aggregate health of the system.\n\nThe health is aggregated\
        \ from all modules making\n    up this system including external dependencies.\n\
        \nThe response is to be interpreted as follows:\n- The status can be either\
        \ UP or DOWN.\n- If the service is healthy, the status will be UP.\n- If the\
        \ service is unhealthy, the status will be DOWN and a reason will be provided.\n\
        - The response will have a 200 OK status code if the service is healthy,\n\
        \    and a 503 Service Unavailable status code if the service is unhealthy.\n\
        \nArgs:\n    service (Service): The service instance.\n    response (Response):\
        \ The FastAPI response object.\n\nReturns:\n    Health: The health of the\
        \ system."
      operationId: health_endpoint_healthz_get
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Health'
          description: Successful Response
      summary: Health Endpoint
      tags:
      - system
  /hello/echo/{text}:
    get:
      description: "Echo back the provided text.\n\nArgs:\n    text (str): The text\
        \ to echo.\n\nReturns:\n    Echo: The echo.\n\nRaises:\n    422 Unprocessable\
        \ Entity: If text is not provided or empty."
      operationId: echo_hello_echo__text__get
      parameters:
      - in: path
        name: text
        required: true
        schema:
          title: Text
          type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Echo'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
      summary: Echo
      tags:
      - hello
  /hello/world:
    get:
      description: "Return a hello world message.\n\nReturns:\n    _HelloWorldResponse:\
        \ A response containing the hello world message."
      operationId: hello_world_hello_world_get
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/_HelloWorldResponse'
          description: Successful Response
      summary: Hello World
      tags:
      - hello
  /system/health:
    get:
      description: "Determine aggregate health of the system.\n\nThe health is aggregated\
        \ from all modules making\n    up this system including external dependencies.\n\
        \nThe response is to be interpreted as follows:\n- The status can be either\
        \ UP or DOWN.\n- If the service is healthy, the status will be UP.\n- If the\
        \ service is unhealthy, the status will be DOWN and a reason will be provided.\n\
        - The response will have a 200 OK status code if the service is healthy,\n\
        \    and a 503 Service Unavailable status code if the service is unhealthy.\n\
        \nArgs:\n    service (Service): The service instance.\n    response (Response):\
        \ The FastAPI response object.\n\nReturns:\n    Health: The health of the\
        \ system."
      operationId: health_endpoint_system_health_get
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Health'
          description: Successful Response
      summary: Health Endpoint
      tags:
      - system
  /system/info:
    get:
      description: "Determine aggregate info of the system.\n\nThe info is aggregated\
        \ from all modules making up this system.\n\nIf the token does not match the\
        \ setting, a 403 Forbidden status code is returned.\n\nArgs:\n    service\
        \ (Service): The service instance.\n    response (Response): The FastAPI response\
        \ object.\n    token (str): Token to present.\n\nReturns:\n    dict:\
        \ The aggregate info of the system."
      operationId: info_endpoint_system_info_get
      parameters:
      - in: query
        name: token
        required: true
        schema:
          title: Token
          type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                additionalProperties: true
                title: Response Info Endpoint System Info Get
                type: object
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
      summary: Info Endpoint
      tags:
      - system

> 2025-04-20 21:19:47 INFO     oe_python_template.oe_python_template.utils.boot ⭐ Booting oe_python_template v0.12.0 (project root /Users/helmut/Code/oe-python-template, pid 61111), parent 'Python'  boot.py:78
