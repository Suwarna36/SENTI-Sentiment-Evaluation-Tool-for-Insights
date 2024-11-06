# SENTI: Sentiment Evaluation Tool for Insights

## Project Overview
SENTI is a sentiment analysis tool that classifies reviews from an e-commerce platform as either positive or negative. Using machine learning and natural language processing (NLP) techniques, SENTI helps businesses gain insights into customer sentiment, enabling data-driven decisions for improving user satisfaction and enhancing product experiences.

This project leverages Python, Dash, and various NLP libraries to build a user-friendly web app where users can view visual insights (such as pie charts and word clouds) and analyze specific reviews.

## Features
- **Sentiment Classification**: Classifies e-commerce reviews as positive or negative.
- **Interactive Visuals**: Displays a pie chart for sentiment distribution and a word cloud of frequently used terms.
- **Review Search**: Allows users to select or input a review and instantly view its sentiment.
- **User Interface**: Built with Dash for interactivity.

## Technologies Used
- **Python**: Main programming language.
- **Dash**: For web app framework, including `dash_html_components` and `dash_core_components`.
- **Machine Learning**: Scikit-Learn for model training.
- **Natural Language Processing (NLP)**: `TfidfTransformer` and `CountVectorizer` for text transformation and vectorization.
- **Visualization**: Matplotlib and WordCloud for generating charts and word clouds.

## Project Structure
```
SENTI/
├── main.py                 # Main application file for running the Dash app
├── requirements.txt        # Lists all dependencies for the project
├── README.md               # Project documentation (this file)
└── static/                 # Folder for any additional static files
```

## Setup and Installation
To set up this project on your local machine:

### Prerequisites
- Python 3.8+
- Git

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SENTI.git
   cd SENTI
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. **Start the Application**:
   ```bash
   python main.py
   ```

2. **Access the App**:
   - Open a browser and go to `http://127.0.0.1:8050` to view the application locally.

## Usage
1. **View Sentiment Insights**:
   - Navigate to the Pie Chart and Word Cloud sections to view overall sentiment distribution and common terms in reviews.

2. **Select or Input a Review**:
   - Choose a review from the dropdown or type your review in the text area, then click **Find** to analyze the sentiment.

## Files and Directories
- **`main.py`**: Contains the main Dash app code, including loading data, model, and defining the app layout.
- **`requirements.txt`**: Lists all necessary packages (e.g., `dash`, `scikit-learn`, `matplotlib`, `wordcloud`).

## Sample UI 


![PIE_CHART](https://github.com/user-attachments/assets/bf8d2b26-3dda-4c4d-99e2-d707caed08fe)



![WORD_CLOUD](https://github.com/user-attachments/assets/7f3befc8-7d56-4eca-af43-d6af76faf104)



![Dropdown_ReviewSelection](https://github.com/user-attachments/assets/0d527143-711d-46c3-bdd5-e97cf1d7f98c)




![FindSentiment](https://github.com/user-attachments/assets/1a2b2c92-0928-4354-b485-3e32a7b7f540)




## Acknowledgments
- **Forsk Technologies** for the project outline and resources.
