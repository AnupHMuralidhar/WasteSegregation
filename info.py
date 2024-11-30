import streamlit as st
import pydeck as pdk

# Landfill information and coordinates
categories = [
    'Great Pacific Garbage Patch', 'Sudokwon Landfill Site', 'Laogang Landfill', 
    'Deonar Dumping Ground', 'Ghazipur Landfill', 'Akwambom Landfill', 
    'West New Territories Landfill', 'Robinsons Landfill', 'Barletta Landfill', 
    'Kabwe Landfill', 'Waste Management Landfill', 'Tirana Landfill'
]

coordinates = [
    (35.0000, -140.0000),  # Great Pacific Garbage Patch
    (37.5000, 126.8000),   # Sudokwon Landfill Site
    (31.0167, 121.6578),   # Laogang Landfill
    (19.0610, 72.9227),    # Deonar Dumping Ground (Mumbai)
    (28.6731, 77.3174),    # Ghazipur Landfill (Delhi)
    (4.0500, 9.7000),      # Akwambom Landfill (Cameroon)
    (22.4490, 113.9570),   # West New Territories Landfill (Hong Kong)
    (14.6500, 121.0650),   # Robinsons Landfill (Philippines)
    (41.3549, 16.3000),    # Barletta Landfill (Italy)
    (-14.4413, 28.4173),   # Kabwe Landfill (Zambia)
    (39.1574, -75.5046),   # Waste Management Landfill (USA)
    (41.3356, 19.8172)     # Tirana Landfill (Albania)
]

landfill_info = {
    "Great Pacific Garbage Patch": """
        **Great Pacific Garbage Patch (Ocean Garbage Patch)**
        - Latitude: 35.0000° N, Longitude: 140.0000° W
        - This is an oceanic garbage patch rather than a traditional landfill. It is one of the largest collections of debris in the world, primarily consisting of plastic waste. This patch spans an area roughly twice the size of Texas.
        - The waste is composed mainly of plastics, but includes other materials such as fishing gear and general debris.
        - AI can play a crucial role in identifying floating plastics and other materials, aiding in collection and implementing recycling strategies to reduce oceanic pollution.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/Great_Pacific_Garbage_Patch)**
    """,
    "Sudokwon Landfill Site": """
        **Sudokwon Landfill Site (South Korea)**
        - Latitude: 37.5000° N, Longitude: 126.8000° E
        - One of the largest landfills in the world, receiving over 10,000 tonnes of waste daily, it is located near Seoul. The landfill spans a huge area, and despite being closed for further waste disposal in 2000, the site is still used for waste treatment.
        - It's difficult to segregate waste due to the large volumes of mixed waste, and its location presents environmental concerns, particularly with the leakage of harmful substances.
        - AI-powered robotic arms could significantly enhance the waste segregation process by identifying recyclable materials and sorting them more effectively.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/Sudokwon_Landfill_Site)**
    """,
    "Laogang Landfill": """
        **Laogang Landfill (Shanghai, China)**
        - Latitude: 31.0167° N, Longitude: 121.6578° E
        - The Laogang Landfill receives more than 8,000 tonnes of waste daily, making it one of the largest landfills in Shanghai.
        - Sorting waste is particularly difficult due to contamination with various types of industrial, household, and plastic waste. Furthermore, methane emissions are a serious environmental concern.
        - AI-driven systems and robotic arms can aid in automatically sorting recyclable materials, decreasing the environmental burden.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/Laogang_Landfill)**
    """,
    "Deonar Dumping Ground": """
        **Deonar Dumping Ground (Mumbai, India)**
        - Latitude: 19.0610° N, Longitude: 72.9227° E
        - One of the oldest and largest landfills in Mumbai, receiving about 3,000 tonnes of waste per day. The site has been operational since 1927.
        - The waste here is highly mixed, with both biodegradable and non-biodegradable materials making segregation difficult.
        - AI and robotic systems integrated with waste segregation mechanisms can significantly improve the efficiency of recycling and reduce manual sorting efforts.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/Deonar_dumping_ground)**
    """,
    "Ghazipur Landfill": """
        **Ghazipur Landfill (Delhi, India)**
        - Latitude: 28.6731° N, Longitude: 77.3174° E
        - Ghazipur is a major landfill in Delhi that receives around 2,000 tonnes of waste daily. The landfill has grown substantially over the years and poses environmental challenges such as air pollution and groundwater contamination.
        - Segregation is difficult because of the huge volume of mixed waste being dumped.
        - Robotic arms and AI-powered systems could assist in sorting recyclables, preventing the further increase of the landfill and reducing the environmental impact.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/Ghazipur_Landfill)**
    """,
    "Akwambom Landfill": """
        **Akwambom Landfill (Cameroon)**
        - Latitude: 4.0500° N, Longitude: 9.7000° E
        - This landfill, located in the outskirts of Douala, the commercial capital of Cameroon, handles municipal waste as well as industrial waste.
        - The lack of proper waste segregation and recycling infrastructure makes it a major challenge to handle the waste appropriately.
        - AI and robotic arms could be used to sort materials, improving the overall efficiency of recycling processes.
    """,
    "West New Territories Landfill": """
        **West New Territories Landfill (Hong Kong)**
        - Latitude: 22.4490° N, Longitude: 113.9570° E
        - This landfill site in Hong Kong receives a significant portion of the city's construction and demolition waste.
        - The large volume of construction debris makes segregation difficult and costly, and it occupies a significant portion of land.
        - AI and robotic systems could automate the segregation of recyclable materials such as metals and plastics, improving the overall efficiency of the site.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/West_New_Territories_Landfill)**
    """,
    "Robinsons Landfill": """
        **Robinsons Landfill (Philippines)**
        - Latitude: 14.6500° N, Longitude: 121.0650° E
        - Located in the Cavite province, this landfill handles around 1,500 tonnes of mixed waste every day.
        - The landfill struggles with proper waste segregation due to a variety of waste types.
        - AI and robotics could help by automating the segregation of recyclables, reducing reliance on human labor, and improving recycling rates.
    """,
    "Barletta Landfill": """
        **Barletta Landfill (Italy)**
        - Latitude: 41.3549° N, Longitude: 16.3000° E
        - This landfill in Southern Italy receives a mix of residential and commercial waste. It has been a major waste disposal site for the region.
        - The increasing volume of waste, coupled with poor segregation practices, has led to a significant environmental impact.
        - AI-powered robotic systems could automate the sorting of recyclables, reducing contamination in recycled materials and improving recycling efficiency.
    """,
    "Kabwe Landfill": """
        **Kabwe Landfill (Zambia)**
        - Latitude: -14.4413° S, Longitude: 28.4173° E
        - This landfill serves the town of Kabwe and receives industrial and household waste.
        - Recycling is inefficient due to mixed waste types and insufficient infrastructure.
        - AI-powered robotic arms could help by sorting recyclables such as plastics and metals, alleviating pressure on the landfill and improving waste management practices.
    """,
    "Waste Management Landfill": """
        **Waste Management Landfill (USA)**
        - Latitude: 39.1574° N, Longitude: -75.5046° W
        - Located in the United States, this landfill handles a significant amount of municipal and industrial waste.
        - The sheer volume of waste and the variety of materials make proper segregation and recycling challenging.
        - AI and robotic systems can assist by automating the sorting process, leading to a higher recovery of recyclable materials and improved efficiency.
        - **[Learn more on Wikipedia](https://en.wikipedia.org/wiki/Waste_Management,_Inc.)**
    """,
    "Tirana Landfill": """
        **Tirana Landfill (Albania)**
        - Latitude: 41.3356° N, Longitude: 19.8172° E
        - Located near the capital city of Albania, Tirana, this landfill has been operational for several years and receives a variety of waste, including household and industrial waste.
        - Recycling is challenging due to improper waste sorting and a lack of efficient waste management infrastructure.
        - AI and robotic systems can be used to automate waste segregation, improving the recycling process and reducing landfill accumulation.
    """
}

