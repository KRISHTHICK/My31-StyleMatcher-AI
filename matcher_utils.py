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
