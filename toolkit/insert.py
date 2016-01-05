from pymongo import MongoClient

client = MongoClient()
db = client.crandom

joke = {
    "content": "有一天小强问他爸爸：“爸爸，我是不是傻孩子啊？”爸爸说：“傻孩子，你怎么会是傻孩子呢？”",
    # "answer": "",
    # "author": "",
    "via": "豆瓣",
    # "via_url": "http://jandan.net/",
    "rank": 3,
}

result = db.joke.insert_one(joke)

print(result.inserted_id)
