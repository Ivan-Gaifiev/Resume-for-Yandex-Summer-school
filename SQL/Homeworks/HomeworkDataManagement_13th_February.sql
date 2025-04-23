-- Создать представление, содержащее следующие сведения: 
-- id и наименование товара, суммарные запасы товара в магазинах, 
-- суммарные запасы товара на складах.

drop view if exists totalInventoryOfGoods;
create view totalInventoryOfGoods(id, name_good, sum_inv_shops, sum_inv_warehouses)
as 
(select Good.id, Good.name, sum(distinct Good_Shop.count), sum(distinct Good_Warehouse.count) 
from Good
left join Good_Shop on (Good.id=Good_shop.id_good) 
left join Good_Warehouse on (Good.id = Good_Warehouse.id_good) 
group by Good.id, Good.name);

-- Обеспечить возможность редактирования сведений по запасам товаров 
-- через представление, учитывая, что по умолчанию товары берутся со 
-- склада, где их количество максимально, а поставки товаров осуществляются 
-- на склады, где их количество минимально.

create or replace function goodsInventoryEditingAvailability()
returns trigger as $$
declare
	id_maxWarehouse int;
	id_minShop int;
begin
	-- find warehouse with max amount of good
	select max(G_W.id_warehouse) into id_maxWarehouse 
	from Good_Warehouse G_W where G_W.id_good = new.id_good;
	-- find shop with min amount of good
	select min(G_S.id_shop) into id_minShop 
	from Good_Shop G_S where G_S.id_good = new.id_good;
	
	if new.count < 0 then  -- it means that we take goods from the warehouse
		update Good_Warehouse
		set count = count + new.count where id_good = new.id_good and id_warehouse = id_maxWarehouse;
	else  -- it means that we put goods to the shop
		update Good_Shop
		set count = count + new.count where id_good = new.id_good and id_shop = id_minShop;
	end if;
	return new;
end;
$$ language plpgsql;

create or replace trigger editingAvailabilityShopTrigger
before insert on Good_Warehouse
for each row execute function goodsInventoryEditingAvailability();

insert into Good_Warehouse (id_good, id_warehouse, count)
values (3, 2, 0);

select * from totalInventoryOfGoods;
