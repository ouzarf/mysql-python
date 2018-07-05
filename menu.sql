-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Ven 16 Février 2018 à 10:34
-- Version du serveur :  5.6.21
-- Version de PHP :  5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `menu`
--

-- --------------------------------------------------------

--
-- Structure de la table `fish`
--

CREATE TABLE IF NOT EXISTS `fish` (
`ID` int(11) NOT NULL,
  `NAME` varchar(30) NOT NULL,
  `PRICE` float(5,2) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `fish`
--

INSERT INTO `fish` (`ID`, `NAME`, `PRICE`) VALUES
(1, 'catfish', 8.50),
(2, 'catfish', 8.50),
(3, 'tuna', 8.00),
(4, 'catfish', 5.00),
(5, 'bass', 6.75),
(6, 'haddock', 6.50),
(7, 'salmon', 9.50),
(8, 'trout', 6.00),
(9, 'tuna', 7.50),
(10, 'yellowfin tuna', 12.00),
(11, 'yellowfin tuna', 13.00),
(12, 'tuna', 7.50);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `fish`
--
ALTER TABLE `fish`
 ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `fish`
--
ALTER TABLE `fish`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=13;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
