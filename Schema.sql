CREATE TABLE employees (
 employee_id INT PRIMARY KEY,
 first_name VARCHAR(50) NOT NULL,
 last_name VARCHAR(50) NOT NULL,
 email VARCHAR(100) UNIQUE,
 hire_date DATE NOT NULL,
 job_role VARCHAR(50) NOT NULL,
 salary DECIMAL(10, 2)
);
