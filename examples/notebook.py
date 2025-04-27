# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "oe-python-template==0.16.11",
# ]
# ///


import marimo
from oe_python_template.utils import __version__

__generated_with = "0.13.0"
app = marimo.App(app_title=f"🧠 OE Python Template v{__version__}", width="full")


@app.cell
def _():
    import marimo as mo
    from oe_python_template.hello import Service

    service = Service()
    message = service.get_hello_world()

    with mo.redirect_stdout():
        print(message)
    return


if __name__ == "__main__":
    app.run()
