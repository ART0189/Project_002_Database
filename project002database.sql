/*
 Navicat Premium Data Transfer

 Source Server         : Project002DataBaseServer
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : project002database

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 13/09/2021 21:04:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for basebanned_hardwarecode
-- ----------------------------
DROP TABLE IF EXISTS `basebanned_hardwarecode`;
CREATE TABLE `basebanned_hardwarecode`  (
  `BanID` int(0) NOT NULL AUTO_INCREMENT,
  `HardwareCodeBanned` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`BanID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of basebanned_hardwarecode
-- ----------------------------

-- ----------------------------
-- Table structure for basebanned_telephone
-- ----------------------------
DROP TABLE IF EXISTS `basebanned_telephone`;
CREATE TABLE `basebanned_telephone`  (
  `BanID` int(0) NOT NULL AUTO_INCREMENT,
  `TelephoneBanned` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`BanID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of basebanned_telephone
-- ----------------------------

-- ----------------------------
-- Table structure for playerbasedata
-- ----------------------------
DROP TABLE IF EXISTS `playerbasedata`;
CREATE TABLE `playerbasedata`  (
  `PlayerBaseID` int(0) NOT NULL AUTO_INCREMENT,
  `PlayerBaseName` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `_Password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Gender` enum('男','女','其他','未知') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `HeadPortrait` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Telephone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `BanStatus` tinyint(1) NOT NULL,
  `HardwareCode` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `_HaveLogin` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`PlayerBaseID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of playerbasedata
-- ----------------------------
INSERT INTO `playerbasedata` VALUES (1, 'Nagato52405', '123456', '未知', 'DefaultPath', 'Home', '13556129449', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (2, 'Mainz54317', '123456', '未知', 'DefaultPath', 'Home', '17800794347', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (3, 'Noshiro86569', '123456', '未知', 'DefaultPath', 'Home', '13159618970', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (4, 'ATRI7493', '123456', '未知', 'DefaultPath', 'Home', '18459954383', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (5, 'Ingraham6602', '123456', '未知', 'DefaultPath', 'Home', '18009924292', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (6, 'ATRI83813', '123456', '未知', 'DefaultPath', 'Home', '17276385585', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (7, 'Swiftsure16098', '123456', '未知', 'DefaultPath', 'Home', '18371774836', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (8, 'Alabama14083', '123456', '未知', 'DefaultPath', 'Home', '13762384990', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (9, 'Tashkent30833', '123456', '未知', 'DefaultPath', 'Home', '15131660587', 0, 'UnInitedHardwareCode', 0);
INSERT INTO `playerbasedata` VALUES (10, 'Poi24819', '123456', '未知', 'DefaultPath', 'Home', '15874419888', 0, 'UnInitedHardwareCode', 0);

-- ----------------------------
-- Table structure for playerdata_project002
-- ----------------------------
DROP TABLE IF EXISTS `playerdata_project002`;
CREATE TABLE `playerdata_project002`  (
  `PlayerID` int(0) NOT NULL AUTO_INCREMENT,
  `PlayerName` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `HeadPortrait` int(0) NOT NULL,
  `PlayerLv` int(0) NOT NULL,
  `PlayerExp` int(0) NOT NULL,
  `PlayerRank` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PlayerToken` int(0) NOT NULL,
  `PlayerToken_1` int(0) NOT NULL,
  `PlayerDefaultOOBName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `HaveLogin` tinyint(1) NOT NULL,
  `FriendsList` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `SourceBaseAccount` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`PlayerID`) USING BTREE,
  INDEX `SourceBaseAccount`(`SourceBaseAccount`) USING BTREE,
  CONSTRAINT `playerdata_project002_ibfk_1` FOREIGN KEY (`SourceBaseAccount`) REFERENCES `playerbasedata` (`PlayerBaseID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of playerdata_project002
-- ----------------------------
INSERT INTO `playerdata_project002` VALUES (1, 'Ingraham', 0, 37, 595, NULL, 10959, 40427235, NULL, 0, '0,5,9,7,', 1);
INSERT INTO `playerdata_project002` VALUES (2, 'Columbia', 5, 14, 393, NULL, 47678, 1465632, NULL, 0, '8,', 2);
INSERT INTO `playerdata_project002` VALUES (3, 'Alabama', 0, 12, 224, NULL, 30458, 25358623, NULL, 0, '9,', 3);
INSERT INTO `playerdata_project002` VALUES (4, 'Poi', 5, 15, 433, NULL, 42628, 8029560, NULL, 0, '8,0,9,5,7,3,', 4);
INSERT INTO `playerdata_project002` VALUES (5, 'Tashkent', 0, 10, 302, NULL, 11379, 53848890, NULL, 0, '', 5);
INSERT INTO `playerdata_project002` VALUES (6, 'Noshiro', 3, 27, 653, NULL, 30539, 65584694, NULL, 0, '1,4,5,8,', 6);
INSERT INTO `playerdata_project002` VALUES (7, 'Nagato', 0, 16, 285, NULL, 41094, 47405282, NULL, 0, '9,1,6,0,4,', 7);
INSERT INTO `playerdata_project002` VALUES (8, 'Shimakaze', 1, 3, 159, NULL, 30527, 4052024, NULL, 0, '8,5,0,', 8);
INSERT INTO `playerdata_project002` VALUES (9, 'Laffey', 4, 6, 166, NULL, 16171, 81409804, NULL, 0, '8,1,9,2,', 9);
INSERT INTO `playerdata_project002` VALUES (10, 'ART', 0, 19, 84, NULL, 32130, 68203258, NULL, 0, '6,9,7,5,4,', 10);

-- ----------------------------
-- Table structure for playerdata_project004
-- ----------------------------
DROP TABLE IF EXISTS `playerdata_project004`;
CREATE TABLE `playerdata_project004`  (
  `PlayerID` int(0) NOT NULL AUTO_INCREMENT,
  `PlayerName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `HaveLogin` tinyint(1) NOT NULL,
  `HardwareCode` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `SourceBaseAccount` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`PlayerID`) USING BTREE,
  INDEX `SourceBaseAccount`(`SourceBaseAccount`) USING BTREE,
  CONSTRAINT `playerdata_project004_ibfk_1` FOREIGN KEY (`SourceBaseAccount`) REFERENCES `playerbasedata` (`PlayerBaseID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of playerdata_project004
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
