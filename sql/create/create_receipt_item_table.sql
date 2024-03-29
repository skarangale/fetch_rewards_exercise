/*
We can further normalize this table
*/

CREATE TABLE IF NOT EXISTS receipt_item (
    id SERIAL PRIMARY KEY,
    barcode VARCHAR(12),
    brand_code VARCHAR FOREIGN KEY REFERENCES brand(brand_code),
    competitive_product BOOLEAN,
    competitor_rewards_group TEXT,
    deleted BOOLEAN,
    description TEXT,
    discounted_item_price DECIMAL,
    final_price DECIMAL,
    item_number VARCHAR(12),
    item_price DECIMAL,
    metabrite_campaign_id TEXT,
    needs_fetch_review BOOLEAN,
    needs_fetch_review_reason TEXT,
    original_final_price DECIMAL,
    original_meta_brite_barcode VARCHAR(12),
    original_meta_brite_description TEXT,
    original_meta_brite_item_price DECIMAL,
    original_meta_brite_quantity_purchased INT,
    original_receipt_item_text TEXT,
    partner_item_id INT,
    points_earned DECIMAL,
    points_not_awarded_reason TEXT,
    points_payer_id VARCHAR(24),
    prevent_target_gap_points BOOLEAN,
    price_after_coupon DECIMAL,
    quantity_purchased INT,
    receipt_id VARCHAR(24) FOREIGN KEY REFERENCES receipt(id),
    rewards_group TEXT,
    rewards_product_partner_id VARCHAR(24),
    targetPrice DECIMAL,
    user_flagged_barcode VARCHAR(12),
    user_flagged_description TEXT,
    user_flagged_new_item BOOLEAN,
    user_flagged_price DECIMAL,
    user_flagged_quantity INT
);