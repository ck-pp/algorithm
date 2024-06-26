SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN SKILLCODES AS S
WHERE D.SKILL_CODE & S.CODE
AND (S.NAME = 'Python' OR S.NAME = 'C#')
ORDER BY D.ID ASC;