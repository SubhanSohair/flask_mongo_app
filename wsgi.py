from app import app
from jinja2 import escape

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)