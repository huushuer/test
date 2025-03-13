from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from socket import socket, AF_INET, SOCK_DGRAM
import constants
from dao import dao_sqlite
import os

# Flaskオブジェクトの生成
app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "124"
socketio = SocketIO(app, cors_allowed_origins="*")


# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    
    constants.prevUrl = "index"
    return render_template("index.html")


# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    constants.prevUrl = "index"
    return render_template("index.html", animal=animal)
    # return render_template("index.html")


# 「/usage_policy」へアクセスがあった場合に、「usage_policy.html」を返す
@app.route("/usage_policy")
def usage_policy():
    constants.prevUrl = "usage_policy"
    return render_template("usage_policy.html")


# 「/contact」へアクセスがあった場合に、「contact.html」を返す
@app.route("/contact")
def contact():
    constants.prevUrl = "contact"
    return render_template("contact.html")


# 「/login」へアクセスがあった場合に、「login.html」を返す
# 参考サイト
# https://qiita.com/Mochieyan/items/bef45356509cd0867ad3
@app.route("/login", methods=["GET", "POST"])
def login():
    print("test1", constants.prevUrlID)
    if request.method == "POST":
        print("test2", constants.prevUrlID)
        # 適正値が入っているか判定する(正規表現)
        username = request.form.get("flask_username")
        password = request.form.get("flask_userpassword")
        db = dao_sqlite(constants.db_name)
        loginFlg = db.login_judge(username, password)
        print(loginFlg)
        print(f"Username: {username}")
        print(f"Password: {password}")
        if loginFlg == False:
            flash("ユーザー名またはパスワードが異なります")
            return render_template("login.html")
        else:
            print("test3", constants.prevUrlID)
            icon = db.select_icon(session.get("id"))
            session["icon"] = icon
            child_account = (
                True
                if db.select_row("F_ParentID", "M_Member", session.get("id")) != "0000"
                else False
            )
            session["child_account"] = child_account
            # 前にいたページに遷移
            if constants.prevUrl == "goods":
                print(constants.prevUrl)
                print("test4", constants.prevUrlID)
                return redirect(url_for(constants.prevUrl, goodsID=constants.prevUrlID))
            elif constants.prevUrl == "animal":
                print(constants.prevUrl)
                print("test4", constants.prevUrlID)
                return redirect(
                    url_for(constants.prevUrl, F_AnimalUniqueID=constants.prevUrlID)
                )
            elif not constants.prevUrl:
                return redirect(url_for("index"))
            else:
                return redirect(constants.prevUrl)
    else:
        return render_template("login.html")


@app.route("/end_session")
def end_session():
    session.clear()
    session["name"] = constants.gestName
    print(session.get("name"))
    return redirect(url_for("hello"))


# 「/child_login」へアクセスがあった場合に、「index.html」を返す
@app.route("/child_login", methods=["GET", "POST"])
def child_login():
    if request.method == "POST":
        # 適正値が入っているか判定する(正規表現)
        username = request.form.get("flask_username")
        password = request.form.get("flask_userpassword")
        db = dao_sqlite(constants.db_name)
        loginFlg = db.login_judge(username, password)
        print(loginFlg)
        print(f"Username: {username}")
        print(f"Password: {password}")
        if loginFlg == False:
            flash("ユーザー名またはパスワードが異なります")
            return render_template("child_login.html")
        else:
            icon = db.select_icon(session.get("id"))
            session["icon"] = icon
            child_account = (
                True
                if db.select_row("F_ParentID", "M_Member", session.get("id")) != "0000"
                else False
            )
            session["child_account"] = child_account
            print("constants.prevUrl:", constants.prevUrl)
            print("icon:", session.get("icon"))
            # print(constants.prevUrl, goodsID=constants.prevUrlID)
            # 前にいたページに遷移
            if constants.prevUrl == "goods":
                print(constants.prevUrl)
                print("test4", constants.prevUrlID)
                return redirect(url_for(constants.prevUrl, goodsID=constants.prevUrlID))
            elif constants.prevUrl == "animal":
                print(constants.prevUrl)
                print("test4", constants.prevUrlID)
                return redirect(
                    url_for(constants.prevUrl, F_AnimalUniqueID=constants.prevUrlID)
                )
            elif not constants.prevUrl:
                return redirect(url_for(index))
            else:
                return redirect(constants.prevUrl)
    else:
        return render_template("child_login.html")


