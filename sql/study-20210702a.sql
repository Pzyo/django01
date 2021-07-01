/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50732
Source Host           : 127.0.0.1:3306
Source Database       : study

Target Server Type    : MYSQL
Target Server Version : 50732
File Encoding         : 65001

Date: 2021-07-02 00:24:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `app01_author`
-- ----------------------------
DROP TABLE IF EXISTS `app01_author`;
CREATE TABLE `app01_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app01_author
-- ----------------------------

-- ----------------------------
-- Table structure for `app01_user`
-- ----------------------------
DROP TABLE IF EXISTS `app01_user`;
CREATE TABLE `app01_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app01_user
-- ----------------------------
INSERT INTO `app01_user` VALUES ('1', 'pzyo', '123');
INSERT INTO `app01_user` VALUES ('2', 'tom', '456');

-- ----------------------------
-- Table structure for `app02_author`
-- ----------------------------
DROP TABLE IF EXISTS `app02_author`;
CREATE TABLE `app02_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `author_detail_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `author_detail_id` (`author_detail_id`) USING BTREE,
  CONSTRAINT `app02_author_author_detail_id_226fa8c4_fk_app02_authordetail_id` FOREIGN KEY (`author_detail_id`) REFERENCES `app02_authordetail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app02_author
-- ----------------------------

-- ----------------------------
-- Table structure for `app02_authordetail`
-- ----------------------------
DROP TABLE IF EXISTS `app02_authordetail`;
CREATE TABLE `app02_authordetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` bigint(20) NOT NULL,
  `addr` varchar(32) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app02_authordetail
-- ----------------------------

-- ----------------------------
-- Table structure for `app02_book`
-- ----------------------------
DROP TABLE IF EXISTS `app02_book`;
CREATE TABLE `app02_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `publish_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `app02_book_publish_id_79be7951_fk_app02_publish_id` (`publish_id`) USING BTREE,
  CONSTRAINT `app02_book_publish_id_79be7951_fk_app02_publish_id` FOREIGN KEY (`publish_id`) REFERENCES `app02_publish` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app02_book
-- ----------------------------

-- ----------------------------
-- Table structure for `app02_book_authors`
-- ----------------------------
DROP TABLE IF EXISTS `app02_book_authors`;
CREATE TABLE `app02_book_authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `app02_book_authors_book_id_author_id_1a895ee1_uniq` (`book_id`,`author_id`) USING BTREE,
  KEY `app02_book_authors_author_id_191af2fa_fk_app02_author_id` (`author_id`) USING BTREE,
  CONSTRAINT `app02_book_authors_author_id_191af2fa_fk_app02_author_id` FOREIGN KEY (`author_id`) REFERENCES `app02_author` (`id`),
  CONSTRAINT `app02_book_authors_book_id_55aef806_fk_app02_book_id` FOREIGN KEY (`book_id`) REFERENCES `app02_book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app02_book_authors
-- ----------------------------

-- ----------------------------
-- Table structure for `app02_publish`
-- ----------------------------
DROP TABLE IF EXISTS `app02_publish`;
CREATE TABLE `app02_publish` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `addr` varchar(32) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app02_publish
-- ----------------------------

-- ----------------------------
-- Table structure for `app03_author`
-- ----------------------------
DROP TABLE IF EXISTS `app03_author`;
CREATE TABLE `app03_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `author_detail_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `author_detail_id` (`author_detail_id`) USING BTREE,
  CONSTRAINT `app03_author_author_detail_id_fe1e6506_fk_app03_authordetail_id` FOREIGN KEY (`author_detail_id`) REFERENCES `app03_authordetail` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app03_author
-- ----------------------------
INSERT INTO `app03_author` VALUES ('1', 'pzyo', '23', '1');
INSERT INTO `app03_author` VALUES ('2', 'tom', '84', '2');
INSERT INTO `app03_author` VALUES ('3', 'tank', '50', '3');

-- ----------------------------
-- Table structure for `app03_authordetail`
-- ----------------------------
DROP TABLE IF EXISTS `app03_authordetail`;
CREATE TABLE `app03_authordetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` bigint(20) NOT NULL,
  `addr` varchar(64) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app03_authordetail
-- ----------------------------
INSERT INTO `app03_authordetail` VALUES ('1', '110', '芜湖');
INSERT INTO `app03_authordetail` VALUES ('2', '120', '山东');
INSERT INTO `app03_authordetail` VALUES ('3', '130', '惠州');

-- ----------------------------
-- Table structure for `app03_book`
-- ----------------------------
DROP TABLE IF EXISTS `app03_book`;
CREATE TABLE `app03_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `publish_date` date NOT NULL,
  `publish_id` int(11) NOT NULL,
  `kucun` int(11) NOT NULL,
  `maichu` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `app03_book_publish_id_a7599a6e_fk_app03_publish_id` (`publish_id`) USING BTREE,
  CONSTRAINT `app03_book_publish_id_a7599a6e_fk_app03_publish_id` FOREIGN KEY (`publish_id`) REFERENCES `app03_publish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app03_book
-- ----------------------------
INSERT INTO `app03_book` VALUES ('1', '三国演义爆款', '623.23', '2021-07-01', '1', '800', '1000');
INSERT INTO `app03_book` VALUES ('2', '红楼梦爆款', '1166.23', '2021-07-01', '2', '2000', '1');
INSERT INTO `app03_book` VALUES ('3', '论语爆款', '1399.00', '2021-07-01', '1', '1000', '800');
INSERT INTO `app03_book` VALUES ('4', '聊斋爆款', '944.25', '2021-07-01', '2', '1000', '1000');
INSERT INTO `app03_book` VALUES ('5', '老子爆款', '833.66', '2021-07-01', '1', '1500', '500');

-- ----------------------------
-- Table structure for `app03_book_authors`
-- ----------------------------
DROP TABLE IF EXISTS `app03_book_authors`;
CREATE TABLE `app03_book_authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `app03_book_authors_book_id_author_id_c1492d91_uniq` (`book_id`,`author_id`) USING BTREE,
  KEY `app03_book_authors_author_id_2ac4fe0f_fk_app03_author_id` (`author_id`) USING BTREE,
  CONSTRAINT `app03_book_authors_author_id_2ac4fe0f_fk_app03_author_id` FOREIGN KEY (`author_id`) REFERENCES `app03_author` (`id`),
  CONSTRAINT `app03_book_authors_book_id_0ef25116_fk_app03_book_id` FOREIGN KEY (`book_id`) REFERENCES `app03_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app03_book_authors
-- ----------------------------
INSERT INTO `app03_book_authors` VALUES ('14', '1', '1');
INSERT INTO `app03_book_authors` VALUES ('18', '1', '2');
INSERT INTO `app03_book_authors` VALUES ('12', '2', '1');
INSERT INTO `app03_book_authors` VALUES ('13', '2', '2');
INSERT INTO `app03_book_authors` VALUES ('15', '3', '1');
INSERT INTO `app03_book_authors` VALUES ('16', '4', '1');
INSERT INTO `app03_book_authors` VALUES ('17', '4', '2');

-- ----------------------------
-- Table structure for `app03_publish`
-- ----------------------------
DROP TABLE IF EXISTS `app03_publish`;
CREATE TABLE `app03_publish` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `addr` varchar(64) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app03_publish
-- ----------------------------
INSERT INTO `app03_publish` VALUES ('1', '东方出版社', '东方', '123@qq.com');
INSERT INTO `app03_publish` VALUES ('2', '北方出版社', '北方', '666@qq.com');

-- ----------------------------
-- Table structure for `app03_user`
-- ----------------------------
DROP TABLE IF EXISTS `app03_user`;
CREATE TABLE `app03_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `register_time` date NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of app03_user
-- ----------------------------
INSERT INTO `app03_user` VALUES ('2', 'pzyo', '23', '2021-06-30');
INSERT INTO `app03_user` VALUES ('3', 'tomasss', '18', '2021-07-20');
INSERT INTO `app03_user` VALUES ('4', 'jerry', '23', '2021-06-02');
INSERT INTO `app03_user` VALUES ('5', 'tom', '77', '2021-07-01');
INSERT INTO `app03_user` VALUES ('6', 'tank', '44', '2020-06-29');

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add user', '7', 'add_user');
INSERT INTO `auth_permission` VALUES ('20', 'Can change user', '7', 'change_user');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete user', '7', 'delete_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can add author', '8', 'add_author');
INSERT INTO `auth_permission` VALUES ('23', 'Can change author', '8', 'change_author');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete author', '8', 'delete_author');
INSERT INTO `auth_permission` VALUES ('25', 'Can add author', '9', 'add_author');
INSERT INTO `auth_permission` VALUES ('26', 'Can change author', '9', 'change_author');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete author', '9', 'delete_author');
INSERT INTO `auth_permission` VALUES ('28', 'Can add publish', '10', 'add_publish');
INSERT INTO `auth_permission` VALUES ('29', 'Can change publish', '10', 'change_publish');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete publish', '10', 'delete_publish');
INSERT INTO `auth_permission` VALUES ('31', 'Can add author detail', '11', 'add_authordetail');
INSERT INTO `auth_permission` VALUES ('32', 'Can change author detail', '11', 'change_authordetail');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete author detail', '11', 'delete_authordetail');
INSERT INTO `auth_permission` VALUES ('34', 'Can add book', '12', 'add_book');
INSERT INTO `auth_permission` VALUES ('35', 'Can change book', '12', 'change_book');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete book', '12', 'delete_book');
INSERT INTO `auth_permission` VALUES ('37', 'Can add user', '13', 'add_user');
INSERT INTO `auth_permission` VALUES ('38', 'Can change user', '13', 'change_user');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete user', '13', 'delete_user');
INSERT INTO `auth_permission` VALUES ('40', 'Can add a uthor', '14', 'add_author');
INSERT INTO `auth_permission` VALUES ('41', 'Can change a uthor', '14', 'change_author');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete a uthor', '14', 'delete_author');
INSERT INTO `auth_permission` VALUES ('43', 'Can add publish', '15', 'add_publish');
INSERT INTO `auth_permission` VALUES ('44', 'Can change publish', '15', 'change_publish');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete publish', '15', 'delete_publish');
INSERT INTO `auth_permission` VALUES ('46', 'Can add book', '16', 'add_book');
INSERT INTO `auth_permission` VALUES ('47', 'Can change book', '16', 'change_book');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete book', '16', 'delete_book');
INSERT INTO `auth_permission` VALUES ('49', 'Can add author detail', '17', 'add_authordetail');
INSERT INTO `auth_permission` VALUES ('50', 'Can change author detail', '17', 'change_authordetail');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete author detail', '17', 'delete_authordetail');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`) USING BTREE,
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`) USING BTREE,
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('8', 'app01', 'author');
INSERT INTO `django_content_type` VALUES ('7', 'app01', 'user');
INSERT INTO `django_content_type` VALUES ('9', 'app02', 'author');
INSERT INTO `django_content_type` VALUES ('11', 'app02', 'authordetail');
INSERT INTO `django_content_type` VALUES ('12', 'app02', 'book');
INSERT INTO `django_content_type` VALUES ('10', 'app02', 'publish');
INSERT INTO `django_content_type` VALUES ('14', 'app03', 'author');
INSERT INTO `django_content_type` VALUES ('17', 'app03', 'authordetail');
INSERT INTO `django_content_type` VALUES ('16', 'app03', 'book');
INSERT INTO `django_content_type` VALUES ('15', 'app03', 'publish');
INSERT INTO `django_content_type` VALUES ('13', 'app03', 'user');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2021-06-28 06:41:16.302309');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2021-06-28 06:41:23.354454');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2021-06-28 06:41:24.821910');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2021-06-28 06:41:24.872077');
INSERT INTO `django_migrations` VALUES ('5', 'app01', '0001_initial', '2021-06-28 06:41:25.116966');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2021-06-28 06:41:26.279997');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2021-06-28 06:41:26.841735');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2021-06-28 06:41:27.098505');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2021-06-28 06:41:27.147516');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2021-06-28 06:41:27.738279');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2021-06-28 06:41:27.781095');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2021-06-28 06:41:27.828845');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2021-06-28 06:41:29.598137');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2021-06-28 06:41:30.290709');
INSERT INTO `django_migrations` VALUES ('15', 'app01', '0002_author', '2021-06-28 09:23:17.074354');
INSERT INTO `django_migrations` VALUES ('16', 'app01', '0003_auto_20210628_1731', '2021-06-28 09:31:46.871824');
INSERT INTO `django_migrations` VALUES ('17', 'app01', '0004_user_info', '2021-06-28 09:33:36.109626');
INSERT INTO `django_migrations` VALUES ('18', 'app01', '0005_user_hobby', '2021-06-28 09:34:39.900625');
INSERT INTO `django_migrations` VALUES ('19', 'app01', '0006_auto_20210628_1736', '2021-06-28 09:36:43.247504');
INSERT INTO `django_migrations` VALUES ('20', 'app01', '0007_auto_20210628_1738', '2021-06-28 09:38:15.642279');
INSERT INTO `django_migrations` VALUES ('21', 'app02', '0001_initial', '2021-06-29 02:33:53.789318');
INSERT INTO `django_migrations` VALUES ('22', 'app03', '0001_initial', '2021-06-30 09:49:26.784787');
INSERT INTO `django_migrations` VALUES ('23', 'app03', '0002_auto_20210701_1505', '2021-07-01 07:05:16.952172');
INSERT INTO `django_migrations` VALUES ('24', 'app03', '0003_auto_20210701_1606', '2021-07-01 08:07:03.004009');
INSERT INTO `django_migrations` VALUES ('25', 'app03', '0004_auto_20210701_2350', '2021-07-01 15:50:59.952763');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for `userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('1', 'pzyo', '123');
INSERT INTO `userinfo` VALUES ('2', 'tom', '456');
INSERT INTO `userinfo` VALUES ('3', 'jerry', '666');
INSERT INTO `userinfo` VALUES ('4', 'oscar', '777');
