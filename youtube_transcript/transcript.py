from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time
import re


def format_title(raw_title):

	stripped_str = raw_title.strip()
	alphanum_str = re.sub("[^0-9a-zA-Z ]+", "", stripped_str.strip())
	formated_title = re.sub(" +", "_", alphanum_str)

	return formated_title

class YoutubeTranscript():

	def __init__(self):
		
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
		
		self.base_url = 'https://www.youtube.com'

		self.browser = webdriver.Chrome()

		DELAY=20
		self.wait = WebDriverWait(self.browser,DELAY)

	def prep_playlist(self,playlist_url):

		datetime = time.strftime("%d_%b_%H_%M", time.localtime() )
		playlist_filename = "playlist_yts_{}.txt".format(datetime)

		self.browser.get(playlist_url)

		playlist_content = self.browser.find_element_by_id("contents")
		video_elements = playlist_content.find_elements_by_id("content")

		all_links=[]
		all_titles=[]

		for each_video in video_elements:

			video_anchor = each_video.find_element_by_tag_name("a")

			video_link = video_anchor.get_attribute('href').split('&')[0]
			title_element = each_video.find_element_by_id('video-title')
			
			raw_title = title_element.get_attribute("title")

			# formated_title = format_title( raw_title )

			all_links.append( video_link )
			all_titles.append( raw_title )


		with open(playlist_filename,'w') as file:

			for i in range(len(all_links)):
				file.writelines(all_links[i]+"<sep>"+all_titles[i]+"\n")
			file.close()

		return all_titles,all_links	

	def transcript_video(self,url,filename):

		self.browser.get( url )

		try:
			options_btn = self.wait.until( 
				EC.presence_of_element_located(
					( By.XPATH, "*//button[@aria-label='More actions']" )
				) 
			)
		except TimeoutException:
			print("Timeout reached.")

		options_btn.click()

		try:
			transcript_btn = self.wait.until( 
				EC.presence_of_element_located(
					( By.XPATH,
					 "*//yt-formatted-string[text() = 'Open transcript']" )
				)
			)
		except TimeoutException:
			print("Timeout reached. ")

		transcript_btn.click()

		try:
			transcript_body = self.wait.until( 
						EC.presence_of_element_located(
							( By.XPATH, "*//ytd-transcript-renderer//div[@id='body']" )
						) 
					)
		except TimeoutException:
			print("Timeout time ")

		transcript_parts = transcript_body.find_elements_by_xpath(
					"*//div[@role='button']"
				   )

		whole_transcript = ""
		for each_part in transcript_parts:
			text_part = each_part.get_attribute("innerText")+" "
			whole_transcript = whole_transcript+text_part

		with open("{}.txt".format(filename),'w') as file:
			file.write( whole_transcript )
			file.close()

		print("Transcript collected from - {}".format(url))

	def transcript_playlist(playlist_url):

		titles,links = prep_playlist(playlist_url)
		for i in range( len(titles) ):
			transcript_video( links[i], titles[i])

		print("All transcripts of playlist collected.")

