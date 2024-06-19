import pytest


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
