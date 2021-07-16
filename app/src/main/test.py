import http.client
import json

# subways = [("Red Line"), ("Mattapan Trolley")]
# print('INSERT INTO routes (long_name) VALUES (%s);' %[(i) for i in subways])

# print('INSERT INTO blog (id, title) VALUES (%s);', [('Blog post #%d'% i) for i in range (1,5)])
# print('INSERT INTO blog (id, title) VALUES (%s, %s);' %[(i, 'Blog post #%d'% i) for i in range (1,5)])

# rows = [(1,7,3000), (1,8,3500), (1,9,3900)]
# values = ', '.join(map(str, rows))
# sql = "INSERT INTO Routes VALUES {}".format(values)

subways = [("Red", "Red Line"), ("Mattapan", "Mattapan Trolley")]
# print('INSERT INTO Routes (id, long_name) VALUES (%s, %s);', subways)
# print(sql)

# rec = []
# for c in subways:
#     rec.append({c[0], c[1]})
# print(rec)

# routes = [ "Red", "Mattapan", "Orange", "Green-B", "Green-C", "Green-D", "Green-E", "Blue" ]
# db_data = []
# for route in routes:
#     # The connection must be opened within the loop otherwise errors will occur
#     connection = http.client.HTTPSConnection('api-v3.mbta.com')
#     # For this get request we are injecting the current value of route in as the filter param
#     connection.request('GET', "/stops?filter[route]=%s" % (route))
#     response = connection.getresponse()
#     data = json.loads(response.read().decode())

#     # for each sub-object in the json response. These will be each stop
#     for i in data["data"]:
#         # since we filtered by the route we can add the route as one of the columns to these data
#         new_data = (route, i['attributes']['municipality'], i['id'])
#         db_data.append(new_data)

#     connection.close()
c = ["Green", "44"]
# jsonData = {}
# jsonData['response']['Route'] = c[0]
# jsonData["response"]["Stops"] = c[1]
# x = json.loads(jsonData)
# print(x)

import json
# print('serialization')
# myDictObj = { "response": { "Route": c[0], "Stops": c[1]},"name":"John", "age":30, "car":None }
# ##convert object to json
# serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
# print(serialized)
# ## now we are gonna convert json to object
# deserialization=json.loads(serialized)
# print(deserialization)
import flask

rec = []
        # for c in self.cursor:
rec.append({ "Stop": "", "Routes": "" })
rec.append({ "Stop": "", "Routes": "" })
print(rec)