import pandas as pd

def clean_netflix(infile='netflix_titles.csv', outfile='cleaned_netflix.csv'):
    # Load dataset
    df = pd.read_csv(infile)

    # Display basic info
    print("Original Data Shape:", df.shape)
    print("\nMissing values per column:\n", df.isnull().sum())

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values with placeholders
    if 'country' in df.columns:
        df['country'].fillna('Unknown', inplace=True)
    if 'cast' in df.columns:
        df['cast'].fillna('No Cast Info', inplace=True)
    if 'director' in df.columns:
        df['director'].fillna('No Director Info', inplace=True)

    # Convert 'date_added' to datetime if present
    if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Save cleaned data
    df.to_csv(outfile, index=False)
    print("\nCleaned Data Shape:", df.shape)
    print("✅ Data cleaning complete and saved as", outfile)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Clean Netflix dataset')
    parser.add_argument('--infile', default='netflix_titles.csv', help='Input CSV file')
    parser.add_argument('--outfile', default='cleaned_netflix.csv', help='Output cleaned CSV file')
    args = parser.parse_args()
    clean_netflix(args.infile, args.outfile)
