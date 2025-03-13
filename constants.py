from flask import session, redirect, url_for
# グローバル変数定義ファイル
# db名
db_name = 'hal_animal.db'

# テーブル名
m_goods = 'm_goods'
m_animal = 'm_animal'
t_cart = 't_cart'
m_member = 'm_member'

# 現在のpage
# リダイレクトする際に、loginページの前に閲覧していたページに飛ぶ
last_page = ''

# ログインユーザ(開発用)
userID = '0001'

# ログイン前ユーザ名
gestName = 'ゲスト'

# 最終URL情報
prevUrl='index'
prevUrlID=''

def login_check():
    if not session.get('id'):
        return redirect(url_for('login'))

okodukai_give = '1'
charge = '2'
okodukai_take = '3'
expence = '4'
