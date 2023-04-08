def average_rating(rating_list):
    """This is a helper method used to calculate the average rating of a book."""
    if not rating_list:
        return 0

    return round(sum(rating_list)/len(rating_list))
