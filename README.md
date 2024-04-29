# BU-EC530 Health Monitoring System
bu-ec530-health-monitoring

## About

Project 2 for EC530 Software Engineering Principles at BU (Spring 2024). 

Implementation of a health monitoring system for patients and medical professionals.


## Install

### Dependencies
```console
pip install -r requirements.txt
```

## Usage

First, run the following to start the server:

```console
python src/app.py
```

Then, in a separate terminal, either run the following to start the program, which will print a summary report of the users:

```console
python main.py
```

Alternatively, to interact directly with the sanitizing SQL database client, run:

```console
python src/client.py
```


### Unit Tests
```console
pytest
```

### Coverage
```console
coverage run -m pytest
coverage [report | html]
```

## Example Output

```json
(venv) (base) christopherkrenz@crc-dot1x-nat-10-239-132-248 bu-ec530-health-monitoring % python main.py
{'user_id': 1, 'name': 'Chris Krenz', 'ssn': '111-11-1111', 'email': 'ckrenz@bu.edu', 'role': 'patient'}
{'user_id': 2, 'name': 'John Doe', 'ssn': '222-22-2222', 'email': 'jonathanbambidoe@bu.edu', 'role': 'admin'}
{'user_id': 3, 'name': 'Jane Doe', 'ssn': '333-33-3333', 'email': 'janemaryjanedoe@bu.edu', 'role': 'patient'}
```


## Contributors

[Chris Krenz](https://github.com/chris-krenz): ckrenz@bu.edu


## License

[MIT License](LICENSE)
