# オブジェクト呼び出しテスト
from Object import Animal
from Object import Goods
from dao import dao_mysql

# 接続処理 開始 ---->
database_name = 'hew_animal'
db = dao_mysql(database_name)
print(db)
# 接続処理 終了 <----

# animal取得select
select_result = db.select_all('m_animal') # select結果を保持するオブジェクトに格納
animals = []
for row in select_result:
    animal = Animal(row[0],row[1],row[2],row[3])

# DB切断 開始 ---->
del(db)
# DB切断 終了 <----

# 接続処理 開始 ---->
database_name = 'hew_animal'
db = dao_mysql(database_name)
print(db)
# 接続処理 終了 <----

# goods取得select
select_result = db.select_all('m_goods') # select結果を保持するオブジェクトに格納
goodss = []
for row in select_result:
    goods = Goods(row[0],row[1],row[2],row[3],row[4],row[5])
    goodss.append(goods)

# DB切断 開始 ---->
del(db)
# DB切断 終了 <----

for goods in goodss:
    print("------goods------")
    print(goods.goodsID)
    print(goods.goodsEx)
    print(goods.goodsStock)
    print(goods.goodsPrice)

