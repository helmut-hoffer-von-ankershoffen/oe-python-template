import marimo

__generated_with = "0.11.13"
app = marimo.App()


@app.cell
def _():
    from oe_python_template import Service

    service = Service()
    message = service.get_hello_world()
    message # type: ignore
    return Service, message, service


if __name__ == "__main__":
    app.run()
