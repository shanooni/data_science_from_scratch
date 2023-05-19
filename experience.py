def predict_pain_and_unpaid(years_of_expereince):
    if years_of_expereince < 3.0:
        return "paid"
    elif years_of_expereince < 8.5:
        return "unpaid"
    else:
        return "paid"