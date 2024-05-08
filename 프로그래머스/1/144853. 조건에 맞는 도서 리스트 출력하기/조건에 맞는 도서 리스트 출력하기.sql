SELECT BOOK_ID, SUBSTR(PUBLISHED_DATE, 1, 11) AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문'
AND YEAR(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE;