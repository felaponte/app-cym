import boto3
from credentials.keys import ACCES_KEY, SECRET_KEY

bucket_name = "felasbucket96"

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
        photo_path_local = "/tmp/photo"
        photo.save(photo_path_local)
        print("photo saved")
        return photo_path_local
    except Exception as err:
        print("Error", err)
        return None
        
def upload_file(s3_resource, photo, photo_path_local, id):
    try:
        photo_name = photo.filename
        extension_photo = photo_name.split(".")[len(photo_name.split("."))-1]
        photo_pad_s3 = " images/" + id + "." + extension_photo
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, photo_pad_s3)
        print("File uploaded")
        return True
    except Exception as err:
        print("Error", err)
        return False
        
def consult_file(s3_resource, id):
    bucket_repo = s3_resource.Bucket(bucket_name)
    bucket_objects = bucket_repo.objects.all()
    for obj in bucket_objects:
        path_file_s3 = obj.key
        path_photo_s3 = path_file_s3.split("/")[len(path_file_s3.split("/"))-1]
        name_photo_process = path_photo_s3.split(".")[0]
        if name_photo_process == id:
            print("Found")
            return path_file_s3
    return None