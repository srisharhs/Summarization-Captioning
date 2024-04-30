# Summarization and Captioning of Academic Research Papers
This project explores automatic summarization and image captioning for academic research papers. It utilizes pre-trained transformer models to extract key information from PDFs containing both text and figures.

**Functionality:**

1. Processes academic research papers in PDF format.
2. Extracts text and figures from the PDF.
3. Summarizes the extracted text using a BERT-based extractive summarizer (specifically, bert-large-uncased).
4. Generates captions for figures using a ViT-gpt2 model.

**Technical Breakdown of Models:**

**_BERT Large Uncased_**:
1. Type: Encoder model 
2. Architecture: Transformer encoder with 12 layers, 768 hidden dimensions, and 1024 feed-forward dimensions.
3. Training Data: Masked Language Modeling (MLM) on a massive dataset of text and code.
4. Strengths: Captures long-range dependencies between words, understands context, effective for various NLP tasks (question answering, summarization).
5. Limitations: Unidirectional (processes text left-to-right only), requires fine-tuning for specific tasks.

_**SBERT paraphraseminiLM**_:
1. Type: Semantic Textual Similarity (STS) model (pre-trained)
2. Architecture: Builds upon Sentence-BERT (BERT for sentence embeddings) with additional training for paraphrase identification.
3. Strengths: Efficient for short text analysis and identifying similar sentences.
4. Limitations: May struggle with complex relationships in longer documents compared to BERT-large-uncased.

**_ViT-gpt2_**:
1. Type: Encoder-decoder architecture likely combining Vision Transformer (ViT) and GPT-2 models.
2. Architecture: (Details may vary) - ViT excels at image recognition by breaking images into patches and processing them with transformers. GPT-2 is a decoder model skilled at generating text. This combination is likely fine-tuned for image captioning tasks.
4. Strengths: Leverages ViT's ability to understand image content and GPT-2's text generation for creating image descriptions.
5. Limitations: Potentially less well-known compared to other models, availability of specific details might be limited.

**Findings**:
bert-large-uncased proved more effective for summarizing large research papers compared to SBERT paraphraseminiLM.
