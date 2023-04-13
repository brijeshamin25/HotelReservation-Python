-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: hotelsign
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `customerinfo`
--

DROP TABLE IF EXISTS `customerinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customerinfo` (
  `custid` int NOT NULL,
  `custfirst` varchar(45) NOT NULL,
  `custlast` varchar(45) NOT NULL,
  `custgen` varchar(45) NOT NULL,
  `custaddr` varchar(45) NOT NULL,
  `custemail` varchar(45) NOT NULL,
  `custphone` varchar(45) NOT NULL,
  `custproof` varchar(45) NOT NULL,
  `custproofnum` varchar(45) NOT NULL,
  `custnation` varchar(45) NOT NULL,
  PRIMARY KEY (`custid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerinfo`
--

LOCK TABLES `customerinfo` WRITE;
/*!40000 ALTER TABLE `customerinfo` DISABLE KEYS */;
INSERT INTO `customerinfo` VALUES (1530,'Dixu','Patel','Female','John F Kennedy','dix@gmail.com','4418936473','Passport','P37T8U7','UK'),(2986,'Bhargav','Sathwara','Male','181 Okha Street','bhargav@gmail.com','9271637892','Passport','P27GU82','Canada'),(3473,'Kushi ','Joshi','Female','Gotri rd.','kuchi@icloud.com','9183720474','Student ID','0284910','Canada'),(3490,'Jay','Patil','Male','267 Carnival street','jay@icloud.com','2803927389','Student ID','0237429','Mexico'),(4055,'Smit','Patel','Male','201 Octan Ave','smit@gmail.com','7718391603','State ID','33319749','India'),(8369,'Brijesh','Amin','Male','50 Barlow Dr','brijesh@icloud.com','2018384021','Driver License','22233387','USA');
/*!40000 ALTER TABLE `customerinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roombook`
--

DROP TABLE IF EXISTS `roombook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roombook` (
  `bookContact` varchar(45) NOT NULL,
  `bookRoom` varchar(45) NOT NULL,
  `bookCheckIn` varchar(45) NOT NULL,
  `bookCheckOut` varchar(45) NOT NULL,
  `bookGuest` varchar(45) NOT NULL,
  `bookMeal` varchar(45) NOT NULL,
  `bookNumDays` varchar(45) NOT NULL,
  `bookSubTT` varchar(45) NOT NULL,
  `bookTax` varchar(45) NOT NULL,
  `bookTotal` varchar(45) NOT NULL,
  PRIMARY KEY (`bookContact`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roombook`
--

LOCK TABLES `roombook` WRITE;
/*!40000 ALTER TABLE `roombook` DISABLE KEYS */;
INSERT INTO `roombook` VALUES ('2018384021','Double Bed','04/01/2023','04/05/2023','2','Lunch','4','$ 1300.00','$ 1.10','$ 1301.10'),('2803927389','King Bed','04/02/2023','04/12/2023','4','Dinner','10','$ 4900.00','$ 0.28','$ 4900.27'),('7718391603','Double Bed','04/01/2023','04/06/2023','2','Dinner','5','$ 2125.00','$ 1.38','$ 2126.38');
/*!40000 ALTER TABLE `roombook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `signup`
--

DROP TABLE IF EXISTS `signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signup` (
  `userName` varchar(45) NOT NULL,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `contact` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signup`
--

LOCK TABLES `signup` WRITE;
/*!40000 ALTER TABLE `signup` DISABLE KEYS */;
INSERT INTO `signup` VALUES ('aksh','Akshar','Patel','Male','aksh@gmail.com','9918473591','Turkey','aksh'),('bhag','Bhargav','Sathwara','Male','bharg@gmail.com','9103748394','China','bhag'),('bkamin','BJ','Amin','Male','bj@icloud.com','9103847283','UK','bjamin'),('bamin','Brijesh','Amin','Male','brijesh@gmail.com','2018374950','USA','amin'),('dix','Dixu','Patel','Female','dixu@gamil.com','4419473820','UK','dixu'),('hardi','Hardik','Patel','Male','hardik@icloud.com','9283627391','Canada','hardi'),('kuchu','Khushi','Joshi','Female','kuchi@icloud.com','8812639174','Mexico','kuchu'),('kunj','Kunj','Patel','Male','kunj@gmail.com','9287382937','Africa','kunj'),('marg','Margi','Shah','Female','margi@gmail.com','9172846374','India','marg'),('spatel','Smit','Patel','Male','smit@gmail.com','7263849274','Canada','patel'),('vraj','Vraj','Patel','Male','vraj@gmail.com','9845904576','Africa','vraj');
/*!40000 ALTER TABLE `signup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-04 20:25:32
