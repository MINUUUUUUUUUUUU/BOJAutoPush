WITH FISH_NAME_MAX AS (
SELECT A.FISH_NAME, MAX(B.LENGTH) AS LENGTH FROM FISH_NAME_INFO AS A
JOIN FISH_INFO AS B ON A.FISH_TYPE = B.FISH_TYPE
GROUP BY A.FISH_NAME
)

SELECT C.ID, D.FISH_NAME, C.LENGTH FROM FISH_INFO AS C
JOIN FISH_NAME_INFO AS D ON C.FISH_TYPE = D.FISH_TYPE
JOIN FISH_NAME_MAX AS E ON D.FISH_NAME = E.FISH_NAME
WHERE C.LENGTH = E.LENGTH