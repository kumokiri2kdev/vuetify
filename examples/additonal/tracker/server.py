import time
import json
from flask import Flask, request, jsonify, make_response, send_from_directory
import time

app = Flask(__name__, static_folder='')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def send_index_file():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/api/path")
def get_path():
    paths = {
        'Device01':[
            [34.72481520361006, 135.35753642536875, 1985, 1567566213, 0],
            [34.72142902133155, 135.36196743458177, 1984, 1567566212, 0],
            [34.719982797047926, 135.36043321112476, 1983, 1567566211, 1],
            [34.718457179399756, 135.3595427177712, 1982, 1567566210, 0]
        ],
        'Device02':[
            [35.70582253387049, 139.75254575733493, 555, 1567566215, 0],
        ]
    }
    device = request.args.get("device", default="", type=str)
    ts = request.args.get("ts", default=-1, type=int)

    print(ts)

    response_json = {
        'device': device,
    }

    if ts >= 0:
        delta_path = []
        for path in paths[device]:
            if path[3] > ts:
                delta_path.append(path)
            else:
                break

        response_json['path'] = delta_path
        response_json['type'] = 'delta'

    else:
        response_json['path'] = paths[device]
        response_json['type'] = 'entire'



    response = make_response(jsonify(response_json))

    #time.sleep(10)
    return response



@app.route("/api/paths", methods=["GET"])
def get_paths():
    paths = {
        'Device01':[
            [34.72142902133155, 135.36196743458177, 1984, 1567566212, 0],
            [34.719982797047926, 135.36043321112476, 1983, 1567566211, 1],
            [34.718457179399756, 135.3595427177712, 1982, 1567566210, 0]
        ],
        'Device02':[
            [35.70582253387049, 139.75254575733493, 555, 1567566215, 0],
        ]
    }

    response = make_response(jsonify(paths))

    return response


@app.route("/api/devices", methods=["GET"])
def get_device():
    devices = [
        'Device01',
        'Device02'
    ]

    response = make_response(jsonify(devices))

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
