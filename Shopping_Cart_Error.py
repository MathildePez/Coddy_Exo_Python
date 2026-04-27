def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    
    # Process each order in the list
    for order in orders:
        try:
            # Check for proper format
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue
                
            # Split the order into item and quantity
            item = order.split(":")[0]
            quantity_str = order.split(":")[1]
            
            # Convert quantity to integer
            quantity = int(quantity_str)
            
            # Check for negative quantity
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue
                
            # Add to cart or update quantity if item exists
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
                
        except ValueError:
            print(f"Invalid quantity: {order}")
            
        except Exception as e:
            print(f"Unexpected error: {e}")
            
    # Return the completed cart
    return cart
