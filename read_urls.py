import re
def log_sort(loglst):
    """ 
    For the logo_data list - returns it sorted alphabetically.
    For the messages_data list - returns it sorted alphabetially by the second word.

        Eg:
            The string z-bbbb-cccc will be placed before a-aaaa-zzzz because
            cccc is earlier than zzzz.

    Args:
        loglst - either the list from the logo_data file or the messages_data file.
    """

    # This regex expression works on both files: logo_data.cyber.org.il, message_data.cyber.org.il
    # It matches the string "/python(everything in between).jpg"

    # Average line is from message_data:
    # 10.254.254.65 - - [06/Aug/2007:00:06:07 -0700] "GET /python/logpuzzle/p-bbfh-baji.jpg HTTP/1.0" 302 18124 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
    # Average line is logo_data:
    # 10.254.254.29 - - [06/Aug/2007:00:09:22 -0700] "GET /python/logpuzzle/a-baai.jpg HTTP/1.0" 200 10496 "-" "facebookbot-mscrawl-moma (enterprise; bar-XYZ; foo123@facebook.com,foo123@facebook.com,foo123@facebook.com,foo123@facebook.com)"

    # The regex respectively returns:        
    # /python/logpuzzle/p-bbfh-baji.jpg
    # /python/logpuzzle/a-baai.jpg
    url_reg = re.compile(r"\/python.*(?=jpg)...")  
