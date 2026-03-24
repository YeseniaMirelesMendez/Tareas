-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para test
CREATE DATABASE IF NOT EXISTS `test` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `test`;

-- Volcando estructura para tabla test.tareas
CREATE TABLE IF NOT EXISTS `tareas` (
  `id_tarea` int(15) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(15) NOT NULL DEFAULT 0,
  `Titulo` varchar(200) NOT NULL DEFAULT '0',
  `Descripcion` text NOT NULL,
  `Fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Fecha_limite` date NOT NULL,
  `Hora_limite` time NOT NULL,
  `Columna 4` int(15) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_tarea`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla test.tareas: ~0 rows (aproximadamente)
DELETE FROM `tareas`;

-- Volcando estructura para tabla test.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(15) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `Apellido` varchar(100) NOT NULL,
  `Email` varchar(150) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `FechaRegistro` timestamp NULL DEFAULT NULL,
  `UltimoAcceso` timestamp NULL DEFAULT NULL,
  `Activo` timestamp NULL DEFAULT NULL,
  `FotoPerfil` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Volcando datos para la tabla test.usuario: ~0 rows (aproximadamente)
DELETE FROM `usuario`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
