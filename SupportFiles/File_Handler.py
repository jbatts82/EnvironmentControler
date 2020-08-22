###############################################################################
# File Name  : File_Handler.py
# Date       : 07/25/2020
# Description: File Handler
###############################################################################

def get_from_file(in_file):
    # open file and put into list
    out_list = []
    with open(in_file, 'r') as filehandle:
        for line in filehandle:
            remove_new_line = line[:-1]
            out_list.append(remove_new_line)
    return out_list
    
def save_to_file(in_list, out_file):
    print("Saving To File..")
    with open(out_file, 'w') as filehandle:
        filehandle.writelines("%s\n" % line for line in in_list)
        
def erase_file(file_to_erase):
    file = open(file_to_erase, 'w')
    file.close()
    
def create_file(file_name):
    f = open(file_name,"w+")
    return f