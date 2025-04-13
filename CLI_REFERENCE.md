# CLI Reference

Command Line Interface of

**Usage**:

```console
$ oe-python-template [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

🧠 OE Python Template v0.10.10 - built with love in Berlin 🐻

**Commands**:

* `hello`: Hello commands
* `system`: System commands

## `oe-python-template hello`

Hello commands

**Usage**:

```console
$ oe-python-template hello [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `echo`: Echo the text.
* `world`: Print hello world message and what&#x27;s in...

### `oe-python-template hello echo`

Echo the text.

Args:
    text (str): The text to echo.
    json (bool): Print as JSON.

**Usage**:

```console
$ oe-python-template hello echo [OPTIONS] [TEXT]
```

**Arguments**:

* `[TEXT]`: The text to echo  [default: Lorem ipsum dolor sit amet, consectetur adipiscing elit.]

**Options**:

* `--json / --no-json`: Print as JSON  [default: no-json]
* `--help`: Show this message and exit.

### `oe-python-template hello world`

Print hello world message and what&#x27;s in the environment variable THE_VAR.

**Usage**:

```console
$ oe-python-template hello world [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `oe-python-template system`

System commands

**Usage**:

```console
$ oe-python-template system [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `health`: Determine and print system health.
* `info`: Determine and print system info.
* `serve`: Start the webservice API server.
* `openapi`: Dump the OpenAPI specification.
* `fail`: Fail by dividing by zero.
* `sleep`: Sleep given for given number of seconds.

### `oe-python-template system health`

Determine and print system health.

Args:
    output_format (OutputFormat): Output format (JSON or YAML).

**Usage**:

```console
$ oe-python-template system health [OPTIONS]
```

**Options**:

* `--output-format [yaml|json]`: Output format  [default: json]
* `--help`: Show this message and exit.

### `oe-python-template system info`

Determine and print system info.

Args:
    include_environ (bool): Include environment variables.
    filter_secrets (bool): Filter secrets from the output.
    output_format (OutputFormat): Output format (JSON or YAML).

**Usage**:

```console
$ oe-python-template system info [OPTIONS]
```

**Options**:

* `--include-environ / --no-include-environ`: Include environment variables  [default: no-include-environ]
* `--filter-secrets / --no-filter-secrets`: Filter secrets  [default: filter-secrets]
* `--output-format [yaml|json]`: Output format  [default: json]
* `--help`: Show this message and exit.

### `oe-python-template system serve`

Start the webservice API server.

Args:
    host (str): Host to bind the server to.
    port (int): Port to bind the server to.
    watch (bool): Enable auto-reload.

**Usage**:

```console
$ oe-python-template system serve [OPTIONS]
```

**Options**:

* `--host TEXT`: Host to bind the server to  [default: 127.0.0.1]
* `--port INTEGER`: Port to bind the server to  [default: 8000]
* `--watch / --no-watch`: Enable auto-reload  [default: watch]
* `--help`: Show this message and exit.

### `oe-python-template system openapi`

Dump the OpenAPI specification.

Args:
    api_version (str): API version to dump.
    output_format (OutputFormat): Output format (JSON or YAML).

Raises:
    typer.Exit: If an invalid API version is provided.

**Usage**:

```console
$ oe-python-template system openapi [OPTIONS]
```

**Options**:

* `--api-version TEXT`: API Version. Available: v1, v2  [default: v1]
* `--output-format [yaml|json]`: Output format  [default: json]
* `--help`: Show this message and exit.

### `oe-python-template system fail`

Fail by dividing by zero.

- Used to validate error handling and instrumentation.

**Usage**:

```console
$ oe-python-template system fail [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `oe-python-template system sleep`

Sleep given for given number of seconds.

Args:
    seconds (int): Number of seconds to sleep.

- Used to validate performance profiling.

**Usage**:

```console
$ oe-python-template system sleep [OPTIONS]
```

**Options**:

* `--seconds INTEGER`: Duration in seconds  [default: 10]
* `--help`: Show this message and exit.
