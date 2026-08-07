import streamlit as st

st.title("BMI Calculator")

st.write("Calculate your BMI using either metric or imperial measurements.")

unit_system = st.radio(
    "Choose your preferred units:",
    ["Metric (Kg and cm)", "Imperial (lb, ft and in)"]
    )
def reset_inputs():
    st.session_state.weight_kg = 0.0
    st.session_state.height_cm = 0.0
    st.session_state.weight_lbs = 0.0
    st.session_state.feet = 0
    st.session_state.inches = 0
    
if unit_system == "Metric (Kg and cm)":
    weight = st.number_input("Enter your weight in Kg:", min_value=0.0, key="weight_kg")
    height = st.number_input("Enter your height in cm:", min_value=0.0, key="height_cm")
else:
    weight = st.number_input("Enter your weight in lbs:", min_value=0.0, key="weight_lbs")
    feet = st.number_input("Enter your height in ft:", min_value=0, key="feet")
    inches = st.number_input("Additional inches:", min_value=0, max_value=11, key="inches")
    
calculate = st.button("Calculate BMI")
st.button("Reset", on_click=reset_inputs)

if calculate:
    BMI = None
    if unit_system == "Metric (Kg and cm)":
        if weight <= 0 or height <= 0:
            st.error("Please enter a valid weight and height")
        else:
            height_metres = height / 100
            BMI = weight / (height_metres ** 2)
    else:
        total_inches = (feet * 12) + inches
        if weight <= 0 or total_inches <= 0:
            st.error("Please enter a valid weight and height")
        else:
            BMI = (weight * 703) / (total_inches ** 2)
            
    if BMI is not None:
        if BMI < 18.5:
            category = "Underweight"
        elif BMI < 25:
            category = "Normal weight"
        elif BMI < 30:
            category = "Overweight"
        elif BMI < 35:
            category = "Obese"
        elif BMI < 40:
            category = "Severely obese"
        else:
            category = "Morbidly obese"
        
        
        st.success(f"Your BMI is {BMI:.1f}") 
        
        if category == "Normal weight":
            st.success(f"Calssification: {category}")
        elif category == "Underweight":
            st.info(f"Calssification: {category}")
        elif category == "Overweight":
            st.warning(f"Calssification: {category}")
        else:
            st.error(f"Calssification: {category}")
            
            
     
        
        
        
        
        
        
        
        
        