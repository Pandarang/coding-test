select ITEM_ID, ITEM_NAME, RARITY
from item_info 
where item_id in (
    select t.item_id
    from item_tree t
    join item_info i on i.item_id = t.parent_item_id
    where i.rarity  = 'RARE'
)
order by item_id desc;