# 「/child_register」へアクセスがあった場合に、「index.html」を返す
@app.route("/child_register", methods=["GET", "POST"])
def child_register():
    if not session.get("id"):
        constants.prevUrl = "child_register"
        return redirect(url_for("login"))

    if request.method == "POST":
        username = request.form.get("flask_username")
        parentName = request.form.get("flask_parentname")
        password = request.form.get("flask_pass")
        confirm_password = request.form.get("flask_pass_confirm")
        db = dao_sqlite(constants.db_name)
        print("test1")

        if not username or not parentName or not password or not confirm_password:
            flash("すべての項目を入力してください。")
            return render_template("child_register.html")

        if password != confirm_password:
            flash("パスワードが一致しません。")
            return render_template("child_register.html")

        # 同じ名前が無いか(countして0だったらTrue)
        if db.check_sameName(username) > 0:
            flash("そのユーザ名はすでに使用されています。")
            return render_template("child_register.html")

        # 取得してきた親の名前がidから取得出来る親の名前と一致するか確認
        if not parentName == db.select_row(
            "F_memberName", "M_Member", session.get("id")
        ):
            constants.prevUrl = "child_register"
            flash(
                "ログイン者と親アカウント名が異なります。登録する親アカウントでログインしてください"
            )
            return redirect(url_for("login"))

        # 親が存在するか(where句でTELを指定してcountして0だったらTrue)
        # if not db.has_Parent(tel):
        #     flash("登録されている親アカウントの電話番号と一致していません。")
        #     return render_template("child_register.html")

        try:
            # 登録処理
            # 親ID取得(SQL)、ユーザ名取得(HTML)、電話番号取得(HTML)、パスワード取得(HTML)
            db.insert_child(username, password, session.get("id"))
            return redirect(url_for("child_login"))
        except Exception as e:
            flash(f"登録に失敗しました: {e}")
            return render_template("child_register.html")
    return render_template("child_register.html")


# 「/register」へアクセスがあった場合に、「register_member.html」を返す
@app.route("/register_member", methods=["GET", "POST"])
def register_member():
    # constants.prevUrl = "index"
    db = dao_sqlite(constants.db_name)
    userid = db.create_userid().zfill(4)

    if request.method == "POST":
        username = request.form.get("flask_username")
        tel = request.form.get("flask_tel")
        password = request.form.get("flask_pass")
        confirm_password = request.form.get("flask_pass_confirm")

        if not username or not tel or not password or not confirm_password:
            flash("すべての項目を入力してください。")
            return render_template("register_member.html")

        if password != confirm_password:
            flash("パスワードが一致しません。")
            return render_template("register_member.html")

        if db.check_sameName(username) > 0:
            flash("そのユーザ名はすでに使用されています。")
            return render_template("register_member.html")

        try:
            db.insert_member(userid, username, tel, password)
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"登録に失敗しました: {e}")
            return render_template("register_member.html")

    return render_template("register_member.html")


# 「/mypage」へアクセスがあった場合に、「mypage.html」を返す
@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    constants.prevUrl = "mypage"
    # ログイン画面遷移処理==>
    if not session.get("id"):
        return redirect(url_for("login"))
    # ログイン画面遷移処理<==
    db = dao_sqlite(constants.db_name)
    members = db.select_Member(session.get("id"))
    if members is None:
        print("No members found")

    if request.method == "POST":
        id = session.get("id")
        member_name = request.form.get("F_MemberName")
        Email = request.form.get("F_Email")
        Phone_Num = request.form.get("F_PhoneNum")
        Postal_Code = request.form.get("F_PostalCode")
        Address = request.form.get("F_Address")

        if not session.get("id"):
            return redirect(url_for("mypage"))
        else:
            db.update_member(id, member_name, Email, Phone_Num, Postal_Code, Address)
            members = db.select_Member(id)
            session["name"] = member_name
            return redirect(url_for("mypage"))
    return render_template("mypage.html", members=members)

@app.route("/mypage_img_upload", methods=["GET", "POST"])
def mypage_img_upload():
    try:
        if request.method == 'POST':
            file = request.files['uploaded-file']
            file_path = os.path.join('./app/static/images/icon', file.filename)
            print('path:', file_path)
            file.save(file_path)
            # 画像をupdate
            db = dao_sqlite(constants.db_name)
            db.update_icon(session.get('id'), file.filename)
            icon = db.select_icon(session.get("id"))
            session["icon"] = icon
        return redirect(url_for('mypage'))
    except FileNotFoundError:
        print('ファイルがありません')
    finally:
        return redirect(url_for('mypage'))

# 「/ninjin_kanri」へアクセスがあった場合に、「ninjin_kanri.html」を返す
@app.route("/ninjin_kanri", methods=["get", "post"])
def ninjin_kanri():
    constants.prevUrl = "ninjin_kanri"
    db = dao_sqlite(constants.db_name)
    purchase = db.select_purchase_history(session.get("id"))
    purchase_date = db.select_purchase_history_date(session.get("id"))
    ninjin = db.select_ninjin(session.get("id"))
    ninjin_history = db.select_ninjin_history(session.get("id"))
    child_info = db.select_child_info(session.get("id"))
    return render_template(
        "ninjin_kanri.html",
        ninjin=ninjin,
        ninjin_historys=ninjin_history,
        purchases=purchase,
        purchase_dates=purchase_date,
        child_infos=child_info,
    )


