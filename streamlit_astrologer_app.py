
# Astrologer Recommendation Engine

import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Astrologer data
astrologers = [
    {"name": "Aarav Sharma", "tags": "career, finance, business"},
    {"name": "Diya Kapoor", "tags": "love, relationships, marriage"},
    {"name": "Rohan Mehta", "tags": "education, study, career"},
    {"name": "Meera Joshi", "tags": "spirituality, peace, life purpose"},
    {"name": "Kabir Singh", "tags": "health, well-being, stress"},
]
df = pd.DataFrame(astrologers)
astrologer_embeddings = model.encode(df['tags'].tolist())

# User input
user_input = st.text_area("Describe your current issue or life situation:")

if st.button("Get Recommendations") and user_input:
    user_embedding = model.encode([user_input])
    scores = cosine_similarity(user_embedding, astrologer_embeddings)[0]
    df['score'] = scores
    top_matches = df.sort_values(by='score', ascending=False).head(3)

    st.subheader("🔮 Top 3 Recommended Astrologers:")
    for i, row in top_matches.iterrows():
        st.markdown(
            f"""**{row['name']}**  
            *Tags:* {row['tags']}  
            *Relevance Score:* `{row['score']:.3f}`  
            """
        )
        st.markdown("---")

