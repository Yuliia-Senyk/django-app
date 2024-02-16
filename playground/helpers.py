from mongoConnection import dbname

collection = dbname['users']


def create_one_document():
    document = {"name": "Bob", "age": 28, "email": "bob.doe@example.com"}
    result = collection.insert_one(document)
    print(f"Inserted document with _id: {result.inserted_id}")
    print(result)
    return result


def create_many_documents():
    documents = [
        {"name": "Jane Smith", "age": 30, "email": "jane.smith@example.com"},
        {"name": "Bob Johnson", "age": 35, "email": "bob.johnson@example.com"},
    ]
    result = collection.insert_many(documents)
    print(f"Inserted {len(result.inserted_ids)} documents")


def read_one_document():
    from bson import ObjectId
    result = collection.find_one({"_id": ObjectId("65cca9e0f611ce8f32c9de5f")})
    if result:
        print("Found document:", result)
    else:
        print("Document not found")
    return list(result)


def read_many_documents():
    results = collection.find()
    # results = collection.find({})
    print("Found documents:")
    return list(results)



def update_one_document():
    query = {}
    update_data = {"$set": {"age": 66, 'name': 'updated'}}
    result = collection.update_one(query, update_data)
    print(f"Modified {result.modified_count} document")


def update_many_documents():
    query = {"age": {"$gte": 30}}
    update_data = {"$set": {"status": "Senior"}}
    result = collection.update_many(query, update_data)
    print(f"Modified {result.modified_count} documents")


def delete_one_document():
    result = collection.delete_one({})
    print(f"Deleted {result.deleted_count} document")


def delete_many_documents():
    result = collection.delete_many({"age": {"$gte": 30}})
    print(f"Deleted {result.deleted_count} documents")



def drop_collection():
    collection.drop()
    print("Collection dropped")

