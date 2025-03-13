# database acssess object
# 参考サイト
# https://qiita.com/believeriver/items/d946e21512190f0078e7
import mysql.connector
import mysql


class dao_mysql(object):
    # コンストラクタ パスワードなし版
    # def __init__(self, database_name, hostname='127.0.0.1', user='root'):
    #     self._hostname = hostname
    #     self._user = user
    #     self._database_name = database_name
    #     self._conn = None
    #     self._curs = None
    #     self._create_database()
    #     self._conn_db()

    # コンストラクタ パスワードあり版
    def __init__(
        self, database_name, password="root", hostname="127.0.0.1", user="root"
    ):
        self._hostname = hostname
        self._user = user
        self._database_name = database_name
        self._password = password  # password用に追記
        self._conn = None
        self._curs = None
        self._create_database()
        self._conn_db()

    # デストラクタ インスタンスを削除する
    def __del__(self):
        self._close_db()
        print("clear dao_mysql instance")

    # オブジェクトの文字列表現を定義するために用いる特殊メソッド
    # デバッグなどの際にオブジェクトの情報が分かりやすくするように作成
    def __str__(self):
        print("check print")
        print("hostname ", self._hostname)
        print("user name", self._user)
        print("database ", self._database_name)
        return ""

    # db接続 パスワードなし版
    # def _conn_db(self):
    #     self._conn = mysql.connector.connect(host=self._hostname,
    #                                         user=self._user,
    #                                         password = self.__password,
    #                                         database=self._database_name)

    # db接続 パスワードあり版
    def _conn_db(self):
        self._conn = mysql.connector.connect(
            host=self._hostname,
            user=self._user,
            password=self._password,
            database=self._database_name,
        )
        self._curs = self._conn.cursor()

    # db切断
    def _close_db(self):
        self._curs.close()
        self._conn.close()
        print("--- close " + self._database_name + " database ---")

    # db作成 パスワードなし版
    # def _create_database(self):
    #     self._conn = mysql.connector.connect(host=self._hostname,
    #                                         user=self._user)
    # db作成 パスワードあり版
    def _create_database(self):
        self._conn = mysql.connector.connect(
            host=self._hostname, user=self._user, password=self._password
        )
        self._curs = self._conn.cursor()
        self._curs.execute("CREATE DATABASE IF NOT EXISTS " + self._database_name)
        self._conn.commit()
        self._curs.close()
        self._conn.close()

    # テーブル作成 使わない
    def create_table(self, table_name):
        self._curs.execute(
            "CREATE TABLE IF NOT EXISTS " + table_name + "("
            "id int NOT NULL AUTO_INCREMENT,"
            "name varchar(14) NOT NULL,"
            "PRIMARY KEY(id))"
        )
        self._conn.commit()
        print("* createv" + table_name + " talbe ")

    # テーブルへのデータ挿入
    def insert_name(self, table_name, name):
        self._curs.execute(
            "INSERT INTO " + table_name + '(name) values("' + name + '")'
        )
        self._conn.commit()
        print("* insert data ")

    # テーブルへのデータ更新
    def update_name(self, table_name, new_name, pre_name):
        self._curs.execute(
            "UPDATE "
            + table_name
            + ' set name = "'
            + new_name
            + '" WHERE name = "'
            + pre_name
            + '"'
        )
        self._conn.commit()
        print("* update data")

    # テーブルからのデータ削除
    def delete_name(self, table_name, name):
        self._curs.execute("DELETE FROM " + table_name + ' WHERE name = "' + name + '"')
        self._conn.commit()
        print("* delete data")

    # 検索
    def select_all(self, table_name):
        self._curs.execute("SELECT * FROM " + table_name)
        result = self._curs.fetchall()
        for row in self._curs:
            print(row)
        return result

    # 検索 変更前
    # def select_all(self, table_name):
    #     self._curs.execute('SELECT * FROM ' + table_name)
    #     for row in self._curs:
    #         print(row)


# test
database_name = "hew_animal"
table_name = "m_animal"
db = dao_mysql(database_name)
print(db)
db.select_all(table_name)  # select結果を保持するオブジェクトに格納
# animal_data_object = db結果
del db

# テスト結果
# check print
# hostname  127.0.0.1
# user name root
# database  hew_animal

# ('0001', 'パンダ', 'フォルダ宛先1', '説明文1')
# ('0002', '羊', 'フォルダ宛先2', '説明文2')
# ('0003', 'カピバラ', 'フォルダ宛先3', '説明文3')
# ('0004', 'ひよこ', 'フォルダ宛先4', '説明文4')
# ('0005', 'いぬ', 'フォルダ宛先5', '説明文5')
# ('0006', 'ねこ', 'フォルダ宛先6', '説明文6')
# --- close hew_animal database ---
# clear dao_mysql instance

    # # # DB処理########################################################
    # # # 接続処理 開始 ---->
    # # database_name = 'hew_animal'
    # # db = dao_mysql(database_name)
    # # print(db)
    # # # 接続処理 終了 <----
    # # # goods取得select
    # # select_result = db.select_all('m_goods')
    # # goodss = []
    # # for row in select_result:
    # #     goods = Goods(row[0],row[1],row[2],row[3],row[4],row[5])
    # #     goodss.append(goods)
    # # # DB切断 開始 ---->
    # # del(db)
    # # # DB切断 終了 <----
    # # # DB処理########################################################
