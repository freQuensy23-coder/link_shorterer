import os
from flask import Flask, redirect
from flask import request, jsonify, abort
import json
import logging

app = Flask(__name__)


@app.route("/<path:path>")
def default(path):

    return redirect("http://www." + path, code=302)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
