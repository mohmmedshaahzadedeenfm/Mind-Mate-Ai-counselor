/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - mindcare_viswajyothi
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mindcare_viswajyothi` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mindcare_viswajyothi`;

/*Table structure for table `answer` */

DROP TABLE IF EXISTS `answer`;

CREATE TABLE `answer` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `answer` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `answer` */

insert  into `answer`(`answer_id`,`question_id`,`answer`,`status`,`type`) values 
(1,1,'Not at all.','No','text'),
(2,1,'Several days.','Yes','text'),
(3,1,'More than half the days.','No','text'),
(4,1,'Nearly every day.','No','text'),
(5,2,'Not at all.','No','text'),
(6,2,'Several days.','No','text'),
(7,2,'More than half the days.','Yes','text'),
(8,2,'Nearly every day.','No','text'),
(9,3,'Not at all.','No','text'),
(10,3,'Several days.','Yes','text'),
(11,3,'More than half the days.','No','text'),
(12,3,'Nearly every day.','No','text'),
(13,4,'Not at all.','No','text'),
(14,4,'Several days.','No','text'),
(15,4,'More than half the days.','No','text'),
(16,4,'Nearly every day.','Yes','text'),
(17,5,'Not at all.','No','text'),
(18,5,'Several days.','No','text'),
(19,5,'More than half the days.','No','text'),
(20,5,'Nearly every day.','Yes','text'),
(21,6,'Not at all.','No','text'),
(22,6,'Several days.','No','text'),
(23,6,'More than half the days.','Yes','text'),
(24,6,'Nearly every day.','No','text'),
(25,7,'Not at all.','No','text'),
(26,7,'Several days.','No','text'),
(27,7,'More than half the days.','No','text'),
(28,7,'Nearly every day.','Yes','text'),
(29,8,'Not at all.','No','text'),
(30,8,'Several days.','No','text'),
(31,8,'More than half the days.','No','text'),
(32,8,'Nearly every day.','Yes','text'),
(33,9,'Not at all.','No','text'),
(34,9,'Several days.','Yes','text'),
(35,9,'More than half the days.','No','text'),
(36,9,'Nearly every day.','No','text');

/*Table structure for table `answers` */

DROP TABLE IF EXISTS `answers`;

