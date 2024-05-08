import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
import csv
import logging
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import time
import html

# Initialize the YouTube Data API with the developer key. Replace 'your_api_key' with your actual API key.
youtube = build('youtube', 'v3', developerKey='your_api_key')
  
def decode_html_entities(text):
    """Convert HTML entities to their corresponding characters in a given text."""
    return html.unescape(text)
    
def setup_logging():
    """Configure the logging system to record errors into a file."""
    logging.basicConfig(filename='vidlog.log', level=logging.ERROR, format='%(message)s')

def close_logging():
    """Shutdown the logging system gracefully."""
    logging.shutdown()

def cleanup_logging():
    """Remove the logging file if it has no content to clean up disk space."""
    close_logging()
    if os.path.exists('vidlog.log') and os.path.getsize('vidlog.log') == 0:
        os.remove('vidlog.log')
   
def fetch_all_videos(keyword):
    """Retrieve all YouTube videos matching a specific keyword via the YouTube Data API."""
    videos = []
    request = youtube.search().list(q=keyword, part='snippet', type='video', maxResults=50)
    while request is not None:
        response = request.execute()
        for item in response.get('items', []):
            videos.append({'title': item['snippet']['title'], 'videoId': item['id']['videoId'], 'description': item['snippet']['description']})
        request = youtube.search().list_next(request, response)
    return videos

def search_transcript(video_id, search_word):
    """Search for a specific word in the YouTube video transcript and return the minute it was found if present."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ar', 'en', 'fr', 'de', 'it', 'es'])
        for text in transcript:
            if search_word.lower() in text['text'].lower():
                minutes = int(text['start'] // 60)
                return True, minutes
    except Exception as e:
        logging.error(f"Error retrieving transcript for video {video_id}: {str(e)}")
    return False, None    

def get_video_views(video_id):
    """Retrieve view count for a given YouTube video using the video ID."""
    request = youtube.videos().list(part="statistics", id=video_id)
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]['statistics']['viewCount']
    else:
        return "No Views Data Found"

def main_app():
    """Set up the GUI for the YouTube Video Scraper application."""
    root = tk.Tk()
    root.title("YouTube Video Scraper")
    root.geometry("900x800")

    tk.Label(root, text="Enter video search keyword:").pack(pady=10)
    search_var = tk.StringVar()
    search_entry = tk.Entry(root, textvariable=search_var, width=50)
    search_entry.pack()

    tk.Label(root, text="Enter transcript search keyword:").pack(pady=10)
    transcript_var = tk.StringVar()
    transcript_entry = tk.Entry(root, textvariable=transcript_var, width=50)
    transcript_entry.pack()

    status_text = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_text)
    status_label.pack()    
    
    results_text = scrolledtext.ScrolledText(root, height=20, width=150)
    results_text.pack(pady=20)
    
    def on_search():
        """Handle the search button click event by fetching videos, checking transcripts, and displaying results."""
        # Clean up any previous log and result files        
        if os.path.exists('vidlog.log'):
            logging.shutdown()
            os.remove('vidlog.log')
        if os.path.exists('results.csv'):
            os.remove('results.csv')     
        setup_logging()
        results_text.delete(1.0, tk.END)  # Clear previous results
        search_word = search_var.get()
        transcript_keyword = transcript_var.get()
        if not search_word or not transcript_keyword:
            messagebox.showerror("Error", "Please enter both search and transcript keywords")
            return

        videos = fetch_all_videos(search_word)
        status_text.set(f"{len(videos)} videos found.")
        root.update()
        time.sleep(2)
        results = []
        for i, video in enumerate(videos):
            status_text.set(f"Processing video {i+1} of {len(videos)}")
            root.update()
            found, minute = search_transcript(video['videoId'], transcript_keyword)
            if found:
                views = get_video_views(video['videoId'])
                title_decoded = decode_html_entities(video['title'])
                description_decoded = decode_html_entities(video['description'])
                results.append((video['videoId'], title_decoded, views, minute, description_decoded))
                results_text.insert(tk.END, f"Video ID - Word Minute: {video['videoId']} - {minute} \nTitle: {title_decoded}\nViews: {views}\nVideo Description: {description_decoded}\n\n")
        time.sleep(2)        
        status_text.set(f"From the {len(videos)} videos, there are {len(results)} videos having a transcript and \"{transcript_keyword}\" in their transcript.")
        root.update()
        with open("results.csv", 'w', newline='', encoding='utf-8-sig') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Video ID', 'Title', 'Views', 'Minute', 'Description'])
            for result in results:
                csv_writer.writerow(result)

    search_button = tk.Button(root, text="Search", command=on_search)
    search_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    try:
        main_app()
    finally:
        cleanup_logging()
        