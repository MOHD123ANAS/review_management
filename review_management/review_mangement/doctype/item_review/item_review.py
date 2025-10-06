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

		if not total:
			self.total_reviews = 0
			self.product_rating = 0
			self.total_feedback = 0
			return


		valid_ratings = [r.rating for r in reviews if r.rating]
		avg_rating = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0

		
		feedback_count = len([r for r in reviews if r.feedback])

		self.total_reviews = total
		self.total_feedback = feedback_count 
		self.product_rating = round(avg_rating, 2)
