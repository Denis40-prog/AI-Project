# Projet : Générateur Multimodal avec Streamlit

Ce projet est une application web interactive développée avec **Streamlit**. Elle permet de générer des images et du texte en utilisant des modèles d'intelligence artificielle avancés. L'application est divisée en trois onglets, chacun dédié à un modèle spécifique.

---

## Fonctionnalités

### 1. 🎨 Générateur d'images avec Stable Diffusion
- **Modèle utilisé** : [Stable Diffusion v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- **Description** : Génère des images à partir d'un prompt textuel.
- **Technologies** :
    - `diffusers` : Bibliothèque pour travailler avec des modèles de diffusion.
    - `torch` : Framework pour le calcul tensoriel et l'accélération GPU.

### 2. 🧠 Générateur de texte avec EleutherAI GPT-Neo
- **Modèle utilisé** : [GPT-Neo 1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B)
- **Description** : Génère du texte à partir d'un contexte donné.
- **Technologies** :
    - `transformers` : Bibliothèque pour les modèles de traitement du langage naturel.
    - `torch` : Utilisé pour l'accélération GPU.

### 3. 🦙 Générateur de texte avec LLaMA
- **Modèle utilisé** : [LLaMA 7B](https://huggingface.co/huggyllama/llama-7b)
- **Description** : Génère du texte à partir d'un début de phrase.
- **Technologies** :
    - `transformers` : Pour le chargement et l'utilisation du modèle.
    - `torch` : Nécessaire pour l'exécution sur GPU.

---

## Prérequis

- **Python** : Version 3.8 ou supérieure.
- **CUDA** : Recommandé pour l'accélération GPU.
- **Bibliothèques Python** :
    - `streamlit`
    - `torch`
    - `transformers`
    - `diffusers`
    - `Pillow`

---

## Installation

1. Clonez le dépôt :
     ```bash
     git clone <URL_DU_DEPOT>
     cd <NOM_DU_DEPOT>
     ```

2. Installez les dépendances :
     ```bash
     pip install -r requirements.txt
     ```

3. Lancez l'application :
     ```bash
     streamlit run main.py
     ```

---

## Utilisation

1. Accédez à l'application via votre navigateur à l'adresse `http://localhost:8501`.
2. Naviguez entre les onglets pour utiliser les différents générateurs :
     - **Stable Diffusion** : Entrez un prompt pour générer une image.
     - **GPT-Neo** : Fournissez un contexte pour générer du texte.
     - **LLaMA** : Donnez un début de phrase pour générer du texte.

---

## Ressources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Hugging Face Models](https://huggingface.co/models)
- [PyTorch Documentation](https://pytorch.org/docs/)

---

## Auteurs

- **Denis** : Développeur principal.

---

## Déployement 

https://ai-project-elective.streamlit.app/

Malheureusement je n'ai pas eu le temps de corriger les problèmes ayant lieu lors de la génération via streamlit cloud.
