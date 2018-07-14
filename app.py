"""
    This endpoint is to redirect requests from Slack into our isolated Tracebacks VPC.
"""
from urllib.parse import parse_qs
import os
import traceback

import requests

from chalice import Chalice



app = Chalice(app_name='lambda-traceback-slack-proxy')

APP_SERVER_URL = os.getenv('APP_SERVER_URL')
APP_CALLBACK_URL = '{}/slack-callback'.format(APP_SERVER_URL)


@app.route(
    '/slack-callback',
    methods=['POST'],
    content_types=['application/x-www-form-urlencoded'],
    cors=True
)
def slack_callback():
    """ redirect post requests from slack to our app server"""
    print('starting lambda')

    try:
        # parse the request
        request = app.current_request
        print('received request: %s' % request)
        data = parse_qs(app.current_request.raw_body)
        print('payload: %s' % data)

        # forward request to tracebacks server
        r = requests.post(APP_CALLBACK_URL, data=data)
        print('response from app server: %s' % r)
        return r
    except Exception:
        traceback.print_exc()
        raise


# just for debugging
@app.route('/')
def index():
    return {'hello': 'world'}
