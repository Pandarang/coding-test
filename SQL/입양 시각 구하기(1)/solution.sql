SELECT (datetime) as HOUR, count(*) as COUNT
FROM animal_outs
group by hour
having hour between 9 and 19
order by hour asc;
