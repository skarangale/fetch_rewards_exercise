import users
import brands
import receipts

def import_data():
    users.create_user_table()
    users.load_users_in_db()

    brands.create_brand_table()
    brands.load_brands_in_db()

    receipts.create_receipt_table()
    receipts.load_receipts_in_db()

if __name__ == "__main__":
    import_data()
