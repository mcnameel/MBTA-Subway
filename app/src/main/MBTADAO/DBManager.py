import mysql.connector
import http.client
import json

class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host,
            database=database,
            auth_plugin='mysql_native_password' # if you want to run this file indepentantly pass in your own password file
        )
        pf.close()

        self.cursor = self.connection.cursor()
        self.populate_db()
    
    def get_stop_data(self, routes):
        connection = None 
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
                new_data = (i['id'], route, i['attributes']['municipality'])
                db_data.append(new_data)

            connection.close()
        return db_data
    
    def get_subway_routes(self):
        # it is better to have a basic http client connection be local because it needs to be opened and closed for each request in python to flush the buffer
        connection = http.client.HTTPSConnection('api-v3.mbta.com')
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


    def populate_db(self):
        # Clear the database info and readd it at init time 
        self.cursor.execute('DROP TABLE IF EXISTS Routes;')
        self.cursor.execute('CREATE TABLE Routes (id VARCHAR(100), long_name VARCHAR(255));')

        # call our function which queries for the subway info we will load into the db
        subways = self.get_subway_routes()
        self.cursor.executemany('INSERT INTO Routes (id, long_name) VALUES (%s, %s);', subways)
        self.connection.commit()

        self.cursor.execute('DROP TABLE IF EXISTS Stops;')
        self.cursor.execute('CREATE TABLE Stops (id VARCHAR(100), route VARCHAR(64), municipality VARCHAR(100));')
        
        # Hard coded for the sake of easy use. This would normally be dynamically pulled by parsing get_subway_routes()
        routes = [ "Red", "Mattapan", "Orange", "Green-B", "Green-C", "Green-D", "Green-E", "Blue" ]
        # global routes
        # call our function which queries for the stops info we will load into the db
        stops = self.get_stop_data(routes)
        self.cursor.executemany('INSERT INTO Stops (id, route, municipality) VALUES (%s, %s, %s);', stops)
        self.connection.commit()

    def query_titles(self):
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    def query_subways(self):
        self.cursor.execute('SELECT long_name FROM Routes')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    def query_max_stops_by_route(self):
        self.cursor.execute('SELECT route, count(*) as count \
                                FROM Stops \
                                GROUP BY route \
                                ORDER BY count DESC \
                                LIMIT 1')
        rec = []
        for c in self.cursor:
            rec.append({ "Route": c[0], "Stops": c[1] })
        return rec

    def query_min_stops_by_route(self):
        self.cursor.execute('SELECT route, count(*) as count \
                                FROM Stops \
                                GROUP BY route \
                                ORDER BY count ASC \
                                LIMIT 1')
        rec = []
        for c in self.cursor:
            rec.append({ "Route": c[0], "Stops": c[1] })
        return rec

    def query_stops_in_somerville(self):
        self.cursor.execute('SELECT municipality,COUNT(*) as count \
                                FROM Stops \
                                WHERE municipality = "Somerville" \
                                GROUP BY municipality \
                                ORDER BY count DESC \
                                LIMIT 1')
        rec = []
        for c in self.cursor:
            rec.append({ "Municipality": c[0], "Stops": c[1]})
        return rec

    def query_connecting_stops(self):
        # here we use the GROUP_CONCAT to allow us to return multiple values all from one column where the conditions are true
        # in this case that means returning all routes as a list where the there the count of id (stop name) is greater than 1
        # This means that there are multiple stop entries for this meaning there will be 2+ routes 
        self.cursor.execute('SELECT id, COUNT(id) AS count, GROUP_CONCAT(route  SEPARATOR ", ") \
                                FROM Stops \
                                GROUP BY id \
                                HAVING count > 1')
        
        rec = []
        for c in self.cursor:
            rec.append({ "Stop": c[0], "Connections": c[1], "Routes": c[2] })

        return rec