"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    shoping_cart = {}
    for item in notes:
        if item in shoping_cart:
            shoping_cart[item] += 1
        else:
            shoping_cart[item] = 1
    return shoping_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for item, data in recipe_updates:
        ideas[item] = data
    return ideas    


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    
    fullfillment_cart = {}
    for item, count in cart.items():
        attributes = aisle_mapping[item]
        new_value = [count] + attributes

        fullfillment_cart[item] = new_value
    return fullfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, data in fulfillment_cart.items():
        remove_count = data[0]
        if item in store_inventory:
            stock = store_inventory[item][0]
            if isinstance:
                new_stock = stock - remove_count
                if new_stock > 0:
                    store_inventory[item][0] = new_stock
                else:
                    store_inventory[item][0] = 'Out of Stock'
    return store_inventory

