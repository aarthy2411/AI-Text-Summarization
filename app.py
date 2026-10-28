
import streamlit as st
from transformers import pipeline


st.set_page_config(
    page_title="AI Text Summarization",
    page_icon="📝",
    layout="centered"
)


st.title("AI Text Summarization")
st.write(
    "Enter a long paragraph and generate a short, meaningful summary using AI."
)


@st.cache_resource
def load_summarizer():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small"
    )


text = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste your paragraph or article here..."
)


summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"]
)


length_settings = {
    "Short": {"max_new_tokens": 50},
    "Medium": {"max_new_tokens": 100},
    "Long": {"max_new_tokens": 150}
}

# Summarize button
if st.button("Generate Summary", type="primary"):

    if not text.strip():
        st.warning("Please enter some text first.")

    elif len(text.split()) < 20:
        st.warning(
            "Please enter at least 20 words for a meaningful summary."
        )

    else:
        try:
            with st.spinner(
                "Loading AI model and generating your summary..."
            ):
                summarizer = load_summarizer()

                # Split long input into manageable chunks
                words = text.split()
                chunk_size = 350
                chunks = [
                    " ".join(words[i:i + chunk_size])
                    for i in range(0, len(words), chunk_size)
                ]

                summaries = []

                for chunk in chunks:
                    prompt = (
                        "Summarize the following text clearly. "
                        "Keep the important information:\n" + chunk
                    )

                    result = summarizer(
                        prompt,
                        max_new_tokens=length_settings[
                            summary_length
                        ]["max_new_tokens"],
                        do_sample=False,
                        truncation=True
                    )

                    summary = result[0]["generated_text"].strip()

                    if summary:
                        summaries.append(summary)

                # Combine generated summaries
                if summaries:
                    final_text = " ".join(summaries)

                    # Summarize again if multiple chunks were used
                    if len(summaries) > 1:
                        result = summarizer(
                            "Summarize this text into one clear "
                            "summary, keeping the key information:\n"
                            + final_text,
                            max_new_tokens=length_settings[
                                summary_length
                            ]["max_new_tokens"],
                            do_sample=False,
                            truncation=True
                        )

                        final_text = result[0][
                            "generated_text"
                        ].strip()

                    st.success("Summary generated successfully!")

                    st.subheader("Generated Summary")
                    st.write(final_text)

                    st.download_button(
                        label="Download Summary",
                        data=final_text,
                        file_name="summary.txt",
                        mime="text/plain"
                    )

                    st.caption(
                        f"Original words: {len(words)} | "
                        f"Summary words: {len(final_text.split())}"
                    )

                else:
                    st.error(
                        "The model returned an empty summary. "
                        "Please try different input text."
                    )

        except Exception as e:
            st.error("Unable to generate the summary.")
            st.write("Error details:", str(e))


st.divider()
st.caption("AI Text Summarization | Built with Python and Streamlit")