# Function to generate the map with red/green dots
def generate_globe_with_map(selected_landfill, categories, coordinates):
    data = [
        {"lat": coord[0], "lon": coord[1], "category": category, "color": [255, 0, 0] if category != selected_landfill else [0, 255, 0]}
        for coord, category in zip(coordinates, categories)
    ]
    dots = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position=["lon", "lat"],
        get_fill_color="color",  # Use color to dynamically change dot color
        get_radius=100000,  # Set radius for visibility
        pickable=True,  # Enable hover functionality
        opacity=0.7,
    )

    map_style = "mapbox://styles/mapbox/satellite-streets-v12"
    view_state = pdk.ViewState(latitude=20.0, longitude=0.0, zoom=2, pitch=0)
    tooltip = {
        "html": "<b>Landfill:</b> {category}",
        "style": {
            "backgroundColor": "lightgray",
            "color": "black",
            "fontFamily": "Arial",
            "padding": "5px",
            "borderRadius": "5px",
        },
    }

    globe = pdk.Deck(layers=[dots], initial_view_state=view_state, map_style=map_style, tooltip=tooltip)
    return globe

# Streamlit setup
st.set_page_config(page_title="Major Landfills in the World", page_icon=":earth_americas:", layout="wide")
st.title("Major Landfills in the World")

# Dropdown to select a landfill
landfill_selection = st.selectbox("Select a Landfill:", categories)

# Map with red/green dots
st.pydeck_chart(generate_globe_with_map(landfill_selection, categories, coordinates))

# Display information about the selected landfill
st.subheader(f"Information about {landfill_selection}")
st.write(landfill_info[landfill_selection])

# Try the AI Model button

st.markdown(
    '<a href="https://wastesegregation-app.streamlit.app" target="_blank">'
    '<button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; cursor: pointer;">Click here to try the AI model</button></a>', 
    unsafe_allow_html=True)