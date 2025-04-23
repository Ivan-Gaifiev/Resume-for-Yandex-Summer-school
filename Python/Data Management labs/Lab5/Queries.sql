-- 1. Create table
create or replace procedure create_table(table_name varchar)
language plpgsql
as $$
begin
	execute format(
	'create table %I
		(   id serial primary key,
			column_1 varchar(60),
			column_2 int,
			column_3 float
		)', table_name);
end;
$$;
-- call create_table('Test');

-- 2. Create database
create or replace procedure createDatabase(db_name varchar, username varchar, password varchar)
language plpgsql
as $$
begin
    perform dblink_exec(
        format('host=localhost dbname=game_market_case user=%s password=%s', username, password),
        format('create database %I', db_name)
    );
end;
$$;
--call createDatabase('Test', 'postgres', '11111111')

-- 3. Drop database
create or replace procedure delete_database(db_name varchar, username varchar, password varchar)
language plpgsql
as $$
begin
    perform dblink_exec(
        format('host=localhost dbname=game_market_case user=%s password=%s', username, password),
        format('drop database %I', db_name)
    );
end;
$$;
-- call delete_database('Test', 'postgres', '11111111')

-- 4. Clear table
create procedure clear_table(table_name varchar)
language plpgsql
as $$
begin
	truncate table table_name;
end;
$$;
-- call clear_table(%s);

-- 5. Add data to tables
-- Games
create or replace procedure add_data_games(val_1 varchar, val_2 varchar, val_3 int)
language plpgsql as $$
begin
	insert into games(name, genre, price)
	values (val_1, val_2, val_3);
end;
$$;
-- call add_data_games('GTA5', 'action-adventure', 2500);

-- 6. Search by field in tables
-- Games
create or replace function search_field_games(field varchar, record varchar)
returns setof games as $$
begin
    return query execute format(
        'select * from games where %I = %L', field, record);
end;
$$ language plpgsql;
-- select * from search_field_games('name', 'GTA5');

-- 7. Update record in tables
-- Games
create or replace procedure update_record_games(val_1 int, val_2 varchar, val_3 varchar, val_4 int)
language plpgsql as $$
begin
	update games
	set
	name = val_2,
	genre = val_3,
	price = val_4
	where id = val_1;
end;
$$;
-- call update_record_games(4, 'GTA5','action-adventure' , 2000);

-- 8. Delete by field in any table
create or replace procedure delete_by_field(table_name varchar, field varchar, record varchar)
language plpgsql as $$
begin
	execute format('delete from %I where %I = %L', table_name, field, record);
end;
$$;
-- call delete_by_field('games', 'price', '2000');

-- 9. Show tables
-- Games
create or replace function show_table_games()
returns setof record as $$
begin
	return query execute format('select * from games');
end;
$$ language plpgsql;
-- select * from show_table_games() as t(id int, name varchar, genre varchar, price int);
