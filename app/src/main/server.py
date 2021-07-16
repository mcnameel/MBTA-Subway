import os
import mysql.connector
import flask
import json
from MBTADAO.DBManager import DBManager

server = flask.Flask(__name__)
conn = None

@server.route('/blogs')
def listBlog():
    global conn
    rec = conn.query_titles()

    result = []
    for c in rec:
        result.append(c)

    return flask.jsonify({"response": result})

@server.route('/subway-routes')
def listRoutes():
    global conn
    rec = conn.query_subways()

    result = []
    for c in rec:
        result.append(c)

    return flask.jsonify({"response": result})

@server.route('/max-stops')
def listMaxStopsByRoute():
    global conn
    rec = conn.query_max_stops_by_route()

    return flask.jsonify({"response": rec})

@server.route('/min-stops')
def listMinStopsByRoute():
    global conn
    rec = conn.query_min_stops_by_route()

    return flask.jsonify({"response": rec})

@server.route('/connecting-stops')
def listConnectingStops():
    global conn
    rec = conn.query_connecting_stops()

    return flask.jsonify({"response": rec})

@server.route('/stops-in-somerville')
def listStopsInSomerville():
    global conn
    rec = conn.query_stops_in_somerville()

    return flask.jsonify({"response": rec})

@server.route('/')
def hello():
    return flask.jsonify({"response": "Hello from Docker!"})


if __name__ == '__main__':
    conn = DBManager(password_file='/run/secrets/db-password')
    server.run(debug=True, host='0.0.0.0', port=5000)