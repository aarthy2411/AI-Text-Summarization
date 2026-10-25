import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Summarization",
    page_icon="📝",
    layout="wide"
)



st.title("AI Text Summarization")

st.write(
    "Summarize text, translate languages, "
    "analyze sentiment, and answer questions using AI."
)



@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )


@st.cache_resource
def load_translator():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-fr"
    )


@st.cache_resource
def load_sentiment_analyzer():
    return pipeline(
        "sentiment-analysis"
    )


@st.cache_resource
def load_question_answerer():
    return pipeline(
        "question-answering",
        model="distilbert/distilbert-base-cased-distilled-squad"
    )



st.sidebar.header("Choose a Task")

task = st.sidebar.selectbox(
    "Select an NLP task",
    [
        "Text Summarization",
        "Translation",
        "Sentiment Analysis",
        "Question Answering"
    ]
)



if task == "Text Summarization":

    st.header("Text Summarization")

    text = st.text_area(
        "Enter your text:",
        height=220,
        placeholder="Paste a long paragraph or article here..."
    )

    if st.button("Summarize Text"):

        if not text.strip():
            st.warning("Please enter some text.")

        elif len(text.split()) < 20:
            st.warning(
                "Please enter a longer paragraph for summarization."
            )

        else:
            try:
                with st.spinner("Generating summary..."):

                    summarizer = load_summarizer()

                    result = summarizer(
                        text,
                        max_length=100,
                        min_length=20,
                        do_sample=False,
                        truncation=True
                    )

                summary = result[0]["summary_text"]

                st.subheader("Generated Summary")
                st.success(summary)

                original_words = len(text.split())
                summary_words = len(summary.split())

                col1, col2 = st.columns(2)

                col1.metric(
                    "Original Word Count",
                    original_words
                )

                col2.metric(
                    "Summary Word Count",
                    summary_words
                )

            except Exception as e:
                st.error(f"Summarization failed: {e}")



elif task == "Translation":

    st.header("English to French Translation")

    text = st.text_area(
        "Enter English text:",
        height=180,
        placeholder="Enter the text you want to translate..."
    )

    if st.button("Translate Text"):

        if not text.strip():
            st.warning("Please enter some text.")

        else:
            try:
                with st.spinner("Translating text..."):

                    translator = load_translator()

                    result = translator(
                        text,
                        max_length=200,
                        truncation=True
                    )

                st.subheader("Translated Text")

                st.success(
                    result[0]["translation_text"]
                )

            except Exception as e:
                st.error(f"Translation failed: {e}")



elif task == "Sentiment Analysis":

    st.header("Sentiment Analysis")

    text = st.text_area(
        "Enter a sentence or review:",
        height=150,
        placeholder="Example: This product is amazing!"
    )

    if st.button("Analyze Sentiment"):

        if not text.strip():
            st.warning("Please enter some text.")

        else:
            try:
                with st.spinner("Analyzing sentiment..."):

                    analyzer = load_sentiment_analyzer()

                    result = analyzer(text[:2000])

                label = result[0]["label"]
                score = result[0]["score"]

                st.subheader("Analysis Result")

                st.write(f"Sentiment: {label}")
                st.write(f"Confidence: {score:.2%}")

                if label == "POSITIVE":
                    st.success("The text expresses positive sentiment.")

                elif label == "NEGATIVE":
                    st.error("The text expresses negative sentiment.")

                else:
                    st.info(f"Predicted sentiment: {label}")

            except Exception as e:
                st.error(f"Sentiment analysis failed: {e}")



elif task == "Question Answering":

    st.header("Question Answering")

    context = st.text_area(
        "Enter the passage or context:",
        height=220,
        placeholder="Paste a passage containing the answer..."
    )

    question = st.text_input(
        "Enter your question:",
        placeholder="Ask a question about the passage..."
    )

    if st.button("Get Answer"):

        if not context.strip() or not question.strip():
            st.warning(
                "Please enter both the passage and the question."
            )

        else:
            try:
                with st.spinner("Finding the answer..."):

                    qa = load_question_answerer()

                    result = qa(
                        question=question,
                        context=context
                    )

                st.subheader("Answer")

                st.success(result["answer"])

                st.caption(
                    f"Model confidence: {result['score']:.2%}"
                )

            except Exception as e:
                st.error(f"Question answering failed: {e}")



st.sidebar.markdown("---")
st.sidebar.caption(
    "Built using Python, Streamlit and Hugging Face"
)
