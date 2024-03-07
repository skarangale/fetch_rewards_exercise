import json
from datetime import datetime
import os

from constants import RAW_DATA_FOLDER, CREATE_QUERY_FOLDER, INSERT_QUERY_FOLDER
from database_helper import execute_query


# raw data
RECEIPTS_JSON_PATH = os.path.join(RAW_DATA_FOLDER, "receipts.json")

# SQL file paths
CREATE_RECEIPT_TABLE_PATH = os.path.join(CREATE_QUERY_FOLDER, "create_receipt_table.sql")
CREATE_RECEIPT_ITEM_TABLE_PATH = os.path.join(CREATE_QUERY_FOLDER, "create_receipt_item_table.sql")

# receipt columns - ['_id', 'bonusPointsEarned', 'bonusPointsEarnedReason', 'createDate', 'dateScanned', 'finishedDate', 'modifyDate', 'pointsAwardedDate', 'pointsEarned', 'purchaseDate', 'purchasedItemCount', 'rewardsReceiptItemList', 'rewardsReceiptStatus', 'totalSpent', 'userId']
# receipt item columns - ['barcode', 'brandCode', 'competitiveProduct', 'competitorRewardsGroup', 'deleted', 'description', 'discountedItemPrice', 'finalPrice', 'itemNumber', 'itemPrice', 'metabriteCampaignId', 'needsFetchReview', 'needsFetchReviewReason', 'originalFinalPrice', 'originalMetaBriteBarcode', 'originalMetaBriteDescription', 'originalMetaBriteItemPrice', 'originalMetaBriteQuantityPurchased', 'originalReceiptItemText', 'partnerItemId', 'pointsEarned', 'pointsNotAwardedReason', 'pointsPayerId', 'preventTargetGapPoints', 'priceAfterCoupon', 'quantityPurchased', 'rewardsGroup', 'rewardsProductPartnerId', 'targetPrice', 'userFlaggedBarcode', 'userFlaggedDescription', 'userFlaggedNewItem', 'userFlaggedPrice', 'userFlaggedQuantity']

def create_receipt_table():
    with open(CREATE_RECEIPT_TABLE_PATH, "r") as file:
        query = file.read()
        execute_query(query)
    with open(CREATE_RECEIPT_ITEM_TABLE_PATH, "r") as file:
        query = file.read()
        execute_query(query)


def read_receipts():
    receipt_records = []
    receipt_items_records = []
    with open(RECEIPTS_JSON_PATH, "r") as file:
        for line in file:
            receipt = json.loads(line)
            id = receipt["_id"]["$oid"]
            bonus_points_earned = receipt["bonusPointsEarned"] if "bonusPointsEarned" in receipt else None
            bonus_points_earned_reason = receipt["bonusPointsEarnedReason"] if "bonusPointsEarnedReason" in receipt else None
            create_date = datetime.utcfromtimestamp(float(receipt["createDate"]["$date"]) / 1000.0)
            date_scanned = datetime.utcfromtimestamp(float(receipt["dateScanned"]["$date"]) / 1000.0)
            finished_date = datetime.utcfromtimestamp(float(receipt["finishedDate"]["$date"]) / 1000.0) if "finishedDate" in receipt else None
            modify_date = datetime.utcfromtimestamp(float(receipt["modifyDate"]["$date"]) / 1000.0) if "modifyDate" in receipt else None
            points_awarded_date = datetime.utcfromtimestamp(float(receipt["pointsAwardedDate"]["$date"]) / 1000.0) if "pointsAwardedDate" in receipt else None
            points_earned = receipt["pointsEarned"] if "pointsEarned" in receipt else None
            purchase_date = datetime.utcfromtimestamp(float(receipt["purchaseDate"]["$date"]) / 1000.0) if "purchaseDate" in receipt else None
            purchased_item_count = receipt["purchasedItemCount"] if "purchasedItemCount" in receipt else None
            rewards_receipt_status = receipt["rewardsReceiptStatus"]
            total_spent = receipt["totalSpent"] if "totalSpent" in receipt else None
            user_id = receipt["userId"]

            receipt_record = (id, bonus_points_earned, bonus_points_earned_reason, create_date, date_scanned, finished_date, modify_date,
                              points_awarded_date, points_earned, purchase_date, purchased_item_count, rewards_receipt_status, total_spent, user_id)
            receipt_records.append(receipt_record)

            if "rewardsReceiptItemList" in receipt:
                for item in receipt["rewardsReceiptItemList"]:
                    receipt_item_record = parse_receipt_item(item, id)
                    receipt_items_records.append(receipt_item_record)


