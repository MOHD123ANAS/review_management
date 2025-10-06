import frappe

def execute():
    frappe.logger().info("Updating total_review for all Item Review records...")

    item_reviews = frappe.get_all("Item Review", fields=["name"])
    updated = 0

    for r in item_reviews:
        try:
            doc = frappe.get_doc("Item Review", r.name)
            doc.update_review_stats()  
            doc.db_update()            
            updated += 1
        except Exception as e:
            frappe.log_error(f"Error updating Item Review {r.name}: {e}")

    frappe.logger().info(f"✅ Successfully updated total_review for {updated} Item Reviews.")
