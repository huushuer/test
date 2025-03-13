/* SQL文の間にあるコメントにはPythonと連携して変数を入れる */
/* 【】の中はページ名 */


/* 【子供用ページ】 */
/* 子供情報削除 */
DELETE from M_Member WHERE F_MemberID = /*選択された子供のID*/

/* 【購入確認ページ】 */
/* 購入処理トランザクション カートを空にする */
DELETE from T_Cart WHERE F_MemberID = /* 選択された会員ID */

/* 【カート】 */
/* カートから削除 */
DELETE from T_Cart where F_Goods = /* クリックした商品 */

/* 【購入確認ページ】 */
/* カートを空にする */
DELETE from T_Cart where F_MemberID = /* 選択している会員ID */