from pymongo import MongoClient

client = MongoClient()
db = client.crandom

joke = {
    "content": "有一只熊走过来，猜一个成语。",
    "answer": "有备而来。",
    # "author": "",
    "via": "豆瓣",
    # "via_url": "http://jandan.net/",
    "rank": 3,
}

result = db.joke.insert_one(joke)

print(result.inserted_id)
