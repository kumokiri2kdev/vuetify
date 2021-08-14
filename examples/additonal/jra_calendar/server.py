import time
import json
from flask import Flask, request, jsonify, make_response, send_from_directory

import server_logic

app = Flask(__name__, static_folder='')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def send_index_file():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/api/event", methods=["GET"])
def get_event():
    month = request.args.get("month", default=0, type=int)

    month = str(month)

    with open('kaisai.json', mode='r', encoding='utf-8') as f:
        events = json.load(f)

    if month in events:
        event = server_logic.filtering(events[month])
    else:
        event = []

    response = make_response(jsonify(event))

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
