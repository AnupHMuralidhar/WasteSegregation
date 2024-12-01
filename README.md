# 🌍 AI Waste Segregation and Classification  

## Project Overview  
This project addresses the pressing global issue of waste management by combining Artificial Intelligence (AI) with innovative waste segregation and classification techniques. Our solution focuses on improving waste segregation practices, especially in major landfills worldwide, by leveraging a trained AI model.  

The project includes:  
1. **Landfill Information Page**: Interactive information about 12 major global landfills with a dynamic map.  
2. **AI Waste Segregation App**: Allows users to upload images of waste and view AI predictions for waste categories.  

## Features  

### 1. Landfill Information Page  
- Displays **12 major landfills worldwide**, marked as red dots on an interactive map.  
- When a landfill is selected:  
  - The dot turns green.  
  - Users can access detailed information about the landfill, including:  
    - The type and amount of waste it receives.  
    - Challenges in waste segregation and recycling.  
    - How AI integration can address these challenges.  
- Highlights the plan to integrate AI predictions with **robotic arms**, **real-time cameras**, and **chemical sensors** for advanced waste management.  

### 2. AI Waste Segregation App  
- A user-friendly web application with the following features:  
  - Users can upload images of waste.  
  - The AI model predicts the waste category.  
  - Displays segregated waste in separate cards based on the predicted categories.  
- **Note**: Predictions are not always 100% accurate, and the app emphasizes this transparency.  

---

## Technology Stack  
- **Frontend**: Streamlit for building interactive web pages.  
- **Backend**: Python and TensorFlow/Keras for training and deploying the AI model.  
- **Model**: A waste classification model trained on 12 waste categories with 98% accuracy.  

---

## How It Works  

### Landfill Information Page  
1. Displays an interactive map with red dots representing global landfills.  
2. Selecting a landfill changes the dot to green and shows relevant landfill information.  
3. Explains how the AI model can solve real-world challenges in waste management.  

### AI Waste Segregation App  
1. Users upload images of waste via the app.  
2. The app uses a trained AI model to classify the waste into categories such as **plastic**, **paper**, **metal**, etc.  
3. Segregated waste categories are displayed as clickable cards for easy viewing.  

---

## Problem Statement  
- **Global Waste Crisis**: Major landfills worldwide are overburdened due to improper waste management and lack of efficient segregation techniques.  
- **Inefficiency in Recycling**: Poor waste classification hinders recycling and leads to increased environmental pollution.  
- **Proposed Solution**: This project addresses these challenges by providing an AI-powered model for better waste segregation at the source.  

---

## AI Model Details  
- **Waste Categories**: Battery, biological, cardboard, clothes, glass (green, brown, white), metal, paper, plastic, shoes, trash.  
- **Accuracy**: Achieved 98% test accuracy with an improved model.  
- **Future Integration**: AI data will be integrated into robotic arms with real-time cameras and chemical sensors for automated waste segregation.  

---

## Project URL
- **https://wastesegregation-info.streamlit.app/**
