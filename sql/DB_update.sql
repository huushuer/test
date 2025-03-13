/* SQL文の間にあるコメントにはPythonと連携して変数を入れる */
/* 【】の中はページ名 */


/*　【マイページ】 */
/* 情報変更時 ID変更 */
update M_Member SET F_MemberID = /* 新しいID */
where M_Member = /* 付与先会員ID */

/* 情報変更時(変更ボタン押下後) パスワード変更 */
update M_Member SET F_Password = /* 新しいpassward */
where M_Member = /* 付与先の会員ID */

/* 情報変更時　住所変更 */
update M_Member SET F_Address = /* 新しい住所 */
where M_Member = /*　付与先の会員ID */

/* 情報変更時 電話番号 */
update M_Member SET F_PhoneNum = /* 新しい電話番号 */
where M_Member = /* 付与先の会員ID */


/* 【ニンジン通貨管理ページ】 */
/* 子供アカウントに人参通貨を付与 */
update M_Member SET F_Carrot = /* 計算後のニンジン通貨(5個減らした数)*//
where F_MemberID = /* 付与先の会員ID */

update M_Member SET F_Carrot = /* 計算後のニンジン通貨(5個減らした数) */
where /*会員ID*/ = /*付与先の会員ID(子供アカウント)*/


/* 【子供用ページ】 */
/* 子供情報変更 */
update M_Member SET F_Password = /* 新しいpassword */
where M_Member = /* クリックされた子供のID */

update M_Member SET F_MemberID = /* 新しいID */
where M_Member = /* クリックされた子供のID */

update M_Member SET F_PhoneNum = /* 新しい電話番号 */
where M_Member = /* クリックされた子供のID */

update M_Member SET F_Address = /* 新しい住所 */
where M_Member = /* クリックされた子供のID */

/*　【購入確認ページ】 */
/*　ニンジン通貨の更新 */
update M_Member SET F_Carrot = F_Carrot - /* 差引額 */

/* 在庫のUPDATE */
update M_Goods SET F_GoodsStock = F_GoodsStock - /* ユーザーが購入した数(を引く) */
where F_GoodsID = /* ユーザーのID */