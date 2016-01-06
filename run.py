from eve import Eve
from pymongo import MongoClient

client = MongoClient()
db = client.crandom

app = Eve()


@app.route('/random/', defaults={'count': 1})
@app.route('/random/<int:count>')
def random(count):
    pass



if __name__ == '__main__':
    app.run(port = app.config.get("LISTEN_PORT"))
