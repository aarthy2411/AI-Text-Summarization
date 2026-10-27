import streamlit as st
from transformers import pipeline

# Page Configuration
st.set_page_config(
    page_title="AR AI Sumatization",
    page_icon="🤖",
    layout="wide"
)

# App Title
st.sidebar.title("AR AI Sumatization")
st.sidebar.write("Choose your AI tool")

task = st.sidebar.selectbox(
    "Select a task",
    [
        "Text Summarization",
        "Translation",
        "Sentiment Analysis",
        "Question Answering"
    ]
)

# Load models only when required
@st.cache_resource
def load_summarizer():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

@st.cache_resource
def load_translator():
    return pipeline(
        "translation_en_to_fr",
        model="Helsinki-NLP/opus-mt-en-fr"
    )

@st.cache_resource
def load_sentiment():
    return pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

@st.cache_resource
def load_qa():
    return pipeline(
        "question-answering",
        model="distilbert/distilbert-base-cased-distilled-squad"
    )


# 1. Text Summarization
if task == "Text Summarization":

    st.title("AR AI Sumatization")
    st.write("Enter your paragraph")

    text = st.text_area(
        "Paragraph",
        height=200,
        placeholder="Enter the paragraph you want to summarize..."
    )

    if st.button("Summarize Text", use_container_width=True):

        if text.strip():

            try:
                with st.spinner("Generating summary..."):
                    summarizer = load_summarizer()

                    result = summarizer(
                        "Summarize this text: " + text,
                        max_new_tokens=100,
                        do_sample=False
                    )

                st.subheader("Summary")
                st.success(result[0]["generated_text"])

            except Exception as e:
                st.error(f"Summarization error: {e}")

        else:
            st.warning("Please enter some text.")


# 2. Translation
elif task == "Translation":

    st.title("English to French Translation")
    st.write("Enter English text to translate into French.")

    text = st.text_area(
        "English Text",
        height=150
    )

    if st.button("Translate Text", use_container_width=True):

        if text.strip():

            try:
                with st.spinner("Translating..."):
                    translator = load_translator()
                    result = translator(text, max_length=200)

                st.subheader("French Translation")
                st.success(result[0]["translation_text"])

            except Exception as e:
                st.error(f"Translation error: {e}")

        else:
            st.warning("Please enter some text.")


# 3. Sentiment Analysis
elif task == "Sentiment Analysis":

    st.title("Sentiment Analysis")
    st.write("Find out whether a sentence is positive or negative.")

    text = st.text_area(
        "Enter your sentence",
        height=150
    )

    if st.button("Analyze Sentiment", use_container_width=True):

        if text.strip():

            try:
                with st.spinner("Analyzing sentiment..."):
                    sentiment_model = load_sentiment()
                    result = sentiment_model(text)

                label = result[0]["label"]
                score = result[0]["score"]

                st.subheader("Analysis Result")
                st.write(f"**Sentiment:** {label}")
                st.write(f"**Confidence:** {score:.2%}")

            except Exception as e:
                st.error(f"Sentiment analysis error: {e}")

        else:
            st.warning("Please enter a sentence.")


# 4. Question Answering
elif task == "Question Answering":

    st.title("Question Answering")
    st.write("Enter a paragraph and ask a question about it.")

    context = st.text_area(
        "Context / Paragraph",
        height=200,
        placeholder="Enter the paragraph here..."
    )

    question = st.text_input(
        "Your Question",
        placeholder="Enter your question..."
    )

    if st.button("Get Answer", use_container_width=True):

        if context.strip() and question.strip():

            try:
                with st.spinner("Finding the answer..."):
                    qa_model = load_qa()

                    result = qa_model(
                        question=question,
                        context=context
                    )

                st.subheader("Answer")
                st.success(result["answer"])

            except Exception as e:
                st.error(f"Question answering error: {e}")

        else:
            st.warning(
                "Please enter both the paragraph and the question."
            )


# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Powered by Hugging Face Transformers")
st.sidebar.caption("Created with Streamlit")
