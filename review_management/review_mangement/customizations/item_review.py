import frappe

def create_item_review_if_not_exists(doc, method=None):

    exists = frappe.db.exists("Item Review", {"item": doc.name})
    if not exists:
        # Create Item Review document
        item_review = frappe.get_doc({
            "doctype": "Item Review",
            "item": doc.name,   
            "product_rating": 0,   
            "total_reviews": 0
        })
        item_review.insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.logger().info(f"✅ Item Review created for Item {doc.name}")
