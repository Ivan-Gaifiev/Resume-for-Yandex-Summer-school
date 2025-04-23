-- drop table if exists ship cascade;
-- drop table if exists loading cascade;
-- drop table if exists loading_place cascade;
-- drop table if exists cargo cascade;

-- -- TABLES INITIALIZATION
-- create table ship
-- (
-- 	id integer primary key check(id > 0),
-- 	name varchar(50) not null,
-- 	home_port varchar(50) not null,
-- 	benefit decimal(5,2) check (benefit >= 0 and benefit <= 100) not null
-- );

-- create table loading_place
-- (
-- 	id integer primary key check(id > 0),
-- 	berth varchar(50) not null,
-- 	port varchar(50) not null,
-- 	loading_fee decimal(5,2) check (loading_fee >= 0 and loading_fee <= 100) not null
-- );

-- create table cargo
-- (
-- 	id integer primary key check(id > 0),
-- 	name varchar(50) not null,
-- 	storage_port varchar(50) not null,
-- 	price float check (price >= 0),
-- 	max_number integer check (max_number >= 0)
-- );

-- create table loading
-- (
-- 	statement_number integer primary key check(statement_number > 0),
-- 	date varchar(50) not null,
-- 	ship_id integer not null,
--  loading_place_id integer not null,
--  cargo_id integer not null,
-- 	number integer check(number >= 0) not null,
-- 	price float check (price >= 0) not null,
-- 	foreign key (ship_id) references ship(id) 
-- 		on update cascade on delete set null,
-- 	foreign key (loading_place_id) references loading_place(id) 
-- 		on update cascade on delete set null,
-- 	foreign key (cargo_id) references cargo(id) 
-- 		on update cascade on delete set null
-- );

-- -- FILLING TABLES WITH THE EXACT DATA
-- insert into ship (id, name, home_port, benefit)
-- values (001,'Балтимор',	'Одесса',3),
--  		(002,'Генуя',	'Одесса',	3),
--  		(003,'ТПР-123',	'Владивосток',	5),
--  		(004,'Ф. Шаляпин',	'Мурманск',	6),
--  		(005,'Рейн',	'Калининград',	4),
--  		(006,'Россия',	'Владивосток',	5);

-- insert into loading_place(id, berth, port, loading_fee)
-- values (001,	'Северный',	'Одесса',	3),
--  		(002,	'Южный',	'Одесса',	4),
--  		(003,	'N1',	'Владивосток',	2),
--  		(004,	'N2',	'Владивосток',	2),
--  		(005,	'N3',	'Владивосток',	2),
--  		(006,	'Основной',	'Калининград',	4);
 
-- insert into cargo(id, name, storage_port, price, max_number)
-- values (001,	'Рис',	'Одесса',	100000,	700),
--  		(002,	'Зерно',	'Одесса',	80000,	890),
--  		(003,	'Хлопок',	'Одесса',	300000,	400),
--  		(004,	'Сахар',	'Владивосток',	140000,	600),
--  		(005,	'Соль',	'Мурманск',	120000,	700),
--  		(006,	'Скобяные изделия',	'Калининград',	300000,	140),
--  		(007,	'Древесина',	'Мурманск',	400000,	260),
--  		(008,	'Уголь',	'Владивосток',	400000,	400);

-- insert into loading(statement_number, date, ship_id, loading_place_id, 
-- 	cargo_id, number, price)
-- values (70204,	'Понедельник',	001,	005,	002,	100,	8000000),
-- 		(70205,	'Понедельник',	003,	003,	006,	4,	1200000),
-- 		(70206,	'Вторник',	001,	005,	007,	2,	800000),
-- 		(70207,	'Вторник',	002,	005,	001,	20,	2000000),
-- 		(70208,	'Вторник',	005,	005,	002,	3,	240000),
-- 		(70209,	'Среда',	003,	003,	006,	4,	1200000),
-- 		(70210,	'Среда',	004,	001,	001,	70,	7000000),
-- 		(70211,	'Среда',	004,	002,	006,	1,	300000),
-- 		(70212,	'Среда',	004,	002,	001,	10,	1000000),
-- 		(70213,	'Четверг',	001,	006,	003,	20,	6000000),
-- 		(70214,	'Четверг',	003,	004,	002,	2,	16000),
-- 		(70215,	'Четверг',	004,	003,	004,	30,	4200000),
-- 		(70216,	'Суббота',	003,	002,	005,	10,	1200000),
-- 		(70217,	'Суббота',	002,	003,	008,	20,	8000000),
-- 		(70218,	'Суббота',	001,	001,	001,	20,	2000000),
-- 		(70219,	'Суббота',	005,	006,	004,	10,	1400000);

-- 1) Реализовать хранимую процедуру, возвращающую текстовую строку, 
-- содержащую информацию о судне (название, порт приписки, дата, место 
-- и стоимость последней погрузки). Обработать ситуацию, когда судно новое, 
-- и еще ни разу не грузилось.
-- Все примеры: судна нет по такому имени, судно уже грузилось, судно 
-- есть и оно не грузилось прежде

-- create or replace function infoAboutTheShip(my_ship_id int)
-- returns text as $$
-- declare
-- 	result_message text; -- text string with info about the ship
-- 	number_of_loadings int; -- how many times this ship has been loaded
-- 	last_load_id int; -- id of the last loading
-- 	ship_name varchar(30);
-- 	h_port varchar(30);
-- 	last_load_date varchar(30);
-- 	last_load_port varchar(30);
-- 	last_load_price int;
-- begin
-- 	select count(*) into number_of_loadings 
-- 		from loading join ship on ship.id = loading.ship_id where my_ship_id = ship.id;
-- 	select max(statement_number) into last_load_id -- id of the last loading the exact ship had
-- 		from loading where ship_id = my_ship_id;
		
