# Authorizer

Authorizer is a Python(3+) application that authorizes a transaction for a specific account following a set of predefined rules.

## Modeling

Deciding about what would be better for this project I based the modeling of the application on two main concepts:

**Imutability and the  event sourcing pattern**

So applying both, the main objects (Account, Transaction) would not be modified in any circunstance (Imutability) and to apply some business rules or calculate some attribute we use the event sourcing pattern e.g. To calculate the available limit from an account, we sum all the transactions realized amount and subtract with the original available-limit of the account, so this way we do not pass the limit of imutability.

## Usage

```bash
$ python3 authorizer.py <file_with_operations>
```

The file passed should be a file like the  `support_files/operations` where each line of the file represents an operation

### Using Docker

To use the docker image you can run the following commands:

Build the docker image
```bash
$ docker build -t authorizer .
```

Run the app:
```bash
$ docker run -v <path_authorizer_app>:/usr/src/app -it authorizer authorizer.py <file_with_operations>
```

Example:
```bash
$ docker run -v ~/Documents/Authorizer:/usr/src/app -it authorizer authorizer.py support_files/operations
```


## Tests

Were implemented unit and integration tests using pytest. So to run the tests you should have pip3 on your machine or you can install pytest lib:

```bash
$ pip3 install pytest
```

Then, you car run the tests using:

```bash
$ pytest
```

