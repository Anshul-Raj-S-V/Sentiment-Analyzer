from transformers import pipeline
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

# Initialize Hugging Face sentiment analyzer
analyzer = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analyser(review):
    """Return the sentiment label of a review"""
    sentiment = analyzer(review)
    return sentiment[0]['label']

def generate_sentiment_barchart(df):
    """Generate a matplotlib bar chart from a DataFrame with 'sentiment' column"""
    if 'Sentiment' not in df.columns:
        raise ValueError("DataFrame must have a 'Sentiment' column")
    
    sentiment_counts = df['Sentiment'].value_counts()
    fig1, ax = plt.subplots(figsize=(3, 4))
    bars = ax.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red', 'gray'])
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1, str(height), ha='center', va='bottom')
    
    ax.set_title("Sentiment Analysis Summary")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Reviews")
    ax.set_ylim(0, max(sentiment_counts.values) + 2)
    
    fig2, ax2 = plt.subplots(figsize=(3,3))
    ax2.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%',
            colors=['green', 'red', 'gray'], startangle=90, counterclock=False)
    ax2.set_title("Sentiment Analysis Summary (Pie Chart)")
    
    return fig1,fig2

def process_csv(file_obj):
    """Read CSV, compute sentiment, and return DataFrame and bar chart figure"""
    df = pd.read_csv(file_obj.name,encoding='latin1')
    
    if 'review' not in df.columns:
        raise ValueError("No 'review' column found in the CSV file.")
    
    df['Sentiment'] = df['review'].apply(sentiment_analyser)
    
    fig1,fig2 = generate_sentiment_barchart(df)
    
    return df, fig1,fig2

# Gradio interface
with gr.Blocks(title="SENTIMENT ANALYZER") as demo:
    with gr.Row():
        with gr.Column():
            chart_bar = gr.Plot(label="Bar Chart")
            chart_pie = gr.Plot(label="Pie Chart")
        with gr.Column():
            csv_input = gr.File(file_types=[".csv"], label="Upload your CSV")
            df_output = gr.Dataframe(label="Sentiments")

    csv_input.change(
        fn=process_csv,
        inputs=[csv_input],
        outputs=[df_output, chart_bar, chart_pie]
    )

demo.launch()

