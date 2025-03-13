/* SQL文の間にあるコメントにはPythonと連携して変数を入れる */
/* 【】の中はページ名 */


/* 【マイページ】 */
/* HTMLを開いた時に子供のIDも取得する */
select F_MemberID from m_member where F_ParentID = F_MemberID

/* ページ取得時SQL */
select F_MemberID,F_MemberName,F_Password,F_PhoneNum,F_Address,F_Carrot from M_Member


/* 【動画紹介画面】*/
/* 選択した動物を参照 */
select F_AnPhotoStorage from M_Animal where F_AnimalID = /* 選択した動物 */

/* 選択したグッズを参照  */
select F_PictureALT from T_PhotoStorage where F_AnimalID = /* 選択した動物 */
/* T_PhotoStorageの中にF_AnimalIDを外部参照する必要がある(?) 11月11日メモ */

/* 【関連グッズ】 */
/* SQL1 */
select F_GoodsID,F_GoodsName,F_ImageStorage from M_Goods Where F_AnimalID = /* 選択した動物 */

/* SQL2(全部の動物) */
select F_GoodsID,F_GoodsName,F_ImageStorage,F_GoodsPrice from M_Goods

/* 【カート】 */
/* SQL1（内部結合) */
select M_Goods.F_GoodsName,M_Goods.F_ProductDescript,M_Goods.F_GoodsPrice,T_Cart.F_GoodsQTY
from M_Goods INNER JOIN T_Cart ON M_Goods.F_GoodsID = T_Cart.F_GoodsID where CartID = /* 会員ID */


/* 【購入確認ページ】*/
/* 初期画面で出す */
select M_Goods.F_GoodsName,M_Goods.F_ProductDescript,M_Goods.F_GoodsPrice,T_Cart.F_GoodsQTY
 from M_Goods INNER JOIN T_Cart ON M_Goods.F_GoodsID = T_Cart.F_GoodsID where
  where CartID = /* 会員ID */

/* 顧客情報 */
select F_MemberName,F_carrot,F_Address from M_Member


