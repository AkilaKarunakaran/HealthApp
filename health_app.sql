-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: May 29, 2026 at 11:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `health_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `glucose` float NOT NULL,
  `haemoglobin` float NOT NULL,
  `cholesterol` float NOT NULL,
  `remarks` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`id`, `name`, `dob`, `email`, `glucose`, `haemoglobin`, `cholesterol`, `remarks`) VALUES
(6, 'pal', '2027-09-28', 'lks@email.com', 12, 12, 120, 'Normal'),
(8, 'venu', '2027-05-03', 'sdf@email.com', 445, 12, 124, 'High risk of Diabetes'),
(9, 'ffg', '2026-06-01', 'kjh@email.com', 130, 10, 120, 'Possible Anemia'),
(11, 'Anu', '2023-07-11', 'anu@gmail.com', 86, 12, 150, 'Normal'),
(12, 'Venu', '2022-07-11', 'venu@gmail.com', 130, 13, 230, 'Borderline Risk'),
(13, 'Karki', '2023-02-28', 'karki@email.com', 11, 14, 280, 'Normal'),
(14, 'Avinesh', '2012-06-12', 'avinesh@gmail.com', 85, 12, 180, 'Normal');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
