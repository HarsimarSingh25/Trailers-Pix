import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Trailers PIX</title>

    <!-- Including Bootstrap -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    
        <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #333;
            color: #CCC;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #444;
            cursor: pointer;
        }
        .movie-tile img {
            box-shadow: 7px 7px 12px #222;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .two{
          color: #42C0FB;
        }
        .one{
          color: #ADFF2F;
        }
    </style>
    <script src="https://kit.fontawesome.com/bfb58adf21.js" crossorigin="anonymous"></script>
    
    <script type="text/javascript" charset="utf-8">
      $(document).ready(function(){

        // Animate in the movies when the page loads
         $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });

        // Pause the video when the modal is closed
        $('.hanging-close, .modal-backdrop, .modal').on('click',function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $('.movie-tile').on('click', function (event) {
            var trailerYouTubeId = $(this).data('trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
      
       });
      
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"><span class="two"><i class="fab fa-tumblr"></i></span><span class="one"><i class="fab fa-product-hunt"></i></span><span class="two"> Trailers</span><span class="one"> PIX</span></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    {page_no}
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2><b><i>{movie_title}</i></b></h2>
    <p>{movie_storyline}</p>
    <p><b><i>Starring</i></b>: {starring}</p>
    <p><b><i>Director</i></b>: {director}</p>
    <p><b><i>Release date</i></b>: {movie_release_date}</p>
</div>
'''
# Next page 
page_no_contentn = '''
<div class="container text-center">
  <a href="fresh_tomatoes2.html" class="btn btn-success">Next</a>
</div> 
'''

# Previous Page
page_no_contentp = '''
<div class="container text-center">
  <a href="fresh_tomatoes.html" class="btn btn-info">Previous</a>
</div>
'''
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            starring=movie.starring,
            director=movie.director,
            movie_release_date=movie.release_date
        )
    return content

def open_movies_page(movies1, movies2):
    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_contentn = main_page_content.format(movie_tiles=create_movie_tiles_content(movies1),page_no=page_no_contentn)
    # Create or overwrite the output file
    output_file2 = open('fresh_tomatoes2.html', 'w')
    rendered_contentp = main_page_content.format(movie_tiles=create_movie_tiles_content(movies2),page_no=page_no_contentp)
    output_file2.write(main_page_head + rendered_contentp)
    output_file2.close()
    output_file = open('fresh_tomatoes.html', 'w')
    
    # Output the file
    output_file.write(main_page_head + rendered_contentn)
    output_file.close()
    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