CREATE TABLE `answers` (
  `Answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `Question_id` int(11) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  `Answer_details` varchar(100) DEFAULT NULL,
  `Mark_awarded` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Answer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `answers` */

insert  into `answers`(`Answer_id`,`Question_id`,`User_id`,`Answer_details`,`Mark_awarded`,`date`,`status`) values 
(1,1,1,'several days ','9.999999999999998','2024-04-23','Neutral'),
(2,2,1,'more than half day ','4.999999999999999','2024-04-23','Neutral'),
(3,3,1,'several days ','9.999999999999998','2024-04-23','Neutral'),
(4,4,1,'nearly every day ','10.000000000000002','2024-04-23','Neutral'),
(5,5,1,'nearly every day ','10.000000000000002','2024-04-23','Neutral'),
(6,6,1,'more than half day ','4.999999999999999','2024-04-23','Neutral'),
(7,7,1,'nearly every day ','10.000000000000002','2024-04-23','Neutral'),
(8,8,1,'nearly every day ','10.000000000000002','2024-04-23','Neutral'),
(9,9,1,'several days ','9.999999999999998','2024-04-23','Neutral');

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `Appointment_id` int(100) NOT NULL AUTO_INCREMENT,
  `Request_id` int(100) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  `Amount` varchar(100) DEFAULT NULL,
  `Appointmentdate` varchar(100) DEFAULT NULL,
  `Appointmenttime` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Appointment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `appointment` */

insert  into `appointment`(`Appointment_id`,`Request_id`,`Details`,`Date`,`Amount`,`Appointmentdate`,`Appointmenttime`,`Status`) values 
(1,3,'vbj','2024-02-15','1000','15/2/2024','11:00','paid'),
(2,1,'ghh','2024-02-15','1000','28/2/2024','11:00','pending'),
(3,2,'cbj','2024-02-15','1000','15/2/2024','02:00','pending'),
(4,3,'gh','2024-02-15','1000','23/2/2024','09:00','pending'),
(5,3,'hdh','2024-02-23','1000','29/2/2024','11:00','pending'),
(6,1,'dr','2024-03-09','1000','9/3/2024','09:00','pending'),
(7,1,'hsh','2024-03-09','1000','27/3/2024','02:00','paid'),
(8,7,'gbb','2024-03-09','1000','30/3/2024','02:00','paid'),
(9,8,'dud','2024-03-09','1000','19/3/2024','02:00','paid'),
(10,8,'bn','2024-04-12','1000','27/4/2024','11:00','paid'),
(11,8,'gh','2024-04-12','1000','26/4/2024','02:00','paid'),
(12,11,'hello','2024-04-12','1000','13/4/2024','09:00','paid'),
(13,1,'fgh','2024-04-23','1000','23/4/2024','11:00','pending');

/*Table structure for table `awearness` */

DROP TABLE IF EXISTS `awearness`;

CREATE TABLE `awearness` (
  `awearness_id` int(11) NOT NULL AUTO_INCREMENT,
  `Medication_id` int(11) DEFAULT NULL,
  `awearness` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `link` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`awearness_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `awearness` */

insert  into `awearness`(`awearness_id`,`Medication_id`,`awearness`,`details`,`link`,`date`) values 
(1,1,'jhhg','jhgdjfh',NULL,'2023-12-16'),
(3,1,'hjgh','hjg','','2024-03-21'),
(4,1,'sd','sd','www.hgvhgh.com','2024-03-13');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `quest_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`quest_id`,`sender_id`,`receiver_id`,`message`,`date`) values 
(1,1,0,4,'Little interest or pleasure in doing things','2024-04-23'),
(2,1,4,0,'several days ','2024-04-23'),
(3,2,0,4,'Feeling down, depressed, or hopeless','2024-04-23'),
(4,2,4,0,'more than half day ','2024-04-23'),
(5,3,0,4,'Trouble falling or staying asleep, or sleeping too much','2024-04-23'),
(6,3,4,0,'several days ','2024-04-23'),
(7,4,0,4,'Feeling tired or having little energy','2024-04-23'),
(8,4,4,0,'nearly every day ','2024-04-23'),
(9,5,0,4,'Poor appetite or overeating','2024-04-23'),
(10,5,4,0,'nearly every day ','2024-04-23'),
(11,6,0,4,'Feeling bad about yourself - or that you are a failure or have let yourself or your family down','2024-04-23'),
(12,6,4,0,'more than half day ','2024-04-23'),
(13,7,0,4,'Trouble concentrating on things, such as reading the newspaper or watching television','2024-04-23'),
(14,7,4,0,'nearly every day ','2024-04-23'),
(15,8,0,4,'Moving or speaking so slowly that other people could have noticed','2024-04-23'),
(16,8,4,0,'nearly every day ','2024-04-23'),
(17,9,0,4,'Thoughts that you would be better off dead, or of hurting yourself','2024-04-23'),
(18,9,4,0,'several days ','2024-04-23');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`Login_id`,`feedback`,`date`) values 
(1,2,'check','2023-12-13'),
(2,3,'ghhg','2023-12-15'),
(3,3,'ghhg','2023-12-15'),
(4,3,'ghhg','2023-12-15'),
(5,3,'gfcv','2023-12-15'),
(6,4,'hiiiiii','2023-12-15'),
(7,3,'hsj','2023-12-16'),
(8,3,'nhj','2023-12-16'),
(9,3,'nbhg','2023-12-16'),
(10,3,'gbb','2023-12-16'),
(11,3,'gbb','2023-12-16'),
(12,3,'gbb','2023-12-16'),
(13,3,'gbb','2023-12-16'),
(14,3,'hdh','2023-12-16'),
(15,3,'ggg','2023-12-16'),
(16,3,'ggg','2023-12-16'),
(17,3,'ghxg','2023-12-16'),
(18,3,'ghxg','2023-12-16'),
(19,3,'kkkkk','2023-12-16'),
(20,4,'ddddd','2023-12-16'),
(21,4,'sfgs','2023-12-16'),
(22,4,'gvvv','2023-12-16'),
(23,4,'ngxh','2023-12-18'),
(24,4,'hdhd','2024-01-08'),
(25,3,'eee','2024-01-08'),
(26,4,'','2024-01-08');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `Usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`Username`,`Password`,`Usertype`) values 
(1,'admin','admin','admin'),
(2,'sumithps123','sumithps123','meditation'),
(3,'aa','aa','psychiatrist'),
(4,'s','s','user'),
(6,'sneha123','sneha123','user'),
(7,'amakvl123','amakvl123','meditation'),
(9,'bshs','hdj2hs','user');

