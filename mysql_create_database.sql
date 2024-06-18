-- create and use database
create database if not exists tire_shop;
use tire_shop;

-- Table: EmployeeorderNumber
-- Description: Stores information about each employee, including contact details
create table Employee (
	employee_id int primary key auto_increment,
    	first_name varchar(50) NOT NULL,
    	last_name varchar(50) NOT NULL,
    	city varchar(100),
    	phone_number varchar(30)
    );
 
-- Table: Customer
-- Description: Holds all relevant customer details, used for billing and customer management
create table Customer (
	customer_id int primary key auto_increment,
    	first_name varchar(50) NOT NULL,
    	last_name varchar(50) NOT NULL,
    	city varchar(100),
    	phone_number varchar(30)
    );
    
-- Table: Invoice    
-- Description: Tracks billing information linked to customers and the employees who done the task
create table Invoice ( 
	invoice_id int primary key auto_increment,
    	invoice_number varchar(100),
    	customer_id int,
    	employee_id int,
    	total_amount decimal(10,2),
    	foreign key (employee_id) references Employee(employee_id),
    	foreign key (customer_id) references Customer(customer_id)
    );
    
-- Table: Task
-- Description: Details specific tasks or services provided, linked to invoices and employees.
create table Task (
	task_id int primary key auto_increment,
    	task_name varchar(50),
    	task_description text,
    	employee_id int,
    	invoice_id int,
    	foreign key (employee_id) references Employee(employee_id),
    	foreign key (invoice_id) references Invoice(invoice_id)
    );

   
-- Table: Material
-- Description: Manages stock and usage of materials for tasks.
create table Material (
	material_id int primary key auto_increment, 
    	material_name varchar(100),
    	amount_in_stock int, 
    	task_id int,
    	foreign key (task_id) references Task(task_id)
    );
    