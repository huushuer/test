import sqlite3;

# データベースを作る
dbname = 'hal_animal.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# m_member作成
cur.execute('''CREATE TABLE IF NOT EXISTS m_member (
    F_MemberID TEXT PRIMARY KEY,
    F_MemberName TEXT,
    F_Password TEXT,
    F_Birthday TEXT,
    F_ParentID TEXT,
    F_Carrot INTEGER,
    F_LoginFlg TEXT,
    F_PostalCode TEXT,
    F_Address TEXT,
    F_PhoneNum TEXT,
    F_Email TEXT
)''')

# m_memberにデータを格納
cur.executemany('''
    INSERT INTO m_member (F_MemberID, F_MemberName, F_Password, F_Birthday, F_ParentID, F_Carrot, F_LoginFlg,F_PostalCode, F_Address, F_PhoneNum, F_Email)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('0001', 'isatoshi', '2222', '2024-03-05', '0000', 10000, '1','2480023', '神奈川県鎌倉市小町一丁目', '04711111111','a@aaa'),
    ('0002', 'hiyoko', '794', '2024-10-16', '0000', 10000, '1','0000000', '平安京', '08022222222','b@bbb'),
    ('0003', 'ryo yamauchi', 'rrrr', '2024-10-15', '0000', 10000, '1','2790023', '千葉県浦安市高洲5-1D-1005', '090-7201-8648', 'c@ccc'),
    ('0004', 'mickey', 'test2', '2024-10-16', '0001', 10000, '2','2790031', '千葉県浦安市舞浜1-1', '09010101010', 'd@ddd'),
    ('0005', 'syu anki', 'ssss', '1995-03-07', '0002', 10000, '1','2720127', '千葉県市川市塩浜２丁目', '08020201111', 'e@eee'),
    ('0006', 'koizumi', 'mmm', '1995-03-07', '0001', 10000, '1','2720127', '千葉県市川市塩浜２丁目', '08020201111', 'e@eee'),
    ('0007', 'rururu', 'rrr', '1995-03-07', '0002', 10000, '1','2720127', '千葉県市川市塩浜２丁目', '08020201111', 'e@eee'),
    ('0008', 'xingke', 'kkkk', '1995-03-07', '0002', 10000, '1','2720127', '千葉県市川市塩浜２丁目', '08020201111', 'e@eee')
])


# m_animal作成
cur.execute('''CREATE TABLE m_animal (
    F_AnimalID TEXT PRIMARY KEY,
    F_AnimalName TEXT,
    F_ImageName TEXT
)''')

cur.executemany('''INSERT INTO m_animal (F_AnimalID, F_AnimalName, F_ImageName)
VALUES (?, ?, ?)
''', [
    ('0001', 'パンダ', 'panda_1.png'),
    ('0002', '羊', 'miemie_3.png'),
    ('0003', 'カピバラ', 'kapibara.GIF'),
    ('0004', 'ひよこ', 'chicken.png'),
    ('0005', 'いぬ', 'dog_1.png')
])

# m_animal作成
cur.execute('''CREATE TABLE m_animalEx (
    F_AnimalID TEXT PRIMARY KEY,
    F_AnimalEx TEXT,
    F_AnimalComment TEXT,
    F_AnimalManager TEXT
)''')

cur.executemany('''INSERT INTO m_animalEx (F_AnimalID, F_AnimalEx, F_AnimalComment,F_AnimalManager)
VALUES (?, ?, ?, ?)
''', [
    ('0001', '別名オオパンダとも呼ばれ、中国の四川、陝西、甘粛省の高山地帯に自然生息する大型のクマ科動物である。彼らは最も識別しやすい野生動物の一つで、その特徴的な黒と白の毛皮、大きな丸い体、そして表情豊かな顔で知られている。成体の体重は通常、100〜150キログラムに達し、オスの方がメスよりやや大きい傾向がある。','よく懐いてくれている、happyなアニマルです。そんな彼女は、餌やりカメラに興味津々！皆さんに会えることをとても楽しみにしていたので、ぜひ遊びに来てください！','張'),
    ('0002', 'ウシ科ヤギ亜科の鯨偶蹄目の動物。 角を持ち、分厚い体毛（羊毛）に覆われている。 主要な家畜であり、ウールを採取するためや羊乳や羊肉を得るために飼育される。草だけでなく、樹皮や木の芽、花も食べる。食草の採食特性は幅広いとされる','よく遊んでいる、マイペースなアニマルです。そんな彼は、餌やりカメラに興味津々！皆さんに会えることをとても楽しみにしていたので、ぜひ遊びに来てください！','張'),
    ('0003', 'テンジクネズミ科カピバラ属に分類される齧歯類。ヒメカピバラH. isthmiusと2種でカピバラ属を構成する。別名オニテンジクネズミ（鬼天竺鼠）。学名はギリシャ語で水の豚を意味し、漢名も水豚と呼ばれる。現生種の齧歯類では最大の種である。南アメリカ東部アマゾン川流域を中心とした、温暖な水辺に生息する','よく眠っている、のんきなアニマルです。そんな彼は、餌やりカメラに興味津々！皆さんに会えることをとても楽しみにしていたので、ぜひ遊びに来てください！','張'),
    ('0004', '初生雛は全身が黄色の初生羽に被われ、孵化後48時間程度で大きく白い若羽が生え始める。また、初生雛は腹腔の卵黄を栄養源としているが、ふ化後48時間程度でほとんど消化吸収してしまう。ふ化直後から歩き出し、エサや水も自ら取ることができるが、体温調整機能は不十分である。そのため親鳥が育てる場合ではないときは人の手で管理する必要があり、農場などでは温度や湿度を調整できる幼雛（ようすう）鶏舎で飼育される','当動物園では、ひよこがたくさん孵ります！彼らは、餌やりカメラに興味津々！皆さんに会えることをとても楽しみにしていたので、ぜひ遊びに来てください！','金子'),
    ('0005', 'イエイヌは人間の手によって改良されて生まれたものである。最も古くに家畜化されたと考えられる動物であり、現代でもイエネコと並んで代表的なペットまたはコンパニオンアニマルとして、広く飼育されて、親しまれている。比較されるネコと違って、種の性格として人間にとって人懐っこいイメージがある。','この間、お手が出来るようになりました。そんな彼女は、餌やりカメラに興味津々！皆さんに会えることをとても楽しみにしていたので、ぜひ遊びに来てください！','張')
])

#  m_animal_unique作成
cur.execute('''CREATE TABLE m_animal_unique (
    F_AnimalUniqueID TEXT PRIMARY KEY,
    F_AnimalUniqueName TEXT,
    F_AnimalID TEXT,
    F_ImageName TEXT,
    F_ImageEX TEXT,
    F_Gender TEXT,
    F_Hobby TEXT,
    F_Age TEXT
)''')

cur.executemany('''INSERT INTO m_animal_unique (F_AnimalUniqueID, F_AnimalUniqueName, F_AnimalID, F_ImageName, F_ImageEX, F_Gender, F_Hobby, F_Age)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('0001', 'パンダ','0001', 'animal_self_indroduce/panda.png', '張さんに似ているパンダ','2','笹いじり','21歳'),
    ('0002', '羊','0002', 'animal_self_indroduce/sheep.png', '働きもののヒツジ','1','編み物','5歳'),
    ('0003', 'カピバラ','0003', 'animal_self_indroduce/karpibara.png', '寝不足のカピバラ','1','昼寝','4歳'),
    ('0004', 'ひよこ','0004', 'animal_self_indroduce/chicken.png', '空を飛べるひよこ','2','脱走','1歳'),
    ('0005', 'いぬ','0005', 'animal_self_indroduce/dog.png', '手品が得意な犬','2','猫の鳴き真似','4歳')
])

