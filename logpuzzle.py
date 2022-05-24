#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import argparse
import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
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
            print(f"Regex mismatch at index {i}.\nValue: {x}Element removed.\n")

        finally:
            i += i
    return lst2

def insert_string_at_index(s1=str,s2=str,index=int):
    """ 
    Returns s1 overrided with s2 at right of index.

        Eg input:
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
        
        Eg input:
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
    Concatenates a string to the start
    of every element in a list.
    
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

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    filename = sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("logfile", help="The name of the log file to sort")
    args = parser.parse_args()
    if args.logfile:

        if os.path.exists(filename):

            # Running the 3 functions that are 
            # necessary for both lists:
            mylist = list_from_file(filename)
            # Matches everything between "python" and "jpg".
            mylist = regex_on_list(r"\/python.*(?=jpg)...",mylist)
            mylist = remove_list_duplicates(mylist)

            if filename == "logo_data.cyber.org.il":
                # Regular alphabetic sort for logo_data file
                mylist = sorted(mylist)
            else:
                # Special sort for message_data file
                mylist = message_sort(mylist)
            mylist = concatenate_to_all_elem("http://data.cyber.org.il",mylist)

        else:
            print(f"The file \"{filename}\" doesn't exist")
            exit()

        return mylist

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, download
  each image into the given directory.
  Give the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Create the directory if necessary.
  """
  # +++your code here+++
  

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
