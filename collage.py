import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image 

def getWithAndHeight(n):
	n1 = [x for x in range(0,n)]
	n2 = [x for x in range(0,n)]
	result = []
	tab = []
	for x in n1:
		for y in n2:
			if x*y == n:
				result.append([x,y])
	for x in result:
		a = abs(x[0]-x[1])
		tab.append(a)
	tab2 = tab.copy()
	tab.sort()
	return result[tab2.index(tab[0])]

def createArtistsCollage(number,pictureSize,term,reverse,show,filename):
	print("Creating Top Artists Collage")
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0a7744871d6849bba8cdc784285218d9",
	client_secret="f9e2a39cbea94b98b7733602cff3b420",
	redirect_uri="http://localhost",scope="user-top-read"))
	width,height = getWithAndHeight(number)
	if reverse:
		width,height = height,width
	collageSizeWidth = pictureSize*width
	collageSizeHeight = pictureSize*height
	collage = Image.new('RGB', (collageSizeWidth, collageSizeHeight))
	results = sp.current_user_top_artists(limit=number, offset=0, time_range=term)
	y = 0 
	x  = 0
	for idx, item in enumerate(results['items']):
		if x == width:
			y+=1
			x = 0
		url = item["images"][0]["url"]
		response = requests.get(url)
		fileName =f"{idx}a.png"
		file = open(fileName, "wb")
		file.write(response.content)
		file.close()
		im = Image.open(fileName)
		im = im.resize((int(pictureSize),int(pictureSize)))
		collage.paste(im, (x*int(pictureSize), y*int(pictureSize)))
		print(f"{idx}/{number}")
		x+=1
	collage.save(filename)
	if show:
		collage.show()

def createTracksCollage(number,pictureSize,term,reverse,show,filename):
	print("Creating Top Tracks Collage")
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="0a7744871d6849bba8cdc784285218d9",
	client_secret="f9e2a39cbea94b98b7733602cff3b420",
	redirect_uri="http://localhost",scope="user-top-read"))
	width,height = getWithAndHeight(number)
	if reverse:
		width,height = height,width
	collageSizeWidth = pictureSize*width
	collageSizeHeight = pictureSize*height
	collage = Image.new('RGB', (collageSizeWidth, collageSizeHeight))
	results = sp.current_user_top_tracks(limit=number, offset=0, time_range=term)
	y = 0 
	x  = 0
	for idx, item in enumerate(results['items']):
		if x == width:
			y+=1
			x = 0
		url = item["album"]["images"][0]["url"]
		response = requests.get(url)
		fileName =f"{idx}t.png"
		file = open(fileName, "wb")
		file.write(response.content)
		file.close()
		im = Image.open(fileName)
		im = im.resize((int(pictureSize),int(pictureSize)))
		collage.paste(im, (x*int(pictureSize), y*int(pictureSize)))
		print(f"{idx}/{number}")
		x+=1
	collage.save(filename)
	if show:
		collage.show()


createArtistsCollage(6,500,"long_term",True,True,"along_term.png")
createArtistsCollage(10,500,"medium_term",True,True,"amedium_term.png")
createArtistsCollage(20,500,"short_term",True,True,"ashort_term.png")

createTracksCollage(18,500,"long_term",True,True,"tlong_term.png")
createTracksCollage(30,500,"medium_term",True,True,"tmedium_term.png")
createTracksCollage(50,500,"short_term",True,True,"tshort_term.png")
