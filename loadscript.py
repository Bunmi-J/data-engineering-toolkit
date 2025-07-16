#from fileinput import filename


def write_strings_to_file(input_filename, output_filename):
   """ read lines from a text file and writes them to another, one per line."""
   with open(input_filename, 'r') as inputlines:
       lines = inputlines.read()
   with open(output_filename, 'w') as the_fole:
        for line in lines:
            the_fole.write(line + '\n\r')  
        print(f"Lines added to {output_filename}")
   

write_strings_to_file(r'C:\Users\obunm\OneDrive\Desktop\dataengineering\data-engineering-toolkit\sample.txt', 
                      r'C:\Users\obunm\OneDrive\Desktop\dataengineering\data-engineering-toolkit\myperson.txt')
	




    
