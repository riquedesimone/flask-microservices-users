from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')


@app.route('/ping', methods=['GET'])
def prig_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
