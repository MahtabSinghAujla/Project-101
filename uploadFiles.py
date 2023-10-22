import dropbox
import os

class TransferData :
    def __init__(self,access_token) :
        self.access_token=access_token
    
    def upload_files(self,file_from,file_to) :
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from) :
            for filename in files :
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f :
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main() :
    access_token='sl.BoQ1IGGo__Bbv2MQ_4D_L69tlEF8LwO72MGF-sJhVUOPQyUv5nQRHgOPvwnEcMWQJNDWitP33rdNMnv3qCuD24SD1v4DfiBApnul14aP4g8N_GbMf5y3eZo1oHUdQzLZ2k51ri4w_9s2C4aXCTT4'
    transferData=TransferData(access_token)
    file_from=input('Enter the path to transfer: ')
    file_to=input('Enter the path to upload: ')
    transferData.upload_files(file_from,file_to)
    print('The files have been moved.')

main()