@app.route("/ninjin_kanri_r1", methods=["get", "post"])
def ninjin_kanri_r1():
    constants.prevUrl = "ninjin_kanri"
    if request.method == "POST":
        add_ninjin = request.form.get("child_okodukai")
        child_id = request.form.get("child_id")
        if not add_ninjin:
            return redirect(url_for("ninjin_kanri"))
        db = dao_sqlite(constants.db_name)
        db.add_child_ninjin(child_id, session.get("id"), add_ninjin)
    return redirect(url_for("ninjin_kanri"))


@app.route("/ninjin_kanri_r2", methods=["get", "post"])
def ninjin_kanri_r2():
    constants.prevUrl = "ninjin_kanri"
    db = dao_sqlite(constants.db_name)
    ninjin = db.select_ninjin(session.get("id"))
    if request.method == "POST":
        prev_ninjin, new_ninjin = ninjin, request.form.get("updated_ninjin")
        if new_ninjin == "NaN":
            print("適切な値を入力してください")
        elif int(prev_ninjin) < int(new_ninjin):
            radio_charge, other_charge = request.form.get(
                "radio_charge"
            ), request.form.get("other_charge")
            addNinjin = radio_charge if radio_charge else other_charge
            db.update_ninjin(
                session.get("id"), new_ninjin, constants.charge, addNinjin
            )  # ニンジン通貨購入したときの処理
        else:
            print("適切な値を入力してください")
        return redirect(url_for("ninjin_kanri"))


# 「/child_account_kanri」へアクセスがあった場合に、「child_account_kanri.html」を返す
@app.route("/child_account_kanri")
def child_account_kanri():
    constants.prevUrl = "child_account_kanri"

    if not session.get("id"):
        return redirect(url_for("login"))

    db = dao_sqlite(constants.db_name)
    members = db.select_child(session.get("id"))

    return render_template("child_account_kanri.html", members=members)


@app.route("/child_mypage", methods=["GET", "POST"])
def child_mypage():
    constants.prevUrl = "child_mypage"

    if not session.get("id"):
        return redirect(url_for("login"))

    db = dao_sqlite(constants.db_name)

    child_id = session.get("child_id", session.get("id"))
    # 選択された子供のIDをセッションから取得（無ければ親のIDを使う）

    members = db.select_mychild(child_id)
    if members is None:
        print("No members found")

    if request.method == "POST":
        member_name = request.form.get("F_MemberName")
        Email = request.form.get("F_Email")
        Phone_Num = request.form.get("F_PhoneNum")
        Postal_Code = request.form.get("F_PostalCode")
        Address = request.form.get("F_Address")

        db.update_member(child_id, member_name, Email, Phone_Num, Postal_Code, Address)
        members = db.select_Member(child_id)
        session["name"] = member_name
        return redirect(url_for("child_mypage"))

    return render_template("child_mypage.html", members=members)


@app.route("/set_child_session/<child_id>")
def set_child_session(child_id):
    print("Received child_id:", child_id)  # デバッグ用
    session["child_id"] = child_id
    return redirect(url_for("child_mypage"))


# 「/intro_animal」へアクセスがあった場合に、「intro_animal.html」を返す
# 動物によって分ける
@app.route("/intro_animal")
def intro_animal():
    constants.prevUrl = "intro_animal"
    return render_template("intro_animal.html")


# 「/live」へアクセスがあった場合に、「live.html」を返す
@app.route("/live")
def live():
    constants.prevUrl = "live"
    return render_template("live.html")


# 「/feed」へアクセスがあった場合に、「feed.html」を返す
@app.route("/feed")
def feed():
    constants.prevUrl = "feed"
    return render_template("feed.html")


# 「/cart」へアクセスがあった場合に、「cart.html」を返す
@app.route("/cart", methods=["GET", "POST"])
def cart():
    constants.prevUrl = "cart"
    if request.method == "POST":
        # ログイン画面遷移処理==>
        if not session.get("id"):
            return redirect(url_for("login"))
        # ログイン画面遷移処理<==
        # DBのcart内容とHTML上の変更を適合させる
        goods_id = request.form.getlist("item_id")  # HTML情報取得
        goods_qty = request.form.getlist("item_count")  # HTML情報取得

        db = dao_sqlite(constants.db_name)
        # 金額が不足していない場合は下記を実行
        db.cart_merge(session.get("id"), goods_id, goods_qty)

        return redirect(url_for("confirm"))
    else:
        db = dao_sqlite(constants.db_name)
        cart_goods = db.select_cart(session.get("id") or "")
        return render_template("cart.html", cart_goods=cart_goods)


