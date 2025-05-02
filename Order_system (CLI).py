# E-Commerce Order Processing System (Stack & Queue Implementation)

# Initialize empty stack (recent orders) and queue (pending orders)
stack_recent_order = []
queue_pending_order = []

print("----------------------------------------------------\nWelcome to the E-Commerce Order Processing System\n----------------------------------------------------")

# Main loop to interact with the user
while True:
    print("\nWhat would you like to do?")
    print("1. Place a new order")
    print("2. View recent orders (Stack)")
    print("3. View pending orders (Queue)")
    print("4. Process next pending order")
    print("5. Exit")

    # User's choice input
    choice = input("Enter your choice (1-5): ")

    # Option 1: Place a new order
    if choice == "1":
        product_name = input("Enter the name of the product you want to order: ")

        # Add the order to both the Stack and Queue
        stack_recent_order.append(product_name)  # Stack for recent orders (LIFO)
        queue_pending_order.append(product_name) # Queue for pending orders (FIFO)

        print(f"Order placed successfully for: {product_name}")

    # Option 2: View recent orders (Stack)
    elif choice == "2":
        if not stack_recent_order:
            print("No recent orders found.")
        else:
            print("\nRecent Orders (Most Recent Last):")
            for order in stack_recent_order:
                print("- " + order)

    # Option 3: View pending orders (Queue)
    elif choice == "3":
        if not queue_pending_order:
            print("No pending orders found.")
        else:
            print("\nPending Orders (First Come First Serve):")
            for order in queue_pending_order:
                print("- " + order)

    # Option 4: Process next pending order
    elif choice == "4":
        if not queue_pending_order:
            print("No pending orders to process.")
        else:
            processed_order = queue_pending_order.pop(0)  # Remove first order from Queue
            print(f"Processed order: {processed_order}")

    # Option 5: Exit
    elif choice == "5":
        print("Exiting the system. Thank you!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
