SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

SET time_zone = "+00:00";

--
-- Database: MKGames
--

-- --------------------------------------------------------

--
-- Table structure for table categories
--
Create database if not exists MKGames;
use MKGames;

CREATE TABLE if not exists Users (
  firstname varchar(50) NOT NULL,
  lastname varchar(50) NOT NULL,
  uname varchar(20) Primary key,
  password varchar(10)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

CREATE TABLE if not exists Feedbacks (
  firstname varchar(50) NOT NULL,
  lastname varchar(50) NOT NULL,
  feedback varchar(250),
  cdate DATETIME
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

CREATE TABLE if not exists Scores (
  uname varchar(50) NOT NULL,
  score int,
  cdate DATETIME
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table categories
--

INSERT INTO Users VALUES
('admin', 'admin', 'admin','admin');

INSERT INTO Feedbacks VALUES
('admin', 'admin', 'good game', NOW());

INSERT INTO Scores VALUES
('admin', 1000, NOW());

-- --------------------------------------------------------

