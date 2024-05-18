# MongoDB Index Checker Usage

This guide explains how to set up and use a Python script to check if your MongoDB queries are using indexes.

## Prerequisites

- Python 3.x
- `pymongo` library
- MongoDB instance

## Installation

1. **Install Python**:
    - Download and install Python from [python.org](https://www.python.org/).

2. **Install `pymongo`**:
    - You can install the `pymongo` library using pip:
      ```sh
      pip install pymongo
      ```

## Setup

1. **MongoDB Connection**:
    - Ensure your MongoDB instance is running and accessible.
    - Insert dummy data + add index on some field's 
    - Replace the `MONGO_URI`, `DATABASE_NAME`, and `COLLECTION_NAME` in the script with your MongoDB details.

2. **Create `queries.txt`**:
    - Create a file named `queries.txt` in the same directory as your script.
    - Add your MongoDB queries in JSON format, one per line. For example:
      ```json
      {"name": "john"}
      {"age": {"$gte": 25}}
      {"city": "New York"}
      ```

## Script

1. **Script Code**:
    - Copy the following script and save it as `check_indexes.py`:
      ```python
      from pymongo import MongoClient
      import json

      # Replace these with your connection details
      MONGO_URI = "mongodb://localhost:27017/"
      DATABASE_NAME = "test_db"
      COLLECTION_NAME = "users"

      client = MongoClient(MONGO_URI)
      db = client[DATABASE_NAME]
      collection = db[COLLECTION_NAME]

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

      client.close()
      ```

2. **queries.txt**:
    - Copy the following text and save it as `queries.txt`:
      ```txt
      {"order_date": { "$gt": "2023-10-31" }}
      {"name": "john"}
      {"email": "janedoe@example.com"}
      ```


## Usage

1. **Run the Script**:
    - Open a terminal and navigate to the directory where your script is located.
    - Run the script using Python:
      ```sh
      python3 run-check.py
      ```

2. **Output**:
    - The script will output whether each query in `queries.txt` likely used an index or not. For example:
      ```
      Query: {'name': 'john'}
        Index likely used! 🎉
      Query: {'age': {'$gte': 25}}
        No clear indication of index usage. 🤔
      ```

## Troubleshooting

- **Connection Issues**:
    - Ensure your MongoDB instance is running and the `MONGO_URI` is correct.
    - Check for network issues or firewall rules that might block the connection.

- **Invalid Queries**:
    - Ensure each line in `queries.txt` is a valid JSON object.

- **Library Installation**:
    - If you encounter issues with `pymongo` installation, ensure your Python and pip versions are compatible.

## Further Enhancements

- **Detailed Analysis**:
    - Modify the script to parse the `explain` dictionary for more detailed analysis instead of converting it to a string.

- **Error Handling**:
    - Add try-except blocks to handle potential errors in database connections and file operations.

By following this guide, you should be able to set up and use the script to check if your MongoDB queries are using indexes effectively.