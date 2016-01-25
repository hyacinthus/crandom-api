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
    'resource_title': '冷笑话',
    'item_title': 'Dry Humor',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000,
            'required': True,
        },
        'answer': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000,
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

fml = {
    # 'title' tag used in item links.
    'resource_title': 'Fuck My Life',
    'item_title': 'Fuck My Life',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000,
            'required': True,
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

dirty = {
    # 'title' tag used in item links.
    'resource_title': '段子',
    'item_title': 'Dirty Joke',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000,
            'required': True,
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
    'resource_title': '随机一个冷笑话',
    'resource_methods': ['GET'],
    'item_methods': [],
    'datasource': {
        'source': 'joke',
        'aggregation': {
            'pipeline': [
                {"$sample": {"size": 1}},
            ]
        }
    },
}

randomten = {
    'resource_title': '随机十个冷笑话',
    'resource_methods': ['GET'],
    'item_methods': [],
    'datasource': {
        'source': 'joke',
        'aggregation': {
            'pipeline': [
                {"$sample": {"size": 10}},
            ]
        }
    }
}

laifudao = {
    # 'title' tag used in item links.
    'item_title': '来福岛源',

    'schema': {
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1000,
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
            'maxlength': 1000,
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
            'maxlength': 1000,
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
            'maxlength': 1000,
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
          'fml': fml,
          'dirty': dirty,
          'random': random,
          'randomten': randomten,
          'laifudao': laifudao,
          'pengfu': pengfu,
          'qiubai': qiubai,
          'fml_zh': fml_zh,
}

