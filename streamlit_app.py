import streamlit as st

# Set the app title
st.title("Personalized Nutrition and Wellness Platform")

# Create a sidebar menu
st.sidebar.title("Menu")
menu_options = ["Home", "Nutrition Plans", "Workout Routines", "Progress Tracking"]
selected_menu = st.sidebar.radio("Select an option", menu_options)

# Home page
if selected_menu == "Home":
    st.header("Welcome to the Personalized Nutrition and Wellness Platform!")
    st.write("This platform offers personalized nutrition and wellness plans based on your health goals, dietary preferences, and lifestyle.")

# Nutrition Plans page
elif selected_menu == "Nutrition Plans":
    st.header("Nutrition Plans")
    st.write("Choose a nutrition plan that suits your needs:")

    nutrition_plans = [
        {"name": "Weight Loss Plan", "description": "A plan designed to help you lose weight."},
        {"name": "Muscle Building Plan", "description": "A plan designed to help you build muscle."},
        {"name": "General Wellness Plan", "description": "A plan focused on overall health and well-being."}
    ]

    for plan in nutrition_plans:
        st.write(f"Name: {plan['name']}")
        st.write(f"Description: {plan['description']}")
        st.write("---")

# Workout Routines page
elif selected_menu == "Workout Routines":
    st.header("Workout Routines")
    st.write("Choose a workout routine that suits your goals and fitness level:")

    workout_routines = [
        {"name": "Beginner's Workout", "description": "A workout routine suitable for beginners."},
        {"name": "Intermediate Workout", "description": "A workout routine for those with some fitness experience."},
        {"name": "Advanced Workout", "description": "A challenging workout routine for advanced fitness levels."}
    ]

    for routine in workout_routines:
        st.write(f"Name: {routine['name']}")
        st.write(f"Description: {routine['description']}")
        st.write("---")

# Progress Tracking page
elif selected_menu == "Progress Tracking":
    st.header("Progress Tracking")
    st.write("Track your progress and view your achievements:")

    # Add progress tracking and achievements code here

    st.write("Coming soon!")


