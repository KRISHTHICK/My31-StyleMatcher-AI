import streamlit as st
from PIL import Image
import os
from matcher_utils import image_to_vector, get_celeb_vectors, find_best_match

st.set_page_config(page_title="👠 StyleMatcher AI", layout="wide")
st.title("👠 StyleMatcher AI – Celebrity Outfit Look-Alike Recommender")

st.markdown("Upload your outfit photo to see which celebrity's style it resembles the most!")

uploaded_file = st.file_uploader("📸 Upload Your Outfit Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    user_img = Image.open(uploaded_file)
    st.image(user_img, caption="Your Uploaded Look", use_column_width=True)

    with st.spinner("Analyzing and matching your style..."):
        user_vector = image_to_vector(user_img)
        celeb_vectors, celeb_names, celeb_images = get_celeb_vectors()
        best_idx, confidence = find_best_match(user_vector, celeb_vectors)

    st.subheader(f"🧑‍🎤 Closest Match: {celeb_names[best_idx]}")
    st.image(celeb_images[best_idx], caption=f"{celeb_names[best_idx]}'s Look", use_column_width=True)
    st.success(f"🧮 Match Confidence: {confidence * 100:.2f}%")

    tips = {
        "Rihanna": "Experiment with edgy cuts and bold accessories.",
        "Zendaya": "Go for structured silhouettes and modern elegance.",
        "Harry_Styles": "Play with colors, patterns, and gender-neutral fits."
    }

    st.info(f"💡 Style Tip: {tips.get(celeb_names[best_idx].replace(' ', '_'), 'Stay confident and own your style!')}")

    # Generate collage
    from PIL import ImageOps

    comparison = Image.new("RGB", (user_img.width + celeb_images[best_idx].width, max(user_img.height, celeb_images[best_idx].height)))
    comparison.paste(ImageOps.contain(user_img, user_img.size), (0, 0))
    comparison.paste(ImageOps.contain(celeb_images[best_idx], celeb_images[best_idx].size), (user_img.width, 0))

    st.subheader("🖼️ Visual Comparison")
    st.image(comparison)

    # Download option
    comparison.save("comparison_result.jpg")
    with open("comparison_result.jpg", "rb") as file:
        btn = st.download_button(
            label="📥 Download Look Comparison",
            data=file,
            file_name="style_match.jpg",
            mime="image/jpeg"
        )
