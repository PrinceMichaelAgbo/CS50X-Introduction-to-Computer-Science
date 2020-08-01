--write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

SELECT name FROM people WHERE people.id IN
(
    SELECT stars.person_id from stars JOIN movies ON movies.id = stars.movie_id WHERE
    stars.movie_id IN
    (
        SELECT movie_id from movies JOIN stars ON movies.id = stars.movie_id WHERE stars.person_id IN
            (SELECT people.id FROM people WHERE name = "Kevin Bacon" AND birth = 1958)
    )
    AND stars.person_id NOT IN (SELECT people.id FROM people WHERE name = "Kevin Bacon" AND birth = 1958)
    --all the ids of the movies where Kevin Bacon stars in
);