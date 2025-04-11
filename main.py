# app.py

import streamlit as st
import torch 

from PIL import Image

# Onglets pour chaque modèle
tab1, tab2, tab3 = st.tabs(["🖼️ Stable Diffusion", "🧠 GPT-Neo", "🦙 LLaMA"])

# --- Onglet 1 : Stable Diffusion ---
with tab1:
    from diffusers import DiffusionPipeline

    st.title("🎨 Générateur d'image avec Stable Diffusion")
    prompt_sd = st.text_input("Entrez votre prompt pour l'image :", "a ball")

    if st.button("Générer l'image", key="sd"):
        with st.spinner("⏳ Génération de l'image..."):
            pipe = DiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
            pipe.to("cuda" if torch.cuda.is_available() else "cpu")
            image = pipe(prompt_sd).images[0]
            st.image(image, caption=f"Résultat pour : {prompt_sd}", use_column_width=True)

# --- Onglet 2 : EleutherAI GPT-Neo ---
with tab2:
    from transformers import pipeline as hf_pipeline

    st.title("🧠 Générateur de texte avec EleutherAI GPT-Neo")
    prompt_gpt = st.text_area("Entrez le contexte :", "The following text is a description of a man:")

    if st.button("Générer le texte", key="gpt"):
        with st.spinner("⏳ Génération en cours..."):
            generator = hf_pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
            output = generator(prompt_gpt, max_length=150, num_return_sequences=1)[0]['generated_text']
            st.text_area("Texte généré :", output, height=200)

# --- Onglet 3 : LLaMA ---
with tab3:
    st.title("🦙 Générateur de texte avec LLaMA")
    prompt_llama = st.text_area("Entrez le début de texte :", "Plants create energy through a process known as")

    if st.button("Générer le texte", key="llama"):
        with st.spinner("⏳ Génération avec LLaMA..."):
            llama_pipeline = hf_pipeline(
                task="text-generation",
                model="huggyllama/llama-7b",
                torch_dtype=torch.float16,
                device=0 if torch.cuda.is_available() else -1  # Nécessite CUDA
            )
            output = llama_pipeline(prompt_llama, max_length=150, num_return_sequences=1)[0]['generated_text']
            st.text_area("Texte généré :", output, height=200)
