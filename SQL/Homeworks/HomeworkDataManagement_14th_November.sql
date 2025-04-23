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
-- 1) Name of the oldest category of products
select GoodCategory.name from Good
join GoodCategory on Good.id_goodCategory = GoodCategory.id
where Good.productionDate <= all (select productionDate from Good);

select distinct GoodCategory.name from GoodCategory 
where exists (
  select 1 from Good 
  where Good.id_goodCategory = GoodCategory.id 
  and Good.productionDate = (select min(productionDate) from Good)
);

select GoodCategory.name from Good 
join GoodCategory on Good.id_goodCategory = GoodCategory.id 
where Good.productionDate = (select min(productionDate) from Good);

select GoodCategory.name from Good 
join GoodCategory on Good.id_goodCategory = GoodCategory.id 
where Good.productionDate = any (select min(productionDate) from Good);


-- 2) id and name of the products that  is out of stock (not in shops and not in warehouses)
select distinct GoodCategory.id, GoodCategory.name
from GoodCategory where GoodCategory.id not in (
select Good.id_goodCategory from Good where Good.id = any (
select id_good from Good_Shop));

select Good.id, Good.name from Good 
where not exists (select 1 from Good_Shop where Good_Shop.id_good = Good.id) 
and not exists (select 1 from Good_Warehouse where Good_Warehouse.id_good = Good.id);

select Good.id, Good.name from Good 
where Good.id <> all (select id_good from Good_Shop) 
and Good.id <> all (select id_good from Good_Warehouse);

select Good.id, Good.name from Good 
where not exists (select 1 from Good_Shop where Good_Shop.id_good = Good.id) 
and not exists (select 1 from Good_Warehouse where Good_Warehouse.id_good = Good.id);

select Good.id, Good.name from Good 
left join Good_Shop on Good.id = Good_Shop.id_good 
left join Good_Warehouse on Good.id = Good_Warehouse.id_good 
where Good_Shop.id_good is null and Good_Warehouse.id_good is null;



-- 3) id and name of the category that isn't being sold anywhere:
select GoodCategory.id, GoodCategory.name from GoodCategory 
where GoodCategory.id not in (
  select Good.id_goodCategory from Good 
  join Good_Shop on Good.id = Good_Shop.id_good
);

select Good.id, Good.name 
from Good where Good.id = 
(select Good_Warehouse.id_good from Good_Warehouse 
where Good_Warehouse.count <= all (select count from Good_Warehouse)
);

select distinct GoodCategory.id, GoodCategory.name from GoodCategory 
left join Good on GoodCategory.id = Good.id_goodCategory 
left join Good_Shop on Good.id = Good_Shop.id_good 
where Good_Shop.id_good is null;

select GoodCategory.id, GoodCategory.name from GoodCategory 
where not exists (
  select 1 from Good 
  join Good_Shop on Good.id = Good_Shop.id_good 
  where Good.id_goodCategory = GoodCategory.id
);

select GoodCategory.id, GoodCategory.name from GoodCategory 
where GoodCategory.id = any (
  select id_goodCategory from Good 
  where Good.id not in (select id_good from Good_Shop)
);



