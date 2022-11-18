import json
import sys
# The following code is purely illustrative
def ingestion():
    try:
        with open("test-resources/samples-votes.jsonl") as votes_in:
             for line in votes_in:
                print(json.loads(line))

    except FileNotFoundError:
        print("Please download the dataset using 'make fetch_data'")

ingestion()
