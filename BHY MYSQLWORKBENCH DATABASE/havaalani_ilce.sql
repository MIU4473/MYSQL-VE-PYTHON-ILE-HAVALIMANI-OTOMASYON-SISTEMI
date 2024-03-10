-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: havaalani
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ilce`
--

DROP TABLE IF EXISTS `ilce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ilce` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SEHIR_ID` int DEFAULT NULL,
  `ILCE_ISMI` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `SEHIR_ID` (`SEHIR_ID`),
  CONSTRAINT `ilce_ibfk_1` FOREIGN KEY (`SEHIR_ID`) REFERENCES `sehir` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=912 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ilce`
--

LOCK TABLES `ilce` WRITE;
/*!40000 ALTER TABLE `ilce` DISABLE KEYS */;
INSERT INTO `ilce` VALUES (1,1,'SEYHAN'),(2,1,'CEYHAN'),(3,1,'FEKE'),(4,1,'KARAİSALI'),(5,1,'KARATAŞ'),(6,1,'KOZAN'),(7,1,'POZANTI'),(8,1,'SAİMBEYLİ'),(9,1,'TUFANBEYLİ'),(10,1,'YUMURTALIK'),(11,1,'YÜREĞİR'),(12,1,'ALADAĞ'),(13,1,'İMAMOĞLU'),(14,2,'ADIYAMAN MERKEZ'),(15,2,'BESNİ'),(16,2,'ÇELİKHAN'),(17,2,'GERGER'),(18,2,'GÖLBAŞI'),(19,2,'KAHTA'),(20,2,'SAMSAT'),(21,2,'SİNCİK'),(22,2,'TUT'),(23,3,'AFYONMERKEZ'),(24,3,'BOLVADİN'),(25,3,'ÇAY'),(26,3,'DAZKIRI'),(27,3,'DİNAR'),(28,3,'EMİRDAĞ'),(29,3,'İHSANİYE'),(30,3,'SANDIKLI'),(31,3,'SİNANPAŞA'),(32,3,'SULDANDAĞI'),(33,3,'ŞUHUT'),(34,3,'BAŞMAKÇI'),(35,3,'BAYAT'),(36,3,'İŞCEHİSAR'),(37,3,'ÇOBANLAR'),(38,3,'EVCİLER'),(39,3,'HOCALAR'),(40,3,'KIZILÖREN'),(41,68,'AKSARAY MERKEZ'),(42,68,'ORTAKÖY'),(43,68,'AĞAÇÖREN'),(44,68,'GÜZELYURT'),(45,68,'SARIYAHŞİ'),(46,68,'ESKİL'),(47,68,'GÜLAĞAÇ'),(48,5,'AMASYA MERKEZ'),(49,5,'GÖYNÜÇEK'),(50,5,'GÜMÜŞHACIKÖYÜ'),(51,5,'MERZİFON'),(52,5,'SULUOVA'),(53,5,'TAŞOVA'),(54,5,'HAMAMÖZÜ'),(55,6,'ALTINDAĞ'),(56,6,'AYAS'),(57,6,'BALA'),(58,6,'BEYPAZARI'),(59,6,'ÇAMLIDERE'),(60,6,'ÇANKAYA'),(61,6,'ÇUBUK'),(62,6,'ELMADAĞ'),(63,6,'GÜDÜL'),(64,6,'HAYMANA'),(65,6,'KALECİK'),(66,6,'KIZILCAHAMAM'),(67,6,'NALLIHAN'),(68,6,'POLATLI'),(69,6,'ŞEREFLİKOÇHİSAR'),(70,6,'YENİMAHALLE'),(71,6,'GÖLBAŞI'),(72,6,'KEÇİÖREN'),(73,6,'MAMAK'),(74,6,'SİNCAN'),(75,6,'KAZAN'),(76,6,'AKYURT'),(77,6,'ETİMESGUT'),(78,6,'EVREN'),(79,7,'ANSEKİ'),(80,7,'ALANYA'),(81,7,'ANTALYA MERKEZİ'),(82,7,'ELMALI'),(83,7,'FİNİKE'),(84,7,'GAZİPAŞA'),(85,7,'GÜNDOĞMUŞ'),(86,7,'KAŞ'),(87,7,'KORKUTELİ'),(88,7,'KUMLUCA'),(89,7,'MANAVGAT'),(90,7,'SERİK'),(91,7,'DEMRE'),(92,7,'İBRADI'),(93,7,'KEMER'),(94,75,'ARDAHAN MERKEZ'),(95,75,'GÖLE'),(96,75,'ÇILDIR'),(97,75,'HANAK'),(98,75,'POSOF'),(99,75,'DAMAL'),(100,8,'ARDANUÇ'),(101,8,'ARHAVİ'),(102,8,'ARTVİN MERKEZ'),(103,8,'BORÇKA'),(104,8,'HOPA'),(105,8,'ŞAVŞAT'),(106,8,'YUSUFELİ'),(107,8,'MURGUL'),(108,9,'AYDIN MERKEZ'),(109,9,'BOZDOĞAN'),(110,9,'ÇİNE'),(111,9,'GERMENCİK'),(112,9,'KARACASU'),(113,9,'KOÇARLI'),(114,9,'KUŞADASI'),(115,9,'KUYUCAK'),(116,9,'NAZİLLİ'),(117,9,'SÖKE'),(118,9,'SULTANHİSAR'),(119,9,'YENİPAZAR'),(120,9,'BUHARKENT'),(121,9,'İNCİRLİOVA'),(122,9,'KARPUZLU'),(123,9,'KÖŞK'),(124,9,'DİDİM'),(125,4,'AĞRI MERKEZ'),(126,4,'DİYADİN'),(127,4,'DOĞUBEYAZIT'),(128,4,'ELEŞKİRT'),(129,4,'HAMUR'),(130,4,'PATNOS'),(131,4,'TAŞLIÇAY'),(132,4,'TUTAK'),(133,10,'AYVALIK'),(134,10,'BALIKESİR MERKEZ'),(135,10,'BALYA'),(136,10,'BANDIRMA'),(137,10,'BİGADİÇ'),(138,10,'BURHANİYE'),(139,10,'DURSUNBEY'),(140,10,'EDREMİT'),(141,10,'ERDEK'),(142,10,'GÖNEN'),(143,10,'HAVRAN'),(144,10,'İVRİNDİ'),(145,10,'KEPSUT'),(146,10,'MANYAS'),(147,10,'SAVAŞTEPE'),(148,10,'SINDIRGI'),(149,10,'SUSURLUK'),(150,10,'MARMARA'),(151,10,'GÖMEÇ'),(152,74,'BARTIN MERKEZ'),(153,74,'KURUCAŞİLE'),(154,74,'ULUS'),(155,74,'AMASRA'),(156,72,'BATMAN MERKEZ'),(157,72,'BEŞİRİ'),(158,72,'GERCÜŞ'),(159,72,'KOZLUK'),(160,72,'SASON'),(161,72,'HASANKEYF'),(162,69,'BAYBURT MERKEZ'),(163,69,'AYDINTEPE'),(164,69,'DEMİRÖZÜ'),(165,14,'BOLU MERKEZ'),(166,14,'GEREDE'),(167,14,'GÖYNÜK'),(168,14,'KIBRISCIK'),(169,14,'MENGEN'),(170,14,'MUDURNU'),(171,14,'SEBEN'),(172,14,'DÖRTDİVAN'),(173,14,'YENİÇAĞA'),(174,15,'AĞLASUN'),(175,15,'BUCAK'),(176,15,'BURDUR MERKEZ'),(177,15,'GÖLHİSAR'),(178,15,'TEFENNİ'),(179,15,'YEŞİLOVA'),(180,15,'KARAMANLI'),(181,15,'KEMER'),(182,15,'ALTINYAYLA'),(183,15,'ÇAVDIR'),(184,15,'ÇELTİKÇİ'),(185,16,'GEMLİK'),(186,16,'İNEGÖL'),(187,16,'İZNİK'),(188,16,'KARACABEY'),(189,16,'KELES'),(190,16,'MUDANYA'),(191,16,'MUSTAFA K. PAŞA'),(192,16,'ORHANELİ'),(193,16,'ORHANGAZİ'),(194,16,'YENİŞEHİR'),(195,16,'BÜYÜK ORHAN'),(196,16,'HARMANCIK'),(197,16,'NÜLİFER'),(198,16,'OSMAN GAZİ'),(199,16,'YILDIRIM'),(200,16,'GÜRSU'),(201,16,'KESTEL'),(202,11,'BİLECİK MERKEZ'),(203,11,'BOZÜYÜK'),(204,11,'GÖLPAZARI'),(205,11,'OSMANELİ'),(206,11,'PAZARYERİ'),(207,11,'SÖĞÜT'),(208,11,'YENİPAZAR'),(209,11,'İNHİSAR'),(210,12,'BİNGÖL MERKEZ'),(211,12,'GENÇ'),(212,12,'KARLIOVA'),(213,12,'KİGI'),(214,12,'SOLHAN'),(215,12,'ADAKLI'),(216,12,'YAYLADERE'),(217,12,'YEDİSU'),(218,13,'ADİLCEVAZ'),(219,13,'AHLAT'),(220,13,'BİTLİS MERKEZ'),(221,13,'HİZAN'),(222,13,'MUTKİ'),(223,13,'TATVAN'),(224,13,'GÜROYMAK'),(225,20,'DENİZLİ MERKEZ'),(226,20,'ACIPAYAM'),(227,20,'BULDAN'),(228,20,'ÇAL'),(229,20,'ÇAMELİ'),(230,20,'ÇARDAK'),(231,20,'ÇİVRİL'),(232,20,'GÜNEY'),(233,20,'KALE'),(234,20,'SARAYKÖY'),(235,20,'TAVAS'),(236,20,'BABADAĞ'),(237,20,'BEKİLLİ'),(238,20,'HONAZ'),(239,20,'SERİNHİSAR'),(240,20,'AKKÖY'),(241,20,'BAKLAN'),(242,20,'BEYAĞAÇ'),(243,20,'BOZKURT'),(244,81,'DÜZCE MERKEZ'),(245,81,'AKÇAKOCA'),(246,81,'YIĞILCA'),(247,81,'CUMAYERİ'),(248,81,'GÖLYAKA'),(249,81,'ÇİLİMLİ'),(250,81,'GÜMÜŞOVA'),(251,81,'KAYNAŞLI'),(252,21,'DİYARBAKIR MERKEZ'),(253,21,'BİSMİL'),(254,21,'ÇERMİK'),(255,21,'ÇINAR'),(256,21,'ÇÜNGÜŞ'),(257,21,'DİCLE'),(258,21,'ERGANİ'),(259,21,'HANİ'),(260,21,'HAZRO'),(261,21,'KULP'),(262,21,'LİCE'),(263,21,'SİLVAN'),(264,21,'EĞİL'),(265,21,'KOCAKÖY'),(266,22,'EDİRNE MERKEZ'),(267,22,'ENEZ'),(268,22,'HAVSA'),(269,22,'İPSALA'),(270,22,'KEŞAN'),(271,22,'LALAPAŞA'),(272,22,'MERİÇ'),(273,22,'UZUNKÖPRÜ'),(274,22,'SÜLOĞLU'),(275,23,'ELAZIĞ MERKEZ'),(276,23,'AĞIN'),(277,23,'BASKİL'),(278,23,'KARAKOÇAN'),(279,23,'KEBAN'),(280,23,'MADEN'),(281,23,'PALU'),(282,23,'SİVRİCE'),(283,23,'ARICAK'),(284,23,'KOVANCILAR'),(285,23,'ALACAKAYA'),(286,25,'ERZURUM MERKEZ'),(287,25,'PALANDÖKEN'),(288,25,'AŞKALE'),(289,25,'ÇAT'),(290,25,'HINIS'),(291,25,'HORASAN'),(292,25,'OLTU'),(293,25,'İSPİR'),(294,25,'KARAYAZI'),(295,25,'NARMAN'),(296,25,'OLUR'),(297,25,'PASİNLER'),(298,25,'ŞENKAYA'),(299,25,'TEKMAN'),(300,25,'TORTUM'),(301,25,'KARAÇOBAN'),(302,25,'UZUNDERE'),(303,25,'PAZARYOLU'),(304,25,'ILICA'),(305,25,'KÖPRÜKÖY'),(306,24,'ÇAYIRLI'),(307,24,'ERZİNCAN MERKEZ'),(308,24,'İLİÇ'),(309,24,'KEMAH'),(310,24,'KEMALİYE'),(311,24,'REFAHİYE'),(312,24,'TERCAN'),(313,24,'OTLUKBELİ'),(314,26,'ESKİŞEHİR MERKEZ'),(315,26,'ÇİFTELER'),(316,26,'MAHMUDİYE'),(317,26,'MİHALIÇLIK'),(318,26,'SARICAKAYA'),(319,26,'SEYİTGAZİ'),(320,26,'SİVRİHİSAR'),(321,26,'ALPU'),(322,26,'BEYLİKOVA'),(323,26,'İNÖNÜ'),(324,26,'GÜNYÜZÜ'),(325,26,'HAN'),(326,26,'MİHALGAZİ'),(327,27,'ARABAN'),(328,27,'İSLAHİYE'),(329,27,'NİZİP'),(330,27,'OĞUZELİ'),(331,27,'YAVUZELİ'),(332,27,'ŞAHİNBEY'),(333,27,'ŞEHİT KAMİL'),(334,27,'KARKAMIŞ'),(335,27,'NURDAĞI'),(336,29,'GÜMÜŞHANE MERKEZ'),(337,29,'KELKİT'),(338,29,'ŞİRAN'),(339,29,'TORUL'),(340,29,'KÖSE'),(341,29,'KÜRTÜN'),(342,28,'ALUCRA'),(343,28,'BULANCAK'),(344,28,'DERELİ'),(345,28,'ESPİYE'),(346,28,'EYNESİL'),(347,28,'GİRESUN MERKEZ'),(348,28,'GÖRELE'),(349,28,'KEŞAP'),(350,28,'ŞEBİNKARAHİSAR'),(351,28,'TİREBOLU'),(352,28,'PİPAZİZ'),(353,28,'YAĞLIDERE'),(354,28,'ÇAMOLUK'),(355,28,'ÇANAKÇI'),(356,28,'DOĞANKENT'),(357,28,'GÜCE'),(358,30,'HAKKARİ MERKEZ'),(359,30,'ÇUKURCA'),(360,30,'ŞEMDİNLİ'),(361,30,'YÜKSEKOVA'),(362,31,'ALTINÖZÜ'),(363,31,'DÖRTYOL'),(364,31,'HATAY MERKEZ'),(365,31,'HASSA'),(366,31,'İSKENDERUN'),(367,31,'KIRIKHAN'),(368,31,'REYHANLI'),(369,31,'SAMANDAĞ'),(370,31,'YAYLADAĞ'),(371,31,'ERZİN'),(372,31,'BELEN'),(373,31,'KUMLU'),(374,32,'ISPARTA MERKEZ'),(375,32,'ATABEY'),(376,32,'KEÇİBORLU'),(377,32,'EĞİRDİR'),(378,32,'GELENDOST'),(379,32,'SİNİRKENT'),(380,32,'ULUBORLU'),(381,32,'YALVAÇ'),(382,32,'AKSU'),(383,32,'GÖNEN'),(384,32,'YENİŞAR BADEMLİ'),(385,76,'IĞDIR MERKEZ'),(386,76,'ARALIK'),(387,76,'TUZLUCA'),(388,76,'KARAKOYUNLU'),(389,46,'AFŞİN'),(390,46,'ANDIRIN'),(391,46,'ELBİSTAN'),(392,46,'GÖKSUN'),(393,46,'KAHRAMANMARAŞ MERKEZ'),(394,46,'PAZARCIK'),(395,46,'TÜRKOĞLU'),(396,46,'ÇAĞLAYANCERİT'),(397,46,'EKİNÖZÜ'),(398,46,'NURHAK'),(399,78,'EFLANİ'),(400,78,'ESKİPAZAR'),(401,78,'KARABÜK MERKEZ'),(402,78,'OVACIK'),(403,78,'SAFRANBOLU'),(404,78,'YENİCE'),(405,70,'ERMENEK'),(406,70,'KARAMAN MERKEZ'),(407,70,'AYRANCI'),(408,70,'KAZIMKARABEKİR'),(409,70,'BAŞYAYLA'),(410,70,'SARIVELİLER'),(411,36,'KARS MERKEZ'),(412,36,'ARPAÇAY'),(413,36,'DİGOR'),(414,36,'KAĞIZMAN'),(415,36,'SARIKAMIŞ'),(416,36,'SELİM'),(417,36,'SUSUZ'),(418,36,'AKYAKA'),(419,37,'ABANA'),(420,37,'KASTAMONU MERKEZ'),(421,37,'ARAÇ'),(422,37,'AZDAVAY'),(423,37,'BOZKURT'),(424,37,'CİDE'),(425,37,'ÇATALZEYTİN'),(426,37,'DADAY'),(427,37,'DEVREKANİ'),(428,37,'İNEBOLU'),(429,37,'KÜRE'),(430,37,'TAŞKÖPRÜ'),(431,37,'TOSYA'),(432,37,'İHSANGAZİ'),(433,37,'PINARBAŞI'),(434,37,'ŞENPAZAR'),(435,37,'AĞLI'),(436,37,'DOĞANYURT'),(437,37,'HANÖNÜ'),(438,37,'SEYDİLER'),(439,38,'BÜNYAN'),(440,38,'DEVELİ'),(441,38,'FELAHİYE'),(442,38,'İNCESU'),(443,38,'PINARBAŞI'),(444,38,'SARIOĞLAN'),(445,38,'SARIZ'),(446,38,'TOMARZA'),(447,38,'YAHYALI'),(448,38,'YEŞİLHİSAR'),(449,38,'AKKIŞLA'),(450,38,'TALAS'),(451,38,'KOCASİNAN'),(452,38,'MELİKGAZİ'),(453,38,'HACILAR'),(454,38,'ÖZVATAN'),(455,71,'DERİCE'),(456,71,'KESKİN'),(457,71,'KIRIKKALE MERKEZ'),(458,71,'SALAK YURT'),(459,71,'BAHŞİLİ'),(460,71,'BALIŞEYH'),(461,71,'ÇELEBİ'),(462,71,'KARAKEÇİLİ'),(463,71,'YAHŞİHAN'),(464,39,'KIRKKLARELİ MERKEZ'),(465,39,'BABAESKİ'),(466,39,'DEMİRKÖY'),(467,39,'KOFÇAY'),(468,39,'LÜLEBURGAZ'),(469,39,'VİZE'),(470,40,'KIRŞEHİR MERKEZ'),(471,40,'ÇİÇEKDAĞI'),(472,40,'KAMAN'),(473,40,'MUCUR'),(474,40,'AKPINAR'),(475,40,'AKÇAKENT'),(476,40,'BOZTEPE'),(477,41,'KOCAELİ MERKEZ'),(478,41,'GEBZE'),(479,41,'GÖLCÜK'),(480,41,'KANDIRA'),(481,41,'KARAMÜRSEL'),(482,41,'KÖRFEZ'),(483,41,'DERİNCE'),(484,42,'KONYA MERKEZ'),(485,42,'AKŞEHİR'),(486,42,'BEYŞEHİR'),(487,42,'BOZKIR'),(488,42,'CİHANBEYLİ'),(489,42,'ÇUMRA'),(490,42,'DOĞANHİSAR'),(491,42,'EREĞLİ'),(492,42,'HADİM'),(493,42,'ILGIN'),(494,42,'KADINHANI'),(495,42,'KARAPINAR'),(496,42,'KULU'),(497,42,'SARAYÖNÜ'),(498,42,'SEYDİŞEHİR'),(499,42,'YUNAK'),(500,42,'AKÖREN'),(501,42,'ALTINEKİN'),(502,42,'DEREBUCAK'),(503,42,'HÜYÜK'),(504,42,'KARATAY'),(505,42,'MERAM'),(506,42,'SELÇUKLU'),(507,42,'TAŞKENT'),(508,42,'AHIRLI'),(509,42,'ÇELTİK'),(510,42,'DERBENT'),(511,42,'EMİRGAZİ'),(512,42,'GÜNEYSINIR'),(513,42,'HALKAPINAR'),(514,42,'TUZLUKÇU'),(515,42,'YALIHÜYÜK'),(516,43,'KÜTAHYA MERKEZ'),(517,43,'ALTINTAŞ'),(518,43,'DOMANİÇ'),(519,43,'EMET'),(520,43,'GEDİZ'),(521,43,'SİMAV'),(522,43,'TAVŞANLI'),(523,43,'ASLANAPA'),(524,43,'DUMLUPINAR'),(525,43,'HİSARCIK'),(526,43,'ŞAPHANE'),(527,43,'ÇAVDARHİSAR'),(528,43,'PAZARLAR'),(529,79,'KİLİS MERKEZ'),(530,79,'ELBEYLİ'),(531,79,'MUSABEYLİ'),(532,79,'POLATELİ'),(533,44,'MALATYA MERKEZ'),(534,44,'AKÇADAĞ'),(535,44,'ARAPGİR'),(536,44,'ARGUVAN'),(537,44,'DARENDE'),(538,44,'DOĞANŞEHİR'),(539,44,'HEKİMHAN'),(540,44,'PÜTÜRGE'),(541,44,'YEŞİLYURT'),(542,44,'BATTALGAZİ'),(543,44,'DOĞANYOL'),(544,44,'KALE'),(545,44,'KULUNCAK'),(546,44,'YAZIHAN'),(547,45,'AKHİSAR'),(548,45,'ALAŞEHİR'),(549,45,'DEMİRCİ'),(550,45,'GÖRDES'),(551,45,'KIRKAĞAÇ'),(552,45,'KULA'),(553,45,'MANİSA MERKEZ'),(554,45,'SALİHLİ'),(555,45,'SARIGÖL'),(556,45,'SARUHANLI'),(557,45,'SELENDİ'),(558,45,'SOMA'),(559,45,'TURGUTLU'),(560,45,'AHMETLİ'),(561,45,'GÖLMARMARA'),(562,45,'KÖPRÜBAŞI'),(563,47,'DERİK'),(564,47,'KIZILTEPE'),(565,47,'MARDİN MERKEZ'),(566,47,'MAZIDAĞI'),(567,47,'MİDYAT'),(568,47,'NUSAYBİN'),(569,47,'ÖMERLİ'),(570,47,'SAVUR'),(571,47,'YEŞİLLİ'),(572,33,'MERSİN MERKEZ'),(573,33,'ANAMUR'),(574,33,'ERDEMLİ'),(575,33,'GÜLNAR'),(576,33,'MUT'),(577,33,'SİLİFKE'),(578,33,'TARSUS'),(579,33,'AYDINCIK'),(580,33,'BOZYAZI'),(581,33,'ÇAMLIYAYLA'),(582,48,'BODRUM'),(583,48,'DATÇA'),(584,48,'FETHİYE'),(585,48,'KÖYCEĞİZ'),(586,48,'MARMARİS'),(587,48,'MİLAS'),(588,48,'MUĞLA MERKEZ'),(589,48,'ULA'),(590,48,'YATAĞAN'),(591,48,'DALAMAN'),(592,48,'KAVAKLI DERE'),(593,48,'ORTACA'),(594,49,'BULANIK'),(595,49,'MALAZGİRT'),(596,49,'MUŞ MERKEZ'),(597,49,'VARTO'),(598,49,'HASKÖY'),(599,49,'KORKUT'),(600,50,'NEVŞEHİR MERKEZ'),(601,50,'AVANOS'),(602,50,'DERİNKUYU'),(603,50,'GÜLŞEHİR'),(604,50,'HACIBEKTAŞ'),(605,50,'KOZAKLI'),(606,50,'ÜRGÜP'),(607,50,'ACIGÖL'),(608,51,'NİĞDE MERKEZ'),(609,51,'BOR'),(610,51,'ÇAMARDI'),(611,51,'ULUKIŞLA'),(612,51,'ALTUNHİSAR'),(613,51,'ÇİFTLİK'),(614,52,'AKKUŞ'),(615,52,'AYBASTI'),(616,52,'FATSA'),(617,52,'GÖLKÖY'),(618,52,'KORGAN'),(619,52,'KUMRU'),(620,52,'MESUDİYE'),(621,52,'ORDU MERKEZ'),(622,52,'PERŞEMBE'),(623,52,'ULUBEY'),(624,52,'ÜNYE'),(625,52,'GÜLYALI'),(626,52,'GÜRGENTEPE'),(627,52,'ÇAMAŞ'),(628,52,'ÇATALPINAR'),(629,52,'ÇAYBAŞI'),(630,52,'İKİZCE'),(631,52,'KABADÜZ'),(632,52,'KABATAŞ'),(633,80,'BAHÇE'),(634,80,'KADİRLİ'),(635,80,'OSMANİYE MERKEZ'),(636,80,'DÜZİÇİ'),(637,80,'HASANBEYLİ'),(638,80,'SUMBAŞ'),(639,80,'TOPRAKKALE'),(640,53,'RİZE MERKEZ'),(641,53,'ARDEŞEN'),(642,53,'ÇAMLIHEMŞİN'),(643,53,'ÇAYELİ'),(644,53,'FINDIKLI'),(645,53,'İKİZDERE'),(646,53,'KALKANDERE'),(647,53,'PAZAR'),(648,53,'GÜNEYSU'),(649,53,'DEREPAZARI'),(650,53,'HEMŞİN'),(651,53,'İYİDERE'),(652,54,'AKYAZI'),(653,54,'GEYVE'),(654,54,'HENDEK'),(655,54,'KARASU'),(656,54,'KAYNARCA'),(657,54,'SAKARYA MERKEZ'),(658,54,'PAMUKOVA'),(659,54,'TARAKLI'),(660,54,'FERİZLİ'),(661,54,'KARAPÜRÇEK'),(662,54,'SÖĞÜTLÜ'),(663,55,'ALAÇAM'),(664,55,'BAFRA'),(665,55,'ÇARŞAMBA'),(666,55,'HAVZA'),(667,55,'KAVAK'),(668,55,'LADİK'),(669,55,'SAMSUN MERKEZ'),(670,55,'TERME'),(671,55,'VEZİRKÖPRÜ'),(672,55,'ASARCIK'),(673,55,'ONDOKUZMAYIS'),(674,55,'SALIPAZARI'),(675,55,'TEKKEKÖY'),(676,55,'AYVACIK'),(677,55,'YAKAKENT'),(678,57,'AYANCIK'),(679,57,'BOYABAT'),(680,57,'SİNOP MERKEZ'),(681,57,'DURAĞAN'),(682,57,'ERGELEK'),(683,57,'GERZE'),(684,57,'TÜRKELİ'),(685,57,'DİKMEN'),(686,57,'SARAYDÜZÜ'),(687,58,'DİVRİĞİ'),(688,58,'GEMEREK'),(689,58,'GÜRÜN'),(690,58,'HAFİK'),(691,58,'İMRANLI'),(692,58,'KANGAL'),(693,58,'KOYUL HİSAR'),(694,58,'SİVAS MERKEZ'),(695,58,'SU ŞEHRİ'),(696,58,'ŞARKIŞLA'),(697,58,'YILDIZELİ'),(698,58,'ZARA'),(699,58,'AKINCILAR'),(700,58,'ALTINYAYLA'),(701,58,'DOĞANŞAR'),(702,58,'GÜLOVA'),(703,58,'ULAŞ'),(704,56,'BAYKAN'),(705,56,'ERUH'),(706,56,'KURTALAN'),(707,56,'PERVARİ'),(708,56,'SİİRT MERKEZ'),(709,56,'ŞİRVARİ'),(710,56,'AYDINLAR'),(711,59,'TEKİRDAĞ MERKEZ'),(712,59,'ÇERKEZKÖY'),(713,59,'ÇORLU'),(714,59,'HAYRABOLU'),(715,59,'MALKARA'),(716,59,'MURATLI'),(717,59,'SARAY'),(718,59,'ŞARKÖY'),(719,59,'MARAMARAEREĞLİSİ'),(720,60,'ALMUS'),(721,60,'ARTOVA'),(722,60,'TOKAT MERKEZ'),(723,60,'ERBAA'),(724,60,'NİKSAR'),(725,60,'REŞADİYE'),(726,60,'TURHAL'),(727,60,'ZİLE'),(728,60,'PAZAR'),(729,60,'YEŞİLYURT'),(730,60,'BAŞÇİFTLİK'),(731,60,'SULUSARAY'),(732,61,'TRABZON MERKEZ'),(733,61,'AKÇAABAT'),(734,61,'ARAKLI'),(735,61,'ARŞİN'),(736,61,'ÇAYKARA'),(737,61,'MAÇKA'),(738,61,'OF'),(739,61,'SÜRMENE'),(740,61,'TONYA'),(741,61,'VAKFIKEBİR'),(742,61,'YOMRA'),(743,61,'BEŞİKDÜZÜ'),(744,61,'ŞALPAZARI'),(745,61,'ÇARŞIBAŞI'),(746,61,'DERNEKPAZARI'),(747,61,'DÜZKÖY'),(748,61,'HAYRAT'),(749,61,'KÖPRÜBAŞI'),(750,62,'TUNCELİ MERKEZ'),(751,62,'ÇEMİŞGEZEK'),(752,62,'HOZAT'),(753,62,'MAZGİRT'),(754,62,'NAZİMİYE'),(755,62,'OVACIK'),(756,62,'PERTEK'),(757,62,'PÜLÜMÜR'),(758,64,'BANAZ'),(759,64,'EŞME'),(760,64,'KARAHALLI'),(761,64,'SİVASLI'),(762,64,'ULUBEY'),(763,64,'UŞAK MERKEZ'),(764,65,'BAŞKALE'),(765,65,'VAN MERKEZ'),(766,65,'EDREMİT'),(767,65,'ÇATAK'),(768,65,'ERCİŞ'),(769,65,'GEVAŞ'),(770,65,'GÜRPINAR'),(771,65,'MURADİYE'),(772,65,'ÖZALP'),(773,65,'BAHÇESARAY'),(774,65,'ÇALDIRAN'),(775,65,'SARAY'),(776,77,'YALOVA MERKEZ'),(777,77,'ALTINOVA'),(778,77,'ARMUTLU'),(779,77,'ÇINARCIK'),(780,77,'ÇİFTLİKKÖY'),(781,77,'TERMAL'),(782,66,'AKDAĞMADENİ'),(783,66,'BOĞAZLIYAN'),(784,66,'YOZGAT MERKEZ'),(785,66,'ÇAYIRALAN'),(786,66,'ÇEKEREK'),(787,66,'SARIKAYA'),(788,66,'SORGUN'),(789,66,'ŞEFAATLI'),(790,66,'YERKÖY'),(791,66,'KADIŞEHRİ'),(792,66,'SARAYKENT'),(793,66,'YENİFAKILI'),(794,67,'ÇAYCUMA'),(795,67,'DEVREK'),(796,67,'ZONGULDAK MERKEZ'),(797,67,'EREĞLİ'),(798,67,'ALAPLI'),(799,67,'GÖKÇEBEY'),(800,17,'ÇANAKKALE MERKEZ'),(801,17,'AYVACIK'),(802,17,'BAYRAMİÇ'),(803,17,'BİGA'),(804,17,'BOZCAADA'),(805,17,'ÇAN'),(806,17,'ECEABAT'),(807,17,'EZİNE'),(808,17,'LAPSEKİ'),(809,17,'YENİCE'),(810,18,'ÇANKIRI MERKEZ'),(811,18,'ÇERKEŞ'),(812,18,'ELDİVAN'),(813,18,'ILGAZ'),(814,18,'KURŞUNLU'),(815,18,'ORTA'),(816,18,'ŞABANÖZÜ'),(817,18,'YAPRAKLI'),(818,18,'ATKARACALAR'),(819,18,'KIZILIRMAK'),(820,18,'BAYRAMÖREN'),(821,18,'KORGUN'),(822,19,'ALACA'),(823,19,'BAYAT'),(824,19,'ÇORUM MERKEZ'),(825,19,'İKSİPLİ'),(826,19,'KARGI'),(827,19,'MECİTÖZÜ'),(828,19,'ORTAKÖY'),(829,19,'OSMANCIK'),(830,19,'SUNGURLU'),(831,19,'DODURGA'),(832,19,'LAÇİN'),(833,19,'OĞUZLAR'),(834,34,'ADALAR'),(835,34,'BAKIRKÖY'),(836,34,'BEŞİKTAŞ'),(837,34,'BEYKOZ'),(838,34,'BEYOĞLU'),(839,34,'ÇATALCA'),(840,34,'EMİNÖNÜ'),(841,34,'EYÜP'),(842,34,'FATİH'),(843,34,'GAZİOSMANPAŞA'),(844,34,'KADIKÖY'),(845,34,'KARTAL'),(846,34,'SARIYER'),(847,34,'SİLİVRİ'),(848,34,'ŞİLE'),(849,34,'ŞİŞLİ'),(850,34,'ÜSKÜDAR'),(851,34,'ZEYTİNBURNU'),(852,34,'BÜYÜKÇEKMECE'),(853,34,'KAĞITHANE'),(854,34,'KÜÇÜKÇEKMECE'),(855,34,'PENDİK'),(856,34,'ÜMRANİYE'),(857,34,'BAYRAMPAŞA'),(858,34,'AVCILAR'),(859,34,'BAĞCILAR'),(860,34,'BAHÇELİEVLER'),(861,34,'GÜNGÖREN'),(862,34,'MALTEPE'),(863,34,'SULTANBEYLİ'),(864,34,'TUZLA'),(865,34,'ESENLER'),(866,35,'ALİAĞA'),(867,35,'BAYINDIR'),(868,35,'BERGAMA'),(869,35,'BORNOVA'),(870,35,'ÇEŞME'),(871,35,'DİKİLİ'),(872,35,'FOÇA'),(873,35,'KARABURUN'),(874,35,'KARŞIYAKA'),(875,35,'KEMALPAŞA'),(876,35,'KINIK'),(877,35,'KİRAZ'),(878,35,'MENEMEN'),(879,35,'ÖDEMİŞ'),(880,35,'SEFERİHİSAR'),(881,35,'SELÇUK'),(882,35,'TİRE'),(883,35,'TORBALI'),(884,35,'URLA'),(885,35,'BEYDAĞ'),(886,35,'BUCA'),(887,35,'KONAK'),(888,35,'MENDERES'),(889,35,'BALÇOVA'),(890,35,'ÇİGLİ'),(891,35,'GAZİEMİR'),(892,35,'NARLIDERE'),(893,35,'GÜZELBAHÇE'),(894,63,'ŞANLIURFA MERKEZ'),(895,63,'AKÇAKALE'),(896,63,'BİRECİK'),(897,63,'BOZOVA'),(898,63,'CEYLANPINAR'),(899,63,'HALFETİ'),(900,63,'HİLVAN'),(901,63,'SİVEREK'),(902,63,'SURUÇ'),(903,63,'VİRANŞEHİR'),(904,63,'HARRAN'),(905,73,'BEYTÜŞŞEBAP'),(906,73,'ŞIRNAK MERKEZ'),(907,73,'CİZRE'),(908,73,'İDİL'),(909,73,'SİLOPİ'),(910,73,'ULUDERE'),(911,73,'GÜÇLÜKONAK');
/*!40000 ALTER TABLE `ilce` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-10 17:40:31
