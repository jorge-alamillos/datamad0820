-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customer` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Customer_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone_number` INT NOT NULL,
  `Email` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State/Province` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Zip/Postal_Code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`, `Customer_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Salesperson` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Staff_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `ID` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`, `Staff_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoice` (
  `Invoice_number` INT NOT NULL AUTO_INCREMENT,
  `Date` DATE NOT NULL,
  `Customer_ID` INT NOT NULL,
  `Customer_Customer_ID` INT NOT NULL,
  `Salesperson_ID` INT NOT NULL,
  `Salesperson_Staff_ID` INT NOT NULL,
  PRIMARY KEY (`Invoice_number`, `Customer_ID`, `Customer_Customer_ID`),
  INDEX `fk_Invoice_Customer1_idx` (`Customer_ID` ASC, `Customer_Customer_ID` ASC) VISIBLE,
  INDEX `fk_Invoice_Salesperson1_idx` (`Salesperson_ID` ASC, `Salesperson_Staff_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Invoice_Customer1`
    FOREIGN KEY (`Customer_ID` , `Customer_Customer_ID`)
    REFERENCES `mydb`.`Customer` (`ID` , `Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_Salesperson1`
    FOREIGN KEY (`Salesperson_ID` , `Salesperson_Staff_ID`)
    REFERENCES `mydb`.`Salesperson` (`ID` , `Staff_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Car` (
  `VIN` INT NOT NULL AUTO_INCREMENT,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` INT(4) NOT NULL,
  `Colour` VARCHAR(45) NOT NULL,
  `Invoice_Invoice_number` INT NOT NULL,
  PRIMARY KEY (`VIN`, `Invoice_Invoice_number`),
  INDEX `fk_Car_Invoice_idx` (`Invoice_Invoice_number` ASC) VISIBLE,
  CONSTRAINT `fk_Car_Invoice`
    FOREIGN KEY (`Invoice_Invoice_number`)
    REFERENCES `mydb`.`Invoice` (`Invoice_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
