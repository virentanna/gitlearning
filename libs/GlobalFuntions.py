def sum(a, b):
    """
    sums up two numberics
    :param a: number
    :param b: number
    :return: sum of numbers
    """
    return a + b

def greet(name):
    """
    Greeting function
    :param name: String Name
    :return: greeting message
    """
    return "Welcome " + name

def pull_first_and_last_name(fullname):
    """
    Function to pull first name & last name
    :param fullname:
    :return: firstname & lastname
    """
    names = fullname.split(" ")
    fname = names[0]
    lname = names[1]

    return "First name : " + fname + "\n" + "Last name : " + lname

def reverse_string(string:str):
    """
    reverses string
    :param str01: string
    :return:
    """
    return string[::-1]
