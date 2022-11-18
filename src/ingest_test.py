import ingest
def ingestion_test():
    assert ingest.ingestion() != "Please download the dataset using 'make fetch_data'"