# m_goods作成
cur.execute('''CREATE TABLE m_goods (
    F_GoodsID TEXT PRIMARY KEY,
    F_GoodsName TEXT NOT NULL,
    F_GoodsPrice INTEGER,
    F_GoodsStock INTEGER,
    F_AnimalID TEXT,
    F_ImageName TEXT,
    F_ProductEx TEXT
)''')

cur.executemany('''INSERT INTO m_goods (
    F_GoodsID, F_GoodsName, F_GoodsPrice, F_GoodsStock, F_AnimalID, F_ImageName, F_ProductEx
)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('0001', 'パンダのぬいぐるみ', 1900, 10000, '0001', 'goods_0001.jpg', '触りたくなると好評のパンダのぬいぐるみ'),
    ('0002', 'パンダのキーホルダー', 800, 10000, '0001', 'goods_0002.webp', 'いつでも一緒！パンダのキーホルダー！'),
    ('0003', 'カピバラ柄のボールペン', 1400, 10000, '0003', 'goods_0003.jpg', '大きいカピバラが特徴！カピバラ柄のボールペン！'),
    ('0004', 'カピバラのぬいぐるみ', 1800, 10000, '0003', 'goods_0004.avif', 'もっちもっち！抱きかかえたくなるカピバラのぬいぐるみ'),
    ('0005', 'ひつじのぬいぐるみ', 1900, 10000, '0002', 'goods_0005.jpg', 'チャックを外して毛刈りができる羊のぬいぐるみ'),
    ('0006', 'ひつじベビーニット', 2800, 10000, '0002', 'goods_0006.jpg', 'あったか！ベビー用の羊のニット'),
    ('0007', 'ひよこの卵黄分離機', 800, 10000, '0004', 'goods_0007.jpg', 'キッチンにあるとかわいい！ひよこの卵黄分離機'),
    ('0008', 'ひよこのしゃもじ', 800, 10000, '0004', 'goods_0008.jpg', '自立する！ひよこのしゃもじ'),
    ('0009', 'いぬのキーホルダー', 500, 10000, '0005', 'goods_0009.webp', '犬のキーホルダー'),
    ('0010', 'いぬのTシャツ', 1000, 10000, '0005', 'goods_0010.jpg', '犬のTシャツ')
])

# m_animalwords作成
cur.execute('''CREATE TABLE m_animalwords (
    F_AnimalID TEXT PRIMARY KEY,
    F_AnimalWords TEXT
)''')

cur.executemany('''INSERT INTO m_animalwords (F_AnimalID, F_AnimalWords)
VALUES (?, ?)
''', [
    ('0001', 'パンダ ぱんだ panda'),
    ('0002', '羊 ひつじ ヒツジ sheep'),
    ('0003', 'カピバラ かぴばら capybara'),
    ('0004', 'ひよこ ヒヨコ hiyoko'),
    ('0005', 'いぬ 犬 イヌ dog')
])

# t_cart
# cur.execute('''CREATE TABLE t_cart (
#     F_CartID TEXT NOT NULL,
#     F_MemberID TEXT NOT NULL,
#     F_GoodsID TEXT NOT NULL,
#     F_GoodsQTY INTEGER NOT NULL
# )''')
cur.execute('''CREATE TABLE t_cart (
    F_MemberID TEXT NOT NULL,
    F_GoodsID TEXT NOT NULL,
    F_GoodsQTY INTEGER NOT NULL
)''')

# cartテーブルは初期データなし
# cur.executemany('''INSERT INTO t_cart (F_CartID, F_MemberID, F_GoodsID, F_GoodsQTY) VALUES (?, ?, ?, ?)
# ''', [
# ('0001', '1405', '0004', 4),
# ('0002', '1114', '0001', 8),
# ('0003', '1114', '0007', 20),
# ('0004', '1404', '0008', 1),
# ('0005', '0023', '0003', 3030)
# ])

# t_login
cur.execute('''CREATE TABLE t_login (
    F_LoginID TEXT NOT NULL,
    F_MemberID TEXT,
    F_LoginTime TEXT NOT NULL,
    F_LoginFlg TEXT
)''')

# loginテーブルは初期データなし
# cur.executemany('''INSERT INTO t_login (F_LoginID, F_MemberID, F_LoginTime, F_LoginFlg) VALUES (?, ?, ?, ?)
# ''', [
#     ('0001241018171101', '0023', '2024-10-18 17:13:15', '1'),
#     ('0002241018171350', '1010', '2024-10-18 17:13:50', '2'),
#     ('0003241021212827', '1114', '2024-10-21 21:28:27', '2'),
#     ('0010241021212638', '1404', '2024-10-21 21:26:38', '2'),
#     ('0011241021212748', '1405', '2024-10-21 21:27:48', '1')
# ])

# t_ninjinhis作成
cur.execute('''CREATE TABLE t_ninjinhis (
    F_NinjinHisID INTEGER PRIMARY KEY,
    F_MemberID TEXT NOT NULL,
    F_Category TEXT,
    F_NinjinTime TEXT,
    F_NinjinTc INTEGER,
    F_NinjinWho TEXT
)''')

cur.executemany('''INSERT INTO t_ninjinhis (F_NinjinHisID, F_MemberID, F_Category, F_NinjinTime, F_NinjinTc, F_NinjinWho)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, '0001', '2', '2024-10-21 21:38:18', 10000, '0002'),
    (2, '0002', '2', '2024-10-21 21:38:18', 10000, '0001'),
    (3, '0003', '2', '2024-10-21 21:39:48', 10000, '0003'),
    (4, '0004', '3', '2024-10-21 21:41:00', 10000, '0005'),
    (5, '0005', '3', '2024-10-21 21:41:36', 10000, '0002'),
    (6, '0008', '3', '2024-10-21 21:41:36', 10000, '0002')
])

# m_image作成
# F_ImageID 子画像のID
#  F_GoodsID 親画像のID
#  F_ImageName 子画像の画像名.拡張子
#  F_ImageALT 子画像のalt
cur.execute('''CREATE TABLE m_image (
    F_ImageID TEXT PRIMARY KEY,
    F_GoodsID TEXT NOT NULL,
    F_ImageName TEXT NOT NULL,
    F_ImageALT TEXT NOT NULL
)''')

cur.executemany('''INSERT INTO m_image (F_ImageID, F_GoodsID, F_ImageName, F_ImageALT)
VALUES (?, ?, ?, ?)
''', [
    ('1', '0005', 'goods_0005_01.jpg', '横向きのぬいぐるみ'),
    ('2', '0008', 'goods_0008_01.jpg', 'ひよこのしゃもじを使っている写真')
])

# t_purchasehis作成
cur.execute('''CREATE TABLE t_purchasehis (
    F_PurchaseHis INTEGER PRIMARY KEY,
    F_MemberID TEXT NOT NULL,
    F_GoodsID TEXT NOT NULL,
    F_PurchaseNum INTEGER,
    F_PurchaseTime TEXT
)''')

cur.executemany('''INSERT INTO t_purchasehis (F_PurchaseHis, F_MemberID, F_GoodsID, F_PurchaseNum, F_PurchaseTime)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, '0001', '0001', 2, '2024-10-21 21:45:17'),
    (2, '0002', '0009', 10, '2024-10-21 21:48:04'),
    (3, '0001', '0010', 4, '2024-10-21 21:48:57'),
    (4, '0002', '0005', 3, '2024-10-21 21:49:30'),
    (5, '0001', '0003', 4, '2024-10-21 21:49:30')
])

# iconテーブル
cur.execute('''CREATE TABLE t_icon (
    F_MemberID TEXT NOT NULL,
    F_icon TEXT
)''')

cur.executemany('''INSERT INTO t_icon (F_MemberID, F_icon)
VALUES (?, ?)
''', [
    ('0001', 'isatosi_sennsei.png'),
    ('0002', 'hiyoko_sticker.png'),
    ('0003', 'hato_sticker.png'),
    ('0004', 'ZOO.png'),
    ('0005', 'neko.jpg'),
    ('0006', 'koizumi.webp'),
    ('0007', 'hato_sticker.png'),
    ('0008', 'president.jpg'),
])

# コミット
conn.commit()
conn.close()