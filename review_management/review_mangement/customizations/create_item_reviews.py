import frappe

def create_item_reviews_for_existing_items():

    items = frappe.get_all("Item", fields=["name"])
    created = 0

    for item in items:
        if not frappe.db.exists("Item Review", {"item": item.name}):
            item_review = frappe.get_doc({
                "doctype": "Item Review",
                "item": item.name,
                "product_rating": 0,
                "total_reviews": 0
            })
            item_review.insert(ignore_permissions=True)
            created += 1

    frappe.db.commit()
    frappe.logger().info(f"✅ Created {created} Item Review docs for existing Items")
