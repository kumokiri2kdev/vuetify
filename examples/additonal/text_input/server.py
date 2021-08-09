import time
import json
from flask import Flask, request, jsonify, make_response, send_from_directory
app = Flask(__name__, static_folder='')


@app.route('/')
def send_index_file():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/post', methods=["POST"])
def receive():
    try:
        body = request.get_data().decode('utf-8')

        json_data = json.loads(body)
        ut = time.time()
        ts = int(ut * 1000)

        json_data['ts'] = ts

        filename = './posted/{}.json'.format(ts)

        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        print(body)

        response = {
            'status' : 'received'
        }
        response = make_response(jsonify(response))
        return response
    except:
        return jsonify({'status': 'server error handled'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