/*Table structure for table `meditation` */

DROP TABLE IF EXISTS `meditation`;

CREATE TABLE `meditation` (
  `Medication_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `Fname` varchar(100) DEFAULT NULL,
  `Lname` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Qualification` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`Medication_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `meditation` */

insert  into `meditation`(`Medication_id`,`Login_id`,`Fname`,`Lname`,`Place`,`Phone`,`Email`,`Qualification`,`image`) values 
(1,2,'SUMITH','PS','Thrissur','7593938855','sumithps78@gmail.com','MCA','static/uploads/723984e8-1d33-4a2d-979c-dee7df2669c4c2.jpg'),
(2,7,'AMAL','KV','Thrissur','8963654999','amal123@gmail.com','MBBS','static/uploads/a7d7d722-62d0-4dec-ac6a-76f94590c5e6c1.jpg');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `Appointment_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `date` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `message` */

/*Table structure for table `motivation` */

DROP TABLE IF EXISTS `motivation`;

CREATE TABLE `motivation` (
  `Motivation_id` int(100) NOT NULL AUTO_INCREMENT,
  `Appointment_id` int(100) DEFAULT NULL,
  `Class` varchar(100) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Motivation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `motivation` */

insert  into `motivation`(`Motivation_id`,`Appointment_id`,`Class`,`Details`,`Date`,`Status`) values 
(5,1,'https://www.youtube.com/','wrong foodddd','2024-01-02','pending'),
(4,1,'https://www.youtube.com/','jhjddd','2024-01-02','pending'),
(6,1,'https://www.youtube.com/','ssgdf','2024-01-07','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `Payment_id` int(100) NOT NULL AUTO_INCREMENT,
  `Appointment_id` int(100) DEFAULT NULL,
  `Amount` int(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`Payment_id`,`Appointment_id`,`Amount`,`Date`) values 
(1,1,1000,'2024-01-01'),
(2,3,1000,'2024-01-01'),
(3,4,1000,'2024-01-01'),
(4,2,1000,'2024-01-08'),
(5,5,1000,'2024-01-08'),
(6,5,1000,'2024-01-08'),
(7,6,1000,'2024-01-08'),
(8,1,1000,'2024-03-09'),
(9,9,1000,'2024-03-09'),
(10,8,1000,'2024-03-09'),
(11,7,1000,'2024-03-09'),
(12,11,1000,'2024-04-12'),
(13,12,1000,'2024-04-12'),
(14,12,1000,'2024-04-12'),
(15,10,1000,'2024-04-12'),
(16,10,1000,'2024-04-12'),
(17,10,1000,'2024-04-12');

/*Table structure for table `psychiatrist` */

DROP TABLE IF EXISTS `psychiatrist`;

CREATE TABLE `psychiatrist` (
  `psychiatrist_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `Fname` varchar(100) DEFAULT NULL,
  `Lname` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Qualification` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`psychiatrist_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `psychiatrist` */

insert  into `psychiatrist`(`psychiatrist_id`,`Login_id`,`Fname`,`Lname`,`Place`,`Phone`,`Email`,`Qualification`,`image`) values 
(1,3,'AMAL','KV','Thiruvananthapuram','8963654798','amal123@gmail.com','BCA','static/uploads/334bf3a9-ba7b-4db6-81cf-5d1c7fb90216c1.jpg');

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(1000) DEFAULT NULL,
  `file` varchar(1000) DEFAULT NULL,
  `testtype` varchar(1000) DEFAULT NULL,
  `roundtype` varchar(1000) DEFAULT NULL,
  `testname` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `qtype` varchar(100) DEFAULT NULL,
  `attend` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`question_id`,`question`,`file`,`testtype`,`roundtype`,`testname`,`date`,`qtype`,`attend`) values 
(1,'Little interest or pleasure in doing things','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(2,'Feeling down, depressed, or hopeless','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(3,'Trouble falling or staying asleep, or sleeping too much','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(4,'Feeling tired or having little energy','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(5,'Poor appetite or overeating','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(6,'Feeling bad about yourself - or that you are a failure or have let yourself or your family down','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(7,'Trouble concentrating on things, such as reading the newspaper or watching television','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(8,'Moving or speaking so slowly that other people could have noticed','NA','Dyscalculia','Round1','text','2024-04-19','text','pending'),
(9,'Thoughts that you would be better off dead, or of hurting yourself','NA','Dyscalculia','Round1','text','2024-04-19','text','pending');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `Request_id` int(100) NOT NULL AUTO_INCREMENT,
  `User_id` int(100) DEFAULT NULL,
  `Appointment_for` int(100) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`Request_id`,`User_id`,`Appointment_for`,`Details`,`Date`,`Status`) values 
(1,1,2,'vhj','2024-04-23','pending');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `r1` varchar(100) DEFAULT NULL,
  `r2` varchar(100) DEFAULT NULL,
  `r3` varchar(100) DEFAULT NULL,
  `r4` varchar(100) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  `Request_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `result` */

/*Table structure for table `suggestedtreatment` */

DROP TABLE IF EXISTS `suggestedtreatment`;

CREATE TABLE `suggestedtreatment` (
  `suggestedtreatment_id` int(11) NOT NULL AUTO_INCREMENT,
  `provided_id` int(11) DEFAULT NULL,
  `Provided_by` varchar(100) DEFAULT NULL,
  `Treatment` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`suggestedtreatment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `suggestedtreatment` */

insert  into `suggestedtreatment`(`suggestedtreatment_id`,`provided_id`,`Provided_by`,`Treatment`,`Date`,`Details`) values 
(1,4,'appointment','hhj','2024-01-01','kkjy'),
(2,4,'appointment','jsjs','2024-01-08','jsj');

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `Test_id` int(100) NOT NULL AUTO_INCREMENT,
  `Request_id` int(100) DEFAULT NULL,
  `User_id` int(100) DEFAULT NULL,
  `test` varchar(100) DEFAULT NULL,
  `test_result` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Test_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `test` */

insert  into `test`(`Test_id`,`Request_id`,`User_id`,`test`,`test_result`) values 
(1,1,NULL,'aaaaa','attended'),
(2,2,NULL,'bbbbb','attended'),
(3,3,NULL,'ccccc','attended'),
(4,4,NULL,'ddddd','attended'),
(5,5,NULL,'jjjjj','attended');

/*Table structure for table `updations` */

DROP TABLE IF EXISTS `updations`;

CREATE TABLE `updations` (
  `Updation_id` int(11) NOT NULL AUTO_INCREMENT,
  `Appointment_id` int(11) DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Updation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `updations` */

insert  into `updations`(`Updation_id`,`Appointment_id`,`Details`,`Date`) values 
(1,4,'jsj','2024-01-01'),
(2,4,'dff','2024-01-08'),
(3,4,'aaa','2024-01-08');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) DEFAULT NULL,
  `Fname` varchar(100) DEFAULT NULL,
  `Lname` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`Login_id`,`Fname`,`Lname`,`Place`,`Phone`,`Email`) values 
(1,4,'sam','kk','thrissur','5599884466','sam@gmail.com'),
(3,6,'arun','jj','kannur ','9566556688','arun@gmail.com'),
(4,9,'sneha','ng','jdj','5656454545','shshsh@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
