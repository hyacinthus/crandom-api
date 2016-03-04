from pymongo import MongoClient

client = MongoClient()
db = client.crandom

joke = {
    "content": "从前有只麋鹿，它在森林里玩儿，不小心走丢了。于是它给它的好朋友长颈鹿打电话：“喂…我迷路啦。”长颈鹿听见了回答说：“喂，我长颈鹿啦~”",
    "answer": "",
    # "author": "",
    # "via": "豆瓣",
    # "via_url": "http://jandan.net/",
    "rank": 5,
}

result = db.joke.insert_one(joke)

print(result.inserted_id)
