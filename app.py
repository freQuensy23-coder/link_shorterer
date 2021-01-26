import os
from flask import Flask, redirect
from flask import request, jsonify, abort
import json
import logging
import db
import logging
from urllib.parse import urljoin

DB = db.DB()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
host = "127.0.0.1:5000/"


@app.route("/add")
def add_new_short_link():
    """"""
    data = request.args.to_dict()
    redirect_to = data["to"]
    link = "s/" + DB.add_new_short_link(redirect_to=redirect_to)
    return f"""You'r link is <a href = "{link}">{host + link}</a>"""


@app.route("/s/<path:path>")
def use_short(path):
    link = DB.get_redirection_link(short_link=path)
    log.debug("Path: " + path)
    log.debug("Link: " + link)
    link_to_redirect = urljoin("https:", link)
    log.debug(link_to_redirect)
    return redirect(link_to_redirect, code=302)


@app.route("/")
def main():
    return """
            <input></input><button>Shorten</button>
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
    app.run(debug=True)
