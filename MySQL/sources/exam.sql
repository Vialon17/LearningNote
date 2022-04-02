/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 10.1.37-MariaDB : Database - exam
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`exam` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `exam`;

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `deptno` int(11) NOT NULL,
  `dname` varchar(50) DEFAULT NULL,
  `loc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`deptno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `dept` */

insert  into `dept`(`deptno`,`dname`,`loc`) values 
(10,'教研部','北京'),
(20,'学工部','上海'),
(30,'销售部','广州'),
(40,'财务部','武汉');

/*Table structure for table `emp` */

DROP TABLE IF EXISTS `emp`;

CREATE TABLE `emp` (
  `empno` int(11) NOT NULL,
  `ename` varchar(50) DEFAULT NULL,
  `job` varchar(50) DEFAULT NULL,
  `mgr` int(11) DEFAULT NULL,
  `hiredate` date DEFAULT NULL,
  `sal` decimal(7,2) DEFAULT NULL,
  `COMM` decimal(7,2) DEFAULT NULL,
  `deptno` int(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_emp` (`mgr`),
  CONSTRAINT `fk_emp` FOREIGN KEY (`mgr`) REFERENCES `emp` (`empno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `emp` */

insert  into `emp`(`empno`,`ename`,`job`,`mgr`,`hiredate`,`sal`,`COMM`,`deptno`) values 
(1001,'甘宁','文员',1004,'2000-12-17',18000.00,0.00,20),
(1002,'黛绮丝','文员',1006,'2000-02-02',18000.00,3000.00,30),
(1003,'殷天正','文员',1006,'2001-02-22',12500.00,1000.00,30),
(1004,'刘备','经理',1009,'2001-04-02',29750.00,100.00,20),
(1005,'谢逊','销售员',1006,'2001-09-28',28500.00,14000.00,20),
(1006,'罗志祥','经理',1009,'2001-05-01',28500.00,0.00,30),
(1007,'张飞','经理',1009,'2001-09-01',24500.00,NULL,10),
(1008,'诸葛亮','分析师',1004,'2007-04-19',30000.00,NULL,20),
(1009,'曾阿牛','董事长',NULL,'2001-11-17',50000.00,NULL,10),
(1010,'韦一笑','销售员',1006,'2001-09-08',15000.00,0.00,30),
(1011,'周泰','文员',1008,'2007-05-23',11000.00,NULL,20),
(1012,'程普','文员',1006,'2001-12-03',11000.00,NULL,30),
(1013,'庞统','分析师',1004,'2001-12-03',12500.00,NULL,20),
(1014,'黄盖','文员',1007,'2002-01-23',13000.00,NULL,10),
(1015,'欧阳','销售员',1004,'2002-09-08',12500.00,3000.00,20),
(1016,'欧阳娜娜','销售助理',1006,'2020-06-19',25000.00,0.00,30);

/*Table structure for table `salgrade` */

DROP TABLE IF EXISTS `salgrade`;

CREATE TABLE `salgrade` (
  `grade` int(11) NOT NULL,
  `losal` int(11) DEFAULT NULL,
  `hisal` int(11) DEFAULT NULL,
  PRIMARY KEY (`grade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `salgrade` */

insert  into `salgrade`(`grade`,`losal`,`hisal`) values 
(1,7000,12000),
(2,12010,14000),
(3,14010,20000),
(4,20010,30000),
(5,30010,99990);

/*Table structure for table `stu` */

DROP TABLE IF EXISTS `stu`;

CREATE TABLE `stu` (
  `sid` int(11) NOT NULL,
  `sname` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gander` varchar(10) DEFAULT NULL,
  `province` varchar(50) DEFAULT NULL,
  `tuition` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `stu` */

insert  into `stu`(`sid`,`sname`,`age`,`gander`,`province`,`tuition`) values 
(0,'王永',23,'男','北京',1500),
(2,'张雷',25,'男','辽宁',2500),
(3,'李强',22,'男','北京',3500),
(4,'宋永合',25,'男','北京',1500),
(5,'叙美丽',23,'女','北京',1000),
(6,'陈宁',22,'女','山东',2500),
(7,'王丽',21,'女','北京',1600),
(8,'李永',23,'男','北京',3500),
(9,'张玲',23,'女','广州',2500),
(10,'啊历',18,'男','山西',3500),
(11,'王刚',23,'男','湖北',4500),
(12,'陈永',24,'男','北京',1500),
(13,'李雷',0,'男','辽宁',2500),
(14,'李沿',22,'男','北京',3500),
(15,'王小明',25,'男','北京',1500),
(16,'王小丽',23,'女','北京',1000),
(17,'唐宁',22,'女','山东',2500),
(18,'唐丽',21,'女','北京',1600),
(19,'啊永',23,'男','北京',3500),
(20,'唐玲',23,'女','广州',2500),
(21,'叙刚',18,'男','山西',3500),
(22,'王累',23,'男','湖北',4500),
(23,'赵安',23,'男','北京',1500),
(24,'关雷',25,'男','辽宁',2500),
(25,'李字',22,'男','北京',3500),
(26,'叙安国',25,'男','北京',1500),
(27,'陈浩难',23,'女','北京',1000),
(28,'陈明',22,'女','山东',2500),
(29,'孙丽',21,'女','北京',1600),
(30,'李治国',23,'男','北京',3500),
(31,'张娜',23,'女','广州',2500),
(32,'安强',18,'男','山西',3500),
(33,'王欢',23,'男','湖北',4500),
(34,'周天乐',23,'男','北京',1500),
(35,'关雷',25,'男','辽宁',2500),
(36,'吴强',22,'男','北京',3500),
(37,'吴合国',25,'男','北京',1500),
(38,'正小和',23,'女','北京',1000),
(39,'吴丽',22,'女','山东',2500),
(40,'冯含',21,'女','北京',1600),
(41,'陈冬',23,'男','北京',3500),
(42,'关玲',23,'女','广州',2500),
(43,'包利',18,'男','山西',3500),
(44,'威刚',23,'男','湖北',4500),
(45,'李永',23,'男','北京',1500),
(46,'张关雷',25,'男','辽宁',2500),
(47,'送小强',22,'男','北京',3500),
(48,'关动林',25,'男','北京',1500),
(49,'苏小哑',23,'女','北京',1000),
(50,'赵宁',22,'女','山东',2500),
(51,'陈丽',21,'女','北京',1600),
(52,'钱小刚',23,'男','北京',3500),
(53,'艾林',23,'女','广州',2500),
(54,'郭林',18,'男','山西',3500),
(55,'周制强',23,'男','湖北',4500),
(56,'天一',23,NULL,NULL,NULL),
(57,'马云',NULL,'',NULL,NULL),
(60,'赵日天',NULL,'',NULL,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
