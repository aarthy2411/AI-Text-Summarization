
import streamlit as st
from transformers import pipeline


st.set_page_config(
    page_title="AI Text Summarization",
    page_icon="📝",
    layout="centered"
)


st.title("AI Text Summarization")
st.write(
    "Summarize long paragraphs and articles into short, "
    "meaningful summaries using an AI language model."
)

st.divider()


@st.cache_resource
def load_model():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )


text = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste a long paragraph or article here..."
)


summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"]
)

length_settings = {
    "Short": {"max_length": 40, "min_length": 10},
    "Medium": {"max_length": 80, "min_length": 20},
    "Long": {"max_length": 130, "min_length": 40}
}


if st.button("Generate Summary", type="primary"):

    if not text.strip():
        st.warning("Please enter some text first.")

    elif len(text.split()) < 40:
        st.warning(
            "Please enter a longer paragraph with at least "
            "40 words for better summarization."
        )

    else:
        try:
            with st.spinner("AI is generating your summary..."):
                summarizer = load_model()

                settings = length_settings[summary_length]

                word_count = len(text.split())

                max_length = min(
                    settings["max_length"],
                    max(20, word_count // 2)
                )

                min_length = min(
                    settings["min_length"],
                    max_length - 1
                )

                result = summarizer(
                    text,
                    max_length=max_length,
                    min_length=min_length,
                    do_sample=False,
                    truncation=True
                )

                summary = result[0]["summary_text"]

            st.success("Summary generated successfully!")

            st.subheader("Generated Summary")
            st.write(summary)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Original Words", len(text.split()))

            with col2:
                st.metric("Summary Words", len(summary.split()))

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(
                "Unable to generate the summary. "
                "Please check your internet connection and try again."
            )
            st.caption(f"Technical details: {e}")

st.divider()

st.caption("Powered by Streamlit and a pretrained Transformer model.")

