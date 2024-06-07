# File: Model/Review.py

class Review:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

    def update_rating(self, new_rating):
        self.rating = new_rating

    def update_comment(self, new_comment):
        self.comment = new_comment

# Example usage
if __name__ == "__main__":
    review1 = Review(5, "Great experience!")
    review2 = Review(4, "Nice place, but noisy.")

