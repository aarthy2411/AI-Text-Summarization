import streamlit as st
import re
from collections import Counter


st.set_page_config(
    page_title="AI Text Summarization",
    page_icon="📝",
    layout="centered"
)


st.title("AI Text Summarization")

st.write(
    "Convert long paragraphs and articles into "
    "short, meaningful summaries using NLP."
)

st.divider()



STOPWORDS = {
    "the", "is", "are", "was", "were", "a", "an",
    "and", "or", "but", "in", "on", "at", "to",
    "of", "for", "with", "by", "from", "as",
    "this", "that", "these", "those", "it",
    "its", "be", "been", "being", "has", "have",
    "had", "do", "does", "did", "will", "would",
    "can", "could", "should", "may", "might",
    "we", "they", "he", "she", "you", "i",
    "their", "them", "our", "your", "his", "her",
    "which", "who", "what", "when", "where",
    "how", "why", "if", "then", "than", "also",
    "not", "no", "so", "such", "into", "about",
    "through", "there", "here"
}



def summarize_text(text, summary_length):

    
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    sentences = [
        sentence.strip()
        for sentence in sentences
        if len(sentence.split()) > 2
    ]

    if len(sentences) <= 1:
        return text.strip()

    
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    words = [
        word for word in words
        if word not in STOPWORDS and len(word) > 2
    ]

    word_frequency = Counter(words)

    if not word_frequency:
        return text.strip()

    
    sentence_scores = []

    for index, sentence in enumerate(sentences):

        sentence_words = re.findall(
            r'\b[a-zA-Z]+\b',
            sentence.lower()
        )

        score = sum(
            word_frequency[word]
            for word in sentence_words
            if word in word_frequency
        )

        score = score / max(len(sentence_words), 1)

        sentence_scores.append((index, score))

    
    length_settings = {
        "Short": 2,
        "Medium": 3,
        "Long": 5
    }

    sentence_count = length_settings[summary_length]

    sentence_count = min(sentence_count, len(sentences))

    
    ranked_sentences = sorted(
        sentence_scores,
        key=lambda item: item[1],
        reverse=True
    )

    selected_indices = {
        index for index, score in ranked_sentences[:sentence_count]
    }

    
    summary = [
        sentence
        for index, sentence in enumerate(sentences)
        if index in selected_indices
    ]

    return " ".join(summary)



st.subheader("Enter Your Text")

text = st.text_area(
    "Paste your paragraph or article below:",
    height=250,
    placeholder="Enter a long paragraph or article here..."
)


summary_length = st.selectbox(
    "Choose Summary Length",
    ["Short", "Medium", "Long"]
)


if st.button("Generate Summary", type="primary"):

    if not text.strip():

        st.warning("Please enter some text first.")

    elif len(text.split()) < 30:

        st.warning(
            "Please enter at least 30 words "
            "for better summarization."
        )

    else:

        with st.spinner("Generating your summary..."):

            summary = summarize_text(
                text,
                summary_length
            )

        if summary:

            st.success("Summary generated successfully!")

            st.subheader("Generated Summary")

            st.info(summary)

            st.divider()

            
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Original Words",
                    len(text.split())
                )

            with col2:
                st.metric(
                    "Summary Words",
                    len(summary.split())
                )

            
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

st.divider()

st.caption(
    "Developed using Python, NLP and Streamlit."
)