def parse_receipt_item(item, record_id):
    barcode = item["barcode"] if "barcode" in item else None
    brand_code = item["brandCode"] if "brandCode" in item else None
    competitive_product = item["competitiveProduct"] if "competitiveProduct" in item else None
    competitor_rewards_group = item["competitorRewardsGroup"] if "competitorRewardsGroup" in item else None
    deleted = item["deleted"] if "deleted" in item else None
    description = item["description"] if "description" in item else None
    discounted_item_price = item["discountedItemPrice"] if "discountedItemPrice" in item else None
    final_price = item["finalPrice"] if "finalPrice" in item else None
    item_number = item["itemNumber"] if "itemNumber" in item else None
    item_price = item["itemPrice"] if "itemPrice" in item else None
    metabrite_campaign_id = item["metabriteCampaignId"] if "metabriteCampaignId" in item else None
    needs_fetch_review = item["needsFetchReview"] if "needsFetchReview" in item else None
    needs_fetch_review_reason = item["needsFetchReviewReason"] if "needsFetchReviewReason" in item else None
    original_final_price = item["originalFinalPrice"] if "originalFinalPrice" in item else None
    original_meta_brite_barcode = item["originalMetaBriteBarcode"] if "originalMetaBriteBarcode" in item else None
    original_meta_brite_description = item["originalMetaBriteDescription"] if "originalMetaBriteDescription" in item else None
    original_meta_brite_item_price = item["originalMetaBriteItemPrice"] if "originalMetaBriteItemPrice" in item else None
    original_meta_brite_quantity_purchased = item["originalMetaBriteQuantityPurchased"] if "originalMetaBriteQuantityPurchased" in item else None
    original_receipt_item_text = item["originalReceiptItemText"] if "originalReceiptItemText" in item else None
    partner_item_id = item["partnerItemId"]
    points_earned = item["pointsEarned"] if "pointsEarned" in item else None
    points_not_awarded_reason = item["pointsNotAwardedReason"] if "pointsNotAwardedReason" in item else None
    points_payer_id = item["pointsPayerId"] if "pointsPayerId" in item else None
    prevent_target_gap_points = item["preventTargetGapPoints"] if "preventTargetGapPoints" in item else None
    price_after_coupon = item["priceAfterCoupon"] if "priceAfterCoupon" in item else None
    quantity_purchased = item["quantityPurchased"] if "quantityPurchased" in item else None
    receipt_id = record_id
    rewards_group = item["rewardsGroup"] if "rewardsGroup" in item else None
    rewards_product_partner_id = item["rewardsProductPartnerId"] if "rewardsProductPartnerId" in item else None
    targetPrice = item["targetPrice"] if "targetPrice" in item else None
    user_flagged_barcode = item["userFlaggedBarcode"] if "userFlaggedBarcode" in item else None
    user_flagged_description = item["userFlaggedDescription"] if "userFlaggedDescription" in item else None
    user_flagged_new_item = item["userFlaggedNewItem"] if "userFlaggedNewItem" in item else None
    user_flagged_price = item["userFlaggedPrice"] if "userFlaggedPrice" in item else None
    user_flagged_quantity = item["userFlaggedQuantity"] if "userFlaggedQuantity" in item else None

    return (barcode, brand_code, competitive_product, competitor_rewards_group, deleted, description, discounted_item_price, final_price,
            item_number, item_price, metabrite_campaign_id, needs_fetch_review, needs_fetch_review_reason, original_final_price,
            original_meta_brite_barcode, original_meta_brite_description, original_meta_brite_item_price, original_meta_brite_quantity_purchased,
            original_receipt_item_text, partner_item_id, points_earned, points_not_awarded_reason, points_payer_id, prevent_target_gap_points, 
            price_after_coupon, quantity_purchased, receipt_id, rewards_group, rewards_product_partner_id, targetPrice, 
            user_flagged_barcode, user_flagged_description, user_flagged_new_item, user_flagged_price, user_flagged_quantity)


