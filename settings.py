import os

# flask listen port
LISTEN_PORT = int(os.environ.get('COLD_PORT', 5000))

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'crandom')

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# page size
PAGINATION_DEFAULT = 10

# CORS settings
X_DOMAINS = '*'
X_HEADERS = None
X_EXPOSE_HEADERS = None
X_ALLOW_CREDENTIALS = None
X_MAX_AGE = 864000

# data
joke = {
    # 'title' tag used in item links.
    'item_title': 'Dry humor',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
            'required': True,
        },
        'answer': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
        },
        'author': {
            'type': 'objectid',
        },
        'via': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },
        'via_url': {
            'type': 'string',
        },
        'rank': {
            'type': 'number',
        },
    }
}

random = {
    'datasource': {
        'source': 'joke',
        'aggregation': {
            'pipeline': [
                {"$sample": {"size": 5}},
            ]
        }
    },

    # 'schema': {
        # 'content': {
            # 'type': 'string',
            # 'minlength': 1,
            # 'maxlength': 200,
            # 'required': True,
        # },
        # 'answer': {
            # 'type': 'string',
            # 'minlength': 1,
            # 'maxlength': 200,
        # },
        # 'author': {
            # 'type': 'objectid',
        # },
        # 'via': {
            # 'type': 'string',
            # 'minlength': 1,
            # 'maxlength': 20,
        # },
        # 'via_url': {
            # 'type': 'string',
        # },
        # 'rank': {
            # 'type': 'number',
        # },
    # }
}

laifudao = {
    # 'title' tag used in item links.
    'item_title': '来福岛源',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
            'required': True,
        },
        'via': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },
        'via_url': {
            'type': 'string',
        },
        'rank': {
            'type': 'number',
        },
    }
}

pengfu = {
    # 'title' tag used in item links.
    'item_title': '捧腹网源',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
            'required': True,
        },
        'via': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },
        'via_url': {
            'type': 'string',
        },
        'rank': {
            'type': 'number',
        },
    }
}

fml_zh = {
    # 'title' tag used in item links.
    'item_title': 'FML翻译源',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
            'required': True,
        },
        'via': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },
        'via_url': {
            'type': 'string',
        },
        'rank': {
            'type': 'number',
        },
    }
}

qiubai = {
    # 'title' tag used in item links.
    'item_title': '糗事百科源',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 200,
            'required': True,
        },
        'via': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },
        'via_url': {
            'type': 'string',
        },
        'rank': {
            'type': 'number',
        },
    }
}

DOMAIN = {'joke': joke,
          'random': random,
          'laifudao': laifudao,
          'pengfu': pengfu,
          'qiubai': qiubai,
          'fml_zh': fml_zh,
}

