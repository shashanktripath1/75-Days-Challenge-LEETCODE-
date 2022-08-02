# Write your MySQL query statement below
SELECT distinct stock_name,
SUM(case when operation = 'Buy' THEN -1*price ELSE price END) AS capital_gain_loss
FROM Stocks
GROUP BY 1