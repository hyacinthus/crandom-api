import uuid
from eve.auth import BasicAuth
from flask import request
from redis import StrictRedis
from flask_oauthlib.provider import OAuth2Provider
from mongokit import Connection, Document

import settings


oauth = OAuth2Provider()
mongo = Connection(host=settings.MONGO_HOST,
                        port=settings.MONGO_PORT)
redisdb = StrictRedis(db=9)


## 认证数据结构
@mongo.register
class User(Document):
    """A user, or resource owner, 
    is usually the registered user on your site."""
    __collection__ = 'users'
    __database__ = 'crandom'
    use_dot_notation = True
    use_schemaless = True

    structure = {
            "username": str,
            "password": str,
    }

@mongo.register
class Client(Document):
    """A client is the app which want to use the resource of a user.
    It is suggested that the client is registered by a user on your site,
    but it is not required."""
    __collection__ = 'clients'
    __database__ = 'crandom'
    use_dot_notation = True
    use_schemaless = True

    structure = {
            "_id": str,
            "client_secret": str,
            "client_type": str,
            "redirect_uris": [str],
            "default_redirect_uri": str,
            "default_scopes": [str],
            "allowed_grant_types": [str],
            "allowed_response_types": [str],
            "validate_scopes": [str]
    }


class Grant():
    """A grant token is created in the authorization flow, 
    and will be destroyed when the authorization finished.
    new empty grant: Grant()
    get exist grant: Grant(client_id,code)"""
    client_id = None
    code = None
    redirect_uri = None
    scopes = None
    user_id = None
    expires = None

    def __init__(self, client_id=None, code=None):
        if client_id and code:
            self.client_id = client_id
            self.code = code
            self.redirect_uri = self._get("redirect_uri")
            self.scopes = self._get("scopes")
            self.user_id = self._get("user_id")
            self.expires = self._get("expires")


    def _get(self, key):
        return redisdb.get("oauth:grant:%s:%s:%s" % (self.client_id,
                                                     self.code,
                                                     key))

    def _set(self, key, value):
        redisdb.set("oauth:grant:%s:%s:%s" % (self.client_id,
                                                     self.code,
                                                     key)),
                    value)

    def save(self):
        if client_id and code:
            self._set("redirect_uri", self.redirect_uri)
            self._set("scopes", self.scopes)
            self._set("user_id", self.user_id)
            self._set("expires", self.expires)


## 校验认证部分
class BearerAuth(BasicAuth):
    """ Overrides Eve's built-in basic authorization scheme and uses Redis to
    validate bearer token
    """
    def __init__(self):
        super(BearerAuth, self).__init__()
        self.redis = StrictRedis()

    def check_auth(self, token, allowed_roles, resource, method):
        """ Check if API request is authorized.
        Examines token in header and checks Redis cache to see if token is
        valid. If so, request is allowed.
        :param token: OAuth 2.0 access token submitted.
        :param allowed_roles: Allowed user roles.
        :param resource: Resource being requested.
        :param method: HTTP method being executed (POST, GET, etc.)
        """
        return token and self.redis.get(token)

    def authorized(self, allowed_roles, resource, method):
        """ Validates the the current request is allowed to pass through.
        :param allowed_roles: allowed roles for the current request, can be a
                              string or a list of roles.
        :param resource: resource being requested.
        """
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            token = None
        return self.check_auth(token, allowed_roles, resource, method)



