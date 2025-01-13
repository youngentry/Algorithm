-- 코드를 작성해주세요
SELECT
    D.DEPT_ID, 
    D.DEPT_NAME_EN, 
    ROUND(AVG(E.SAL)) AS AVG_SAL
FROM
    HR_DEPARTMENT D
JOIN
    HR_EMPLOYEES E
ON
    D.DEPT_ID = E.DEPT_ID
GROUP BY
    E.DEPT_ID
ORDER BY
    AVG_SAL DESC
# HR_DEPARTMENT 테이블의 구조는 다음과 같으며 
# DEPT_ID, DEPT_NAME_KR, DEPT_NAME_EN, LOCATION은 각각 
# 부서 ID, 국문 부서명,    영문 부서명,     부서 위치를 의미

# HR_EMPLOYEES 테이블의 구조는 다음과 같으며 
# EMP_NO, EMP_NAME, DEPT_ID, POSITION, EMAIL, COMP_TEL, HIRE_DATE, SAL은 각각 
# 사번,   성명,      부서 ID,  직책,      이메일, 전화번호,  입사일,     연봉을 의미