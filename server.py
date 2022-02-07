from flask import Flask
from flask import request, Response
import sys

app = Flask(__name__)
port = sys.argv[1];

@app.route("/")
def home():
    return "Hello LIVEPERSON !! - My Name is Mario Fried" 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
