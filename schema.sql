CREATE DATABASE permit_tracker;

CREATE TABLE permits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    permit_type VARCHAR(50) NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'submitted',
    submitted_date DATE NOT NULL,
    approval_date DATE,
    expiration_date DATE,
    inspector_notes TEXT
);