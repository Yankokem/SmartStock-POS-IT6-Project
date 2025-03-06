-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2025 at 04:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartstock_inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `adjustments`
--

CREATE TABLE `adjustments` (
  `AdjustmentID` int(11) NOT NULL,
  `AdminID` int(11) DEFAULT NULL,
  `Reason` text NOT NULL,
  `AdjustmentDate` datetime NOT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `adjustment_details`
--

CREATE TABLE `adjustment_details` (
  `AdjustmentDetailID` int(11) NOT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `AdjustmentID` int(11) DEFAULT NULL,
  `AdjustmentType` varchar(50) NOT NULL,
  `QuantityAdjusted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `CategoryID` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Description` text DEFAULT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

-- INSERT INTO `categories` (`CategoryID`, `Name`, `Description`, `Created_At`, `Created_By`, `Updated_At`, `Updated_By`) VALUES
-- (1, 'CPU', 'Central Processing Unit', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1),
-- (2, 'Memory', 'RAM and other memory components', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1),
-- (3, 'Storage', 'Hard drives, SSDs, and other storage devices', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1),
-- (4, 'Motherboard', 'Main circuit board of the computer', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1),
-- (5, 'Power Supply', 'Power supply units for computers', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1),
-- (6, 'Peripherals', 'Keyboards, mice, monitors, and other peripherals', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1),
-- (7, 'Chassis', 'Computer cases and chassis', '2025-03-05 22:09:52', 1, '2025-03-05 22:09:52', 1);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `CustomerID` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` text NOT NULL,
  `PhoneNumber` varchar(255) NOT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `EmployeeID` int(11) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Role` char(15) NOT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) DEFAULT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`EmployeeID`, `FirstName`, `LastName`, `Username`, `Password`, `Role`, `Created_At`, `Created_By`, `Updated_At`, `Updated_By`) VALUES
(1, 'Junits', 'Coretico', 'junitsstore_admin', '$2y$10$WfGbACvKiCJM40LAMkFAf.AYENhhGddZSszrlFeIYGJjF8MdbMc3S', 'admin', '2025-03-01 15:01:46', NULL, '2025-03-01 16:51:17', 1),
(2, 'Jeriel', 'Sanao', 'jerielsanao1', '$2y$10$gNysNXP63PW21vIkuqMjJufdCDApTJDs2BsIpJ6uOo8lb3sPxSASG', 'Employee', '2025-03-01 15:46:32', 1, '2025-03-01 15:46:32', 1),
(3, 'Russel', 'Labiaga', 'russelito1', '$2y$10$lIpDauqYu1cmpxxkehhxiOuxtmj269dcygSV4TW2omlbEiAPG6i5O', 'Employee', '2025-03-01 16:03:13', 1, '2025-03-01 16:03:13', 1),
(4, 'Jeriel', 'Sanao', 'jerielsanao27', '$2y$10$Cn0TZh6.wg9Gnwas.gCQcO6CUz4VpfyNox/dT8V2t/VRCsl9w7.0.', 'Employee', '2025-03-01 16:39:57', 1, '2025-03-01 16:56:23', 4);

-- --------------------------------------------------------

--
-- Table structure for table `orderline`
--

