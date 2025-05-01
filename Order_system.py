import streamlit as st

# Initialize session state to store orders
if 'stack_recent_order' not in st.session_state:
    st.session_state.stack_recent_order = []

if 'queue_pending_order' not in st.session_state:
    st.session_state.queue_pending_order = []

st.title("🛒 E-Commerce Order Processing System")

# Input Section
product_name = st.text_input("Enter Product Name:")

if st.button("Place Order"):
    if product_name:
        st.session_state.stack_recent_order.append(product_name)
        st.session_state.queue_pending_order.append(product_name)
        st.success(f"Order placed for: {product_name}")
    else:
        st.warning("Please enter a product name.")

# Display Buttons
if st.button("View Recent Orders"):
    if st.session_state.stack_recent_order:
        st.subheader("Recent Orders (Stack)")
        st.write("\n".join(st.session_state.stack_recent_order))
    else:
        st.info("No recent orders found.")

if st.button("View Pending Orders"):
    if st.session_state.queue_pending_order:
        st.subheader("Pending Orders (Queue)")
        st.write("\n".join(st.session_state.queue_pending_order))
    else:
        st.info("No pending orders found.")

if st.button("Process Next Order"):
    if st.session_state.queue_pending_order:
        processed = st.session_state.queue_pending_order.pop(0)
        st.success(f"Processed order: {processed}")
    else:
        st.warning("No pending orders to process.")
