import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify, redirect, url_for
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests
import os
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Check if required files exist
required_files = ['nlp_model.pkl', 'tranform.pkl', 'main_data.csv']
for file in required_files:
    if not os.path.exists(file):
        logger.error(f"Required file '{file}' not found. Please make sure it exists in the project directory.")

# Load the nlp model and tfidf vectorizer from disk
try:
    filename = 'nlp_model.pkl'
    clf = pickle.load(open(filename, 'rb'))
    vectorizer = pickle.load(open('tranform.pkl','rb'))
    logger.info("NLP model and vectorizer loaded successfully")
except Exception as e:
    logger.error(f"Error loading model files: {str(e)}")
    clf = None
    vectorizer = None

def create_similarity():
    try:
        data = pd.read_csv('main_data.csv')
        # creating a count matrix
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(data['comb'])
        # creating a similarity score matrix
        similarity = cosine_similarity(count_matrix)
        logger.info("Similarity matrix created successfully")
        return data, similarity
    except Exception as e:
        logger.error(f"Error creating similarity matrix: {str(e)}")
        return None, None

def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
        if data is None or similarity is None:
            return 'Error loading movie data. Please check the logs for more information.'
    
    if m not in data['movie_title'].unique():
        return('Sorry! The movie that you have requested is not in our database. Please check the spelling or try with some other movies')
    else:
        i = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l
    
# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    if not my_list:
        return []
    try:
        my_list = my_list.split('","')
        my_list[0] = my_list[0].replace('["','')
        my_list[-1] = my_list[-1].replace('"]','')
        return my_list
    except Exception as e:
        logger.error(f"Error converting to list: {str(e)}")
        return []

def get_suggestions():
    try:
        data = pd.read_csv('main_data.csv')
        return list(data['movie_title'].str.capitalize())
    except Exception as e:
        logger.error(f"Error getting suggestions: {str(e)}")
        return []

@app.route("/")
@app.route("/home")
def home():
    try:
        suggestions = get_suggestions()
        return render_template('home.html', suggestions=suggestions)
    except Exception as e:
        logger.error(f"Error in home route: {str(e)}")
        return render_template('error.html', error=str(e))

@app.route("/similarity", methods=["POST"])
def similarity():
    try:
        movie = request.form['name']
        rc = rcmd(movie)
        if type(rc)==type('string'):
            return rc
        else:
            m_str="---".join(rc)
            return m_str
    except Exception as e:
        logger.error(f"Error in similarity route: {str(e)}")
        return f"An error occurred: {str(e)}"

