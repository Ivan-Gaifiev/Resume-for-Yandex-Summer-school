-- initializing our tables

create table Good (
id int primary key,
name varchar(20) not null,
productionDate Date,
price int not null,
weight float not null,
id_goodCategory int
);

alter table Good
alter column id type int;

insert into Good (id,name, productionDate, price, weight, id_goodCategory)
values (1,'Apple iPhone 14', '01-09-2022', 140000, 0.7,1),
(2,'Phone case 6.5', '01-09-2022', 1000, 0.1,3),
(3,'Computer table','02-06-2022', 4500, 14.7,2);

create table GoodCategory (
id serial primary key,
name text,
ageMin int);

insert into GoodCategory (name,ageMin)
values ('Electronics',16),
('Furniture',16),
('Acessories',null);

alter table Good
add constraint id_goodCategory foreign key (id_goodCategory) 
references Goodcategory(id)
on update cascade 
on delete set null;

create table Shop (
id serial primary key check (id>0),
name text,
address text);

insert into Shop (name, address)
values ('MVideo', 'Gorkogo st., 165'),
('Eldorado','Timiryazeva st., 22');

create table Good_Shop (
id_good int 
references Good(id)
on update cascade
on delete cascade, 
id_shop int 
references Shop(id)
on update cascade
on delete set null, 
count int);

insert into Good_shop (id_good, id_shop, count)
values (1,1,3),(1,2,1),(2,1,10),(2,2,4),(3,1,2);

create table Warehouse (
id serial primary key check (id>0),
address text);

insert into Warehouse (address)
values ('Gorkogo st., 165'),
('Timiryazeva st., 22');

create table Good_Warehouse (
id_good int references Good(id)
on update cascade
on delete cascade,
id_warehouse int references Warehouse(id)
on update cascade
on delete cascade,
count int
);

insert into Good_Warehouse (id_good, id_warehouse, count)
values (1,1,5),(2,1,6),(3,2,2);



-- Completing given home assignments:
-- 1) Blitz-task #1
select Good.id, Good.name, count(distinct Good_Warehouse.id_warehouse) as warehouse_count, 
sum(Good_Warehouse.count) as total_quantity from Good join 
Good_Warehouse on Good.id = Good_Warehouse.id_good group by Good.id, Good.name;

-- 2) Blitz-task #2
select Shop.id as shop_id, Shop.name as shop_name, 
count(distinct Good.id_goodcategory) as unique_category_count
from Shop join Good_Shop on Shop.id = Good_Shop.id_shop
join Good on Good_Shop.id_good = Good.id group by Shop.id, Shop.name;

-- 3) Hometask #1: display the id and name of the products that are presented in stores in the smallest quantity
select Good.id, Good.name from Good
join Good_Shop on Good.id = Good_Shop.id_good group by Good.id, Good.name
having sum(Good_Shop.count) = (select min(total_count) from 
(select sum(Good_Shop.count) as total_count from Good_Shop
group by Good_Shop.id_good) as counts);


