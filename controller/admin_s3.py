import boto3
from credentials.keys import ACCES_KEY, SECRET_KEY

def connection_s3() :
    try:
        session_aws = boto3.session.Session(ACCES_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print("Connected to S3")
        return s3_resource
    except Exception as err:
        print("Error" , err)
        
def save_file(photo):
    try:    
        photo_path_local = "/tmp/photo.JPG"
        photo.save(photo_path_local)
        print("photo saved")
        return photo_path_local
    except Exception as err:
        print("Error", err)
        return None
        
def upload_file(s3_resource, photo, photo_path_local, id):
    try:
        bucket_name = "felasbucket96"
        photo_name = photo.filename
        extension_photo = photo_name.split(".")[1]
        photo_pad_s3 = " images/" + id + "." + extension_photo
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, photo_pad_s3)
        print("File uploaded")
        return True
    except Exception as err:
        print("Error", err)
        return False
    