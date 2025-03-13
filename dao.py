import sqlite3;
from flask import session
import constants;
from datetime import datetime
import constants;

class dao_sqlite(object):
    def __init__(self, dbname):
        self.__dbname = dbname
        self.__conn = None
        self.__cur = None
        self._conn_db()
    
    def __del__(self):
        self._close_db()
        print("clear dao_mysql instance")
    
    def _conn_db(self):
        self.__conn = sqlite3.connect(self.__dbname)
        self.__cur = self.__conn.cursor()

    def _close_db(self):
        self.__cur.close()
        self.__conn.close()

    def select_all(self, table_name):
        self.__cur.execute("SELECT * FROM " + table_name)
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        result_dict = []
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        return result_dict
    
    def select_maxID(self, row, table):
        sql = "select max(" + row + ") from " + table
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        if result[0][0]:
            maxID = int(result[0][0]) + 1
            strID = str(maxID)
        else:
            strID = '1'
        return strID
    
    def select_row(self, row, table, userid):
        sql = "select " + row + " from " + table + " where F_MemberID = '" + userid + "'"
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        return result[0][0]
    
    def select_purchase_history(self, memberID):
        sql ="""
        select
                m_goods.F_ImageName
        ,		m_goods.F_GoodsName
        ,		m_goods.F_ProductEX
        ,  		t_purchasehis.F_purchaseNum
        ,		DATE(t_purchasehis.F_purchaseTime) as 'date'
        from	t_purchasehis left outer join  m_goods
        on		t_purchasehis.F_GoodsID = m_goods.F_GoodsID
        where	F_MemberID = '""" + memberID + """'
        order by t_purchasehis.F_purchasehis desc
        """
        self.__cur.execute(sql)
        result_dict = []
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        return result_dict

    def select_purchase_history_date(self, memberID):
        sql ="""
        select distinct DATE(t_purchasehis.F_purchaseTime) as 'date'
        from	t_purchasehis
        where	F_MemberID = '""" + memberID + """'
        order by t_purchasehis.F_purchasehis desc
        """
        self.__cur.execute(sql)
        result_dict = []
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        print('date:',sql)
        return result_dict
    
    def select_child(self):
        print('== child data ==')


    def login_judge(self, userid, password):
        sql = "SELECT count(*) FROM m_member where F_MemberName = '" + str(userid) + "' AND F_Password = '"+ str(password) + "'"
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        if result[0][0] == 1:
            sql = "SELECT F_MemberID FROM m_member where F_MemberName = '" + str(userid) + "' AND F_Password = '"+ str(password) + "'"
            self.__cur.execute(sql)
            result = self.__cur.fetchall()
            session['id'] = result[0][0]
            sql = "SELECT F_Membername FROM m_member where F_MemberID = '" + str(result[0][0]) + "' AND F_Password = '"+ str(password) + "'"
            self.__cur.execute(sql)
            name = self.__cur.fetchall()
            session['name'] = name[0][0]
            judge = True
        else:
            session['name'] = constants.gestName
            judge = False
        return judge
    
    def create_userid(self):
        sql = "select max(F_MemberID) from m_member"
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        userid = int(result[0][0]) + 1
        userid = str(userid)
        # なんかstr型で前に000つけなきゃならない
        return userid

    def insert_member(self, userid, username, tel, password):
        sql = """INSERT INTO M_Member (F_MemberID,F_MemberName,F_Password,F_Birthday,F_ParentID,F_Address,F_PhoneNum,F_Carrot) VALUES ('""" + userid +"""', '""" + username + """' , '""" + password + """' , null , '0000' , null , '""" + tel + """' ,'0');"""
        self.__cur.execute(sql)
        self.__conn.commit()

    # 名前チェック
    def check_sameName(self, username):
        sql = "SELECT count(*) FROM m_member where F_MemberName = '" + str(username) + "'"
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        return result[0][0]

    # # 親チェック
    # def has_Parent(self, tel):
    #     print('check_Parent')
    #     return True

    # 子供メンバー登録処理
    def insert_child(self, childName, childPass, ParentID):
        # 登録処理
        sql = """INSERT INTO M_Member (F_MemberID,F_MemberName,F_Password,F_Birthday,F_ParentID,F_Address,F_PhoneNum,F_Carrot) VALUES ('""" + self.create_userid().zfill(4) +"""', '""" + childName + """' , '""" + childPass + """' , null ,'"""+ ParentID +"""', null , null ,'0');"""
        self.__cur.execute(sql)
        self.__conn.commit()
    
    def update_member(self, id, member_name, Email, Phone_Num, Postal_Code, Address):
        sql = """ UPDATE M_Member SET  F_MemberName = '""" + member_name + """', F_Email = '""" + Email + """', F_PhoneNum = '""" + Phone_Num + """', F_PostalCode = '""" + Postal_Code + """',F_Address = '""" + Address + """' WHERE F_MemberID = '""" + id + """' """
        self.__cur.execute(sql)
        self.__conn.commit()

    def select_goods(self, goodsID):
        self.__cur.execute("SELECT * FROM m_goods where F_GoodsID = '" + goodsID + "'")
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        for row in result:
            dect_zip = dict(zip(column_names, row))
        return dect_zip

    # ニンジン残高取得
    def select_ninjin(self, userid):
        self.__cur.execute("SELECT F_Carrot FROM m_member where F_MemberID = '" + userid + "'")
        ninjin = self.__cur.fetchall()
        return ninjin[0][0]
    
    # ニンジン管理画面で取得
    def update_ninjin(self, userid, new_ninjin, category, add_ninjin):
        sql = """update m_member set F_Carrot = """ + new_ninjin + """ where F_MemberID = '""" + userid + """'"""
        self.__cur.execute(sql)
        self.insert_ninjin_history(userid, category, add_ninjin, userid)
        self.__conn.commit()

    # ニンジン購入履歴出力で使用
    def select_ninjin_history(self,userid):
        sql = """
        select	DATE(F_NinjinTime) as 'date'
,		case
			when F_Category = '1' then  (select F_memberName from m_member where F_MemberID = t_ninjinhis.F_Ninjinwho)||'へのお小遣い'
			when F_Category = '2' then 'チャージ'
			when F_Category = '3' then 'お小遣い'
			when F_Category = '4' then 'お買い物'
			else 'その他'
		end	as 'subject'
,		case
			when F_Category = '2' OR F_Category = '3' then F_NinjinTc
			when F_Category = '1' OR F_Category = '4' then ''
			else 'その他'
		end	as 'charge'
,		case
			when F_Category = '1' OR F_Category = '4' then F_NinjinTc
			when F_Category = '2' OR F_Category = '3' then ''
			else 'その他'
		end	as 'expence'
        from t_ninjinhis
        where	F_MemberID = '""" + userid + """'
        order by F_ninjinhisID desc
        """
        self.__cur.execute(sql)
        result_dict = []
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        return result_dict
    

    def insert_ninjin_history(self, userid, category, ninjin, who):
        maxID = self.select_maxID('F_NinjinHisID', 't_ninjinhis')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = """INSERT INTO t_ninjinhis (
        F_NinjinHisID,
        F_MemberID,
        F_Category,
        F_NinjinTime,
        F_NinjinTc,
        F_NinjinWho) VALUES (
        '""" + maxID + """' ,
        '""" + userid + """' ,
        '""" + category + """' ,
        '""" + timestamp + """' ,
        """ + str(ninjin) + """ ,
        '""" + who + """'
        );"""
        self.__cur.execute(sql)
        # self.__conn.commit()
    
    def insert_purchase_history(self, userid, goodsid, qty):
        maxID = self.select_maxID('F_purchaseHis', 't_purchasehis')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = """
        insert into t_purchasehis(
            F_purchaseHis
            ,	F_MemberID
            ,	F_GoodsID
            ,	F_PurchaseNum
            ,	F_PurchaseTime
            )values(
            """  + maxID + """
            ,	'""" + userid + """'
            ,	'""" + goodsid + """'
            ,	"""+ str(qty) +"""
            ,	'""" + timestamp + """'
        )"""
        self.__cur.execute(sql)

    def select_Member(self, MemberID):
        self.__cur.execute("SELECT * FROM m_member where F_MemberID = '"+ MemberID +"' ")
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        if not result:
            return None 
        dect_zip = {}
        for row in result:
            dect_zip = dict(zip(column_names, row))        
        return dect_zip
    
    def select_child(self,MemberID):
        self.__cur.execute("""
        SELECT M_Member.F_MemberID,
               M_Member.F_MemberName,
               M_Member.F_Carrot,
               t_icon.F_icon
        FROM M_Member
        LEFT JOIN t_icon
        ON M_Member.F_MemberID = t_icon.F_MemberID
        WHERE F_ParentID = '""" + MemberID + """'
    """)

        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()

        return [dict(zip(column_names, row)) for row in result]

    def select_mychild(self, child_id):
        self.__cur.execute("""
        SELECT m_member.*, t_icon.F_icon 
        FROM m_member 
        LEFT JOIN t_icon 
        ON m_member.F_MemberID = t_icon.F_MemberID 
        WHERE m_member.F_MemberID = '""" + child_id + """'
    """)
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        if not result:
            return None 
        dect_zip = {}
        for row in result:
            dect_zip = dict(zip(column_names, row))        
        return dect_zip    
    

    def select_animals(self, F_AnimalUniqueID):
        self.__cur.execute("""  SELECT * 
                                FROM    m_animal_unique
                                join    m_animalEx
                                on      m_animal_unique.F_AnimalUniqueID = m_animalEx.F_AnimalID 
                                where F_AnimalUniqueID = '""" + F_AnimalUniqueID + "'""")
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        for row in result:
            dect_zip = dict(zip(column_names, row))
        return dect_zip

    # goodsページで購入ボタンが押された場合に使用
    def insert_cart(self, memberID, GoodsID, QTY):
        sql = '''INSERT INTO t_cart (F_MemberID,F_GoodsID,F_GoodsQTY)
        VALUES (?, ?, ?)
        '''
        self.__cur.executemany(sql,[(memberID, GoodsID, QTY)])
        self.__conn.commit()

    #  cart画面で購入ボタンが押された場合の処理
    def cart_merge(self, memberID, GoodsID, QTY):
        sql = '''delete from t_cart where F_memberID = ? '''
        self.__cur.execute(sql,[(memberID)])

        for i in range(len(GoodsID)):
            sql = '''INSERT INTO t_cart (F_MemberID,F_GoodsID,F_GoodsQTY)
            VALUES (?, ?, ?)
            '''
            self.__cur.executemany(sql,[(memberID, GoodsID[i], QTY[i])])
        self.__conn.commit()

    # cart画面・confirm画面の表示の際に使用
    def select_cart(self, memberID):
        self.__cur.execute("""select
                        M_Goods.F_GoodsID
                        ,M_Goods.F_GoodsName
                        ,M_Goods.F_ProductEx
                        ,M_Goods.F_GoodsPrice
                        ,sum(T_Cart.F_GoodsQTY) as F_GoodsQTY
                        ,M_Goods.F_ImageName
                        from M_Goods INNER JOIN T_Cart ON M_Goods.F_GoodsID = T_Cart.F_GoodsID
                        where t_cart.F_memberID = '""" + memberID + """'
                        and F_GoodsQTY > 0
                        group by M_Goods.F_GoodsName, M_Goods.F_ProductEx,M_Goods.F_GoodsPrice
                        """)
        
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        result_dict = []
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        return result_dict
    
    # ニンジン減算などの計算で使用
    def sum_cart(self, memberID):
        self.__cur.execute("""
                        select sum(F_GoodsPrice * F_GoodsQTY)
                        from(
                        select
                        M_Goods.F_GoodsName as F_GoodsName
                        ,M_Goods.F_ProductEx as F_ProductEx
                        ,M_Goods.F_GoodsPrice as F_GoodsPrice
                        ,sum(T_Cart.F_GoodsQTY) as F_GoodsQTY
                        from M_Goods INNER JOIN T_Cart ON M_Goods.F_GoodsID = T_Cart.F_GoodsID where t_cart.F_memberID = '""" + memberID + """'
                        group by M_Goods.F_GoodsName, M_Goods.F_ProductEx,M_Goods.F_GoodsPrice)
                        """)
        result = self.__cur.fetchall()
        return result

    # カートにあるGoodsIdを取得
    # 在庫削除処理などで使用
    def select_cart_goodsId(self, memberID):
        self.__cur.execute("""select
                        F_GoodsID
                        ,F_GoodsQTY
                        from T_Cart
                        where F_memberID = '""" + memberID + """'
                        """)
        result_tuple_array = self.__cur.fetchall()
        # 現時点でresultsは下記の型 => [('0010',), ('0009',)]
        # result_array = []
        # for result_tuple in result_tuple_array:
        #     for result in result_tuple:
        #         result_array.append(result)
        return result_tuple_array

    def confirm(self, memberID):
        try:
            self.__cur.execute("BEGIN")
            # 在庫変更処理
            cart_goods = self.select_cart_goodsId(memberID)
            for cart_good in cart_goods:
                # select文で元の値を取得
                self.__cur.execute("""
                            select
                                    F_goodsID
                            ,       F_GoodsStock
                            from    m_goods
                            where   F_goodsID = '""" + str(cart_good[0]) + """'
                            """)
                old_m_goods = self.__cur.fetchall()
                for old_m_good in old_m_goods:
                    # 更新前在庫数取得
                    self.__cur.execute("""select
                            F_goodsID
                            ,F_GoodsQTY
                            from t_cart
                            where F_goodsID = '""" + str(cart_good[0]) + """'
                            and F_memberid = '"""+ memberID +"""'""")
                    selected_cart = self.__cur.fetchall()

                    # 更新在庫数計算
                    new_stock = old_m_good[1] - selected_cart[0][1]
                    # 在庫を更新後在庫数で上書き
                    sql = """ UPDATE M_GOODS SET F_GOODSSTOCK =  """ + str(new_stock) +""" WHERE F_GOODSID = '""" + selected_cart[0][0]+"""'"""
                    self.__cur.execute(sql)

                # 購入履歴更新
                self.insert_purchase_history(memberID, cart_good[0], cart_good[1])

            # ニンジン変更
            print('--- delete ninjin ---')
            # カート情報取得
            sum_cart = self.sum_cart(memberID)
            # 更新前ニンジン取得
            self.__cur.execute("""select
                            F_MemberID
                            ,F_Carrot
                            from M_MEMBER
                            where F_MemberID = '""" + memberID + """'
                            """)
            old_m_member_ninjin = self.__cur.fetchall()

            # 残ニンジン算出減算
            new_ninjin = old_m_member_ninjin[0][1] - sum_cart[0][0]

            # ニンジン更新処理
            sql = """ UPDATE M_MEMBER SET F_Carrot =  """ + str(new_ninjin) +""" WHERE F_MemberID = '""" + memberID +"""'"""
            self.__cur.execute(sql)

            # にんじん使用履歴更新(支出)
            self.insert_ninjin_history(memberID, constants.expence, str(sum_cart[0][0]), memberID)

            # カートの中身削除
            print('--- delete cart ---')
            sql = '''delete from t_cart where F_memberID = ? '''
            self.__cur.execute(sql,[(memberID)])

            self.__conn.commit()
        except Exception as e:
            self.__cur.execute("ROLLBACK")
            print(f"Error:{e}")
        finally:
            print('== confirm処理終了 ==')

    def select_icon(self, userid):
        self.__cur.execute("""
        select  count(F_icon)
        from    t_icon
        where   F_MemberID = '""" + userid + """'
                        """)
        result = self.__cur.fetchall()

        if result[0][0] != 0:
            self.__cur.execute("""
            select  F_icon
            from    t_icon
            where   F_MemberID = '""" + userid + """'
            """)
            result = self.__cur.fetchall()
            return result[0][0]
        return 'default_icon.jpg'
    
    # 画像をupdate
    def update_icon(self, userid, icon):
        # select
        self.__cur.execute("""
        select  count(F_icon)
        from    t_icon
        where   F_MemberID = '""" + userid + """'
                        """)
        result = self.__cur.fetchall()

        if result[0][0] != 0:
            sql = """ UPDATE t_icon SET  F_icon = '""" + icon + """' WHERE F_MemberID = '""" + userid + """' """
            self.__cur.execute(sql)
            self.__conn.commit()
        else:
            sql = """INSERT INTO t_icon (F_MemberID,F_icon) VALUES ('""" + userid +"""', '""" + icon + """');"""
            self.__cur.execute(sql)
            self.__conn.commit()


    def select_child_info(self, userid):
        self.__cur.execute("""select	m_member.F_Carrot as F_Carrot
        ,		m_member.F_MemberID as F_MemberID
        ,		t_icon.F_icon as F_icon
        ,       m_member.F_MemberName as F_MemberName
        from	m_member left outer join t_icon
        on		m_member.F_MemberID = t_icon.F_MemberID
        where	m_member.F_ParentID = '""" + userid + """'
        """)
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        result_dict = []
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        return result_dict
    
    def add_child_ninjin(self, child_id, parent_id, add_ninjin):
        
        child_ninjin = self.select_ninjin(child_id)
        parent_ninjin = self.select_ninjin(parent_id)

        child_ninjin = int(child_ninjin) + int(add_ninjin) 
        parent_ninjin = int(parent_ninjin) - int(add_ninjin)

        sql = """ UPDATE M_MEMBER SET F_Carrot =  """ + str(child_ninjin) +""" WHERE F_MemberID = '""" + child_id +"""'"""
        self.__cur.execute(sql)

        sql = """ UPDATE M_MEMBER SET F_Carrot =  """ + str(parent_ninjin) +""" WHERE F_MemberID = '""" + parent_id +"""'"""
        self.__cur.execute(sql)

        # にんじん使用履歴更新(支出)
        self.insert_ninjin_history(child_id, constants.okodukai_take, str(add_ninjin), parent_id)
        self.insert_ninjin_history(parent_id, constants.okodukai_give, str(add_ninjin), child_id)

        self.__conn.commit()

    def search(self, search_array):
        sql = """select
                M_Goods.F_GoodsID as F_GoodsID
        ,       M_Goods.F_GoodsName as F_GoodsName
        ,       M_Goods.F_ImageName as F_ImageName
        ,       M_Goods.F_ProductEx as F_ProductEx
        from    M_Goods
        join    m_animalwords
        on      M_Goods.F_AnimalID = m_animalwords.F_AnimalID
        where   m_animalwords.F_Animalwords like '%""" + search_array[0] + """%'"""
        for search in search_array:
            sql = sql + """or     F_GoodsName like '%""" + search + """%'
                or F_ProductEx like '%""" + search + """%'"""
        print(sql)
        self.__cur.execute(sql)
        column_names = [desc[0] for desc in self.__cur.description]
        result = self.__cur.fetchall()
        result_dict = []
        for row in result:
            dect_zip = dict(zip(column_names, row))
            result_dict.append(dect_zip)
        return result_dict

