from pymongo import MongoClient
import json

# Replace these with your connection details
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "test_db"
COLLECTION_NAME = "users"
QUERY = {"name": "john"}

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Get the explain result
explain_result = collection.find(QUERY).explain()

# Convert explain result to string
explain_string = str(explain_result)

with open("queries.txt", "r") as f:
    queries = [json.loads(line.strip()) for line in f]

for query in queries:
    # Explain the query and get the explain string
    explain_result = collection.find(query).explain()
    explain_string = str(explain_result)

    # Check for index usage and print results
    if "IXSCAN" in explain_string:
        print(f"Query: {query}")
        print("  Index likely used! 🎉")
    else:
        print(f"Query: {query}")
        print("  No clear indication of index usage. 🤔")
        # You can add further analysis here, like extracting stage names.

client.close()
