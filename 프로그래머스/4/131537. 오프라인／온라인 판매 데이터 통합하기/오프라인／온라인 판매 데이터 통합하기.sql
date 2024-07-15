# 동일한 날짜, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE
    , PRODUCT_ID
    , USER_ID
    , SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'

UNION ALL

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE
    , PRODUCT_ID
    , NULL
    , SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;