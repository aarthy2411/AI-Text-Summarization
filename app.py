import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Hugging Face NLP Toolkit",
    page_icon="🤗"
)

st.title("🤗 Hugging Face NLP Toolkit")

st.write("Perform NLP tasks using Hugging Face Pipelines.")

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

task = st.sidebar.selectbox(
    "Choose a Task",
    [
        "Sentiment Analysis",
        "Text Summarization",
        "Translation",
        "Question Answering"
    ]
)

if task == "Sentiment Analysis":

    st.header("😊 Sentiment Analysis")

    text = st.text_area(
        "Enter your text",
        placeholder="Example: I love this application!"
    )

    if st.button("Analyze Sentiment"):

        if text.strip():

            try:
                with st.spinner("Analyzing..."):
                    model = load_model()
                    result = model(text[:4000])[0]

                st.success(f"Sentiment: {result['label']}")
                st.write(
                    f"Confidence: {result['score'] * 100:.2f}%"
                )

            except Exception as e:
                st.error(f"Error: {e}")

        else:
            st.warning("Please enter some text.")

elif task == "Text Summarization":
    st.info("Text Summarization will be added next.")

elif task == "Translation":
    st.info("Translation will be added next.")

elif task == "Question Answering":
    st.info("Question Answering will be added next.")
