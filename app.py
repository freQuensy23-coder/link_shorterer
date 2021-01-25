import os
from flask import Flask, redirect
from flask import request, jsonify, abort
import json
import logging
import db
import logging

DB = db.DB()

app = Flask(__name__)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
host = "127.0.0.1:5000/"


@app.route("/add")
def add_new_short_link():
    """"""
    data = request.args.to_dict()
    redirect_to = data["to"]
    link = DB.add_new_short_link(redirect_to=redirect_to, )
    return f"""You'r link is <a href = "{link}">{host + link}</a>"""


@app.route("/<path:path>")
def use_short(path):
    link = DB.get_redirection_link(short_link=path)
    log.debug(path)
    return redirect("http://www." + link, code=302)


@app.route("/")
def main():
    return """
            <input></input><button>Add</button>
            <script>
                const button = document.querySelector('button');
                const input = document.querySelector('input');
                button.addEventListener('click', updateButton);

                function updateButton() {
                  
                  window.location.replace("/add?to=" + input.value);
                  
                }
            </script>
            """


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run()