@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    try:
        # Check if this is a GET request with movie parameter
        if request.method == "GET" and request.args.get('movie'):
            movie_name = request.args.get('movie')
            # Fetch movie data from API (would typically use TMDB API)
            # For demo purposes, using placeholder data
            
            # Sample data structure for demo
            sample_data = {
                'title': movie_name,
                'poster': 'https://via.placeholder.com/500x750?text='+movie_name.replace(' ', '+'),
                'overview': 'This is a sample overview of the movie. In a real implementation, this would be fetched from a movie API.',
                'vote_average': '8.5',
                'vote_count': '1250',
                'release_date': '2023-01-01',
                'runtime': '120',
                'status': 'Released',
                'genres': 'Drama, Action',
                'imdb_id': 'tt0000000',
                'cast_ids': '[1, 2, 3, 4]',
                'cast_names': '["Actor 1","Actor 2","Actor 3","Actor 4"]',
                'cast_chars': '["Character 1","Character 2","Character 3","Character 4"]',
                'cast_profiles': '["https://via.placeholder.com/150","https://via.placeholder.com/150","https://via.placeholder.com/150","https://via.placeholder.com/150"]',
                'cast_bdays': '["1980-01-01","1982-02-02","1985-03-03","1990-04-04"]',
                'cast_bios': '["Bio 1","Bio 2","Bio 3","Bio 4"]',
                'cast_places': '["Place 1","Place 2","Place 3","Place 4"]',
                'rec_movies': '["Recommended Movie 1","Recommended Movie 2","Recommended Movie 3","Recommended Movie 4"]',
                'rec_posters': '["https://via.placeholder.com/300x450","https://via.placeholder.com/300x450","https://via.placeholder.com/300x450","https://via.placeholder.com/300x450"]',
            }
            
            # Get the recommendations using the rcmd function
            movie_recs = rcmd(movie_name)
            if isinstance(movie_recs, list):
                sample_data['rec_movies'] = json.dumps(movie_recs)
                rec_posters = [f"https://via.placeholder.com/300x450?text={movie.replace(' ', '+')}" for movie in movie_recs]
                sample_data['rec_posters'] = json.dumps(rec_posters)
            
            # Redirect to POST endpoint with sample data
            return render_template('recommend.html', 
                title=sample_data['title'],
                poster=sample_data['poster'],
                overview=sample_data['overview'],
                vote_average=sample_data['vote_average'],
                vote_count=sample_data['vote_count'],
                release_date=sample_data['release_date'],
                runtime=sample_data['runtime'],
                status=sample_data['status'],
                genres=sample_data['genres'],
                movie_cards={rec_posters[i]: movie_recs[i] for i in range(len(movie_recs)) if isinstance(movie_recs, list)},
                reviews={"This is a sample review. In a real implementation, these would be fetched from IMDB.": "Good"},
                casts={f"Actor {i+1}": [i+1, f"Character {i+1}", f"https://via.placeholder.com/150"] for i in range(4)},
                cast_details={f"Actor {i+1}": [i+1, f"https://via.placeholder.com/150", f"1980-0{i+1}-01", f"Place {i+1}", f"Bio {i+1}"] for i in range(4)}
            )
            
        # Handle POST requests from the original code
        elif request.method == "POST":
            # getting data from AJAX request
            title = request.form['title']
            cast_ids = request.form['cast_ids']
            cast_names = request.form['cast_names']
            cast_chars = request.form['cast_chars']
            cast_bdays = request.form['cast_bdays']
            cast_bios = request.form['cast_bios']
            cast_places = request.form['cast_places']
            cast_profiles = request.form['cast_profiles']
            imdb_id = request.form['imdb_id']
            poster = request.form['poster']
            genres = request.form['genres']
            overview = request.form['overview']
            vote_average = request.form['rating']
            vote_count = request.form['vote_count']
            release_date = request.form['release_date']
            runtime = request.form['runtime']
            status = request.form['status']
            rec_movies = request.form['rec_movies']
            rec_posters = request.form['rec_posters']

            # get movie suggestions for auto complete
            suggestions = get_suggestions()

            # call the convert_to_list function for every string that needs to be converted to list
            rec_movies = convert_to_list(rec_movies)
            rec_posters = convert_to_list(rec_posters)
            cast_names = convert_to_list(cast_names)
            cast_chars = convert_to_list(cast_chars)
            cast_profiles = convert_to_list(cast_profiles)
            cast_bdays = convert_to_list(cast_bdays)
            cast_bios = convert_to_list(cast_bios)
            cast_places = convert_to_list(cast_places)
            
            # convert string to list (eg. "[1,2,3]" to [1,2,3])
            if cast_ids:
                cast_ids = cast_ids.split(',')
                cast_ids[0] = cast_ids[0].replace("[","")
                cast_ids[-1] = cast_ids[-1].replace("]","")
            else:
                cast_ids = []
            
            # rendering the string to python string
            for i in range(len(cast_bios)):
                cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"','\"')
            
            # combining multiple lists as a dictionary which can be passed to the html file so that it can be processed easily and the order of information will be preserved
            movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
            
            casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}

            cast_details = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

            # web scraping to get user reviews from IMDB site
            reviews_list = []  # list of reviews
            reviews_status = []  # list of comments (good or bad)
            
            # Add rate limiting and error handling for web scraping
            try:
                sauce = urllib.request.urlopen(f'https://www.imdb.com/title/{imdb_id}/reviews?ref_=tt_ov_rt', timeout=10).read()
                soup = bs.BeautifulSoup(sauce, 'lxml')
                soup_result = soup.find_all("div", {"class": "text show-more__control"})

                for reviews in soup_result:
                    if reviews.string:
                        reviews_list.append(reviews.string)
                        # passing the review to our model
                        if clf and vectorizer:
                            movie_review_list = np.array([reviews.string])
                            movie_vector = vectorizer.transform(movie_review_list)
                            pred = clf.predict(movie_vector)
                            reviews_status.append('Good' if pred else 'Bad')
                        else:
                            reviews_status.append('Unknown')
                            
            except Exception as e:
                logger.error(f"Error scraping IMDB reviews: {str(e)}")
                reviews_list = ["Could not retrieve reviews"]
                reviews_status = ["Unknown"]

            # combining reviews and comments into a dictionary
            movie_reviews = {reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))}     

            # passing all the data to the html file
            return render_template('recommend.html', title=title, poster=poster, overview=overview, vote_average=vote_average,
                vote_count=vote_count, release_date=release_date, runtime=runtime, status=status, genres=genres,
                movie_cards=movie_cards, reviews=movie_reviews, casts=casts, cast_details=cast_details)
        
        else:
            # Redirect to home if neither GET with movie parameter nor POST
            return redirect(url_for('home'))
                
    except Exception as e:
        logger.error(f"Error in recommend route: {str(e)}")
        return render_template('error.html', error=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
