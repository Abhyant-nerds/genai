import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Rossy WorkflowAI", page_icon="📧", layout="wide")

# Define custom styles for the app
st.markdown("""
    <style>
    .header {
        background-color: #FFFAF0; /* Warm color for the header */
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .form-container {
        background-color: #FFF5E1; /* Light warm color for the form */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .btn-submit {
        background-color: #FF6F61; /* Warm color for buttons */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn-submit:hover {
        background-color: #FF3D2A; /* Darker shade on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Header of the app
st.markdown('<div class="header"><h1>Rossy WorkflowAI</h1></div>', unsafe_allow_html=True)

# Form layout
with st.form(key='email_form', clear_on_submit=True):
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Email From
    email_from = st.text_input("Email From", placeholder="example@domain.com")
    
    # Email To
    email_to = st.text_input("Email To", placeholder="recipient@domain.com")
    
    # Subject
    subject = st.text_input("Subject", placeholder="Subject of the email")
    
    # Content/Body of Email
    content = st.text_area("Content/Body of Email", placeholder="Enter the body of the email here...")
    
    # Attachment
    attachment = st.file_uploader("Attachment", type=["pdf", "docx", "jpg", "png"], label_visibility="visible")
    
    # Submit button
    submit_button = st.form_submit_button(label="Send", help="Click to send the email")

    st.markdown('</div>', unsafe_allow_html=True)

# Placeholder for form submission logic
if submit_button:
    st.success("Email sent successfully!")
    st.write("**Email From**:", email_from)
    st.write("**Email To**:", email_to)
    st.write("**Subject**:", subject)
    st.write("**Content/Body of Email**:")
    st.write(content)
    
    if attachment:
        st.write("**Attachment**:", attachment.name)

    # Optionally, you can add logic to handle the email sending here
    # For example, integrate with an email API or service to actually send the email