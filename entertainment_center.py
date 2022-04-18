"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    cm = media.Movie("Housefull 4",
                          "Housefull 4 is a 2019 Indian comedy film and is based on reincarnation, spanning a period of 600 years from 1419 to 2019",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Housefull_4_poster.jpg/220px-Housefull_4_poster.jpg",
                          "https://www.youtube.com/watch?v=gcHH34cEl3Y",
                          "Akshay Kumar,Ritesh Deshmukh,Bobby Deol",
                          "Farhad Samji",
                          "October 25, 2019")

    ae = media.Movie("Joker(2019)",
                          "Joker is a 2019 American psychological thriller film that follows Arthur Fleck, a failed stand-up comedian who turns to a life of crime and chaos in Gotham City",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcSJKLiEyyz1Q9RC8EBYl3ijr3nuGeyO2ETmwy6Kdq0AQtD0elWD",
                          "https://www.youtube.com/watch?v=zAGVQLHvwOY",
                          "Joaquin Phoenix, Robert De Niro, Zazie Beetz",
                          "Todd Phillips",
                          "August 31, 2019")

    sm = media.Movie("Star Wars:ROS",
                           "Star Wars: The Rise of Skywalker is an American epic space opera film and will be the third installment of the Star Wars sequel trilogy.",
                           "https://upload.wikimedia.org/wikipedia/en/a/af/Star_Wars_The_Rise_of_Skywalker_poster.jpg",
                           "https://www.youtube.com/watch?v=8Qn_spdM5Zg",
                           "Billie Lourd, Daisy Ridley, Carrie Fisher",
                           "J.J. Abrams",
                           "December 20, 2019")

    xm = media.Movie("Dabangg 3",
                         "Dabangg 3 is an action comedy film and is the third installment of Dabangg series.",
                         "https://upload.wikimedia.org/wikipedia/en/8/89/Dabangg_3_poster.jpg",
                         "https://www.youtube.com/watch?v=-AJ7cLi1Jfk",
                         "Salman Khan, Sonakshi Sinha, Sudeep",
                         "Prabhu Deva",
                         "December 20, 2019")

    sz = media.Movie("Jumanji:The Next Level",
                           "Jumanji: The Next Level is an upcoming American fantasy adventure comedy film and is a sequel of Jumanji: Welcome to the Jungle",
                           "https://upload.wikimedia.org/wikipedia/en/3/3c/JumanjiTheNextLevelTeaserPoster.jpg",
                           "https://www.youtube.com/watch?v=rBxcF-r9Ibs",
                           "Karen Gillan, Dwayne Johnson, Madison Iseman",
                           "Jake Kasdan",
                           "December 13, 2019")
    ach = media.Movie("WAR(2019)",
                          "War(2019) is a action thriller film that follows an Indian soldier assigned to eliminate his former mentor who has gone rogue.",
                          "https://upload.wikimedia.org/wikipedia/en/6/6f/War_official_poster.jpg",
                          "https://www.youtube.com/watch?v=tQ0mzXRk-oM",
                          "Hrithik Roshan, Tiger Shroff, Vaani Kapoor",
                          "Siddharth Anand",
                          "October 2, 2019")

    cma = media.Movie("Captain Marvel",
                          "Carol Danvers becomes one of the universe's most powerful heroes when Earth is caught in the middle of a galactic war between two alien races",
                          "https://stat.ameba.jp/user_images/20190108/19/jumbooomori/68/06/j/o0821120014335603368.jpg?caw=800",
                          "https://www.youtube.com/watch?v=0LHxvxdRnYc",
                          "Brie Larson, Samuel L. Jackson",
                          " Anna Boden, Ryan Fleck",
                          "March 8, 2019")

    ksa = media.Movie("Kabir Singh",
                      "Kabir Singh is a movie where a short-tempered house surgeon gets used to drugs and drinks when his girlfriend is forced to marry another person",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Kabir_Singh.jpg/220px-Kabir_Singh.jpg",
                      "https://www.youtube.com/watch?v=RiANSSgCuJk",
                      "Shahid Kapoor, Kiara Advani",
                      "Sandeep Reddy Vanga",
                      "June 20, 2019")

    aea = media.Movie("Avengers: EndGame",
                          "With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
                          "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg",
                          "https://www.youtube.com/watch?v=TcMBFSGVi1c",
                          "Robert Downey Jr., Chris Evans, Mark Ruffalo",
                          "Anthony Russo, Joe Russo",
                          "April 26, 2019")
    
    cha = media.Movie("Chhichhore",
                      "Following a group of friends from university as they progress into middle-age life and go their own separate ways.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Chhichhore_Poster.jpg/220px-Chhichhore_Poster.jpg",
                      "https://www.youtube.com/watch?v=tsxemFX0a7k",
                      "Sushant Singh,Shraddha Kapoor,Varun Sharma",
                      "Nitesh Tiwari",
                      "September 6, 2019")

    sma = media.Movie("Spider-Man: FFH",
                           "Following the events of Avengers: Endgame (2019), Spider-Man must step up to take on new threats in a world that has changed forever.",
                           "https://terrigen-cdn-dev.marvel.com/content/prod/1x/sffh_venice-high-res.jpg",
                           "https://www.youtube.com/watch?v=Nt9L1jCKGnE",
                           "Tom Holland, Samuel L. Jackson",
                           "Jon Watts",
                           "July 5, 2019")

    sua = media.Movie("Super 30",
                      "Based on life of Patna-based mathematician Anand Kumar who runs the famed Super 30 program for IIT aspirants in Patna.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Super_30_The_Film.jpg/220px-Super_30_The_Film.jpg",
                      "https://www.youtube.com/watch?v=QpvEWVVnICE",
                      "Hrithik Roshan, Mrunal Thakur, Nandish Singh",
                      "Vikas Bahl",
                      "July 12, 2019")


    # Store the Movie objects in a list.
    movies = [cm, ae, sm, xm, sz, ach]
    movies2 = [cma,ksa,aea,cha,sma,sua]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies, movies2)

if __name__ == '__main__':
    main()
