SELECT UGB.WRITER_ID, UGU.NICKNAME, SUM(UGB.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS UGB
JOIN USED_GOODS_USER AS UGU
ON UGB.WRITER_ID = UGU.USER_ID
WHERE UGB.STATUS = 'DONE'
GROUP BY WRITER_ID
HAVING SUM(UGB.PRICE) >= 700000
ORDER BY TOTAL_SALES;