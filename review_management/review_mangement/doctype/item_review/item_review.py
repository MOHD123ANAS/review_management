# Copyright (c) 2025, Winspire Tech Pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ItemReview(Document):
	def autoname(self):
		self.name = self.item
	def validate(self):
		
		self.update_review_stats()

	def update_review_stats(self):
		reviews = self.reviews or []
		total = len(reviews)

		if total > 0:
			avg_rating = sum([r.rating for r in reviews if r.rating]) / total
		else:
			avg_rating = 0

		
		self.total_reviews = total
		self.product_rating = round(avg_rating, 2)  
