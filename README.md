# youtube-transcript

This is an CLI to provide automate scraping of youtube transcript using headless browser for playlists.

# Why?
Allows you to scrape transcript from a video or a complete playlist. Also can be used for learning purposes.

Yes, Youtube provides a official API for transcript fetching. For scraping on large scale, it is the best solution.

But if you are looking for quick solution for a some videos or a playlist, this package is for you.

# Usage
- First, clone the repo. Using `git clone https://github.com/Help-a-Sloth/youtube-transcript.git`
- Use Cmd Line, and make traverse to the cloned repo. Execute the command as in following example.

**Example -**

For a video -

    python -m youtube_transcript -v=VIDEO_URL

For a playlist -

    python -m youtube_transcript -p=PLAYLIST_URL
	
	
**Arguments -**

**--path PATH** : Path where prepared transcript has to be saved.

**-v VIDEO, --video VIDEO** : Youtube Video URL of which transcript has to scraped.

**-p PLAYLIST, --playlist PLAYLIST** :  Youtube Playlist URL for scraping all added video's transcript.

**Feel free to contribute to help other and provide feedback.**
