# TriTest - Sample REST application

## Running the application

### Run the application using Docker
Quickest and easiest is to build and run the image using Docker:

```bash
docker build -t tri_test:1.0.0 https://github.com/goliat43/tri_test.git#master
docker run --publish 5000:5000 -e APP_SETTINGS='tri_test.config.StagingConfig' --name tri_test tri_test:1.0.0
```

And then to do a quick test:
```bash
curl --header "Content-Type: application/json" --request POST --data '{\"sender\": \"User1\",\"receiver\": \"User2\",\"content\": \"foobar\"}' http://127.0.0.1:5000/message/
curl --header "Content-Type: application/json" --request POST --data '{\"sender\": \"User1\",\"receiver\": \"User3\",\"content\": \"foobar2\"}' http://127.0.0.1:5000/message/
curl --header "Content-Type: application/json" --request POST --data '{\"sender\": \"User1\",\"receiver\": \"User3\",\"content\": \"foobar3\"}' http://127.0.0.1:5000/message/

curl --request GET 'http://127.0.0.1:5000/message/?include_read_messages=False&from_index=1&to_index=3'
curl --request DELETE 'http://127.0.0.1:5000/message/?include_read_messages=False&from_index=1&to_index=2'

```

### Debug on local machine
The application can be started with the built in Flask web server using the command `flask run` in the tri_test directory.

For debug purposes the application can be started by calling _\_init__.py as main.
### Selecting configuration
Use the environment variable 'APP_SETTINGS' to select settings to use. Default is to use configuration for 'Dev' mode.


Valid values include:
* tri_test.config.ProdConfig
* tri_test.config.StagingConfig
* tri_test.config.TestConfig
* tri_test.config.DevConfig

Prod settings _are not included_.
Use the 'Staging' setting to get a persistent database, 'Dev' and 'Test' modes
use in memory databases. 

## Using the application
All endpoints accept and emit Content-Type: application/json

###Create a new message using `message` endpoint
Use the message endpoint with POST method to create a new message.
Include json body on the following format:
```json
{
    "sender": "User1",
    "receiver": "User2",
    "content": "foobar"
}
```
E.g. `curl --header "Content-Type: application/json" --request POST --data '{\"sender\": \"User1\",\"receiver\": \"User2\",\"content\": \"foobar\"}' http://127.0.0.1:5000/message/`

### Mark a single message as read
Using POST method to the `message/<id>/read` endpoint.

E.g. `curl --request POST http://127.0.0.1:5000/message/1/read`

### Fetch a single message
Using GET a single message can be fetched by using the specific id with the message endpoint, e.g.
`http://127.0.0.1:5000/message/<id>`

E.g. `curl --request GET http://127.0.0.1:5000/message/1`

### Delete a single message
Using DELETE method to the `message/<id>` endpoint.

E.g. `curl --request DELETE http://127.0.0.1:5000/message/1`


### Fetch and delete multiple messages using `message` endpoint

#### Fetch multiple messages using a query
Using GET multiple messages can be fetched with a query pattern. Valid arguments are 
* Required: `from_index` and `to_index`
* Optional: `include_read_messages`.

E.g. `curl --request GET 'http://127.0.0.1:5000/message/?include_read_messages=False&from_index=5&to_index=20'`

#### Delete multiple messages using a query
Using DELETE multiple messages can be deleted with a query pattern. Valid arguments are 
* Required: `from_index` and `to_index`

E.g. `curl --request DELETE 'http://127.0.0.1:5000/message/?include_read_messages=False&from_index=5&to_index=20'`

