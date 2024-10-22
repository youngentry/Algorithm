-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
# ANIMAL_ID,    ANIMAL_TYPE,  DATETIME,    INTAKE_CONDITION,  NAME,  SEX_UPON_INTAKE는 각각 
# 동물의 아이디, 생물 종,       보호 시작일,  보호 시작 시 상태,  이름,  성별 및 중성화 여부