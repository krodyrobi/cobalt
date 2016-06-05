config = {
    'etcd': {
        'host': '127.0.0.1',
        'port': 4001,
        'srv_domain': None,
        'version_prefix': '/v2',
        'read_timeout': 60,
        'allow_redirect': True,
        'protocol': 'http',
        'cert': None,
        'ca_cert': None,
        'username': None,
        'password': None,
        'allow_reconnect': False,
        'use_proxies': False,
        'expected_cluster_id': None,
        'per_host_pool_size': 10,
    },
    'engine': {
        'leaser': {
            'lease_ttl': 60,
            'refresh_ttl': 40,
        },
        'executor': {
            'timeout': 10
        }
    },
    'api': {
        'host': '',
        'port': 5000
    },
    'agent': {
        'agent_ttl': 60,
        'max_error_count': 3,
        'node': {
            'volume_path': '/volumes',
            'conf_path': '/etc/cobalt.conf'
        },
        'watch_timeout': 10
    },
    'services': ['api', 'engine', 'agent'],
    'mount_point': None
}