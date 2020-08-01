--write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated

SELECT title FROM movies join ratings ON movies.id = ratings.movie_id WHERE movies.id IN
(
    SELECT ratings.movie_id FROM ratings WHERE ratings.movie_id IN -- gets the ratings of movies in which chad Boseman starred in
    (
        SELECT movie_id from movies JOIN stars ON movies.id = stars.movie_id WHERE stars.person_id IN --gets the id's of movies in which chad boseman starred in
        (
            SELECT people.id FROM people WHERE name = "Chadwick Boseman"
        )
    )

)  ORDER BY ratings.rating DESC LIMIT 5