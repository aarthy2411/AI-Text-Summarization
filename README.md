# AI-Text-Summarization

AI Text Summarization is a Python-based web application that uses Natural Language Processing (NLP) techniques to generate concise summaries from lengthy paragraphs and articles.

The application identifies important sentences from the input text and produces a shorter version while preserving the main information. It provides different summary length options to make reading and understanding large amounts of text easier. Try the application here:http://localhost:8501/
<img width="997" height="812" alt="Screenshot 2026-10-30 225058" src="https://github.com/user-attachments/assets/23656d20-9591-4467-9201-592100dcc562" /><img width="1052" height="752" alt="Screenshot 2026-10-30 225114" src="https://github.com/user-attachments/assets/2bad7a4d-c5c3-4c62-b700-793e4f61aeef" />



## Features

* **Text Input:** Enter or paste long paragraphs and articles.
* **Automatic Summarization:** Extracts important sentences from the given text.
* **Multiple Summary Lengths:** Choose between Short, Medium, and Long summaries.
* **Word Count:** Displays the original and summarized word counts.
* **Download Summary:** Download the generated summary as a text file.
* **Simple Interface:** Easy-to-use web interface built with Streamlit.

## Technologies Used

* Python
* Natural Language Processing (NLP)
* Streamlit


## How It Works

1. The user enters a paragraph or article into the application.
2. The input text is divided into individual sentences.
3. Word frequencies are calculated after removing common stopwords.
4. Each sentence is assigned a score based on the frequency of important words.
5. The highest-scoring sentences are selected.
6. The selected sentences are arranged in their original order to generate the summary.
7. The user can view and download the generated summary.

## Summary Options

| Option | Description                    |
| ------ | ------------------------------ |
| Short  | Selects 2 important sentences. |
| Medium | Selects 3 important sentences. |
| Long   | Selects 5 important sentences. |



## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aarthy2411/AI-Text-Summarization.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Text-Summarization
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

### 5. Open in Browser

The application will open at:

```text
http://localhost:8501
```

## Application Workflow

**Input Text → Text Preprocessing → Word Frequency Calculation → Sentence Scoring → Important Sentence Selection → Final Summary**

## Applications

* Summarizing lengthy articles and documents.
* Preparing short study notes.
* Extracting important information from paragraphs.
* Understanding lengthy text quickly.
* Reducing reading time.

## Future Enhancements

* PDF and document upload support.
* Keyword extraction.
* Improved summarization techniques.
* Support for multiple languages.
* AI-based abstractive summarization.

## Author

**Aarthy V**

GitHub: [aarthy2411](https://github.com/aarthy2411)

## License

This project is developed for educational and learning purposes.
