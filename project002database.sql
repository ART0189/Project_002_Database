/*
 Navicat Premium Data Transfer

 Source Server         : TestMySQLServer
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : project002database

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 04/09/2021 17:39:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for playerbasedata
-- ----------------------------
DROP TABLE IF EXISTS `playerbasedata`;
CREATE TABLE `playerbasedata`  (
  `PlayerBaseID` int(0) NOT NULL AUTO_INCREMENT,
  `PlayerBaseName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `_Password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Gender` enum('男','女','其他','未知') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `HeadPortrait` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Telephone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `_HaveLogin` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`PlayerBaseID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of playerbasedata
-- ----------------------------
INSERT INTO `playerbasedata` VALUES (1, 'ART0189', '123456', '未知', 'DefaultPath', 'Home', '18302318793', 0);
INSERT INTO `playerbasedata` VALUES (2, 'Aressions', '1919810', '未知', 'DefaultPath', 'Home', '114514', 0);
INSERT INTO `playerbasedata` VALUES (3, 'RegTest', 'XXXX', '未知', 'DefaultPath', 'Home', '183023', 0);

-- ----------------------------
-- Table structure for playerdata_project002
-- ----------------------------
DROP TABLE IF EXISTS `playerdata_project002`;
CREATE TABLE `playerdata_project002`  (
  `PlayerID` int(0) NOT NULL AUTO_INCREMENT,
  `PlayerName` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `HeadPortrait` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PlayerLv` int(0) NOT NULL,
  `PlayerExp` int(0) NOT NULL,
  `HaveLogin` tinyint(1) NOT NULL,
  `HardwareCode` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `SourceBaseAccount` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`PlayerID`) USING BTREE,
  INDEX `SourceBaseAccount`(`SourceBaseAccount`) USING BTREE,
  CONSTRAINT `playerdata_project002_ibfk_1` FOREIGN KEY (`SourceBaseAccount`) REFERENCES `playerbasedata` (`PlayerBaseID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of playerdata_project002
-- ----------------------------
INSERT INTO `playerdata_project002` VALUES (1, 'Ayanami', 'NeedInit', 0, 0, 0, 'UnInitedHardwareCode', 1);
INSERT INTO `playerdata_project002` VALUES (2, 'Aression', 'NeedInit', 0, 0, 0, 'UnInitedHardwareCode', 2);
INSERT INTO `playerdata_project002` VALUES (3, 'RegTest002', 'NeedInit', 0, 0, 0, 'NoHardware', 3);

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
