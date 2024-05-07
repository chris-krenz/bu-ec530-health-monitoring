# BU-EC530 Health Monitoring System
bu-ec530-health-monitoring

## About

Final Project for EC530 Software Engineering Principles at BU (Spring 2024). 

Implementation of a health monitoring system for patients and medical professionals.

This is a simple app intended to be run via Docker.

It consists of a backend Flask server (with an SQL database) and a frontend React webapp.

Accessing the site permits basic CRUD operations.

If any additional features are required, please let me know.


## Usage

To create the Docker images, run:

```console
docker-compose up --build
```

Alternatively, you can get the images from Docker Hub via: 

```console
docker pull ckrenz/bu530
```

You can then run the containers with the following commands (in separate terminals):

```console
docker run -p 8000:5000 ckrenz/bu530:server-latest
docker run -p 3000:3000 ckrenz/bu530:webapp-latest
```

Then go to http://localhost:3000/ to interact with the app.  

You can also go to http://localhost:8000/api to check the server is running.

Once you have access, you can perform basic GET, POST, and DELETE operations on the user database.

### (For Developers...)


### Dependencies

```console
pip install -r requirements.txt
```

Then, run the following to start the server:

```console
python src/server.py
```

Then from the webapp folder run:

```console
npm install
npm start
```

(Or you could run the following for a CLI-based GET commands; handy just to check server status:)

```console
python src/client.py 
```

Note, the webapp is contained entirely inside the webapp folder, and the server is contained within the root src folder.


### Unit Tests
```console
pytest
```


## Contributors

[Chris Krenz](https://github.com/chris-krenz): ckrenz@bu.edu


## License

[GNU License](LICENSE)
