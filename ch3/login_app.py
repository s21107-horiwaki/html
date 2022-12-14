from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = 'm9XE4JH5dB0QK4o4'

# ログインに使うユーザー名とパスワード ---
USERLIST = {
	'taro': 'aaa', 
	'jiro': 'bbb', 
	'sabu': 'ccc',
}

@app.route('/')
def index():
	# ログインフォームの表示 --- 
	return """
	<html><body><h1>ログインフォーム</h1>
	<form action="/check_login" method="POST">
	ユーザー名: <br/>
	<input type="text" name="user"><br>
	パスワード: <br>
	<input type="password" name="pw"><br>
	<input type="submit" value="ログイン">
	</form>
	<p><a href="/private">→秘密のページ</a></p></body></html>
	"""

@app.route('/check_login', methods=['POST'])
def check_login():
	# フォームの値を取得 ---
	user, pw = (None, None)
	if 'user' in request.form:
	    user = request.form['user']
	if 'pw' in request.form:
	    pw = request.form['pw']
	if (user is None) or (pw is None):
	    return redirect('/')
	# ログインチェック ---
	if try_login(user, pw) == False:
	    return """
	    <h1>ユーザー名かパスワードの間違い</h1>
	    <p><a href="/">→戻る</a></p>
	    """
	# 非公開ページに飛ぶ ---
	return redirect('/private')

@app.route('/private')
def private_page():
    # ログインしていなければトップへ飛ばす ---
    if not is_login():
        return """
        <h1>ログインしてください</h1>
        <p><a href="/">→ログインする</a></p>
        """
    # ログイン後のページを表示 ---
    return """
    <h1>ここは秘密のページ</h1>
    <p>あなたはログイン中です。</p>
    <p><a href="/logout">→ログアウト</a></p>
    """

@app.route('/logout')
def logout_page():
    try_logout() # ログアウト処理を実行 ---
    return """
    <h1>ログアウトしました</h1>
    <p><a href="/">→戻る</a></p>
    """

# ログイン処理を行う --- 
def try_login(user, password):
    # ユーザーがリストにあるか？
    if not user in USERLIST:
        return False
    # パスワードがあっているか？
    if USERLIST[user] != password:
        return False
    # ログイン処理を実行
    session['login'] = user
    return True

# ログアウトする ---
def try_logout():
    session.pop('login', None)
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0')
