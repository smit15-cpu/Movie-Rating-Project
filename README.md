[README.md](https://github.com/user-attachments/files/17530360/README.md)
# Movie Analyzer 🎬


A Python project to analyze IMDb ratings and genres of user-selected movies, displaying insights through visualizations. Users can input multiple movie names, and the program fetches relevant data from the OMDb API to compute the average rating, analyze genre distribution, and showcase the top-rated movies in easy-to-read graphs.

## Features
- **User-Defined Movies**: Allows users to input their favorite movie titles.
- **Average Rating Calculation**: Computes the average IMDb rating of selected movies.
- **Genre Distribution**: Analyzes genres across all selected movies.
- **Top 5 Movies**: Displays the highest-rated movies in a bar chart.
- **Visualizations**: Provides graphical insights through genre distribution (pie chart) and top ratings (bar chart).

## Project Structure
```plaintext
movie-rating-analyzer/
├── movie_rating_analyzer.py  # Main program file
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
└── .env                      # Contains API key (not shared)
```

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/movie-rating-analyzer.git
   cd movie-rating-analyzer
   ```

2. **Install Dependencies**
   - Ensure you have Python 3.x installed. Install required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **Get an OMDb API Key**
   - Sign up at [OMDb API](http://www.omdbapi.com/apikey.aspx) to get a free API key.
   - Add this key to a `.env` file in the root directory:
     ```plaintext
     OMDB_API_KEY=your_api_key_here
     ```

## Usage

1. **Run the Program**
   ```bash
   python movie_rating_analyzer.py
   ```

2. **Enter Movie Names**: 
   - The program will prompt you to enter at least three movie names (comma-separated). Example:
     ```plaintext
     Enter movie names separated by commas (at least 3 movies): Inception, The Matrix, Parasite
     ```

3. **View Results**: 
   - The program calculates and prints the average rating, displays genre distribution, and shows the top 5 movies by rating in bar and pie charts.

## Example Output

- **Average IMDb Rating**: Displays the computed average rating for all entered movies.
- **Genre Distribution**: Shows the percentage of each genre among the selected movies.
- **Top 5 Movies by Rating**: Bar chart of the top 5 movies by IMDb rating.

## Screenshots

> **Top 5 Movies Bar Chart**
![1](https://github.com/user-attachments/assets/be37b371-8951-414b-bbe7-3239c9af0d91)


> **Genre Distribution Pie Chart**
![2](https://github.com/user-attachments/assets/99df3f14-c9b6-4ffc-bf55-2d6cada085ff)

## Contributing
Contributions are welcome! Please feel free to open issues, submit pull requests, or suggest features.

