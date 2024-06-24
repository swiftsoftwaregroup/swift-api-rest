# swift-api-rest

## Run

```bash
source configure.sh

./watch.sh
```

Browse the docs and test the API via the Swagger UI:

```bash
open http://127.0.0.1:8001/docs
```

## Updating the code

```bash
source configure.sh
```

Open the project directory in Visual Studio Code:

```bash
code .
```

## Development

Format it with the [black](https://black.readthedocs.io/en/stable/) formatter:

```sh
black .
```

Correct the import order with [isort](https://pycqa.github.io/isort/):

```sh
isort .
```

Verify the typing:

```sh
mypy src/
```

Run the tests (from the command line):

```sh
pytest
```

Generate test coverage report:

```bash
coverage run -m pytest
coverage combine
coverage report
```

## Tasks

List tasks:

```bash
inv --list
```

## Run in Podman / Docker 

Rebuild container image and start container:

```bash
inv podman
```

Delete container and image:

```bash
inv podman-delete
```

## Generate API Clients

### Setup

Download `openapi-generator`:

```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.3.0/openapi-generator-cli-7.3.0.jar --output-document openapi-generator-cli.jar
```

List available generators:

```bash
java -jar openapi-generator-cli.jar list
```

### TypeScript

#### List config options

```bash
java -jar openapi-generator-cli.jar config-help --generator-name typescript
```

#### Generate `swift-api-rest-ng` 

##### Start Server

In Terminal in Visual Studio Code:

```bash
./watch.sh
```

##### Create / Update Angular client

In separate Terminal:

```bash
inv update-client-ng
```

That will generate Angular Typescript client in `../swift-api-rest-ng`. 

## License

`swift-api-rest` is distributed under the terms of the [Apache 2.0 ](https://spdx.org/licenses/Apache-2.0.html) license.
