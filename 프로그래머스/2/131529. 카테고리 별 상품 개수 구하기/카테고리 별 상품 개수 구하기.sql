-- 코드를 입력하세요
SELECT SUBSTRING(PRODUCT_CODE, 1, 2) AS CATEGORY, COUNT(SUBSTRING(PRODUCT_CODE, 1, 2)) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY 