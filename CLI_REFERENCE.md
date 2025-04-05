# CLI Reference

Command Line Interface of OE Python Template

**Usage**:

```console
$ oe-python-template [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `health`: Indicate if service is healthy.
* `info`: Print info about service configuration.
* `echo`: Echo the text.
* `hello-world`: Print hello world message and what&#x27;s in...
* `serve`: Start the API server.
* `openapi`: Dump the OpenAPI specification to stdout...

## `oe-python-template health`

Indicate if service is healthy.

**Usage**:

```console
$ oe-python-template health [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `oe-python-template info`

Print info about service configuration.

**Usage**:

```console
$ oe-python-template info [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `oe-python-template echo`

Echo the text.

**Usage**:

```console
$ oe-python-template echo [OPTIONS] [TEXT]
```

**Arguments**:

* `[TEXT]`: The text to echo  [default: Lorem ipsum dolor sit amet, consectetur adipiscing elit.]

**Options**:

* `--json / --no-json`: Print as JSON  [default: no-json]
* `--help`: Show this message and exit.

## `oe-python-template hello-world`

Print hello world message and what&#x27;s in the environment variable THE_VAR.

**Usage**:

```console
$ oe-python-template hello-world [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `oe-python-template serve`

Start the API server.

**Usage**:

```console
$ oe-python-template serve [OPTIONS]
```

**Options**:

* `--host TEXT`: Host to bind the server to  [default: 127.0.0.1]
* `--port INTEGER`: Port to bind the server to  [default: 8000]
* `--watch / --no-watch`: Enable auto-reload  [default: watch]
* `--help`: Show this message and exit.

## `oe-python-template openapi`

Dump the OpenAPI specification to stdout (YAML by default).

**Usage**:

```console
$ oe-python-template openapi [OPTIONS]
```

**Options**:

* `--api-version [v1|v2]`: API Version  [default: v1]
* `--output-format [yaml|json]`: Output format  [default: yaml]
* `--help`: Show this message and exit.
