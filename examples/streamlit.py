"""
Streamlit web application that demonstrates a simple interface for OE Python Template.

This module creates a web interface using Streamlit to demonstrate the usage of the service provided by
OE Python Template.
"""

import streamlit as st

from oe_python_template import (
    Service,
    __version__,
)

sidebar = st.sidebar
sidebar.write(
    f" [OE Python Template v{__version__}](https://oe-python-template.readthedocs.io/en/latest/)",
)
sidebar.write("Built with love in Berlin 🐻")

st.title("🧠 OE Python Template ")

# Initialize the service
service = Service()

# Get the message
message = service.get_hello_world()

# Print the message
st.write(f"{message}")
