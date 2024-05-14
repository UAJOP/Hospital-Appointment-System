-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 28 Ara 2023, 20:41:29
-- Sunucu sürümü: 8.0.31
-- PHP Sürümü: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `hastane`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktorlar`
--

DROP TABLE IF EXISTS `doktorlar`;
CREATE TABLE IF NOT EXISTS `doktorlar` (
  `doktor_id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `soyad` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `uzmanlik_alani` varchar(100) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `telefon` varchar(15) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `adres` text COLLATE utf8mb3_turkish_ci,
  `kullanici_adi` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `sifre` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  PRIMARY KEY (`doktor_id`),
  UNIQUE KEY `kullanici_adi` (`kullanici_adi`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

--
-- Tablo döküm verisi `doktorlar`
--

INSERT INTO `doktorlar` (`doktor_id`, `ad`, `soyad`, `uzmanlik_alani`, `telefon`, `email`, `adres`, `kullanici_adi`, `sifre`) VALUES
(8, 'Ayhan', 'Balcı', 'Dahiliye', '05051333382', 'ayhan@hotmail.com', 'adresim', 'ayhan', 'ayhan'),
(9, 'Sırma', 'Balcı', 'Cildiye', '05041333382', 'sırma@hotmail.com', 'adresim', 'sırma', 'sırma');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktor_randevu`
--

DROP TABLE IF EXISTS `doktor_randevu`;
CREATE TABLE IF NOT EXISTS `doktor_randevu` (
  `doktor_id` int NOT NULL,
  `randevu_id` int NOT NULL,
  PRIMARY KEY (`doktor_id`,`randevu_id`),
  KEY `randevu_id` (`randevu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hastalar`
--

DROP TABLE IF EXISTS `hastalar`;
CREATE TABLE IF NOT EXISTS `hastalar` (
  `hasta_id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `soyad` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `tc_kimlik` varchar(11) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `dogum_tarihi` date DEFAULT NULL,
  `cinsiyet` varchar(10) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `telefon` varchar(15) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `adres` text COLLATE utf8mb3_turkish_ci,
  `kullanici_adi` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `sifre` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  PRIMARY KEY (`hasta_id`),
  UNIQUE KEY `tc_kimlik` (`tc_kimlik`),
  UNIQUE KEY `kullanici_adi` (`kullanici_adi`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

--
-- Tablo döküm verisi `hastalar`
--

INSERT INTO `hastalar` (`hasta_id`, `ad`, `soyad`, `tc_kimlik`, `dogum_tarihi`, `cinsiyet`, `telefon`, `email`, `adres`, `kullanici_adi`, `sifre`) VALUES
(15, 'kaan', 'balcı', '34955374190', '2025-06-20', 'erkek', '05071333382', 'kaan-balci777@hotmail.com', 'adresim', 'kaan', 'kaan');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hasta_randevu`
--

DROP TABLE IF EXISTS `hasta_randevu`;
CREATE TABLE IF NOT EXISTS `hasta_randevu` (
  `hasta_id` int NOT NULL,
  `randevu_id` int NOT NULL,
  PRIMARY KEY (`hasta_id`,`randevu_id`),
  KEY `randevu_id` (`randevu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `randevular`
--

DROP TABLE IF EXISTS `randevular`;
CREATE TABLE IF NOT EXISTS `randevular` (
  `randevu_id` int NOT NULL AUTO_INCREMENT,
  `tarih` datetime DEFAULT NULL,
  `hasta_id` int DEFAULT NULL,
  `doktor_id` int DEFAULT NULL,
  `durum` enum('Planlanan','Onaylanan','Tamamlandı') COLLATE utf8mb3_turkish_ci DEFAULT 'Planlanan',
  `sikayet` text COLLATE utf8mb3_turkish_ci,
  PRIMARY KEY (`randevu_id`),
  UNIQUE KEY `doktor_id` (`doktor_id`,`tarih`),
  KEY `hasta_id` (`hasta_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

--
-- Tablo döküm verisi `randevular`
--

INSERT INTO `randevular` (`randevu_id`, `tarih`, `hasta_id`, `doktor_id`, `durum`, `sikayet`) VALUES
(32, '2023-12-21 10:00:00', 15, 8, 'Tamamlandı', 'deneme'),
(33, '2023-12-21 12:00:00', 15, 9, 'Onaylanan', 'deneme1'),
(34, '2023-12-23 00:00:00', 15, 8, 'Tamamlandı', 'deneme2'),
(35, '2023-12-23 12:00:00', 15, 8, 'Tamamlandı', 'dadasda'),
(36, '2023-12-25 14:17:34', 15, 8, 'Planlanan', 'ljçhl'),
(37, '2024-01-07 10:00:00', 15, 9, 'Planlanan', 'fdsfdf');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sekreterler`
--

DROP TABLE IF EXISTS `sekreterler`;
CREATE TABLE IF NOT EXISTS `sekreterler` (
  `sekreter_id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `soyad` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `telefon` varchar(15) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `adres` text COLLATE utf8mb3_turkish_ci,
  `kullanici_adi` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  `sifre` varchar(50) COLLATE utf8mb3_turkish_ci DEFAULT NULL,
  PRIMARY KEY (`sekreter_id`),
  UNIQUE KEY `kullanici_adi` (`kullanici_adi`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

--
-- Tablo döküm verisi `sekreterler`
--

INSERT INTO `sekreterler` (`sekreter_id`, `ad`, `soyad`, `telefon`, `email`, `adres`, `kullanici_adi`, `sifre`) VALUES
(1, 'Seher', 'Güven', '05061333382', 'kaan-balci666@hotmail.com', 'adresim', 'seher', 'seher');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sekreterler_randevu`
--

DROP TABLE IF EXISTS `sekreterler_randevu`;
CREATE TABLE IF NOT EXISTS `sekreterler_randevu` (
  `sekreter_id` int NOT NULL,
  `randevu_id` int NOT NULL,
  PRIMARY KEY (`sekreter_id`,`randevu_id`),
  KEY `randevu_id` (`randevu_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_turkish_ci;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `doktor_randevu`
--
ALTER TABLE `doktor_randevu`
  ADD CONSTRAINT `doktor_randevu_ibfk_1` FOREIGN KEY (`doktor_id`) REFERENCES `doktorlar` (`doktor_id`),
  ADD CONSTRAINT `doktor_randevu_ibfk_2` FOREIGN KEY (`randevu_id`) REFERENCES `randevular` (`randevu_id`);

--
-- Tablo kısıtlamaları `hasta_randevu`
--
ALTER TABLE `hasta_randevu`
  ADD CONSTRAINT `hasta_randevu_ibfk_1` FOREIGN KEY (`hasta_id`) REFERENCES `hastalar` (`hasta_id`),
  ADD CONSTRAINT `hasta_randevu_ibfk_2` FOREIGN KEY (`randevu_id`) REFERENCES `randevular` (`randevu_id`);

--
-- Tablo kısıtlamaları `randevular`
--
ALTER TABLE `randevular`
  ADD CONSTRAINT `randevular_ibfk_1` FOREIGN KEY (`hasta_id`) REFERENCES `hastalar` (`hasta_id`),
  ADD CONSTRAINT `randevular_ibfk_2` FOREIGN KEY (`doktor_id`) REFERENCES `doktorlar` (`doktor_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