-- 	if my_ship_id not in (select id from ship) then -- situation when ship with this id doesn't exist
-- 		raise notice 'Ship with this id doesnt exist!';
-- 		return 'Ship not found';
-- 	end if;
	
-- 	if my_ship_id in (select id from ship) and number_of_loadings = 0 then -- this ship is new and hasn't been loaded before 
-- 		select name, home_port into ship_name, h_port
-- 		from ship where id = my_ship_id;
-- 		result_message = ship_name || ', ' || h_port || '. This ship hasnt been loaded before.';
-- 	else 
-- 		select name, home_port into ship_name, h_port
-- 		from ship where id = my_ship_id;
-- 		select loading.date, loading_place.port, loading.price
-- 		into last_load_date, last_load_port, last_load_price
-- 		from loading join loading_place on loading_place_id = loading_place.id
-- 		where loading.statement_number = last_load_id;
-- 		result_message = ship_name || ', ' || h_port || ', ' || last_load_date || ', '
-- 		|| last_load_port ||  ', ' || last_load_price;
-- 	end if;
-- 	return result_message;
-- end;
-- $$ language plpgsql;
-- -- example of the function usage
-- select infoAboutTheShip(3);



-- 2) Добавить таблицу, содержащую списки возможных грузов для каждого места погрузки. 
-- При вводе погрузки проверять, может ли присутствовать данный груз в указанном месте погрузки.
-- триггер на инсёрт

-- create table possible_cargo as  -- this table contains info about the place where various cargos are located
-- select loading_place_id, cargo_id from loading
-- select * from possible_cargo order by loading_place_id;

-- create or replace function exactCargoInLoadingPlaceAvailability()
-- returns trigger as $$
-- declare
-- 	text_mes text;
-- begin
-- 	-- check if inputed parameters are correct
-- 	if new.loading_place_id in (select p_c.loading_place_id from possible_cargo as p_c) and new.cargo_id in (select p_c.cargo_id from possible_cargo as p_c) then
-- 		-- check if this exact cargo is already in this exact loading place
-- 		if exists (select 1 from possible_cargo where new.loading_place_id = loading_place_id and new.cargo_id = cargo_id) then
-- 			raise notice 'This cargo is already in the loading place';
-- 			return new;
-- 		else
-- 			raise notice 'This cargo is not in the loading place yet';
-- 			return new;
-- 		end if;
-- 	else
-- 		text_mes = 'Cargo or loading_place with these id dont exist';
-- 		raise exception '%',text_mes;-- неправильный ввод этих двух параметров
-- 	end if;
-- end;
-- $$ language plpgsql;

-- create or replace trigger cargoAvailabilityTrigger
-- before insert or update on loading
-- for each row execute function exactCargoInLoadingPlaceAvailability();
-- -- check if the trigger works and provides as the information on cargo availability 
-- insert into loading (statement_number, date, ship_id, loading_place_id, cargo_id, number, price)
-- values (1, 'Вторник', 001, 004, 002, 124, 3900000);


-- 3) Реализовать триггер такой, что при вводе строки в таблице погрузок, 
-- если сумма не указана, то она вычисляется 

-- create or replace function countingSumIfNecessary()
-- returns trigger as $$
-- declare
-- 	loading_sum bigint;
-- begin
-- 	loading_sum = new.number * (select cargo.price from cargo where cargo.id = new.cargo_id);
-- 	if new.price is null then
-- 		new.price = loading_sum;
-- 		return new;
-- 	else
-- 		return new;
-- 	end if;
-- end;
-- $$ language plpgsql;

-- create or replace trigger countingSumTrigger
-- before insert or update on loading
-- for each row execute function countingSumIfNecessary();
-- -- check if the trigger works and provides as the information on cargo availability 
-- insert into loading (statement_number, date, ship_id, loading_place_id, cargo_id, number)
-- values (1, 'Вторник', 001, 004, 002, 124)
-- insert into loading (statement_number, date, ship_id, loading_place_id, cargo_id, number, price)
-- values (2, 'Вторник', 001, 004, 002, 124, 2352353);



-- 4) Создать представление (view), содержащее поля: номер ведомости, дата, название судна, 
-- льгота, название груза, количество, стоимость. Обеспечить возможность изменения 
-- редоставленной льготы. При этом должна быть пересчитана стоимость.

-- create view infoAboutLoading(num_statement, date, ship_name, ship_benefit, cargo_name, cargo_num, price) as
-- (select loading.statement_number, loading.date, ship.name, ship.benefit, cargo.name, loading.number, loading.price
-- from loading join ship on ship.id = loading.ship_id join cargo on cargo.id = loading.cargo_id)

create or replace function changeBenefitAndRecountprice ()
returns trigger as $$
declare

begin
	if new.benefit is null or new.benefit < 0 or new.benefit > 100 then
		raise exception 'Value of benefit must be between 1 and 100';	
	else
		update loading
		set price = (1 - new.benefit * 0.01) * price 
		from ship
		where ship_id = new.id;
		return new;
	end if;
end;
$$ language plpgsql;

create or replace trigger changeBenefitTrigger
before update on ship
for each row execute function changeBenefitAndRecountprice ();

update ship
set benefit = 5
where ship.id = 2;

select * from infoAboutLoading;
