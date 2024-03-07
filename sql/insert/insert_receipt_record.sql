INSERT INTO brand (
    id,
    bonus_points_earned,
    bonus_points_earned_reason,
    create_date,
    date_scanned,
    finished_date,
    modify_date,
    points_awarded_date,
    points_earned,
    purchase_date,
    purchased_item_count,
    rewards_receipt_status,
    total_spent,
    user_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);