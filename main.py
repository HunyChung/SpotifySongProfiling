import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from dotenv import load_dotenv
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt


# Load variables from .env file
load_dotenv()

# Get environment variables
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')


def main():

    # Setup auth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read playlist-read-private"
    ))

    print(sp.current_user())

    
    features = sp.audio_features(['3n3Ppam7vgaVa1iaRUc9Lp'])
    print(features)
    # token_info = sp.auth_manager.get_access_token(as_dict=True)
    # print("Token info:", token_info)
    # if not token_info or not token_info.get("access_token"):
    #     print("Failed to get access token. Check your credentials and redirect URI.")

    # # --- 1. Load data from Spotify API ---
    # # Get user's saved tracks (limit to 100 for simplicity)
    # results = sp.current_user_saved_tracks(limit=10)
    # tracks = results['items']

    # # Extract track IDs and names
    # track_ids = [item['track']['id'] for item in tracks if item['track']['id'] is not None]
    # song_names = [item['track']['name'] for item in tracks if item['track']['id'] is not None]

    # # Get audio features for these tracks
    # features_list = sp.audio_features(track_ids)

    # # Build DataFrame
    # data = pd.DataFrame([{
    #     'danceability': f['danceability'],
    #     'energy': f['energy'],
    #     'valence': f['valence'],
    #     'tempo': f['tempo'],
    #     'acousticness': f['acousticness'],
    #     'popularity': tracks[i]['track']['popularity'],
    #     'song_name': song_names[i]
    # } for i, f in enumerate(features_list) if f is not None])

    # # --- 2. Normalize features ---
    # features = ['danceability', 'energy', 'valence', 'tempo', 'acousticnepython --versionss', 'popularity']
    # scaler = StandardScaler()
    # data_scaled = scaler.fit_transform(data[features])

    # # --- 3. Run K-Means clustering ---
    # k = 4  # You can experiment with different values
    # kmeans = KMeans(n_clusters=k, random_state=42)
    # data['cluster'] = kmeans.fit_predict(data_scaled)

    # # --- 4. Visualize clusters ---
    # sns.pairplot(data, hue='cluster', vars=features[:4])
    # plt.suptitle("Clustered Songs Based on Audio Features", y=1.02)
    # plt.show()

    # # --- 5. Analyze clusters ---
    # cluster_summary = data.groupby('cluster')[features].mean()
    # print("\nCluster Feature Averages:")
    # print(cluster_summary)

    # # Optional: Show top 3 songs per cluster
    # for c in range(k):
    #     print(f"\nCluster {c} sample songs:")
    # print(data[data['cluster'] == c]['song_name'].head(3).to_string(index=False))


# Run the main function
if __name__ == "__main__":
        main()