select a.AUTHOR_ID,
        a.AUTHOR_NAME, 
        b.CATEGORY, 
        sum(s.sales * b.price) as TOTAL_SALES
from book_sales s
join book b on s.book_id = b.book_id
join author a on a.author_id = b.author_id
where date_format(s.sales_date, "%Y-%m") = '2022-01'
group by a.author_id, a.AUTHOR_NAME, b.category
order by a.author_id asc, b.category desc;