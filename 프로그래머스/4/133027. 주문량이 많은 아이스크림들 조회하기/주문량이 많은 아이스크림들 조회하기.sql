-- 코드를 입력하세요
SELECT J.FLAVOR
FROM FIRST_HALF F
LEFT JOIN JULY J
ON F.FLAVOR = J.FLAVOR
GROUP BY J.FLAVOR 
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC LIMIT 3
# ORDER BY J.FLAVOR LIMIT 3

# FIRST_HALF 상반기, JULY 7월

# SHIPMENT_ID,                                  FLAVOR,     TOTAL_ORDER는 각각 
# 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량

# 7월에는 아이스크림 주문량이 많아 같은 아이스크림에 대하여 서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우가 있습니다. 이 경우 같은 맛의 아이스크림이라도 다른 출하 번호를 갖게 됩니다.

# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.