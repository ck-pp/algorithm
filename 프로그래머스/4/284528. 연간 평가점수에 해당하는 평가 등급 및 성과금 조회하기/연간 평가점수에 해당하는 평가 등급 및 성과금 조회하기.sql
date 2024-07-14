SELECT G.EMP_NO, E.EMP_NAME, 
    CASE
        WHEN AVG(G.SCORE) >= 96 THEN 'S'
        WHEN AVG(G.SCORE) >= 90 THEN 'A'
        WHEN AVG(G.SCORE) >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE, 
    CASE
        WHEN AVG(G.SCORE) >= 96 THEN E.SAL * 0.2
        WHEN AVG(G.SCORE) >= 90 THEN E.SAL * 0.15
        WHEN AVG(G.SCORE) >= 80 THEN E.SAL * 0.1
        ELSE 0
    END AS BONUS
FROM HR_DEPARTMENT AS D
JOIN HR_EMPLOYEES AS E ON D.DEPT_ID = E.DEPT_ID
JOIN HR_GRADE AS G ON E.EMP_NO = G.EMP_NO
GROUP BY E.EMP_NO, E.EMP_NAME
ORDER BY EMP_NO;