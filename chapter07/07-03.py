"""
    Modified
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”

    Example 7-3. The promos list is filled by the promotion decorator
"""

promos = []

def promotion(promo_func):
    """Promotion decorator adds new `promo_func` to promotion list,
        then it returns the `promo_fun` unchanged.
        With this decorator, we avoid the mistake 
        of adding a new promotional strategy function without also adding it
        to the promotion list.
    """
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 \
        if order.customer.fidelity >= 1000 \
            else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)


"""
Notes
---
    * Note that no changes are needed for `best_promo` for any new promotional strategy
    that is added.
    * The promotional strategy functions don't need to adhere to 
    special naming conventions, like _promo.
    * The decorator makes it easy to disable a promotion -- just remove the decoration.
    * Promotional strategy functions can be defined elsewher in the system, 
    as long as they have access to the decorator @promotion.
"""