import pickle
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from matplotlib import pyplot as plt
from dash.dependencies import Input, Output, State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import os
from wordcloud import WordCloud, STOPWORDS

# Declaring Global variables
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = None

# Function to load the model and data
def load_model():
    global scrappedReviews, pickle_model, vocab, chart_dropdown_values
    scrappedReviews = pd.read_csv('scrappedReviews.csv')
    
    # Load the sentiment model and vocabulary
    with open("pickle_model.pkl", 'rb') as file:
        pickle_model = pickle.load(file)
    with open("features.pkl", 'rb') as file:
        vocab = pickle.load(file)

    # Prepare dropdown values
    chart_dropdown_values = [
        {"label": review[:80] + '...' if len(review) > 80 else review, "value": review}
        for review in scrappedReviews['reviews']
    ]

# Function to check sentiment of a given review
def check_review(reviewText):
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace", vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))
    return pickle_model.predict(vectorised_review)

# Function to open the browser with the web app
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')

# Function to create the app UI
def create_app_ui():
    return html.Div(
        style={
            'background-color': '#eaeaea', 'padding': '20px', 'text-align': 'center', 'font-family': 'Arial'
        },
        children=[
            html.H1("SENTI - Sentiment Evaluation Tool for Insights", 
                    style={'color': '#333', 'margin-bottom': '20px', 'text-shadow': '1px 1px 2px grey','text-decoration': 'underline'}),

            html.H2("PIE CHART", style={'color': '#333', 'margin': '40px 0', 'text-decoration': 'underline'}),
            html.Div(
                html.Img(src=app.get_asset_url('sentiment.png'), style={'width': '700px', 'height': '400px'}),
                style={'text-align': 'center'}
            ),
            html.Hr(style={'border': '0', 'border-top': '1px solid #ddd', 'margin': '40px 0'}),  # Faded Line

            html.H2("WORD CLOUD", style={'color': '#333', 'margin': '40px 0', 'text-decoration': 'underline'}),
            html.Div(
                html.Img(src=app.get_asset_url('wordCloud.png'), style={'width': '700px', 'height': '400px'}),
                style={'text-align': 'center'}
            ),
            html.Hr(style={'border': '0', 'border-top': '1px solid #ddd', 'margin': '40px 0'}),  # Faded Line

            html.H2("SELECT A REVIEW", style={'color': '#333', 'margin': '40px 0', 'text-decoration': 'underline'}),
            dcc.Dropdown(
                id='Chart_Dropdown',
                options=chart_dropdown_values,
                placeholder='Select a Review',
                style={'font-size': '20px', 'width': '80%', 'margin': '0 auto', 'text-align': 'center'}
            ),
            html.H3(id='sentiment1', children='Sentiment: Missing', style={'color': '#000', 'margin': '20px'}),
            html.Hr(style={'border': '0', 'border-top': '1px solid #ddd', 'margin': '40px 0'}),  # Faded Line

            html.H2("FIND SENTIMENT", 
                    style={'color': '#333', 'margin': '40px 0', 'text-decoration': 'underline'}),

            dcc.Textarea(
                id='textarea_review',
                placeholder='Enter the review here...',
                style={'width': '66%', 'height': '150px', 'font-size': '20px', 'margin': '0 auto'}
            ),
            html.Div(
                dbc.Button(
                    'FIND',
                    id='button_review',
                    color='primary',
                    style={'margin-top': '20px', 'width': '30%', 'font-size': '18px'}
                ),
                style={'display': 'flex', 'justify-content': 'center'}
            ),
            html.H3(id='result', children='Sentiment: Missing', style={'color': '#000', 'margin': '20px'})
        ]
    )

# Callbacks
@app.callback(
    Output('result', 'children'),
    [Input('button_review', 'n_clicks')],
    [State('textarea_review', 'value')]
)
def update_app_ui_2(n_clicks, textarea_value):
    if n_clicks is not None and n_clicks > 0:
        if textarea_value:
            response = check_review(textarea_value)
            result = 'Positive' if response[0] == 1 else 'Negative'
            return f'Sentiment: {result}'
    return 'Sentiment: Missing'

@app.callback(
    Output("sentiment1", "children"),
    [Input("Chart_Dropdown", "value")]
)
def update_sentiment(review1):
    if review1:
        sentiment = 'Positive' if check_review(review1) == 1 else 'Negative'
        return f'Sentiment: {sentiment}'
    return 'Sentiment: Missing'

# Main function
def main():
    load_model()
    open_browser()
    app.title = "SENTI"
    app.layout = create_app_ui()
    app.run_server()

# Start the app
if __name__ == '__main__':
    main()
