/* SQL文の間にあるコメントにはPythonと連携して変数を入れる */
/* 【】の中はページ名 */


/* 【人参通貨管理ページ】 */
/* 履歴の種別を登録(親or自分の場合) */
INSERT INTO T_Ninjinhis (F_Category) VALUES (1) where F_MemberID = /* ユーザーのID */

/* 履歴の種別を登録(子供の場合) */
INSERT INTO T_Ninjinhis (F_Category) VALUES (3) where F_MemberID = /* ユーザーのID */

/* 【会員登録】 */
/* 会員登録をする */
INSERT INTO M_Member (F_MemberID,F_MemberName,F_Password,F_Birthday,F_ParentID,F_Address,F_PhoneNum) 
VALUES (/* 登録ユーザーの会員ID */,/* 登録ユーザーの会員名 */,/* 登録ユーザーのパスワード */,/* 登録ユーザーの生年月日 */,
/* 登録ユーザーの親アカウントID */,/* 登録ユーザーの住所 */,/* 登録ユーザーの電話番号 */);

/* 【子供用ページ】 */
/* 子供登録　*/
INSERT INTO M_Member (,,,) VALUES (,"","",) where F_MemberID = /* ユーザーのID */;

/* 【購入確認ページ】 */
/*　購入履歴へINSERT */
INSERT INTO t_purchasehis(F_PurchaseHis,F_MemberID,F_GoodsID,F_GoodsQTY,F_PurchaseTime) VALUES
 (/* 購買ID */,/* 会員ID */,/* 商品ID */,/* F_GoodsQTY */,/* F_PurchaseTime */);