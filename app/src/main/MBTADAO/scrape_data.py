import http.client
import json

from mysql.connector import connect

class DataScraper:

    connection = None

    def __init__(self):
        # Establish connection with basic http client library
        global connection 
        connection = http.client.HTTPSConnection('api-v3.mbta.com')
    
    def get_subway_routes():
        global connection
        # Set query parameters to speficify that we want to filter for the type of rail heavy and light (0 and 1)
        params = "?filter[type]=0,1"
        # Put the connection string and parameters together and specify we are making a GET request
        connection.request('GET', ('/routes' + params))

        response = connection.getresponse()

        # From the response, read then decode, then load as a python json readable object
        data = json.loads(response.read().decode())
        db_data = []
        for i in data["data"]:
            new_route = (i['attributes']['long_name'], i['id'])
            db_data.append(new_route)

        return db_data

    def get_stop_data(routes):
        global connection 
        db_data = []
        for route in routes:
            # The connection must be opened within the loop otherwise errors will occur
            connection = http.client.HTTPSConnection('api-v3.mbta.com')
            # For this get request we are injecting the current value of route in as the filter param
            connection.request('GET', "/stops?filter[route]=%s" % (route))
            response = connection.getresponse()
            data = json.loads(response.read().decode())

            # for each sub-object in the json response. These will be each stop
            for i in data["data"]:
                # since we filtered by the route we can add the route as one of the columns to these data
                new_data = (route, i['attributes']['municipality'], i['id'])
                db_data.append(new_data)

            connection.close()
        return db_data