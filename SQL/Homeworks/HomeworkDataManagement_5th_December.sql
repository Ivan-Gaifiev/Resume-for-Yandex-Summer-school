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
-- 1) Blitz-task #2

with TotalGoods as (select count(*) as total_count from Good),
ShopGoodsCount as (select gs.id_shop, count(distinct gs.id_good) as goods_count
from Good_Shop gs group by gs.id_shop)
select s.id, s.name from ShopGoodsCount sgc
join TotalGoods tg on 1=1
join Shop s on s.id = sgc.id_shop
where sgc.goods_count > tg.total_count / 2;

select s.id, s.name from Shop s
join Good_Shop gs on s.id = gs.id_shop
group by s.id, s.name
having count(distinct gs.id_good) > (select count(*) / 2 from Good);

-- 2) Home assignment #1

select s.id as shop_id, s.name as shop_name, gc.name as category_name
from Shop s join Good_Shop gs on s.id = gs.id_shop
join Good g on gs.id_good = g.id
join GoodCategory gc on g.id_goodCategory = gc.id
group by s.id, s.name, gc.name having count(gs.id_good) = (
select min(count) from (
select gs.id_shop, g.id_goodCategory, count(*) as count
from Good_Shop gs join Good g on gs.id_good = g.id
group by gs.id_shop, g.id_goodCategory) sub
where sub.id_shop = s.id);

select disctinct on (s.id) s.id as shop_id, s.name as shop_name, gc.name as category_name, 
count(gs.id_good) as goods_count
from Shop s join Good_Shop gs on s.id = gs.id_shop
join Good g on gs.id_good = g.id
join GoodCategory gc on g.id_goodCategory = gc.id
group by s.id, s.name, gc.name
order by s.id, goods_count asc;

-- 3) Home assignment #2

select w.id, w.address from Warehouse w
join Good_Warehouse gw on w.id = gw.id_warehouse
group by w.id, w.address
having sum(gw.count) < (select sum(count) / 2 from Good_Warehouse);

select id, address, total_count from (
select w.id, w.address, sum(gw.count) as total_count, 
sum(sum(gw.count)) over () as total_warehouse_count
from Warehouse w join Good_Warehouse gw on w.id = gw.id_warehouse
group by w.id, w.address) sub
where total_count < total_warehouse_count / 2;






