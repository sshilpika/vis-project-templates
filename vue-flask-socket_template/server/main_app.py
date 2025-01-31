from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

import sys
import json
import os
from collections import defaultdict
import pandas as pd

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!' #TODO
# socketio = SocketIO(app)

app.config.from_mapping(
    SECRET_KEY='dev',
    SESSION_REFRESH_EACH_REQUEST=False,
    SESSION_TYPE='filesystem',
    CORS_HEADERS='Content-Type',
    TESTING=True
)

CORS(app)
async_mode = None#"asgi"
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")



# test socketio
@socketio.on('my event')
def handle_message(data):
    print("Data from client", data)
    server_data = {
    "message": "Server says, hi!"
    }
    emit('my response', json.loads(json.dumps(server_data)))


if __name__ == '__main__':
    socketio.run(app, port="8082")
