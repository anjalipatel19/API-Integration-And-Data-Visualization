import requests
import pandas as pd
import matplotlib.pyplot as plt

# NASA API configuration
API_KEY = 'API_KEY'
START_DATE = '2025-05-09'     # Start date (YYYY-MM-DD)
END_DATE = '2025-05-15'       # End date (YYYY-MM-DD)
API_URL = 'https://api.nasa.gov/neo/rest/v1/feed'

def fetch_asteroid_data():
    """Fetch asteroid data from NASA API"""
    try:
        params = {
            'start_date': START_DATE,
            'end_date': END_DATE,
            'api_key': API_KEY
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Check for errors
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    """Process the raw API data into a clean DataFrame"""
    asteroid_counts = []
    asteroid_sizes = []

    # Convert to list of tuples and sort by date
    date_asteroids = sorted(data['near_earth_objects'].items(), key=lambda x: x[0])
    
    for date, asteroids in date_asteroids:
        # Count asteroids for this date
        asteroid_counts.append({
            'Date': date,
            'Count': len(asteroids)
        })
        
        # Calculate average size for this date
        total_size = 0
        for asteroid in asteroids:
            diameter = asteroid['estimated_diameter']['kilometers']
            avg_size = (diameter['estimated_diameter_min'] + diameter['estimated_diameter_max']) / 2
            total_size += avg_size
            
        asteroid_sizes.append({
            'Date': date,
            'Average Size (km)': total_size / len(asteroids)
        })
    
    # Create DataFrames
    count_df = pd.DataFrame(asteroid_counts)
    size_df = pd.DataFrame(asteroid_sizes)
    
    # Convert dates to datetime objects
    count_df['Date'] = pd.to_datetime(count_df['Date'])
    
    size_df['Date'] = pd.to_datetime(size_df['Date'])
    
    # Sort DataFrames by date
    count_df = count_df.sort_values('Date')
    size_df = size_df.sort_values('Date')

    return count_df, size_df

def create_visualizations(count_data, size_data):
    """Create two simple visualizations"""
    plt.figure(figsize=(12, 5))

    # Convert dates to strings for plotting
    date_labels = count_data['Date'].dt.strftime('%Y-%m-%d')
    
    # Asteroid count plot
    plt.subplot(1, 2, 1)
    plt.bar(count_data['Date'].astype(str), count_data['Count'], color='skyblue')
    plt.title('Asteroids Near Earth')
    plt.xlabel('Date')
    plt.ylabel('Number of Asteroids')
    plt.xticks(rotation=45)
    
    # Average size plot
    plt.subplot(1, 2, 2)
    plt.plot(size_data['Date'].astype(str), size_data['Average Size (km)'], 
             marker='o', color='orange')
    plt.title('Average Asteroid Size')
    plt.xlabel('Date')
    plt.ylabel('Diameter (km)')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('asteroid_report.png')
    plt.show()

def main():
    """Main function to run the program"""
    print("Fetching asteroid data from NASA...")
    raw_data = fetch_asteroid_data()
    
    if raw_data:
        print("Processing data...")
        count_df, size_df = process_data(raw_data)
        
        print("Creating visualizations...")
        create_visualizations(count_df, size_df)
        print("Done! Check 'asteroid_report.png' for your visualizations.")
    else:
        print("Failed to get data. Please check your API key and try again.")

if __name__ == "__main__":
    main()