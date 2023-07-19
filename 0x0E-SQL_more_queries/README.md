# SQL Queries :wink:

This repository contains a collection of SQL queries for various tasks related to managing a MySQL server. Each task focuses on a specific query or operation to perform on the database.

### Task 0: My Privileges

To list the privileges of the MySQL users `user_0d_1` and `user_0d_2`, use the following command:

```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

### Task 1: Root User

To create the MySQL server user `user_0d_1` with all privileges, run the `1-create_user.sql` script:

```bash
cat 1-create_user.sql | mysql -hlocalhost -uroot -p
```

### Task 2: Read User

To create the database `hbtn_0d_2` and the user `user_0d_2` with only SELECT privilege, execute the `2-create_read_user.sql` script:

```bash
cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
```
### Task 3: Always a Name

To create the table `force_name` in the MySQL server, use the `3-force_name.sql` script:

```bash
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```
### Task 4: ID Can't be Null
To create the table `id_not_null` with a default value of 1 for id, use the `4-never_empty.sql` script:

```bash
cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```
### Task 5: Unique ID
To create the table `unique_id` with a unique and auto-generated id, run the `5-unique_id.sql` script:

```bash
cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```
### Task 6: States Table
To create the database `hbtn_0d_usa` and the table states, use the `6-states.sql` script:

```bash
cat 6-states.sql | mysql -hlocalhost -uroot -p
```
### Task 7: Cities Table
To create the database `hbtn_0d_usa` and the table cities with a foreign key constraint, execute the `7-cities.sql` script:

```bash
cat 7-cities.sql | mysql -hlocalhost -uroot -p
```
### Task 8: Cities of California
To list all the cities of California from the `hbtn_0d_usa` database, use the `8-cities_of_california_subquery.sql` script:

```bash
cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```
### Task 9: Cities by States
To list all cities contained in the `hbtn_0d_usa` database along with their corresponding states, run the `9-cities_by_state_join.sql` script:

```bash
cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```
### Task 10: Genre ID by Show
To list all shows from the `hbtn_0d_tvshows` database along with their genre IDs, use the `10-genre_id_by_show.sql` script:

```bash
cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```
### Task 11: Genre ID for All Shows
To list all shows from the `hbtn_0d_tvshows` database along with their genre IDs, including shows without a genre, execute the `11-genre_id_all_shows.sql` script:

```bash
cat `11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows`
```
### Task 12: No Genre
To list all shows from the `hbtn_0d_tvshows` database that do not have a genre linked, use the `12-no_genre.sql` script:

```bash
cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```
### Task 13: Number of Shows by Genre
To list all genres from the `hbtn_0d_tvshows` database along with the number of shows linked to each genre, run the `13-count_shows_by_genre.sql` script:

```bash
cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```
### Task 14: My Genres
To list all genres of the show Dexter from the `hbtn_0d_tvshows` database, use the `14-my_genres.sql` script:

```bash
cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```
### Task 15: Only Comedy
To list all Comedy shows from the `hbtn_0d_tvshows` database, execute the `15-comedy_only.sql` script:

```bash
cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

### Task 16: List Shows and Genres
To list all shows from the `hbtn_0d_tvshows` database along with their linked genres, use the `16-shows_by_genre.sql` script:

```bash
cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```
### Task 17: Not My Genre
To list all genres not linked to the show Dexter from the `hbtn_0d_tvshows` database, use the `100-not_my_genres.sql` script:

```bash
cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

### Task 18: No Comedy Tonight!
To list all shows without the genre Comedy from the `hbtn_0d_tvshows` database, run the `101-not_a_comedy.sql` script:

```bash
cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

### Task 19: Rotten Tomatoes
To list all shows from the `hbtn_0d_tvshows_rate` database along with their ratings, use the `102-rating_shows.sql` script:

```bash
cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
```

### Task 20: Best Genre
To list all genres from the `hbtn_0d_tvshows_rate` database along with their ratings, run the `103-rating_genres.sql` script:

```bash
cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
```

Feel free to explore the repository and execute the scripts to perform the desired tasks on your MySQL server.
Note: Replace -uroot and -p with your MySQL username and password, respectively, if they differ.

If you encounter any issues or have any questions, please feel free to reach out.

Happy querying!
