# My31-StyleMatcher-AI
GenAI

Here’s a **new, unique fashion AI project idea** with **add-on features**, ready to run in **VS Code** without `venv`:

---

# 👠 **StyleMatcher AI – Celebrity Outfit Look-Alike Recommender**

---

## 🧠 **What It Does**

StyleMatcher AI allows users to:

1. **Upload an outfit image**.
2. **Match it to a celebrity outfit look-alike** using visual similarity.
3. **Show matching confidence score**.
4. **Get fashion tips based on the celebrity style**.
5. **Download a side-by-side comparison collage**.
6. **Save looks locally for future reference**.

---

## ✨ **Add-On Features**

| Feature                       | Description                                                               |
| ----------------------------- | ------------------------------------------------------------------------- |
| 🔍 Visual Similarity Matching | Compares uploaded image to a mini celeb look-book using image embeddings. |
| 🧾 Fashion Tips Generator     | Shows personalized suggestions based on matched celeb.                    |
| 🖼️ Side-by-Side Collage      | Creates a visual comparison between your image and celebrity style.       |
| 💾 Save Looks                 | Downloads the comparison + results locally.                               |
| 🧠 Lightweight - Runs Offline | No venv, no APIs, 100% local processing.                                  |

---

## 🗂 Folder Structure

```
StyleMatcher-AI/
├── app.py
├── matcher_utils.py
├── celeb_data/
│   ├── rihanna.jpg
│   ├── zendaya.jpg
│   ├── harry_styles.jpg
├── requirements.txt
└── README.md
```

---

## 📦 `requirements.txt`

```txt
streamlit
Pillow
numpy
scikit-learn
```

---

## 🧠 `matcher_utils.py`

```python
from PIL import Image
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

def image_to_vector(img, size=(100, 100)):
    img = img.resize(size).convert("RGB")
    return np.array(img).flatten().reshape(1, -1)

def get_celeb_vectors(path="celeb_data/"):
    vectors, names, images = [], [], []
    for file in os.listdir(path):
        if file.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(os.path.join(path, file))
            vectors.append(image_to_vector(img))
            names.append(file.split(".")[0].title())
            images.append(img)
    return vectors, names, images

def find_best_match(user_vector, celeb_vectors):
    similarities = [cosine_similarity(user_vector, cv)[0][0] for cv in celeb_vectors]
    best_idx = int(np.argmax(similarities))
    return best_idx, similarities[best_idx]
```

---

## 🚀 `app.py`

```python
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
```

---

## 🖼 Add Sample Images to `celeb_data/`

You can add 3-5 celeb outfit images. Here are examples:

* `rihanna.jpg`
* `zendaya.jpg`
* `harry_styles.jpg`

Ensure they are clear outfit images.

---

## 📝 `README.md`

````markdown
# 👠 StyleMatcher AI – Celebrity Outfit Look-Alike Recommender

StyleMatcher lets users upload an outfit photo and matches it with the most visually similar celebrity style using cosine similarity on image features.

## 🧠 Features
- Upload outfit photo
- Match with a celebrity from lookbook
- Show confidence score
- Display fashion tip
- Generate visual side-by-side collage
- Download the comparison

## 📦 Setup
```bash
pip install -r requirements.txt
streamlit run app.py
````

> 💡 No virtualenv needed.

## 📁 Add your celeb images to the `/celeb_data` folder.

```

---

Would you like me to:
- Add **OpenCV** for face/body detection?
- Include **auto-style tags** like “Street”, “Glam”, “Athleisure”?
- Build a **profile-based fashion memory** to store your past looks?

Let me know and I’ll extend this project further for you!
```
