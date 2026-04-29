CREATE DATABASE  IF NOT EXISTS `atividade_pratica_gabrielferreira` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `atividade_pratica_gabrielferreira`;
-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: atividade_pratica_gabrielferreira
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `aluno`
--

DROP TABLE IF EXISTS `aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefone` varchar(20) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aluno`
--

LOCK TABLES `aluno` WRITE;
/*!40000 ALTER TABLE `aluno` DISABLE KEYS */;
INSERT INTO `aluno` VALUES (1,'Joao Silva','joao@email.com','(83) 91234-5678',NULL),(2,'','maria@email.com','(83) 98888-2222',NULL),(3,'Carlos Souza','carlos@email.com','(83) 97777-3333',NULL),(4,'Gabriel Americo','gabriel@email.com','(83) 96666-4444',NULL),(5,'Julio Américo','julio@email.com','83 9999-2221','2007-05-13'),(6,'Vitoria Ferreira meu AMOR','Vitoria@email.com','83 98654-8711','2008-01-01'),(7,'Caio Lucas','Caio@email.com','83 82312-1232','2004-10-10'),(8,'Adrian Artur','Adrian@email.com','83 9677-0987','2004-02-10'),(9,'Gabriel Cunha','gabrielcunha@email.com','83 98752-0945','2006-07-02'),(10,'Iago Veras','Iago@email.com','83 96555-5423','2006-12-02'),(11,'Rafael Santos','Rafael@email.com','83 88888-0254','2002-05-15'),(12,'Doricleide Lima','Doris@email.com','83 55553-7654','1980-12-10'),(14,'Adrian José','Adrianj@email','83 88574-2832','2005-08-17'),(15,'Maria Cunha','mariac@email.com','83 99992-0986','2008-03-22'),(16,'Emanuel','EmanuelA@email.com','83 9929-0264','1969-12-25'),(17,'Jose Paulo','josepaulo@email.com','83 99893-2343','2006-10-26');
/*!40000 ALTER TABLE `aluno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-29 14:32:42
