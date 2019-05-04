import json
# saves the a class in a file with json
def save(file, string):
    # opens/creates file in write mode
    with open(file, 'wb') as data:
        # dumps all of the  __dict__ for a class into a variable in json
        save = json.dumps(string)
        # writes all of the json to said file
        data.write(save.encode())


# loads a class with json into an object
def load(file):
    # open the save file in read mode
    with open(file, 'r') as data:
        # reads data into variable
        raw_data = data.read()

    # makes the data be python and not json
    read_data = json.loads(raw_data)
    # loads the data into the object
    return read_data