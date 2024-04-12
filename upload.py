# this script will define a function to upload a file to a gcloud bucket
# the credentials file is stored in the root directory of the project

import os
from google.cloud import storage
from google.oauth2 import service_account

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # credentials file
    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    
    # check if the file was uploaded
    if blob.exists():
        # delete the file from the local directory
        os.remove(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
    return blob.public_url # return the public url of the file

# test the function
print(upload_blob('image_coloring_bucket', 'image.jpg', 'imageUpload.jpg'))