import streamlit as st
import time

# --- Hard-coded Data ---
attendance_records = {
    "Prathit": 95,
    "Pranav": 75,
    "Harshvardhan": 69,
    "Gaurav": 100,
}
# --- ---

st.title("Attendance Record Query System")
st.write("Ask for the attendance record of the student.")

# User input to ask the question
user_query = st.text_input("Enter a name to check their attendance record:")

if st.button("Get Record"):
    if user_query:
        # Normalize the input for matching
        name = user_query.lower().strip()
        
        # Check if the name exists in our records
        if name in attendance_records:
            with st.spinner("Thinking..."):
                # Simulate the 3-5 second delay
                time.sleep(4)
            
            attendance = attendance_records[name]
            st.success(f"Attendance record for {name.capitalize()}:")
            st.metric(label=f"Attendance Percentage", value=f"{attendance}%")
        else:
            st.warning("Sorry, that name is not in the attendance records.")
    else:
        st.error("Please enter a name to check.")
