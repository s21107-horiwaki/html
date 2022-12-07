from flask import Flask

# Flaskのインスタンスを作成
app = Flask(__name__)

#ルーティングの指定
@app.route('/')
def index():
	return "Hello,World!"

#実行する
if __name__ == '__main__':
	app.run(port=8502)
