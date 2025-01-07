import streamlit as st
import requests

# Function to fetch picnic spot data from API
def get_picnic_data(destination):
    url = 'https://faux-api.com/api/v1/picnictellerapi_47438506650545564'  # Your API URL
    response = requests.get(url)
    data = response.json()
    
    # Filter data for the requested destination
    for spot in data['result']:
        if destination.lower() in spot['name'].lower():
            return spot
    return None

# Set page configuration for better look
st.set_page_config(page_title="Picnic Teller", page_icon="🌄", layout="wide")

# Add a title and description to the app
st.title("Welcome to AI-Powered Picnic Teller 🌄")
st.write("Just search for any picnic spot on your mind & leave the rest to find essential details for a smooth picnic experience on us.")

# Add a search box for the user to input the picnic destination
destination = st.text_input("Enter Picnic Spot (eg Shogran,Murree..etc.)", placeholder="Search a picnic spot...")

# If the user presses the "Search" button
if st.button("Search"):
    if destination:
        st.spinner("Fetching data...")
        
        # Fetch picnic spot data
        spot_data = get_picnic_data(destination)

        if spot_data:
            # Display Picnic Spot Information in a clean and attractive layout
            st.markdown(f"### **{spot_data['name']}**")
            st.markdown(f"**Location**: {spot_data['location']}")
            st.markdown(f"**People Density🚶‍♂️**: {spot_data['people_density']}")
            st.markdown(f"**Weather🌤**: {spot_data['weather']}")
            st.markdown(f"**Traffic Condition🚗**: {spot_data['traffic_condition']}")
            
            st.markdown(
    """
    Note: The provided data is solely based on estimations. The data provide can miss match depending on various situations.
    """
)
        
        else:
            st.warning("Oops! You got us we are still gathering information about your given destination. Would you like to try any other location?")
    else:
        st.error("Oops! You got us we are still gathering information about your given destination.")

# Footer with professional touch
st.markdown(
    """
    ---
    Created by Khizar Ul Islam & Team. 
    Providing real-time information for the best picnic experience in Pakistan! 🇵🇰
    """
)
