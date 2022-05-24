# This is a testing file
import argparse
import os
import sys
import re

def list_from_file(textfile):
    """ 
    Returns a list where every element is a copied line from the text file,
    corrosponding with the number of the line.
        Eg: 
            Line 1 will be copied to element 0 of the list.
            Line 2 will be copied to element 1 of the list.

        Args: 
            file - A text file
    """
    lst = []
    with open(textfile,'r') as input_file:
        for line in input_file.readlines():
            lst.append(line)
    return lst

def remove_list_duplicates(lst): 
    """ 
    Removes duplicate elements from a list.

    Args:
         lst - a list
    """
    return list(dict.fromkeys(lst))

def regex_on_list(regex_expression,lst=str):
    """ 
    Returns a list of strings containing only the 
    substrings which answer the regex expression and
    removing all other elements.

    Args:
            regex_expression - r"expression"\n
            lst - a list
    """
    lst2 = []
    for i,x in enumerate(lst):
        try:
            lst2.append(re.search(regex_expression,x).group())

        # Removes all elements which don't answer the regex, or aren't str.
        except (AttributeError,TypeError):
            #print(f"Regex mismatch at index {i}.\nValue: {x}Element removed.\n")
            pass
        finally:
            i += i
    return lst2

def insert_string_at_index(s1=str,s2=str,index=int):
    """ 
    Returns s1 overrided with s2 at right of index.

        Eg:
            s1 = 'aacc'

            s2 = 'BB'

            index = 1

        Output:
            'aBBc'
    Args:
        s1 = string to be overrided.

        s2 = string to override with.

        index = position in s1 to override from.

    Note:
        To run this over 2 lists of strings use enumerate:
        
        for i, x in enumerate(list1):
            list1[i] = insert_string_at_index(x,list2[i],insertion_index)
        
        Eg:
            list1 = ['aacc','xxzz']

            list2 = ['BB','YY']

            index = 1

        Output:
            list1 = ['aBBc','xYYz']


    """
    s1 = list(s1)

    # Removing the range of characters that s2 will occupy 
    s1  = s1[:index] + s1[index + len(s2):]

    s1.insert(index,s2)
    s1 = ''.join(s1)
    return s1

def concatenate_to_all_elem(s,lst):
    """ 
    Concatenates a string to every element
    in a list.
    
    Args:
        s - string to concatenate
        lst - list 
    """
    lst = [s + i for i in lst]
    return lst

def message_sort(message_list):
    """
    This is a special sort that is required for the message
    log file. The list shall be sorted alphabetically by it's 
    element's second word. A sorted list is returned.

    Args: 
        message_list: a list containing the lines from the 
        "message_data.cyber.org.il" log file.

    Eg. of a second word from the line '/python/logpuzzle/p-bccc-bbdc'
    ---> bbdc
    """
    only_second_word = [
        x[25:29]
        for x in message_list
    ]
    
    only_second_word = sorted(only_second_word)

    for i, x in enumerate(only_second_word):
        message_list[i] = insert_string_at_index(message_list[i],x,25)   

    return message_list    

def main():
    FILENAME = sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("filecheck", help="checks if file is in current dir")
    args = parser.parse_args()
    if args.filecheck:

        if os.path.exists(FILENAME):

            # Running the 3 functions that are 
            # necessary for both lists:
            mylist = list_from_file(FILENAME)

            # Matches everything between the strings "python" and "jpg".
            mylist = regex_on_list(r"\/python.*(?=jpg)...",mylist)

            mylist = remove_list_duplicates(mylist)

            if FILENAME == "logo_data.cyber.org.il":
                mylist = sorted(mylist)
            else:
                mylist = message_sort(mylist)
            mylist = concatenate_to_all_elem("http://data.cyber.org.il",mylist)

        else:
            print(f"The file \"{FILENAME}\" doesn't exist")
            exit()

        print(mylist)

main()