WITH MAXS AS (SELECT MAX(SIZE_OF_COLONY) AS MAX_SIZE, 
                  YEAR(DIFFERENTIATION_DATE) AS YEAR
                 FROM ECOLI_DATA
                 GROUP BY YEAR)

SELECT YEAR(E.DIFFERENTIATION_DATE) AS YEAR, 
(M.MAX_SIZE - E.SIZE_OF_COLONY) AS YEAR_DEV, E.ID
FROM ECOLI_DATA AS E
INNER JOIN MAXS AS M
ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC;