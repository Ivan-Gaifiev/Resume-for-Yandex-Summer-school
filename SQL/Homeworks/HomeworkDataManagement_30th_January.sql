-- 1) Реализовать хранимую функцию/процедуру, возвращающую общее количество остатков 
-- заданного наименования товара в магазинах и на складах.
create or replace function getTotalNumberOfRemaindersInShopsAndWarehouses(good_name varchar)
returns int as $$
declare 
numberOfRemainders int; --total number
numInShops int; --number of remainders in shops
numInWarehouses int; --number of remainders in warehouses
begin
-- count numInShops
select sum(gs.count) into numInShops from Good_Shop gs join Good g
on gs.id_good = g.id where g.name = good_name;
-- count numInWarehouses
select sum(gw.count) into numInWarehouses from Good_Warehouse gw join Good g
on gw.id_good = g.id where g.name = good_name;
-- sum of numInShops and numInWarehouses
numberOfRemainders := numInShops + numInWarehouses;
return numberOfRemainders;
end;
$$ language plpgsql;
-- example of the function usage
SELECT getTotalNumberOfRemaindersInShopsAndWarehouses('Phone case 6.5');


-- 2) Реализовать хранимую функцию/процедуру, которая по наименованию 
-- товара и возрасту покупателя выводит сообщение о возможности приобретения
-- данного товара данным покупателем.
create or replace function agePermissionToBuyTheExactProduct(customer_age int, product_name varchar)
returns boolean as $$
declare
res boolean; -- wheather it allowed or not
begin
select customer_age>=gc.ageMin into res from GoodCategory gc join Good g
on gc.id = g.id_goodCategory where g.name = product_name limit 1;
if res is null then res := true; -- if ageMin is null, it means that there is no age limit
end if;
if res = true then
raise notice 'You are allowed to buy this product. Congratulations!'; -- notes appear in Messages block
else raise notice 'Unfortunately, you are not allowed to buy this product(';
end if;
return res;
end;
$$ language plpgsql;
-- example of the function usage
SELECT agePermissionToBuyTheExactProduct(16, 'Apple iPhone 14');


-- 3) Реализовать хранимую функцию/процедуру, которая оценивает возможность 
-- покупки заданного количества товара в магазине (название магазина и товара 
-- задаются пользователем). При этом необходимо также проверить возрастные 
-- ограничения покупателя (используя функцию из п.2).
create or replace function checkingTheOpportunityToBuyProductsWithConditions(
shop_name varchar, good_name varchar, num_goods int, customer_age int)
returns boolean as $$
declare 
res boolean; -- final answer (true - it is possible to buy, false - not possible)
enough_num_goods boolean; -- chechking the number of goods available to buy in shops
enough_age boolean; -- checks age permission by using function from 2nd task
begin
select gs.count>=num_goods into enough_num_goods from Good_Shop gs join 
Good g on gs.id_good = g.id join Shop s on gs.id_shop = s.id
where g.name = good_name and s.name = shop_name;
select agePermissionToBuyTheExactProduct(customer_age, good_name) = true into enough_age;
select enough_num_goods and enough_age into res; -- both conditions must be completed
return res;
end;
$$ language plpgsql;
-- example of the function usage
SELECT checkingTheOpportunityToBuyProductsWithConditions('Eldorado', 'Apple iPhone 14', 1, 16);


--1st task using satic cursors)
create or replace function getTotalNumberOfRemaindersInShopsAndWarehouses(good_name varchar)
returns int as $$
declare
-- initializing coursor for shops
curs_shop cursor for select gs.count from good_shop gs join good g on gs.id_good = g.id
where g.name = good_name;
-- initializing coursor for waregouses
curs_warehouse cursor for select gw.count from good_warehouse gw join good g on gw.id_good = g.id
where g.name = good_name;
shop_count int;
warehouse_count int;
total_remainders int;
begin
-- opening coursor for shops
open curs_shop;
loop
fetch next from curs_shop into shop_count;
if not found then exit; 
end if;
total_remainders = total_remainders + shop_count;
end loop;
close curs_shop;
-- opening coursor for warehouses
open curs_warehouse;
loop
fetch next from curs_warehouse into warehouse_count;
if not found then exit; end if;
total_remainders = total_remainders + warehouse_count;
end loop;
close curs_warehouse;
return total_remainders;
end;
$$ language plpgsql;
