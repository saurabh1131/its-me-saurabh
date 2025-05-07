import streamlit as st
import json
import os

# Load JSON configuration
with open('config.json') as f:
    data = json.load(f)

# Set page configuration
st.set_page_config(page_title="Saurabh - Personal Profile", layout="wide", initial_sidebar_state="collapsed", page_icon="🙂")

# Header section with profile picture, name, and tagline
col1, col2 = st.columns([1, 3])
with col1:
    st.image(data["header"]["profile_picture"], width=150, caption="Stay Curious!")
with col2:
    st.title(data["header"]["name"])
    st.subheader(data["header"]["tagline"])
st.write("---")

# Introduction
with st.container():
    st.header("About Me 👋")
    st.write(data["personal"]["introduction"])
    st.write("---")

# Personal Details
with st.container():
    st.header("A Glimpse Into My Life 🌟")
    st.write(f"**🎓 Education:** {data['personal']['education']}")
    st.write(f"**🔥 My Passions:** {', '.join(data['personal']['passions'])}")
    st.write(f"**📖 Favorite Reads:** {', '.join(data['personal']['favorite_reads'])}")
    # st.write(f"**Languages Spoken:** {', '.join(data['personal']['languages'])}")
    st.write(f"**🎂 Wish Me On:** {data['personal']['dob']}")
    # st.write(f"**Height:** {data['personal']['height']}")
    st.write("---")

# Career Highlights
with st.container():
    st.header("Career Highlights 💼")
    st.write(f"*Work Profile: [{data['contact']['website']}]({data['contact']['website']})*")
    for job in data["job"]["work_experience"]:
        with st.expander(f"{job['role']}"):
            st.write(f"**Duration:** {job['duration']}")
            st.write(job["description"])
    st.write("---")

# Family Background
with st.container():
    st.header("Family Background 👨‍👩‍👧")
    st.write(data["family"]["description"])
    st.write("---")

# Achievements
with st.container():
    st.header("Achievements 🏆")
    for achievement in data["achievements"]:
        st.write(f"- {achievement}")
    st.write("---")

# Contact Information
with st.container():
    st.header("Get in Touch 📞")
    st.write(f"**Phone:** {data['contact']['phone']}")
    st.write(f"**Email:** [{data['contact']['email']}](mailto:{data['contact']['email']})")
    st.write(f"**Work Profile:** [{data['contact']['website']}]({data['contact']['website']})")
    # st.write(f"**Medium:** [{data['contact']['medium']}]({data['contact']['medium']})")
    st.write(f"**Instagram:** [{data['contact']['instagram']}]({data['contact']['instagram']})")
    st.write(f"**LinkedIn:** [{data['contact']['linkedin']}]({data['contact']['linkedin']})")
    st.write("---")

# Photos
with st.container():
    st.header("Moments 📸")
    cols = st.columns(4)
    for i, photo in enumerate(data["photos"]):
        cols[i % 4].image(photo, use_container_width=True)
    st.write("---")

# # Footer section with visitor counter
# def footer_section():
#     """App Footer section with visitor counter"""
#     visitor_file = 'visitor_count.json'
    
#     if 'visitor_counted' not in st.session_state:
#         st.session_state.visitor_counted = False
        
#         if os.path.exists(visitor_file):
#             try:
#                 with open(visitor_file, 'r') as f:
#                     visitor_data = json.load(f)
#                     visitor_count = visitor_data.get('count', 0)
#             except (json.JSONDecodeError, FileNotFoundError):
#                 visitor_count = 0
#         else:
#             visitor_count = 0
        
#         visitor_count += 1
        
#         with open(visitor_file, 'w') as f:
#             json.dump({'count': visitor_count}, f)
        
#         st.session_state.visitor_counted = True
#     else:
#         if os.path.exists(visitor_file):
#             try:
#                 with open(visitor_file, 'r') as f:
#                     visitor_data = json.load(f)
#                     visitor_count = visitor_data.get('count', 0)
#             except (json.JSONDecodeError, FileNotFoundError):
#                 visitor_count = 0
#         else:
#             visitor_count = 0
    
#     st.markdown(
#         f"""
#         <style>
#             #footer {{
#                 position: fixed;
#                 bottom: 10px;
#                 left: 50%;
#                 transform: translateX(-50%);
#                 font-size: 14px;
#                 color: gray;
#                 text-align: center;
#                 z-index: 1000;
#             }}
#         </style>
#         <div id="footer">
#             Built by <b>XploreMe@Sports</b> with 🫰〔Visits: {visitor_count}〕
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# footer_section()

# Thanks for Visiting
with st.container():
    st.subheader("Thanks for Visiting! 🙌")
    st.write("I hope you enjoyed learning more about me. Have a great time ahead!")
    st.write("---")