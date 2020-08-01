--write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred

SELECT title FROM movies WHERE movies.id IN
(
    SELECT movies.id from movies JOIN stars ON movies.id = stars.movie_id WHERE
    movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Johnny Depp"))

    AND

    movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Helena Bonham Carter"))
);