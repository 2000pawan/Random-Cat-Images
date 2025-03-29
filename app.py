import streamlit as st
import requests

API_KEY = "live_rEgUs5mRGp9yoJl4BoweLdbcYwPMVC70Iq7G1LQXwmKHs9zuYDl0ZnYyk3Cvfzsr"
BASE_URL = "https://api.thecatapi.com/v1"

def fetch_breeds():
    res = requests.get(f"{BASE_URL}/breeds", headers={"x-api-key": API_KEY})
    return res.json() if res.status_code == 200 else []

def fetch_cats(breed_id=""):
    url = f"{BASE_URL}/images/search?limit=9&order=DESC&size=small&breed_ids={breed_id}"
    res = requests.get(url, headers={"x-api-key": API_KEY})
    return res.json() if res.status_code == 200 else []

st.title("🐱 Random Cat Gallery")

breeds = fetch_breeds()
breed_options = {breed["id"]: breed["name"] for breed in breeds}
breed_options[""] = "All Breeds"

selected_breed = st.selectbox("Filter by Breed:", options=list(breed_options.keys()), format_func=lambda x: breed_options[x])

if st.button("Load Cats"):
    cats = fetch_cats(selected_breed)
    
    if cats:
        cols = st.columns(3)
        for index, cat in enumerate(cats):
            with cols[index % 3]:
                st.image(cat["url"], caption=f"Cat {index+1}", use_container_width=True)
    else:
        st.write("No cats found.")

st.write("Developed by @Pawan Yadav")
