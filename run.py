from eve import Eve
from oauth2 import BearerAuth
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve(auth=BearerAuth)
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')
app.run(port=app.config.get("LISTEN_PORT"),debug=True)
