import base64
import streamlit as st
import openai
import os

# openai.api_key = ""
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.set_page_config(
    page_title="DALL·E 2 Image Generator",
    page_icon="🎨",
    layout="wide",
)
# Custom CSS styles
st.markdown(
    """
    <style>
    .download-button {
        background-color: #221e5b;
        color: #ffffff;
        padding: 10px 15px;
        border: 25px;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        font-weight: bold;
    }

    .download-button:hover {
        background-color: #ff5588;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("DALL·E 2 Image🖼️ Generator")

# Prompt input
prompt = st.text_area("Enter the prompt:👇", height=5)

# Size selection
size_options = ["256x256", "512x512", "1024x1024"]
selected_size = st.selectbox("Select image size:", size_options)
# href = f'<a class="download-button" href="data:image/png;base64,{"Hello"}" download="generated_image.png">Download</a>'
# st.markdown(href, unsafe_allow_html=True)


if st.button("See Magic🪄"):
    # Generate image
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=selected_size,
            response_format="b64_json",
        )

        # Display image

        if response["data"]:
            image_data = base64.b64decode(response["data"][0]["b64_json"])
            st.image(image_data, use_column_width=True)

            # Download button
            b64_image = base64.b64encode(image_data).decode()
            href = f'<a class="download-button" href="data:image/png;base64,{b64_image}" download="generated_image.png">Download</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No image generated.")
    except Exception as e:
        st.error(e)
        print(e)