create table customers(
    id int not null,
    name varchar(20) not null,
    age int not null,
    address varchar(100),
    salary decimal(18, 2),
    primary key(id)
);

insert into customers (id, name, age, address, salary) values (1, 'Ramesh', 35, 'Banashankari, Bangalore', '1500000.00');
insert into customers (id, name, age, address, salary) values (2, 'Rajesh', 36, 'Jayanagar, Bangalore', '1600000.00');
insert into customers (id, name, age, address, salary) values (3, 'Anil', 37, 'Malleshwaram, Bangalore', '1700000.00');
insert into customers (id, name, age, address, salary) values (4, 'Amitha', 38, 'Rajajinagar, Bangalore', '1800000.00');
insert into customers (id, name, age, address, salary) values (5, 'Smitha', 25, 'Basavanagudi, Bangalore', '1000000.00');
insert into customers (id, name, age, address, salary) values (6, 'John', 27, 'J P Nagar, Bangalore', 1200000.00);

select * from customers;
select name, age, address from customers;
select * from customers where salary > 1500000;
select name, age, address from customers where salary > 1500000;
select * from customers where salary > 1500000 and id < 5;
select * from customers where salary > 1500000 or age < 30;

update customers set salary = 1750000 where name = 'Anil';
update customers set name = 'Ramesh Kumar', address = 'Vijaynagar, Bangalore' where id = 1;

delete from customers where id = 4;

drop table customers;
