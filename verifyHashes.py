#import cryptography library
from cryptography.hazmat.primitives import hashes
# importing os module
import os

def main():

  os.chdir('binaryfiles')
  # Confirm the current directory
  directory = os.getcwd()

  # print('Current Working Directory is: ', os.getcwd())


# read the file with hashed content   
  arr=readHashedFile()
  
  # iterate over files in the directory
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # checking if it is a file
    if os.path.isfile(f):
        
        # opening bin file 
        binFile = open(f,"rb")
          
        # reading data the binary files
      
        readBinFile = binFile.read()
        
        # call all the three methods and pass file to hash
       
        sha256file=cryptSHA256(readBinFile)
       
        SHA3_224file=cryptSHA3_224(readBinFile) 
       
        md5file=cryptMD5(readBinFile)
           
      # loop through the values of the text file

        for x in arr:
        
        # //check length of the strings and remove the last character
         if len(x[:-1])==len(str(sha256file)):
          # check for corrupt sha256 hash
            if str(x[:-1]) == str(sha256file):
                print('hash success sha256')
            else:
              print("corrupted sha256 is "+ x[:-1])


         if len(x[:-1])==len(str(SHA3_224file)): 
                # check for  corrupt SHA3_224 hash
              if str(x[:-1])==  str(SHA3_224file) :
                print('hash success  SHA3_224')
              else:
               print("corrupted SHA3_224 is "+ x[:-1]) 

         if len(x[:-1])==len(str(md5file)): 
              #check for corrupt md5 hash   
              if str(x[:-1]) ==  str(md5file) :
                print('hash success md5') 
              else:
               print("corrupted md5 is "+ x[:-1])   
         
        
  
             

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

def readHashedFile():
    os.chdir('../HashedValues')
    # print('Current Working Directory is: ', os.getcwd())
    # opening the text file 
    f = open('File-hashes.txt')
    
    # reading data from file
    data = f.read()
  
    #split string by gap
    splits = data.split(' ')

    return splits
         

main() 


