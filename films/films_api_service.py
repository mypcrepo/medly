import requests

class FilmsAPIService(object):

    # Your API token. Needed to successfully authenticate when calling the films endpoint. 
    # This needs to be included in the Authorization header in the request you send to the films endpoint.
    api_token = "8c5996d5-fb89-46c9-8821-7063cfbc18b1" 

    def get_all_films(self):
        """TODO Implement
        Retrieves the data for all films by calling the https://app.codescreen.dev/api/assessments/films endpoint.
        """
        films_endpoint_url = "https://app.codescreen.dev/api/assessments/films"

        headers = {"Authorization": "Bearer 8c5996d5-fb89-46c9-8821-7063cfbc18b1"}
        resp = requests.get(films_endpoint_url,headers=headers).json()

        return resp

