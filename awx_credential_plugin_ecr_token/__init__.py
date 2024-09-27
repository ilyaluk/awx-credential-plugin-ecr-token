import collections
from base64 import b64decode

import boto3

CredentialPlugin = collections.namedtuple('CredentialPlugin', ['name', 'inputs', 'backend'])


def lookup(region):
    client = boto3.client('ecr', region_name=region)
    result = client.get_authorization_token()
    auth = result['authorizationData'][0]
    auth_token = b64decode(auth['authorizationToken']).decode()
    _, password = auth_token.split(':')
    return password


ecr_plugin = CredentialPlugin(
    'ECR Password',
    inputs={
        'fields': [{
            'id': 'region',
            'label': 'AWS region',
            'type': 'string',
        }],
        'metadata': [],
        'required': ['region'],
    },
    backend=lookup,
)
