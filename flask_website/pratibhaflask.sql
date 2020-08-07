-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2020 at 08:07 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pratibhaflask`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` text NOT NULL,
  `msg` varchar(50) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'pratibha', 'pr@gmail.com', '8978778787', 'hi there how are you ', '2020-07-25 12:22:57'),
(2, 'pratibha', 'pr@gmail.com', '8978778787', 'Hey are you ok ?', '2020-07-25 12:23:05'),
(3, 'zxax', 'pratibharan@gmail.com', '8989898977', 'fsfsfsafas', '2020-07-25 18:08:13'),
(4, 'zxax', 'prati@gmail.com', '8989898977', 'hi Ruchi how are you', '2020-07-30 10:24:39'),
(5, 'ruchi', 'pratibha@gmail.com', '8989898977', 'hi paoa', '2020-07-30 11:56:12'),
(6, 'zxax', 'zxax@gmail.com', '8989898977', 'zcZC', '2020-07-30 14:32:57'),
(7, 'my mail', 'maol@gmail.com', '8989898977', 'hey mail', '2020-07-30 21:27:20'),
(8, 'my mail', 'maol@gmail.com', '8989898977', 'hey mail', '2020-07-30 21:29:04'),
(9, 'my mail', 'maol@gmail.com', '8989898977', 'hey mail', '2020-07-30 21:37:51'),
(10, 'my mail', 'maol@gmail.com', '8989898977', 'hey mail', '2020-07-30 21:40:08');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `slug` varchar(30) NOT NULL,
  `img_file` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `content`, `date`, `slug`, `img_file`) VALUES
(1, 'This is my post', 'First post is always awsome and I love itLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin faucibus tempus lorem sollicitudin sagittis. Vestibulum eu placerat tortor. Sed eu magna quis sapien ultricies euismod. Quisque ligula erat, tempus porttitor sem ac, congue malesuada nunc. Vestibulum lobortis turpis quis nisl commodo, vel scelerisque nisl fermentum. Cras scelerisque lectus eget aliquet auctor. Curabitur vestibulum orci ante, in bibendum dolor euismod quis. Nullam nulla nisi, malesuada vitae accumsan ac, blandit eu dui. Pellentesque ut ligula ex. Donec lacinia eros et arcu rhoncus, sit amet vestibulum justo efficitur. Nulla facilisi. Integer a sem aliquet, dapibus ipsum eu, vehicula dui. Fusce id leo tellus. Ut eu accumsan arcu. Aliquam at vestibulum felis.\r\n\r\n', '2020-07-31 11:25:52', 'first_post', '/activity-img1.png'),
(2, 'This is second post', 'Second post is always awsome and I love it.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin faucibus tempus lorem sollicitudin sagittis. Vestibulum eu placerat tortor. Sed eu magna quis sapien ultricies euismod. Quisque ligula erat, tempus porttitor sem ac, congue malesuada nunc. Vestibulum lobortis turpis quis nisl commodo, vel scelerisque nisl fermentum. Cras scelerisque lectus eget aliquet auctor. Curabitur vestibulum orci ante, in bibendum dolor euismod quis.\r\n\r\n', '2020-07-31 11:25:57', 'second_post', '/activity-img2.png'),
(3, 'What is Lorem Ipsum?\r\n', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n\r\n', '2020-07-31 21:58:23', 'third_post', '/feed-img2.png'),
(4, 'What is Lorem Ipsum?\r\n', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n\r\n', '2020-07-31 21:58:40', 'forth_post', '/recent-img2.jpg'),
(5, 'What is Lorem Ipsum?\r\n', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n\r\n', '2020-07-31 21:58:40', 'fifth_post', ''),
(6, 'What is Lorem Ipsum?\r\n', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n\r\n', '2020-07-31 21:58:41', 'sixth_post', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
