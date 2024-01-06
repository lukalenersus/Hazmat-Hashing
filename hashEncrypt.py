#import cryptography library
from cryptography.hazmat.primitives import hashes
# importing os module
import os

def main():

  # gives the path of demo.py
  # path = os.path.realpath(__file__)
  # # gives the directory where demo.py
  # # exists
  # dir = os.path.dirname(path)

  os.chdir('binaryfiles')
  # Confirm the current directory
  directory = os.getcwd()

  # print('Current Working Directory is: ', os.getcwd())

  index = 0 

  # iterate over files in directory
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    index += 1
    # checking if it is a file
    if os.path.isfile(f):
       
        # opening bin file 
        binFile = open(f,"rb")
          
        # reading data from binary file
    
        readBinFile = binFile.read()
        # call all the three methods and pass binary files
       
        sha256file=cryptSHA256(readBinFile)
       
        SHA3_224file=cryptSHA3_224(readBinFile) 
       
        md5file=cryptMD5(readBinFile)
     
        
        # navigate up one step out of the directory
        
        os.chdir('../HashedValues')

        # create file and add the three hashed values.

        # check index and corrupt hashes 5 to 6
        if index == 6 or index == 7 or index == 8 or index == 9 or index == 10:

          with open('File-hashes.txt', 'a') as f:
            
            # corruptedStr=str(sha256file)

            # change swap first and last value
            newHash=corrupT(readBinFile)
            # print( "new hash"+newHash)

        #  write the hashed values in the text file
            f.write("File-"+str(index)+ ", "+sha256file +", " +SHA3_224file +", " +newHash+ '\n')
            

        elif  index == 1 or index == 2 or index == 3 or index == 4 or index == 5: 

           #  write the hashed values in the text file
          with open('File-hashes.txt', 'a') as f:
            f.write("File-"+str(index)+ ", "+sha256file +", " +SHA3_224file+", " +md5file+ '\n')
           
        else:

         print("I don't know who you are!")    


# encryption method for sha256
def  cryptSHA256(data):
    digest = hashes.Hash(hashes.SHA256())

    digest.update(data)

    c =digest.finalize()

    return str(c)
# encryption method for SHA224
def  cryptSHA3_224(data):
  digest = hashes.Hash(hashes.SHA224())

  digest.update(data)

  c =digest.finalize()

  return str(c)

# encryption method for MD5
def  cryptMD5(data):
  digest = hashes.Hash(hashes.MD5())

  digest.update(data)

  c =digest.finalize()
 
  return str(c)

# hashes corrupting method 
def corrupT(data):
   digest = hashes.Hash(hashes.MD5())

   digest.update(data)

   digest.update(b'hey')

   c=digest.finalize()
     

   return str(c)

def read_in_chunks(file, chunk_size=100):  # Default chunk size: 10k.
    while True:
        chunk = file.read(chunk_size)
        if chunk:
            yield chunk
        else: # The chunk was empty, which means we're at the end of the file
            return


main() 


