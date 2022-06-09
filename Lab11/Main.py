import re

if __name__ == "__main__":

    file = open('access_log', 'r')

    result = re.findall("\d+/.+/\d\d\d\d:0[3-6]:[0-5][0-6].+(png|PNG|jpg|JPG|jpeg|JPEG|gif|GIF)", file.read())

    print(len(result))
