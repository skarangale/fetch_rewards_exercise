/*
1. What are the top 5 brands by receipts scanned for most recent month?
*/

WITH recent_month AS ( -- CTE to find the most recent month present in the receipt table
    SELECT DATE_TRUNC('month', MAX(date_scanned)) AS recent_month -- maximum value of the date_scanned column and truncating it to the beginning of the month
    FROM receipt
)
SELECT brand.name, COUNT(receipt_id) AS count
FROM receipt
JOIN receipt_item ON receipt.id = receipt_item.receipt_id -- join receipt_item with receipt with receipt_id
JOIN brand ON receipt_item.brand_id = brand.id -- join receipt_item with brand with brand_id
WHERE DATE_TRUNC('month', receipt.date_scanned) = (SELECT recent_month FROM recent_month) -- filter to include only those from the most recent month found in the recent_month CTE
GROUP BY brand.name
ORDER BY count DESC -- order based on receipt count
LIMIT 5; -- get top 5 results