# Python-CodeScreen-Films-API

The CodeScreen Film API is a service that contains one endpoint,<br/>
`GET https://app.codescreen.dev/api/assessments/films`, which returns the details of a large number of different films.

When you send an `HTTP GET` request to the endpoint, the response will be a `200 OK`, which includes a body containing a list of film data in `JSON` format. 
<br>

For authentication, you need to send your API token in the `Authorization HTTP header` using the [Bearer authentication scheme](https://tools.ietf.org/html/draft-ietf-oauth-v2-bearer-20#section-2.1). Your API token is `8c5996d5-fb89-46c9-8821-7063cfbc18b1`.

Here is an example of how to send the request from [cURL](https://curl.haxx.se/):

    curl -H "Authorization: Bearer 8c5996d5-fb89-46c9-8821-7063cfbc18b1" \
    https://app.codescreen.dev/api/assessments/films

An example response is the following:

     [
       {
         "name": "Batman Begins",
         "length": 140,
         "rating": 8.2,
         "releaseDate": "2006-06-16",
         "directorName": "Christopher Nolan"
       },
       {
         "name": "Alien",
         "length": 117,
         "rating": 8.4,
         "releaseDate": "1979-09-06",
         "directorName": "Ridley Scott"
       }
     ]


The `name` field represents the name of the film. The `length` field represents the duration of the film in minutes. The `rating` is the <a href="https://www.imdb.com/" target="_blank">`IMDb`</a> rating for the film, out of 10.
The `releaseDate` is the date in which the film was released in the United Kingdom, and the `directorName` field is the name of the film's director.

## Your Task

You are required to implement all the methods marked with `TODO Implement` in the [FilmsAPIService](films/films_api_service.py) and [FilmDataStatsGenerator](films/films_data_stats_generator.py) classes in such a way that
all the unit tests in [test_films_data_stats_generator.py](test/test_films_data_stats_generator.py) pass.

[FilmsAPIService](films/films_api_service.py) should be implemented in such a way that you only need to call out to the CodeScreen Films API
endpoint once per full run of the [test_films_data_stats_generator.py](test/test_films_data_stats_generator.py) test suite.

## Requirements

The [test_films_data_stats_generator.py](test/test_films_data_stats_generator.py) file should not be modified. If you would like to add your own unit tests, you
can add these in a separate file in the `test` folder.

The [requirements.txt](requirements.txt) file should only be modified to add any third-party dependencies required for your solution.<br> Please note that all third-party depdencies required for your solution **MUST** be added to the [requirements.txt](requirements.txt) file.

You are free to use whichever libraries you want (Python or third-party) when implementing your solution. </br>
Note we recommend using the <a href="https://docs.python.org/3.7/library/datetime.html" target="_blank">`Python datetime`</a> library for working with dates, and the <a href="https://pypi.org/project/requests/" target="_blank">`Requests`</a> HTTP client library to interact with the CodeScreen Film API service.

Your solution also must use/be compatible with `Python version 3.7`.

##

This test should take no longer than 2 hours to complete successfully.

Good luck!

## Submitting your solution

Please push your changes to the `master branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Complete task` link on <a href="https://app.codescreen.dev/#/codescreentest657a0909-a8cf-4c72-a8b0-98f0c0cf0e60" target="_blank">this screen</a>.