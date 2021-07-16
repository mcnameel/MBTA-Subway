# MBTA Subway Service

This service is a docker compose project made up of 3 different docker images: app, web, and db. Docker compose will take all three and set them up to work together. 


## Build

Docker compose makes this process about as seemless as it can be. Just make sure you have Docker and docker-compose installed and running.

```bash
docker-compose build
```

## Run

Make sure that you have nothing running on ports 3306 or 8080 as these will be needed in the application.

```bash
docker-compose up
```
If you want to rebuild the images before running
```bash
docker-compose up --build
```
## Use
Navigate to [localhost:8080](http://localhost:8080). You should see a very basic landing page as a front-end interface for accessing the API. Enter one of the suggestions like "stops-in-somerville" and click the button to view the results

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)