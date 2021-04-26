from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result
from cloudant.result import Result, ResultByKey


# IBM Cloudant Legacy authentication
client = Cloudant("9e8bd3ea-e4c4-4422-bab7-544cee38a065-bluemix", "24a7fd88784c4c435b2e1baabc0a9701fd85fbea222b9ec898bd03c430eb8663",
                  url="https://9e8bd3ea-e4c4-4422-bab7-544cee38a065-bluemix:24a7fd88784c4c435b2e1baabc0a9701fd85fbea222b9ec898bd03c430eb8663@9e8bd3ea-e4c4-4422-bab7-544cee38a065-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "imageurl"

my_database = client.create_database(database_name)

if my_database.exists():
    print(f"'{database_name}' successfully created.")
    json_document = {
                    "_id": "1001",
                    "name":"divya"
                    }
    new_document = my_database.create_document(json_document)
    if new_document.exists():
        print("Document '{new_document}' successfully created.")

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']  #search by id, if id=1001   

print("---------------")
print("the data with id =1001 is")
print (result)
print("---------------")
# Iterate over the result collection
for result in result_collection:
    print(result)# it will print all the records

# First retrieve the document
for document in my_database:
    my_document = my_database['1001'] 

# Update the document content
# This can be done as you would any other dictionary
my_document['name'] = 'divya'
my_document['email'] = 'divya@gmail.com'
my_document['mobile'] = 9999099990

# You must save the document in order to update it on the database
my_document.save()

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']     
# Iterate over the result collection
print (result)


