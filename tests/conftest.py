import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def hello_world_html_string():
    return """
    <html>
      <head>
        <title>Fast Zero</title>
      </head>
      <body>
        <h1>Hello World :)</h1>
      </body>
    </html>"""
