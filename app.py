import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('waste_model.h5')

# Function to preprocess the image for prediction
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize the image to the input size expected by the model
    img_array = np.array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch size
    img_array = img_array / 255.0  # Normalize the image
    return img_array

# Function to predict the category of the image
def predict_category(img):
    img_array = preprocess_image(img)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)  # Get the index of the predicted class
    class_labels = ['battery', 'biological', 'brownglass', 'cardboard', 'clothes', 
                    'greenglass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'whiteglass']
    return class_labels[class_idx[0]], prediction[0][class_idx[0]]

# Create a list of categories and corresponding colors
categories = ['battery', 'biological', 'brownglass', 'cardboard', 'clothes', 
              'greenglass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'whiteglass']
category_colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 
                   'brown', 'pink', 'gray', 'lightblue']

# Streamlit UI setup
st.set_page_config(page_title="Waste Classification Demo", page_icon=":recycle:", layout="wide")
st.title("Waste Classification Demo with our Trained AI Model")

# Add file uploader on the left
st.sidebar.header("Upload Images")
uploaded_files = st.sidebar.file_uploader("Choose files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Create a dictionary to store images for each category
category_images = {category: [] for category in categories}

# Loop over the uploaded files and categorize them
if uploaded_files is not None:
    st.write(f"Number of images uploaded: {len(uploaded_files)}")
    
    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file)
        category, confidence = predict_category(img)

        # Append the image to the respective category list
        category_images[category].append((img, uploaded_file.name, confidence))

# Initialize session state to track the visibility of category images
if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = {category: False for category in categories}

# Create a container to display the categories as cards
category_cards = st.container()

# Display categories as cards and images below them
for category, color in zip(categories, category_colors):
    with category_cards:
        # Card UI for each category
        card = st.button(f"View {category.capitalize()} Images", key=category, help=f"Click to view {category} images")

        if card:
            # Toggle the visibility of images for the selected category
            st.session_state.selected_categories[category] = not st.session_state.selected_categories[category]
        
        # Show images if the category is selected
        if st.session_state.selected_categories[category]:
            st.subheader(f"Images of {category.capitalize()} Category")
            images_for_category = category_images[category]
            
            if images_for_category:
                for img, name, confidence in images_for_category:
                    st.image(img, caption=f"{name} - Confidence: {confidence:.2f}", use_container_width=True)
            else:
                st.write(f"No images for {category} category.")