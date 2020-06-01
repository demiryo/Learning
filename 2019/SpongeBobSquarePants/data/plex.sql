-- SQLite

select * from metadata_items where title like '%SpongeBob%' and metadata_type=2;

select season_index, [index] as episod_index, * from metadata_items
	join (select [index] as season_index, id as season_id from metadata_items where parent_id=16514) on parent_id = season_id
order by season_index, episod_index;

SELECT * FROM `media_parts` where `file` like 'C:\Users\Public\Videos\Series\SpongeBob SquarePants (1999)\%';

SELECT id as season_media_id FROM `media_items` 
join (
select id as metadata_id from metadata_items
	join (select [index] as season_index, id as season_id from metadata_items where parent_id=16514) on parent_id = season_id) on metadata_item_id = metadata_id;

SELECT season_index, episod_index, * FROM `media_parts`
join (
SELECT season_index, episod_index, id as season_media_id FROM `media_items` 
join (
select season_index, [index] as episod_index, id as metadata_id from metadata_items
	join (select [index] as season_index, id as season_id from metadata_items where parent_id=16514) on parent_id = season_id) on metadata_item_id = metadata_id)
on media_item_id = season_media_id;

