import matplotlib.pyplot as plt


def create_rating_histogram():
    """
        Creates and saves a histogram of movie ratings.

        This function:
        - Retrieves movie data from the storage.
        - Extracts the ratings from the movie data.
        - Plots a histogram of the ratings, assuming integer ratings between 0 and 10.
        - Prompts the user to enter a file name to save the histogram.
        - Saves the histogram as an image file and clears the plot for future use.
    """
    movies = get_movies()
    ratings = [value["rating"] for value in movies.values()]

    if not ratings:
        print("No ratings available to create a histogram.")
        return

    # Plot the histogram
    plt.hist(ratings, bins=range(0, 12), edgecolor='black', align='left')
    plt.title('Movie Rating Histogram')
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.xticks(range(0, 11))  # Assuming ratings are integers between 0 and 10

    file_name = input("Enter the file name to save the histogram (e.g., 'histogram.png'): ")

    plt.savefig(file_name)
    print(f"Histogram saved as {file_name}")
    plt.clf()