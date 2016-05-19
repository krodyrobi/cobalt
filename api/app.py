from flask import Flask
from flask_restful import Api as RestApi

from api.volume import Volume, VolumeList

errors = {
    'EtcdConnectionFailed': {
        'message': "The ETCD cluster is not responding.",
        'status': 503,
    }
}


app = Flask(__name__)
api = RestApi(app, errors=errors, catch_all_404s=True)

app.config['RESTFUL_JSON'] = {
    'separators': (', ', ': '),
    'indent': 2,
    'sort_keys': False
}

api.add_resource(VolumeList, '/volumes')
api.add_resource(Volume, '/volumes/<volume_id>')

# Disable this for error handling to take effect
app.debug = True
