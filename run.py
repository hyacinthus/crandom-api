from eve import Eve

app = Eve()


if __name__ == '__main__':
    app.run(port=app.config.get("LISTEN_PORT"),debug=True)
