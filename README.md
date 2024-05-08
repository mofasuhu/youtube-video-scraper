# YouTube Video Scraper

YouTube Video Scraper is a Python application built using the Tkinter GUI library that allows users to search for YouTube videos based on keywords, check for specific words within the transcripts of these videos, and retrieve related video information including view counts. The tool is particularly useful for content creators, marketers, and researchers who need to gather insights from YouTube content.

## Features

- Search YouTube videos by keywords.
- Search for specific words within the video transcripts.
- Display video titles, descriptions, and view counts.
- Log errors and issues during the scraping process.
- Save search results in a CSV file format.

## Prerequisites

Before you can run the YouTube Video Scraper, you need to have the following installed:

- Python 3.6 or higher
- Pip (Python package installer)

This application also requires several Python libraries, which can be installed using pip:

```
pip install google-api-python-client
pip install youtube-transcript-api
pip install tkinter
```

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/youtube-video-scraper.git
cd youtube-video-scraper
```

<h2>Setup</h2>
<ol>
    <li>
        <p>Obtain a Google API key:</p>
        <ul>
            <li>Go to the <a target="_new"
                    rel="noreferrer"
                    href="https://console.cloud.google.com/">Google
                    Cloud Console</a>.</li>
            <li>Create a new project.</li>
            <li>Enable the YouTube Data API
                v3.</li>
            <li>Create credentials to get
                your API key.</li>
        </ul>
    </li>
    <li>
        <p>Replace
            <code>'your_api_key'</code> in
            the script with your actual API
            key or better, set it as an
            environment variable for
            security reasons:</p>
    </li>
</ol>

```
import os
developerKey=os.getenv('YOUTUBE_DEVELOPER_KEY')
```

<h2>Usage</h2>
<p>To run the application, execute the following command in the terminal:</p>

```
python YTSCr.py
```

<p>The GUI will prompt you to enter search
    parameters and display results based on
    your queries.</p>
<h2>Contributing</h2>
<p>Contributions to enhance or expand the
    functionality of YouTube Video Scraper
    are welcome. Please follow these steps
    to contribute:</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch
        (<code>git checkout -b feature-branch</code>).
    </li>
    <li>Make your changes.</li>
    <li>Commit your changes
        (<code>git commit -am 'Add some feature'</code>).
    </li>
    <li>Push to the branch
        (<code>git push origin feature-branch</code>).
    </li>
    <li>Create a new Pull Request.</li>
</ol>
<h2>License</h2>
<p>Distributed under the MIT License. See
    <code>LICENSE</code> for more
    information.</p>
<h2>Contact</h2>
<p>Muhammad Farouk - <a target="_new" href="mailto:mofasuhu@gmail.com"
        rel="noreferrer">mofasuhu@gmail.com</a>
</p>
<p>Project Link: <a target="_new"
        rel="noreferrer"
        href="https://github.com/mofasuhu/youtube-video-scraper">https://github.com/mofasuhu/youtube-video-scraper</a>
</p>
<h2>Acknowledgments</h2>
<ul>
    <li>Google APIs for providing the YouTube Data API.</li>
    <li>YouTube Transcript API for
        transcript access.</li>
    <li>All contributors who participate in
        the development of this application.
    </li>
</ul>