# 「/comfirm」へアクセスがあった場合に、「comfirm.html」を返す
@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    constants.prevUrl = "confirm"
    if request.method == "POST":
        print("POST送信")
        # ログイン画面遷移処理==>
        if not session.get("id"):
            return redirect(url_for("login"))
        # ログイン画面遷移処理<==
        db = dao_sqlite(constants.db_name)
        # お金が足りるかチェック
        carrot = db.select_row("F_Carrot", "M_Member", session.get('id'))
        cart = db.sum_cart(session.get('id'))
        if carrot < cart[0][0]:
            flash('にんじん通貨が足りないよ！')
            db = dao_sqlite(constants.db_name)
            cart_goods = db.select_cart(session.get("id"))
            return render_template("confirm.html", cart_goods=cart_goods)
        else:
            db.confirm(session.get("id"))
            return redirect(url_for("thankyou"))

    else:
        db = dao_sqlite(constants.db_name)
        cart_goods = db.select_cart(session.get("id"))
        return render_template("confirm.html", cart_goods=cart_goods)


@app.route("/thankyou")
def thankyou():
    constants.prevUrl = "thankyou"
    return render_template("thankyou.html")


# 「/shop」へアクセスがあった場合に、「comfirm.html」を返す
@app.route("/shop")
def shop():
    constants.prevUrl = "shop"
    db = dao_sqlite(constants.db_name)
    goods = db.select_all(constants.m_goods)
    animals = db.select_all(constants.m_animal)
    return render_template("shop.html", goods=goods, animals=animals)


# 「/goods」へアクセスがあった場合に、「goods.html」を返す
@app.route("/goods/<string:goodsID>", methods=["GET", "POST"])
def goods(goodsID):
    constants.prevUrl = "goods"
    constants.prevUrlID = goodsID
    if request.method == "POST":
        # ログイン画面遷移処理==>
        if not session.get("id"):
            return redirect(url_for("login"))
        # ログイン画面遷移処理<==
        qty = request.form.get("flask_qty")
        if not qty:
            db = dao_sqlite(constants.db_name)
            goods = db.select_goods(goodsID)
            return render_template("goods.html", goods=goods)
        # t_cart登録処理
        db = dao_sqlite(constants.db_name)
        db.insert_cart(session.get("id"), goodsID, qty)
        return redirect(url_for("cart"))

    else:
        db = dao_sqlite(constants.db_name)
        goods = db.select_goods(goodsID)
        return render_template("goods.html", goods=goods)


@app.route("/animal/<string:F_AnimalUniqueID>")
def animal(F_AnimalUniqueID):
    constants.prevUrl = "animal"
    constants.prevUrlID = F_AnimalUniqueID
    print(F_AnimalUniqueID)
    print(constants.prevUrlID)
    db = dao_sqlite(constants.db_name)
    animals = db.select_animals(F_AnimalUniqueID)
    return render_template("animal.html", animals=animals)


@app.route("/feed_live")
def feed_live():
    return render_template("feed_live.html")


@app.route("/broadcaster")
def broadcaster():
    return render_template("broadcaster.html")

@app.route("/search", methods=["POST"])
def search():
    # 該当グッズのID、Name、Image、Exを取得する
    try:
        db = dao_sqlite(constants.db_name)
        search = request.form.get('searchForm')
        search_array = search.split()
        results = db.search(search_array)
        return render_template("search.html", results = results)
    except Exception as e:
            print('サーチ失敗')
            if constants.prevUrl == "goods":
                print(constants.prevUrl)
                return redirect(url_for(constants.prevUrl, goodsID=constants.prevUrlID))
            elif constants.prevUrl == "animal":
                print(constants.prevUrl)
                print("test4", constants.prevUrlID)
                return redirect(
                    url_for(constants.prevUrl, F_AnimalUniqueID=constants.prevUrlID)
                )
            elif not constants.prevUrl:
                return redirect(url_for("index"))
            else:
                return redirect(constants.prevUrl)
            # return render_template("search.html", results = results)

# WebRTC 信令交换
@socketio.on("offer")
def handle_offer(data):
    emit("offer", data, broadcast=True)


@socketio.on("answer")
def handle_answer(data):
    emit("answer", data, broadcast=True)


@socketio.on("candidate")
def handle_candidate(data):
    emit("candidate", data, broadcast=True)


HOST = ""
PORT = 2390
ADDRESS = "192.168.0.154"


def send_udp_command(cmd):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(cmd.encode(), (ADDRESS, PORT))
    s.close()
    return jsonify({"status": "success", "command": cmd})


@app.route("/g")
def g():
    return send_udp_command("g")


@app.route("/s")
def stop():
    return send_udp_command("s")


@app.route("/r")
def right():
    return send_udp_command("r")


@app.route("/l")
def left():
    return send_udp_command("l")


@app.route("/b")
def back():
    return send_udp_command("b")
