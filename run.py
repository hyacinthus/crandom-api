from eve import Eve
from pymongo import MongoClient

client = MongoClient()
db = client.crandom

app = Eve()


@app.route('/random/', defaults={'count': 1})
@app.route('/random/<int:count>')
def random(count):
    cursor = db.joke.aggregate([{'$sample': {'size': 3}}])
    return cursor.resault



if __name__ == '__main__':
    app.run(port=app.config.get("LISTEN_PORT"),debug=True)
