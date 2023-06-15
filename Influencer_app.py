import streamlit as st

# Set the app title
st.title("Kenyan Influencer App")

# Create a sidebar menu
st.sidebar.title("Menu")
menu_options = ["Home", "Influencers", "Campaigns", "Analytics"]
selected_menu = st.sidebar.radio("Select an option", menu_options)

# Home page
if selected_menu == "Home":
    st.header("Welcome to the Kenyan Influencer App!")
    st.write("This app provides information and tools for Kenyan influencers.")

# Influencers page
elif selected_menu == "Influencers":
    st.header("Kenyan Influencers")
    st.write("Here are some popular Kenyan influencers:")

    influencers = [
        {"name": "Influencer 1", "followers": 10000},
        {"name": "Influencer 2", "followers": 5000},
        {"name": "Influencer 3", "followers": 20000}
    ]

    for influencer in influencers:
        st.write(f"Name: {influencer['name']}")
        st.write(f"Followers: {influencer['followers']}")
        st.write("---")

# Campaigns page
elif selected_menu == "Campaigns":
    st.header("Campaigns")
    st.write("Here are some ongoing campaigns in Kenya:")

    campaigns = [
        {"name": "Campaign 1", "brand": "Brand 1", "budget": "$1000"},
        {"name": "Campaign 2", "brand": "Brand 2", "budget": "$500"},
        {"name": "Campaign 3", "brand": "Brand 3", "budget": "$2000"}
    ]

    for campaign in campaigns:
        st.write(f"Name: {campaign['name']}")
        st.write(f"Brand: {campaign['brand']}")
        st.write(f"Budget: {campaign['budget']}")
        st.write("---")

# Analytics page
elif selected_menu == "Analytics":
    st.header("Analytics")
    st.write("View analytics for your influencer campaigns in Kenya.")

    # Add your analytics code here

