import pymongo

url = 'mongodb+srv://webdev:webdevPass@cluster0.8fnhiow.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")    


dbname = client['test']