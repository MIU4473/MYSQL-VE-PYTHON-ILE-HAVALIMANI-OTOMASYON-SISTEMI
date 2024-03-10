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
-- Table structure for table `sehir`
--

DROP TABLE IF EXISTS `sehir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sehir` (
  `ID` int NOT NULL,
  `ULKE_ID` int DEFAULT NULL,
  `SEHIR_ISMI` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ULKE_ID` (`ULKE_ID`),
  CONSTRAINT `sehir_ibfk_1` FOREIGN KEY (`ULKE_ID`) REFERENCES `ulke` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sehir`
--

LOCK TABLES `sehir` WRITE;
/*!40000 ALTER TABLE `sehir` DISABLE KEYS */;
INSERT INTO `sehir` VALUES (1,1,'Adana'),(2,1,'Adıyaman'),(3,1,'Afyon'),(4,1,'Ağrı'),(5,1,'Amasya'),(6,1,'Ankara'),(7,1,'Antalya'),(8,1,'Artvin'),(9,1,'Aydın'),(10,1,'Balıkesir'),(11,1,'Bilecik'),(12,1,'Bingöl'),(13,1,'Bitlis'),(14,1,'Bolu'),(15,1,'Burdur'),(16,1,'Bursa'),(17,1,'Çanakkale'),(18,1,'Çankırı'),(19,1,'Çorum'),(20,1,'Denizli'),(21,1,'Diyarbakır'),(22,1,'Edirne'),(23,1,'Elazığ'),(24,1,'Erzincan'),(25,1,'Erzurum'),(26,1,'Eskişehir'),(27,1,'Gaziantep'),(28,1,'Giresun'),(29,1,'Gümüşhane'),(30,1,'Hakkari'),(31,1,'Hatay'),(32,1,'Isparta'),(33,1,'Mersin'),(34,1,'İstanbul'),(35,1,'İzmir'),(36,1,'Kars'),(37,1,'Kastamonu'),(38,1,'Kayseri'),(39,1,'Kırklareli'),(40,1,'Kırşehir'),(41,1,'Kocaeli'),(42,1,'Konya'),(43,1,'Kütahya'),(44,1,'Malatya'),(45,1,'Manisa'),(46,1,'K.Maraş'),(47,1,'Mardin'),(48,1,'Muğla'),(49,1,'Muş'),(50,1,'Nevşehir'),(51,1,'Niğde'),(52,1,'Ordu'),(53,1,'Rize'),(54,1,'Sakarya'),(55,1,'Samsun'),(56,1,'Siirt'),(57,1,'Sinop'),(58,1,'Sivas'),(59,1,'Tekirdağ'),(60,1,'Tokat'),(61,1,'Trabzon'),(62,1,'Tunceli'),(63,1,'Şanlıurfa'),(64,1,'Uşak'),(65,1,'Van'),(66,1,'Yozgat'),(67,1,'Zonguldak'),(68,1,'Aksaray'),(69,1,'Bayburt'),(70,1,'Karaman'),(71,1,'Kırıkkale'),(72,1,'Batman'),(73,1,'Şırnak'),(74,1,'Bartın'),(75,1,'Ardahan'),(76,1,'Iğdır'),(77,1,'Yalova'),(78,1,'Karabük'),(79,1,'Kilis'),(80,1,'Osmaniye'),(81,1,'Düzce');
/*!40000 ALTER TABLE `sehir` ENABLE KEYS */;
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
