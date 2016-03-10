from eve import Eve
from flask import request
from oauth2 import BearerAuth, oauth
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve(auth=BearerAuth)
oauth.init_app(app)
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')


@app.route('/oauth/authorize', methods=['GET', 'POST'])
@oauth.authorize_handler
def authorize(*args, **kwargs):
    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        client = Client.query.filter_by(client_id=client_id).first()
        kwargs['client'] = client
        return render_template('oauthorize.html', **kwargs)

    confirm = request.form.get('confirm', 'no')
    return confirm == 'yes'


@app.route('/oauth/token', methods=['GET', 'POST'])
@oauth.token_handler
def access_token():
    return None

app.run(port=app.config.get("LISTEN_PORT"),debug=True)
