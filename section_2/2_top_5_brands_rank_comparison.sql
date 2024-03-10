/*
1. How does the ranking of the top 5 brands by receipts scanned for the recent month compare to the ranking for the previous month?
*/

WITH recent_months AS ( -- CTE to find the most recent two month present in the receipt table
    SELECT DATE_TRUNC('month', date_scanned) AS month -- truncating date_scanned to get month
    FROM receipt
    ORDER BY month DESC
    LIMIT 2 -- get recent two monthts
),
brand_counts AS ( -- CTE to calculate the counts of each brand for the recent months
    SELECT DATE_TRUNC('month', receipt.date_scanned) AS month, brand.name, COUNT(receipt.id) AS count -- extract month and get count of receipts
    FROM receipt
    JOIN receipt_item ON receipt.id = receipt_item.receipt_id -- join receipt_item with receipt with receipt_id
    JOIN brand ON receipt_item.brand_id = brand.id -- join receipt_item with brand with brand_id
    WHERE DATE_TRUNC('month', receipt.date_scanned) IN (SELECT month FROM recent_months) -- filter to include only those from the most recent two month found in the recent_month CTE
    GROUP BY month, brand.name
),
ranked_brands AS ( -- CTE to calculate the ranking of each brand for each month in brand_counts CTE
    SELECT month, name, count,
           RANK() OVER (PARTITION BY month ORDER BY count DESC) AS ranking
    FROM brand_counts
)
SELECT rb.month AS recent_month, rb.name AS brand_name, rb.ranking AS recent_ranking, COALESCE(rb_prev.ranking, 0) AS previous_ranking -- assign rank 0 to brands not present in previous month
FROM ranked_brands rb
LEFT JOIN ranked_brands rb_prev ON rb.month = rb_prev.month - INTERVAL '1 month' AND rb.name = rb_prev.name -- self join ranked_brands using month in rb and substracting 1 month in rb_prev 
WHERE rb.month = (SELECT month FROM recent_months LIMIT 1) -- select only the recent month as we are already self joining to map previous month
ORDER BY rb.count DESC
LIMIT 5; -- et top 5 results