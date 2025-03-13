# 作品概要

動物園 EC 地図を巡り、かわいい動物たちの店に訪ね、人参通貨を使って親子ともに安全な買い物を楽しむことができます。手持ちのスマホでも簡単に自動走行車を運転できます。
また、ライブ配信機能で動物にレアルな餌やりをしましょう。これまでのない革新な動物園体験です。

![image](https://github.com/user-attachments/assets/e1745ecb-fc1c-4a6f-ac65-0080fba70f12)


# 実行方法

```sh
$ python3 -m venv venv
$ source venv/bin/activate

$ pip3 install flask
# Using cached MarkupSafe-3.0.2-cp311-cp311-macosx_10_9_universal2.whl (14 kB)
# Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
# Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 flask-3.1.0 itsdangerous-2.2.0

$ pip3 install -r requirements.txt
#   Attempting uninstall: MarkupSafe
#     Found existing installation: MarkupSafe 3.0.2
#     Uninstalling MarkupSafe-3.0.2:
#       Successfully uninstalled MarkupSafe-3.0.2

$ pip3 install flask_socketio
$ pip3 install flask_cors
$ pip3 install constants

$ python3 run.py
#  * Serving Flask app 'app.app'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:8080
#  * Running on http://192.168.1.19:8080
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 141-636-774

```
