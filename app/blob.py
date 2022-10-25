from azure.storage.blob import BlobClient



class blob():
    blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

    with open("./data_blob.json", "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)



