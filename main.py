import requests
import matplotlib.pyplot as plt

# OMDb API
def fetch_movie_data(title, api_key):
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        if movie_data['Response'] == "True":
            return movie_data
        elif movie_data['Error'] == "Invalid API key!":
            print("Error: Invalid API Key.")
        elif movie_data['Error'] == "Request limit reached!":
            print("Error: API request limit reached.")
        else:
            print(f"Movie '{title}' not found.")
    else:
        print("Error fetching data from OMDb API.")
    return None

# Function to get average rating
def average_rating(movies):
    ratings = [float(movie['imdbRating']) for movie in movies if movie and movie['imdbRating'] != 'N/A']
    return sum(ratings) / len(ratings) if ratings else 0

# Function to analyze genres
def genre_analysis(movies):
    genre_count = {}
    for movie in movies:
        if movie:
            genres = movie['Genre'].split(", ")
            for genre in genres:
                genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count

# Function to plot the top movies by rating
def plot_top_movies(movies):
    # Sort movies by rating
    sorted_movies = sorted([movie for movie in movies if movie], key=lambda x: float(x['imdbRating']), reverse=True)
    top_movies = sorted_movies[:5]  # Get top 5 movies
    
    titles = [movie['Title'] for movie in top_movies]
    ratings = [float(movie['imdbRating']) for movie in top_movies]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.barh(titles, ratings, color='skyblue')
    plt.xlabel("IMDb Rating")
    plt.title("Top 5 Movies by IMDb Rating")
    plt.gca().invert_yaxis()  # Highest rating on top
    plt.show()

# Function to plot genre distribution
def plot_genre_distribution(genre_count):
    genres = list(genre_count.keys())
    counts = list(genre_count.values())
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.pie(counts, labels=genres, autopct='%1.1f%%', startangle=140)
    plt.title("Genre Distribution")
    plt.show()

# Main function to run the Movie Rating Analyzer
def main():
    api_key = 'f3230988'  

    # Prompt user to input at least 3 movie names
    movie_titles = []
    while len(movie_titles) < 3:
        titles_input = input("Enter movie names separated by commas (at least 3 movies): ")
        movie_titles = [title.strip() for title in titles_input.split(",") if title.strip()]
        if len(movie_titles) < 3:
            print("Please enter at least 3 movie names.")
    
    # Fetch movie data for each title
    movies = []
    for title in movie_titles:
        movie = fetch_movie_data(title, api_key)
        movies.append(movie)
    
    # Calculate average rating
    avg_rating = average_rating(movies)
    print(f"\nAverage IMDb Rating of Selected Movies: {avg_rating:.2f}")

    # Analyze genres
    genre_count = genre_analysis(movies)
    print("\nGenre Distribution:")
    for genre, count in genre_count.items():
        print(f"{genre}: {count}")
    
    # Plotting
    plot_top_movies(movies)
    plot_genre_distribution(genre_count)

if __name__ == "__main__":
    main()
