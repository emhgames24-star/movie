import streamlit as st

def calculate_ticket(age, is_member, seat_type):
    base_price = 15
    show_time = "Evening"
    is_weekend = False
    discount = 0
    messages = []

    if age > 17:
        messages.append("User is eligible to book a ticket")
    elif age < 16:
        return None, ["Not eligible without adult supervision"]

    if is_member and age >= 21:
        discount = 4
        messages.append("Membership discount applied")

    if seat_type == "Gold":
        base_price = 18
    elif seat_type == "Premium":
        base_price = 20
    elif seat_type == "Platinum":
        base_price = 23

    extra_charges = 2 if show_time == "Evening" else 0

    service_charges = 3 if seat_type == "Gold" else 5 if seat_type == "Premium" else 1

    total = base_price + service_charges + extra_charges - discount
    return total, messages


set.title("Movie Ticket Calculator")

age = st.number_input("Age", min_value=1, max_value=100)
is_member = st.checkbox("Are you a member?")
seat_type = st.selectbox("Seat Type", ["Gold", "Premium", "Platinum"])

if st.button("Calculate"):
    total, messages = calculate_ticket(age, is_member, seat_type)
    for m in messages:
        st.write(m)

    st.success(f"Total price: ${total}")

