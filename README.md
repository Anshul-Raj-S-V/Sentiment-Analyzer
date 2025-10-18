## SENTIMENT ANALYZER 📝💬😀😞
A web-based application to analyze sentiment in textual reviews using Hugging Face Transformers.
Users can upload a CSV of reviews, and the app provides sentiment classification along with visual summaries (bar and pie charts).

### Project Overview 📝

The Sentiment Analyzer uses state-of-the-art Natural Language Processing (NLP) models to classify text reviews into positive, negative, or neutral sentiments.

It leverages Hugging Face’s distilbert-base-uncased-finetuned-sst-2-english model, a lightweight variant of BERT fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset for sentiment analysis.

    1.Users can upload a CSV file containing textual reviews, and the app will automatically:

    2.Classify each review as Positive, Negative, or Neutral

    3.Display results in a DataFrame

    4.Generate bar and pie charts summarizing sentiment distribution



### Key Features ⚡

    1.CSV Upload: Easily upload a CSV file containing reviews.

    2.Transformer-based NLP: Uses Hugging Face Transformers for accurate sentiment prediction.

    3.Visualization: Automatically generates bar and pie charts for sentiment distribution.

    4.Interactive Web Interface: Built with Gradio for quick, user-friendly interactions.

    5.Lightweight and Fast: Uses DistilBERT, optimized for performance while maintaining accuracy.


    
### Transformer Model Architecture 🧠

  The project uses DistilBERT, a smaller, faster version of BERT, optimized for inference speed while retaining most of BERT’s accuracy.

  Architecture Highlights:

        Based on BERT Transformer encoder layers
    
        Uses attention mechanisms to understand contextual meaning of words

        Fine-tuned on SST-2 dataset for binary sentiment classification

        Outputs probability scores for each sentiment class, selecting the highest as the predicted label

  Why Hugging Face Transformers?

        Pretrained models allow fast deployment without training from scratch

        Optimized for NLP tasks like classification, summarization, and question answering

        Seamless integration with Python pipelines


### Tech Stack 🛠️

    Programming Language : Python 3.12
    NLP & Transformers	 : Hugging Face Transformers, PyTorch
    Data Handling	       : Pandas, NumPy
    Visualization	       : Matplotlib
    Web Interface	       : Gradio
    Deployment	         : Local / Cloud-based Python environment



### Installation 💻

  # Clone the repository:

      git clone https://github.com/YourUsername/Sentiment-Analyzer.git
      cd Sentiment-Analyzer


  # Install dependencies:

    pip install -r requirements.txt


  # Run the Gradio interface:

    python app.py
    Open the URL printed in the terminal (usually http://127.0.0.1:7860) to access the app.



### Usage 🖱️

  1.Click Upload your CSV to select a CSV file of reviews.

  2.The app will process the CSV and return:

  3.A DataFrame with reviews and predicted sentiments

  4.Bar chart showing counts of each sentiment

  5.Pie chart showing the percentage distribution

  6.Scroll to view the results interactively.

  

### CSV File Format 📄

  The CSV must have a column named review containing textual reviews.

  Example:

  review
  I love this product, it works perfectly!
  Very disappointing experience.
  The item is okay, not great.

  
### Visualizations 📊

  Bar Chart: Shows the number of reviews in each sentiment category (Positive, Negative, Neutral).

  Pie Chart: Displays percentage distribution of sentiments.

  Example:

  Positive | ###### 50
  Negative | ### 20


  Pie chart shows slices for each sentiment with percentages.

## UI

Here is the user interface of the Sentiment Analyzer:

![Sentiment Analyzer Interface](https://github.com/Anshul-Raj-S-V/Sentiment-Analyzer/raw/main/1.png)



### Contributing 🤝

    1.Fork the repository

    2.Create a branch: git checkout -b feature-name

    3.Commit your changes: git commit -m "Add feature"

    4.Push: git push origin feature-name

    5.Open a Pull Request
