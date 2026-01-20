select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i
where i.ITEM_ID not in (
    select t.PARENT_ITEM_ID
    from ITEM_TREE t
    where not isnull(t.PARENT_ITEM_ID))
order by i.ITEM_ID desc;