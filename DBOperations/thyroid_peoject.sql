-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2022 at 01:44 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thyroid_peoject`
--

-- --------------------------------------------------------

--
-- Table structure for table `info_data`
--

CREATE TABLE `info_data` (
  `id` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `TSH` float NOT NULL,
  `T3` float NOT NULL,
  `TT4` float NOT NULL,
  `FTI` float NOT NULL,
  `sex_M` int(11) NOT NULL,
  `T3_measured_t` int(11) NOT NULL,
  `referral_source_SVI` int(11) NOT NULL,
  `referral_source_other` int(11) NOT NULL,
  `Result` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `info_data`
--

INSERT INTO `info_data` (`id`, `age`, `TSH`, `T3`, `TT4`, `FTI`, `sex_M`, `T3_measured_t`, `referral_source_SVI`, `referral_source_other`, `Result`) VALUES
(1, 51, 1.9, 2.2, 74, 81, 1, 1, 0, 1, 1),
(2, 51, 1.9, 2.2, 74, 81, 1, 1, 0, 1, 1),
(3, 51, 1.9, 2.2, 74, 81, 1, 1, 0, 1, 1),
(4, 51, 1.9, 2.2, 74, 81, 1, 1, 0, 1, 0),
(5, 51, 1.9, 2.2, 74, 81, 1, 1, 0, 0, 0),
(6, 44, 12, 1, 3.11, 33, 0, 1, 0, 1, 1),
(7, 78, 2.6, 0.3, 87, 91, 0, 1, 1, 0, 1),
(8, 42, 6.1, 2.2, 74, 100, 0, 1, 0, 1, 1),
(9, 79, 143, 0.7, 73, 72, 0, 1, 0, 1, 0),
(10, 51, 12, 2, 3.11, 33, 1, 1, 0, 1, 0),
(11, 37, 45, 2, 3.11, 33, 0, 0, 0, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `login_table`
--

CREATE TABLE `login_table` (
  `user_id` varchar(255) NOT NULL,
  `admin_password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login_table`
--

INSERT INTO `login_table` (`user_id`, `admin_password`) VALUES
('mujtaba9012', 'Aa@12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `info_data`
--
ALTER TABLE `info_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `info_data`
--
ALTER TABLE `info_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
