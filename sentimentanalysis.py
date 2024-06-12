import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon if not already downloaded
# nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment():
    user_input = text_entry.get("1.0", "end").strip()

    if user_input:
        # Perform sentiment analysis using VADER
        vader_sentiment = vader_analyzer.polarity_scores(user_input)

        # Perform sentiment analysis using TextBlob
        textblob_blob = TextBlob(user_input)
        textblob_sentiment = textblob_blob.sentiment.polarity

        # Convert sentiment scores to text
        if vader_sentiment['compound'] > 0.5 or textblob_sentiment > 0.5:
            sentiment_text = "Positive"
        elif vader_sentiment['compound'] <= -0.5 or textblob_sentiment < 0:
            sentiment_text = "Negative"
        else:
            sentiment_text = "Neutral"

        messagebox.showinfo("Sentiment Analysis Result",
                            f"Review: {user_input}\n\n"
                            f"VADER Sentiment: {sentiment_text}\n"
                            f"VADER Compound Score: {vader_sentiment['compound']}\n\n"
                            f"TextBlob Sentiment: {sentiment_text}\n"
                            f"TextBlob Polarity Score: {textblob_sentiment}")
                            
    else:
        messagebox.showwarning("Empty Review", "Please enter your review.")

# Create the GUI window
window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("400x400")

# Create a label
label = tk.Label(window, text="Enter your review:")
label.pack(pady=10)

# Create a text entry box
text_entry = tk.Text(window, height=8)
text_entry.pack()

# Create a button to perform sentiment analysis
analyze_button = tk.Button(window, text="Analyze", command=analyze_sentiment)
analyze_button.pack(pady=10)

# Run the GUI
window.mainloop()
