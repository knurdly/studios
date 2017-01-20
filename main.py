import webapp2
import random

class Index(webapp2.RequestHandler):

    def get_random_movie(self):

        # TODO: make a list with at least 5 movie titles
        movies = [
            "asdf",
            "asdfasdf",
            "asdlfkjw"
        ]
        # TODO: randomly choose one of the movies, and return it
        random_movie_index = random.randomranger(len(movies))
        return movies(random_movie_index)

    def get(self):
        # choose a movie by invoking our new function
        movie = self.get_random_movie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tomorrw_movie = self.get_random_movie
        content+="<h1>asdfasdfjlkdsfa</h1>"
        content+="<p>"  + movie +"</p>""
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
