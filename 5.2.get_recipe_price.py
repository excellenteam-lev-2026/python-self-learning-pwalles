def get_recipe_price(prices,optional=None, **kwargs):
    final_price=0
    for product, price in kwargs.items():
        if product in prices and (optional is None or product not in optional):
            final_price+=(prices[product]/100.0)*price
    return final_price

if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))