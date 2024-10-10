SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY PRODUCT_ID, USER_Id
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC


# # select product_id, count(sales_amount) as cnt
# select *
# from online_sale
# # group by product_id
# order by product_id;