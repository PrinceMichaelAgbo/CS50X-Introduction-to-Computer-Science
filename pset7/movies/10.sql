--write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.


SELECT name FROM people WHERE people.id IN
(

    SELECT directors.person_id FROM directors WHERE directors.movie_id IN
    (

        SELECT movies.id from movies JOIN ratings ON movies.id = ratings.movie_id WHERE rating >= 9.0

    )

);