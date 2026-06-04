-- Create Database
CREATE DATABASE IF NOT EXISTS aegisai_db;

-- Use Database
USE aegisai_db;

-- Table 1: system_metrics
CREATE TABLE IF NOT EXISTS system_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    cpu_usage FLOAT NOT NULL,
    memory_usage FLOAT NOT NULL,
    disk_usage FLOAT NOT NULL,
    network_sent BIGINT NOT NULL,
    network_received BIGINT NOT NULL,
    process_count INT NOT NULL
);

-- Table 2: process_metrics
CREATE TABLE IF NOT EXISTS process_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    process_id INT NOT NULL,
    process_name VARCHAR(255) NOT NULL,
    process_cpu_usage FLOAT NOT NULL,
    process_memory_usage FLOAT NOT NULL,
    execution_path TEXT,
    parent_process VARCHAR(255)
);