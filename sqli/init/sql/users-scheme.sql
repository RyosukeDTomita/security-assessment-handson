SET NAMES utf8mb4;
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS user_info;
CREATE SCHEMA user_info;
USE user_info;

CREATE TABLE users (
  id INTEGER NOT NULL,
  user_id VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at DATETIME NOT NULL,
  update_at DATETIME NOT NULL,
  PRIMARY KEY (id)
);
