CREATE TABLE IF NOT EXISTS receipt (
    id VARCHAR(24) PRIMARY KEY,
    bonus_points_earned INT,
    bonus_points_earned_reason TEXT,
    create_date DATE NOT NULL,
    date_scanned DATE NOT NULL,
    finished_date DATE,
    modify_date DATE,
    points_awarded_date DATE,
    points_earned DECIMAL,
    purchase_date DATE,
    purchased_item_count INT,
    rewards_receipt_status VARCHAR,
    total_spent DECIMAL,
    user_id VARCHAR(24) REFERENCES "user"(id)
);