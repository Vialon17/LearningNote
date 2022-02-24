/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 10.1.37-MariaDB : Database - day4
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`stu` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `stu`;

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `cno` varchar(20) NOT NULL,
  `cname` varchar(20) NOT NULL,
  `tno` varchar(20) NOT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `course` */

insert  into `course`(`cno`,`cname`,`tno`) values 
('3-105','计算机导论','825'),
('3-245','操作系统','804'),
('6-166','数字电路','856'),
('9-888','高等数学','831');

/*Table structure for table `grade` */

DROP TABLE IF EXISTS `grade`;

CREATE TABLE `grade` (
  `low` int(11) DEFAULT NULL,
  `upp` int(11) DEFAULT NULL,
  `ranks` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `grade` */

insert  into `grade`(`low`,`upp`,`ranks`) values 
(90,100,'A'),
(80,89,'B'),
(70,79,'C'),
(60,69,'D'),
(0,59,'D');

/*Table structure for table `score` */

DROP TABLE IF EXISTS `score`;

CREATE TABLE `score` (
  `sno` varchar(20) NOT NULL,
  `cno` varchar(20) NOT NULL,
  `degree` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `score` */

insert  into `score`(`sno`,`cno`,`degree`) values 
('103','3-245',86),
('105','3-245',75),
('109','3-245',68),
('103','3-105',92),
('105','3-105',98),
('109','3-105',76),
('103','3-105',64),
('105','3-105',91),
('109','3-105',78),
('103','6-166',85),
('105','6-166',79),
('109','6-166',81);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `sno` varchar(20) NOT NULL,
  `sname` varchar(20) NOT NULL,
  `ssex` varchar(20) NOT NULL,
  `sbirthday` date DEFAULT NULL,
  `class` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `student` */

insert  into `student`(`sno`,`sname`,`ssex`,`sbirthday`,`class`) values 
('101','李军','男','1976-02-20','95033'),
('103','陆君','男','1974-06-03','95031'),
('105','匡明','男','1975-10-02','95031'),
('107','王丽','','1976-01-23','95033'),
('108','曾华','男','1977-09-01','95033'),
('109','王芳','女','1975-02-10','95031');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `tno` varchar(20) NOT NULL,
  `tname` varchar(20) NOT NULL,
  `tsex` varchar(20) NOT NULL,
  `tbirthday` date DEFAULT NULL,
  `prof` varchar(20) DEFAULT NULL,
  `depart` varchar(20) NOT NULL,
  PRIMARY KEY (`tno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `teacher` */

insert  into `teacher`(`tno`,`tname`,`tsex`,`tbirthday`,`prof`,`depart`) values 
('804','李诚','男','1958-12-02','副教授','计算机系'),
('825','王萍','女','1972-05-05','助教','计算机系'),
('831','刘冰','女','1977-08-14','助教','电子工程系'),
('856','张旭','男','1969-03-12','讲师','电子工程系');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
