# API v2 Reference
## OE Python Template v2.0.0

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

[Terms of service](https://oe-python-template.readthedocs.io/en/latest/)
Email: [Helmut Hoffer von Ankershoffen](mailto:helmuthva@gmail.com) Web: [Helmut Hoffer von Ankershoffen](https://github.com/helmut-hoffer-von-ankershoffen)

## Basics

### echo_v2_echo_post



> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/echo', headers = headers)

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

fetch('/echo',
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

`POST /echo`

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

r = requests.get('/hello-world', headers = headers)

print(r.json())

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/hello-world',
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

`GET /hello-world`

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


## Observability

### health_health_get



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

*Health*

Check the health of the service.

This endpoint returns the health status of the service.
The health status can be either UP or DOWN.
If the service is healthy, the status will be UP.
If the service is unhealthy, the status will be DOWN and a reason will be provided.
The response will have a 200 OK status code if the service is healthy,
and a 500 Internal Server Error status code if the service is unhealthy.

Returns:
    Health: The health status of the service.

> Example responses

> 200 Response

```json
{
  "reason": "string",
  "status": "UP"
}
```

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Health](#schemahealth)|


This operation does not require authentication


### health_healthz_get



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

*Health*

Check the health of the service.

This endpoint returns the health status of the service.
The health status can be either UP or DOWN.
If the service is healthy, the status will be UP.
If the service is unhealthy, the status will be DOWN and a reason will be provided.
The response will have a 200 OK status code if the service is healthy,
and a 500 Internal Server Error status code if the service is unhealthy.

Returns:
    Health: The health status of the service.

> Example responses

> 200 Response

```json
{
  "reason": "string",
  "status": "UP"
}
```

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Health](#schemahealth)|


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
  "reason": "string",
  "status": "UP"
}

```

Health

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
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
|status|[HealthStatus](#schemahealthstatus)|true|none|Health status enumeration.|

### HealthStatus






```json
"UP"

```

HealthStatus

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|HealthStatus|string|false|none|Health status enumeration.|

##### Enumerated Values

|Property|Value|
|---|---|
|HealthStatus|UP|
|HealthStatus|DOWN|

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
