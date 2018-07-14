"""
    This endpoint is to redirect requests from Slack into our isolated Tracebacks VPC.
"""
import os

import requests

from chalice import Chalice


app = Chalice(app_name='lambda-traceback-slack-proxy')

APP_SERVER_URL = os.environ('APP_SERVER_URL')
APP_CALLBACK_URL = APP_SERVER_URL + '/slack-callback'


@app.route('/slack-callback', methods=['POST'])
def slack_callback():
    """ redirect post requests from slack to our app server"""
    # parse the request
    request = app.current_request
    data = request.json_body

    # forward request to tracebacks server
    r = requests.post(APP_CALLBACK_URL, data=data)
    print(r)


# just for debugging
@app.route('/')
def index():
    return {'hello': 'world'}