CREATE TABLE `orderline` (
  `OrderLineID` int(11) NOT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `OrderID` int(11) DEFAULT NULL,
  `Quantity` int(11) NOT NULL,
  `Price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `OrderID` int(11) NOT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  `Date` datetime NOT NULL,
  `Total` decimal(10,2) NOT NULL,
  `Status` char(5) NOT NULL,
  `Delivery` int(11) NOT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `ProductID` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Description` text DEFAULT NULL,
  `CategoryID` int(11) DEFAULT NULL,
  `Price` decimal(10,2) NOT NULL,
  `StockQuantity` int(11) NOT NULL,
  `Status` enum('In Stock','Out of Stock') NOT NULL DEFAULT 'In Stock',
  `SupplierID` int(11) NOT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

-- INSERT INTO `products` (`ProductID`, `Name`, `Description`, `CategoryID`, `Price`, `StockQuantity`, `Status`, `SupplierID`, `Created_At`, `Created_By`, `Updated_At`, `Updated_By`) VALUES
-- (12, 'AMD Ryzen 9 5900X', 'AMD Ryzen 9 12-Core Processor', 1, 549.99, 30, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (13, 'Corsair Vengeance LPX 16GB', '16GB DDR4 3200MHz Memory Kit', 2, 79.99, 100, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (14, 'G.Skill Trident Z RGB 32GB', '32GB DDR4 3600MHz Memory Kit', 2, 159.99, 50, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (15, 'Samsung 970 EVO Plus 1TB', '1TB NVMe M.2 SSD', 3, 129.99, 75, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (16, 'Western Digital Blue 2TB', '2TB SATA III HDD', 3, 59.99, 120, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (17, 'ASUS ROG Strix Z690-E', 'Intel Z690 ATX Motherboard', 4, 399.99, 25, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (18, 'MSI MAG B550 Tomahawk', 'AMD B550 ATX Motherboard', 4, 179.99, 40, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (19, 'Corsair RM850x', '850W 80+ Gold Fully Modular PSU', 5, 129.99, 60, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (20, 'EVGA SuperNOVA 750 G5', '750W 80+ Gold Fully Modular PSU', 5, 109.99, 45, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (21, 'Logitech G Pro X Keyboard', 'Mechanical Gaming Keyboard', 6, 149.99, 80, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (22, 'Razer DeathAdder V2', 'Gaming Mouse with Optical Sensor', 6, 69.99, 150, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (23, 'NZXT H510', 'Compact ATX Mid-Tower Case', 7, 89.99, 90, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (24, 'Lian Li PC-O11 Dynamic', 'ATX Mid-Tower Case with Tempered Glass', 7, 149.99, 50, 'In Stock', 2, '2025-03-05 22:12:49', 1, '2025-03-05 22:12:49', 1),
-- (25, 'Intel Core i7-12700K', '12th Gen Intel Core i7 Processor', 1, 399.99, 50, 'In Stock', 2, '2025-03-05 22:24:42', 1, '2025-03-05 22:24:42', 1);

-- -- --------------------------------------------------------

--
-- Table structure for table `receiving`
--

CREATE TABLE `receiving` (
  `ReceivingID` int(11) NOT NULL,
  `SupplierID` int(11) DEFAULT NULL,
  `Date` datetime NOT NULL,
  `Status` varchar(20) DEFAULT 'Pending',
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `receiving_details`
--

CREATE TABLE `receiving_details` (
  `ReceivingDetailID` int(11) NOT NULL,
  `ReceivingID` int(11) DEFAULT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `Quantity` int(11) NOT NULL,
  `UnitCost` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `returns`
--

CREATE TABLE `returns` (
  `ReturnID` int(11) NOT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  `OrderID` int(11) DEFAULT NULL,
  `ReturnDate` datetime NOT NULL,
  `Reason` text DEFAULT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `returntosupplier`
--

CREATE TABLE `returntosupplier` (
  `ReturnSupplierID` int(11) NOT NULL,
  `SupplierID` int(11) DEFAULT NULL,
  `ReturnDate` datetime NOT NULL,
  `Reason` text NOT NULL,
  `Status` int(11) NOT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `returntosupplierdetails`
--

CREATE TABLE `returntosupplierdetails` (
  `ReturnSupplierDetailID` int(11) NOT NULL,
  `ReturnSupplierID` int(11) DEFAULT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `QuantityReturned` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `return_details`
--

CREATE TABLE `return_details` (
  `ReturnDetailID` int(11) NOT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `ReturnID` int(11) DEFAULT NULL,
  `QuantityReturned` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `SupplierID` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` text NOT NULL,
  `PhoneNumber` varchar(255) NOT NULL,
  `ProfileImage` varchar(255) DEFAULT NULL,
  `Created_At` datetime NOT NULL DEFAULT current_timestamp(),
  `Created_By` int(11) NOT NULL,
  `Updated_At` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Updated_By` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`SupplierID`, `Name`, `Address`, `PhoneNumber`, `ProfileImage`, `Created_At`, `Created_By`, `Updated_At`, `Updated_By`) VALUES
(2, 'Supplier2', 'supplier2, address', '0912345689', NULL, '2025-03-03 14:29:33', 1, '2025-03-03 14:29:33', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adjustments`
--
ALTER TABLE `adjustments`
  ADD PRIMARY KEY (`AdjustmentID`),
  ADD KEY `AdminID` (`AdminID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `adjustment_details`
--
ALTER TABLE `adjustment_details`
  ADD PRIMARY KEY (`AdjustmentDetailID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `AdjustmentID` (`AdjustmentID`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`CategoryID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CustomerID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`EmployeeID`),
  ADD KEY `employees_ibfk_1` (`Created_By`),
  ADD KEY `employees_ibfk_2` (`Updated_By`);

--
-- Indexes for table `orderline`
--
ALTER TABLE `orderline`
  ADD PRIMARY KEY (`OrderLineID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `OrderID` (`OrderID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `CustomerID` (`CustomerID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ProductID`),
  ADD KEY `CategoryID` (`CategoryID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `receiving`
--
ALTER TABLE `receiving`
  ADD PRIMARY KEY (`ReceivingID`),
  ADD KEY `SupplierID` (`SupplierID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `receiving_details`
--
ALTER TABLE `receiving_details`
  ADD PRIMARY KEY (`ReceivingDetailID`),
  ADD KEY `ReceivingID` (`ReceivingID`),
  ADD KEY `ProductID` (`ProductID`);

--
-- Indexes for table `returns`
--
ALTER TABLE `returns`
  ADD PRIMARY KEY (`ReturnID`),
  ADD KEY `CustomerID` (`CustomerID`),
  ADD KEY `OrderID` (`OrderID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `returntosupplier`
--
ALTER TABLE `returntosupplier`
  ADD PRIMARY KEY (`ReturnSupplierID`),
  ADD KEY `SupplierID` (`SupplierID`),
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- Indexes for table `returntosupplierdetails`
--
ALTER TABLE `returntosupplierdetails`
  ADD PRIMARY KEY (`ReturnSupplierDetailID`),
  ADD KEY `ReturnSupplierID` (`ReturnSupplierID`),
  ADD KEY `ProductID` (`ProductID`);

--
-- Indexes for table `return_details`
--
ALTER TABLE `return_details`
  ADD PRIMARY KEY (`ReturnDetailID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `ReturnID` (`ReturnID`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`SupplierID`),
  ADD UNIQUE KEY `Name` (`Name`),
  ADD UNIQUE KEY `PhoneNumber` (`PhoneNumber`),
  ADD UNIQUE KEY `Address` (`Address`) USING HASH,
  ADD KEY `Created_By` (`Created_By`),
  ADD KEY `Updated_By` (`Updated_By`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adjustments`
--
ALTER TABLE `adjustments`
  MODIFY `AdjustmentID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `adjustment_details`
--
ALTER TABLE `adjustment_details`
  MODIFY `AdjustmentDetailID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `CategoryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `CustomerID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `EmployeeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orderline`
--
ALTER TABLE `orderline`
  MODIFY `OrderLineID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `OrderID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `receiving`
--
ALTER TABLE `receiving`
  MODIFY `ReceivingID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `receiving_details`
--
ALTER TABLE `receiving_details`
  MODIFY `ReceivingDetailID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `returns`
--
ALTER TABLE `returns`
  MODIFY `ReturnID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `returntosupplier`
--
ALTER TABLE `returntosupplier`
  MODIFY `ReturnSupplierID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `returntosupplierdetails`
--
ALTER TABLE `returntosupplierdetails`
  MODIFY `ReturnSupplierDetailID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `return_details`
--
ALTER TABLE `return_details`
  MODIFY `ReturnDetailID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `SupplierID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`Created_By`) REFERENCES `employees` (`EmployeeID`) ON DELETE SET NULL,
  ADD CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`Updated_By`) REFERENCES `employees` (`EmployeeID`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
