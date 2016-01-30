import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""
	VALID_RATINGS = ["G","PG","PG-13","R"]

	#initialize space for the movies' description
	def __init__(self,title,storyline,image,youtube):
		self.title=title
		self.storyline=storyline
		self.poster_image_url=image
		self.trailer_youtube_url=youtube

	#method to open a browser and show trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

