# flask app
from flask import Flask

app = Flask(__name__)

app.route("/", method=['get'])
def index():
    return "Running"


if __name__ == "__main__":
    app.run(debug=True, port=8000)