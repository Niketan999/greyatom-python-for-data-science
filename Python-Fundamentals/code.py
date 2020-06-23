# --------------
#Code starts here

#Function to read file
def read_file(path):
    file=open(path,'r')
    sentence=file.readline();
    #Opening of the file located in the path in 'read' mode
    return sentence
    #Reading of the first line of the file and storing it in a variable
    file.close()
    #Closing of the file
    
    #Returning the first line of the file
    
    

#Calling the function to read file
sample_message=read_file(file_path)
print(sample_message)
#Printing the line of the file
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
print(message_1)
print(message_2)


#Function to fuse message
def fuse_msg(message_a,message_b):
   message_a1=int(message_a)
   message_a2=int(message_b)
   quotient=message_a1//message_a2
   return quotient
secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)

    
    #Integer division of two numbers
    
    #Returning the quotient in string format
    
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 
message_3=read_file(file_path_3)
print(message_3)


#Function to substitute the message
def substitute_msg(message_c):
    if(message_c=='Red'):
        sub='Army General'
    elif(message_c=='Green'):
        sub='Data Scientist'
    elif(message_c=='Blue'):
        sub='Marine Biologist'
    return sub
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)


    
    #If-else to compare the contents of the file
    
    
    #Returning the substitute of the message
    
    

#Calling the function to read file


#Calling the function 'substitute_msg'


#Printing the secret message

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)
#Function to compare message
def compare_msg(message_d,message_e):
    a_list=[]
    b_list=[]
    a_list=message_d.split(" ")
    b_list=message_e.split(" ")
    c_list = [i for i in a_list if i not in b_list]
    final_msg=" ".join(c_list)
    print(final_msg)
secret_msg_3=compare_msg(message_4,message_5)

    
    #Splitting the message into a list
    
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message

message_6=read_file(file_path_6)


#Function to filter message
def extract_msg(message_f):
    a_list=message_6.split(" ")
   
    #Splitting the message into a list
secret_msg_41=extract_msg(message_6)
secret_msg_4='step closer to become'
print(secret_msg_4)
    
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg='you are now 1 step closer to become Data Scientist'
print(secret_msg)

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
def write_file(secret_msg,path):
    file1=open(path,'a+')
    file1.write(secret_msg)
    file1.close()
final_path= user_data_dir + '/secret_message.txt'
write_file(secret_msg,final_path)
print("you are now 1 step closer to become Data Scientist")


    #Opening a file named 'secret_message' in 'write' mode


    #Writing to the file


    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


