-- hew_animal
CREATE DATABASE hew_animal;
use hew_animal;

--
-- テーブルのデータのダンプ `m_member`
--

CREATE TABLE `m_member` (
  `F_MemberID` char(4) NOT NULL,
  `F_MemberName` varchar(50) NOT NULL,
  `F_Password` varchar(15) NOT NULL,
  `F_Birthday` date DEFAULT NULL,
  `F_ParentID` char(4) DEFAULT NULL,
  `F_Carrot` int(11) DEFAULT NULL,
  `F_LoginFlg` char(1) DEFAULT NULL,
  `F_Address` varchar(50) DEFAULT NULL,
  `F_PhoneNum` char(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `m_member` (`F_MemberID`, `F_MemberName`, `F_Password`, `F_Birthday`, `F_ParentID`, `F_Carrot`, `F_LoginFlg`, `F_Address`, `F_PhoneNum`) VALUES
('0023', 'test03', '2222', '2024-03-05', '2142', 11235006, '1', '神奈川県鎌倉市小町一丁目', '04711111111'),
('1010', 'testuser03', 'test', '2024-10-16', '0000', 555, '1', '東京都千代田区丸の内一丁目９番１号', '08022222222'),
('1114', '山内 遼', 'rrrr', '2024-10-15', '0000', 554, '1', '千葉県浦安市高洲5-1D-1005', '090-7201-8648'),
('1404', 'test02', 'test2', '2024-10-16', '0001', 200, '2', '千葉県浦安市舞浜1-1', '09010101010'),
('1405', 'testuser04', 'test', '2024-10-16', '0002', 222, '1', '千葉県市川市塩浜２丁目', '08020201111');

ALTER TABLE `m_member`
  ADD PRIMARY KEY (`F_MemberID`);
COMMIT;

CREATE TABLE `m_animal` (
  `F_AnimalID` char(4) NOT NULL,
  `F_AnimalName` varchar(50) DEFAULT NULL,
  `F_AnPhotoStorage` varchar(50) DEFAULT NULL,
  `F_AnimalOverview` varchar(4000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `m_animal`
--

INSERT INTO `m_animal` (`F_AnimalID`, `F_AnimalName`, `F_AnPhotoStorage`, `F_AnimalOverview`) VALUES
('0001', 'パンダ', 'フォルダ宛先1', '説明文1'),
('0002', '羊', 'フォルダ宛先2', '説明文2'),
('0003', 'カピバラ', 'フォルダ宛先3', '説明文3'),
('0004', 'ひよこ', 'フォルダ宛先4', '説明文4'),
('0005', 'いぬ', 'フォルダ宛先5', '説明文5'),
('0006', 'ねこ', 'フォルダ宛先6', '説明文6');

ALTER TABLE `m_animal`
  ADD PRIMARY KEY (`F_AnimalID`);
COMMIT;

CREATE TABLE `m_goods` (
  `F_GoodsID` char(4) NOT NULL,
  `F_GoodsName` varchar(50) NOT NULL,
  `F_GoodsPrice` int(11) NOT NULL,
  `F_GoodsStock` int(11) DEFAULT NULL,
  `F_AnimalID` char(4) NOT NULL,
  `F_ImageStorage` varchar(50) DEFAULT NULL,
  `F_ProductDescript` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `m_goods` (`F_GoodsID`, `F_GoodsName`, `F_GoodsPrice`, `F_GoodsStock`, `F_AnimalID`, `F_ImageStorage`, `F_ProductDescript`) VALUES
('0001', 'パンダのぬいぐるみ', 1900, 20, '0001', 'NULL', 'NULL'),
('0002', 'パンダのキーホルダー', 800, 50, '0001', 'NULL', 'NULL'),
('0003', 'カピバラ柄のボールペン', 1400, 21, '0003', 'NULL', 'NULL'),
('0004', 'カピバラのぬいぐるみ', 1800, 19, '0003', 'NULL', 'NULL'),
('0005', 'ひつじのぬいぐるみ', 1900, 24, '0002', 'NULL', 'NULL'),
('0006', 'ひつじのキャップ', 2800, 30, '0002', 'NULL', 'NULL'),
('0007', 'ひよこのぬいぐるみ', 800, 19, '0004', 'NULL', 'NULL'),
('0008', 'ひよこのTシャツ', 800, 25, '0004', 'NULL', 'NULL'),
('0009', 'いぬのキーホルダー', 500, 40, '0005', 'NULL', 'NULL'),
('0010', 'いぬのTシャツ', 1000, 30, '0005', 'NULL', 'NULL');

ALTER TABLE `m_goods`
  ADD PRIMARY KEY (`F_GoodsID`),
  ADD KEY `fk_M_Goods_M_animal` (`F_AnimalID`);

ALTER TABLE `m_goods`
  ADD CONSTRAINT `fk_M_Goods_M_animal` FOREIGN KEY (`F_AnimalID`) REFERENCES `m_animal` (`F_AnimalID`);
COMMIT;

--
-- テーブルのインデックス `t_cart`
--

CREATE TABLE `t_cart` (
  `F_CartID` char(4) NOT NULL,
  `F_MemberID` char(4) NOT NULL,
  `F_GoodsID` char(4) NOT NULL,
  `F_GoodsQuantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `t_cart` (`F_CartID`, `F_MemberID`, `F_GoodsID`, `F_GoodsQuantity`) VALUES
('0001', '1405', '0004', 4),
('0002', '1114', '0001', 8),
('0003', '1114', '0007', 20),
('0004', '1404', '0008', 1),
('0005', '0023', '0003', 3030);

ALTER TABLE `t_cart`
  ADD PRIMARY KEY (`F_CartID`);

ALTER TABLE `t_cart`
  ADD CONSTRAINT `FK_t_cart_M_Goods` FOREIGN KEY (`F_GoodsID`) REFERENCES `m_goods` (`F_GoodsID`),
  ADD CONSTRAINT `FK_t_cart_M_member` FOREIGN KEY (`F_MemberID`) REFERENCES `m_member` (`F_MemberID`);
COMMIT;

--
-- テーブルのインデックス `t_login`
--

CREATE TABLE `t_login` (
  `F_LoginID` char(16) NOT NULL,
  `F_MemberID` char(4) DEFAULT NULL,
  `F_LoginTime` datetime NOT NULL,
  `F_LoginFlg` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `t_login` (`F_LoginID`, `F_MemberID`, `F_LoginTime`, `F_LoginFlg`) VALUES
('0001241018171101', '0023', '2024-10-18 17:13:15', '1'),
('0002241018171350', '1010', '2024-10-18 17:13:50', '2'),
('0003241021212827', '1114', '2024-10-21 21:28:27', '2'),
('0010241021212638', '1404', '2024-10-21 21:26:38', '2'),
('0011241021212748', '1405', '2024-10-21 21:27:48', '1');

ALTER TABLE `t_login`
  ADD PRIMARY KEY (`F_LoginID`),
  ADD KEY `FK_t_login_m_member` (`F_MemberID`);

ALTER TABLE `t_login`
  ADD CONSTRAINT `FK_t_login_m_member` FOREIGN KEY (`F_MemberID`) REFERENCES `m_member` (`F_MemberID`);
COMMIT;



--
-- テーブルの構造 `t_ninjinhis`
--
CREATE TABLE `t_ninjinhis` (
  `F_NinjinHisID` char(4) NOT NULL,
  `F_MemberID` char(4) NOT NULL,
  `F_Category` char(4) DEFAULT NULL,
  `F_NinjinTime` datetime DEFAULT NULL,
  `F_NinjinTc` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `t_ninjinhis` (`F_NinjinHisID`, `F_MemberID`, `F_Category`, `F_NinjinTime`, `F_NinjinTc`) VALUES
('0001', '0023', '1', '2024-10-21 21:38:18', 600),
('0002', '1010', '2', '2024-10-21 21:39:48', 920),
('0003', '1114', '3', '2024-10-21 21:39:48', 4000),
('0004', '1404', '3', '2024-10-21 21:41:00', 3020),
('0005', '1405', '1', '2024-10-21 21:41:36', 390);

ALTER TABLE `t_ninjinhis`
  ADD PRIMARY KEY (`F_NinjinHisID`);
COMMIT;

ALTER TABLE `t_ninjinhis`
  ADD CONSTRAINT `FK_t_ninjinhis_m_member` FOREIGN KEY (`F_MemberID`) REFERENCES `m_member` (`F_MemberID`);
COMMIT;

--
-- テーブルの構造 `t_photostorage`
--
CREATE TABLE `t_photostorage` (
  `F_GoodsPhotoID` char(4) NOT NULL,
  `F_GoodsID` char(4) NOT NULL,
  `F_GoPhotoStorage` varchar(100) NOT NULL,
  `F_PictureALT` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `t_photostorage`
  ADD PRIMARY KEY (`F_GoodsPhotoID`),
  ADD KEY `FK_T_photoStorage_M_goods` (`F_GoodsID`);

ALTER TABLE `t_photostorage`
  ADD CONSTRAINT `FK_T_photoStorage_M_goods` FOREIGN KEY (`F_GoodsID`) REFERENCES `m_goods` (`F_GoodsID`);
COMMIT;




CREATE TABLE `t_purchasehis` (
  `F_PurchaseHis` char(16) NOT NULL,
  `F_MemberID` char(4) NOT NULL,
  `F_GoodsID` char(4) NOT NULL,
  `F_PurchaseNum` int(11) DEFAULT NULL,
  `F_PurchaseTime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `t_purchasehis` (`F_PurchaseHis`, `F_MemberID`, `F_GoodsID`, `F_PurchaseNum`, `F_PurchaseTime`) VALUES
('0023241021214517', '0023', '0001', 2, '2024-10-21 21:45:17'),
('1010241021214804', '1010', '0009', 10, '2024-10-21 21:48:04'),
('1114241021214857', '1114', '0010', 4, '2024-10-21 21:48:57'),
('1404241021214930', '1404', '0005', 3, '2024-10-21 21:49:30'),
('1405241021214930', '1405', '0003', 4, '2024-10-21 21:49:30');

ALTER TABLE `t_purchasehis`
  ADD PRIMARY KEY (`F_PurchaseHis`),
  ADD KEY `FK_t_purchasehis_m_member` (`F_MemberID`),
  ADD KEY `FK_t_purchasehis_m_Goods` (`F_GoodsID`);

ALTER TABLE `t_purchasehis`
  ADD CONSTRAINT `FK_t_purchasehis_m_Goods` FOREIGN KEY (`F_GoodsID`) REFERENCES `m_goods` (`F_GoodsID`),
  ADD CONSTRAINT `FK_t_purchasehis_m_member` FOREIGN KEY (`F_MemberID`) REFERENCES `m_member` (`F_MemberID`);
COMMIT;




/* ALTER TABLEのSQL文で何個かカラム名が変わっているので必ず反映させる事 */