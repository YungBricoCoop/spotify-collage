# spotify-collage
Create collage for top artists and tracks

To create collage for artists just use the method :
<br>    <code> createArtistsCollage(numberOfArtists,pictureSize,term,reverse,show,filename)</code><br><br>
To create collage for tracks just use the method :
<br>    <code> createArtistsCollage(numberOfArtists,pictureSize,term,reverse,show,filename)</code><br><br>
  <b>numberOfArtists</b> : Number of artists picture displayed on the collage <br>
  <b>pictureSize</b> : int, Size of each individual picture of the collage in pixels<br>
  <b>term</b>        : String, long_term, medium_term, short_term <br>
  <b>reverse</b>     : boolean, vertical or horizontal<br>
  <b>show</b>        : boolean, show image when done<br>
  <b>filename</b>    : String, path and extension of the file to save<br>
  
  Examples : 
  
<code>createArtistsCollage(10,500,"medium_term",True,True,"amedium_term.png")
createArtistsCollage(20,500,"short_term",True,True,"ashort_term.png")

createTracksCollage(18,500,"long_term",True,True,"tlong_term.png")
createTracksCollage(30,500,"medium_term",True,True,"tmedium_term.png")</code>
