-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS `count`
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE
ORDER BY NAME DESC

# ANIMAL_ID,   ANIMAL_TYPE, DATETIME,  INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 
# 동물의 아이디, 생물 종, 보호 시작일,     보호 시작 시 상태,  이름,  성별 및 중성화 여부