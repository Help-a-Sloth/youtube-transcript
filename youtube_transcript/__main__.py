import argparse
from .transcript import *

parser = argparse.ArgumentParser(
			prog="youtube-transcript",
			description="A CLI to provide automated scraping of youtube transcript using a headless browser from videos and playlists.",
			epilog="Thanks for Using.")

parser.add_argument(
					'--path',
					type=str,
					default=".",
					help="Path where prepared transcript has to be saved."					
					)

parser.add_argument(
					'-v',
					'--video',
					type=str,
					help="Youtube Video URL of which transcript has to scraped."
					)

parser.add_argument(
					'-p',
					'--playlist',
					type=str,
					help=("Youtube Playlist URL for scraping all added video's transcript.")
					)

args = parser.parse_args()


if args.video!=None:
	
	yt_obj = YoutubeTranscript()
	yt_obj.transcript_video( args.video, args.path )

elif args.playlist!=None:
	
	yt_obj = YoutubeTranscript()
	yt_obj.transcript_playlist( args.playlist, args.path )
	
else:
	raise( 
		Exception( 
			("Either video or playlist URL has to be provided.\n"
			 "Example youtube_transcript -v=URL or -p=URL."	)	
		)
	)


print("Thanks for using. See 'Help-a-Sloth' on GitHub.")

