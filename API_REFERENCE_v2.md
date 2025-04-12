# API v2 Reference
## OE Python Template v2.0.0

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

[Terms of service](https://oe-python-template.readthedocs.io/en/latest/)
Email: [Helmut Hoffer von Ankershoffen](mailto:helmuthva@gmail.com) Web: [Helmut Hoffer von Ankershoffen](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template) 

## system

### health_endpoint_health_get



> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/health', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/health',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /health`

*Health Endpoint*

Check the health of the system.

This operation returns the health of the system.
The status can be either UP or DOWN.
If the service is healthy, the status will be UP.
If the service is unhealthy, the status will be DOWN and a reason will be provided.
The response will have a 200 OK status code if the service is healthy,
and a 500 Internal Server Error status code if the service is unhealthy.

Returns:
    Health: The health of the system.

> Example responses

> 200 Response

```json
{
  "components": {
    "property1": {
      "components": {},
      "reason": "string",
      "status": "UP"
    },
    "property2": {
      "components": {},
      "reason": "string",
      "status": "UP"
    }
  },
  "reason": "string",
  "status": "UP"
}
```

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Health](#schemahealth)|


This operation does not require authentication


### health_endpoint_healthz_get



> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/healthz', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/healthz',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /healthz`

*Health Endpoint*

Check the health of the system.

This operation returns the health of the system.
The status can be either UP or DOWN.
If the service is healthy, the status will be UP.
If the service is unhealthy, the status will be DOWN and a reason will be provided.
The response will have a 200 OK status code if the service is healthy,
and a 500 Internal Server Error status code if the service is unhealthy.

Returns:
    Health: The health of the system.

> Example responses

> 200 Response

```json
{
  "components": {
    "property1": {
      "components": {},
      "reason": "string",
      "status": "UP"
    },
    "property2": {
      "components": {},
      "reason": "string",
      "status": "UP"
    }
  },
  "reason": "string",
  "status": "UP"
}
```

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Health](#schemahealth)|


This operation does not require authentication


## hello

### echo_v2_hello_echo_post



> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/hello/echo', headers = headers)

print(r.json())

```

```javascript
const inputBody = '{
  "text": "Hello, world!"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/hello/echo',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /hello/echo`

*Echo V2*

Echo back the provided utterance.

Args:
    request (Utterance): The utterance to echo back.

Returns:
    Echo: The echo.

Raises:
    422 Unprocessable Entity: If utterance is not provided or empty.

> Body parameter

```json
{
  "text": "Hello, world!"
}
```

#### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Utterance](#schemautterance)|true|none|

> Example responses

> 200 Response

```json
{
  "text": "HELLO, WORLD!"
}
```

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Echo](#schemaecho)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|


This operation does not require authentication


### hello_world_hello_world_get



> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/hello/world', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/hello/world',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /hello/world`

*Hello World*

Return a hello world message.

Returns:
    _HelloWorldResponse: A response containing the hello world message.

> Example responses

> 200 Response

```json
{
  "message": "Hello, world!"
}
```

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[_HelloWorldResponse](#schema_helloworldresponse)|


This operation does not require authentication


## Schemas

### Echo






```json
{
  "text": "HELLO, WORLD!"
}

```

Echo

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|text|string|true|none|The echo|

### HTTPValidationError






```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

### Health






```json
{
  "components": {
    "property1": {
      "components": {},
      "reason": "string",
      "status": "UP"
    },
    "property2": {
      "components": {},
      "reason": "string",
      "status": "UP"
    }
  },
  "reason": "string",
  "status": "UP"
}

```

Health

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|components|object|false|none|none|
|» **additionalProperties**|[Health](#schemahealth)|false|none|Represents the health status of a service with optional components and failure reasons.A health object can have child components, each with its own health status.The parent health is automatically computed from its components - it isconsidered UP only if all child components are UP. If any component is DOWN,the parent will also be DOWN with a reason listing the failed components.|
|reason|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|[_HealthStatus](#schema_healthstatus)|true|none|none|

### Utterance






```json
{
  "text": "Hello, world!"
}

```

Utterance

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|text|string|true|none|The utterance to echo back|

### ValidationError






```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

### _HealthStatus






```json
"UP"

```

_HealthStatus

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_HealthStatus|string|false|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|_HealthStatus|UP|
|_HealthStatus|DOWN|

### _HelloWorldResponse






```json
{
  "message": "Hello, world!"
}

```

_HelloWorldResponse

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|true|none|The hello world message|
