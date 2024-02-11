# **AirBnB clone project**

## Description
This project implements a command-line interface (CLI) for managing a simplified version of an AirBnB-like application. It includes the following features:

* A parent class called BaseModel that handles initialization, serialization, and deserialization of instances.
* Serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
* Classes for AirBnB entities such as User, State, City, Place, etc., all inheriting from BaseModel.
* The first abstracted storage engine, File Storage.
* Unit tests to validate all classes and the storage engine.

...
## Command Interpreter
The command interpreter, or console, allows users to interact with the application's data model. It provides functionalities to create, update, destroy, and manage objects via a command-line interface. Objects are stored and persisted to a file in JSON format.

The console serves as a tool to validate the storage engine abstraction. It ensures that objects can be manipulated without having to be concerned about the underlying storage mechanism. This abstraction also facilitates easy switching of storage types without significant changes to the codebase.

### Getting Started
To start the command interpreter, run the console.py script. This will launch the interactive prompt where commands can be entered.

```Bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
==========================================================
EOF  help  quit  show  create  destroy  update  all  count

(hbnb)
(hbnb) help all
Prints all string representation of all instances of a class

(hbnb) help EOF
Exit the program. Usage: Ctrl-D

(hbnb)
(hbnb) quit
$

### How to Use
Once the console is running, you can use various commands to interact with the application's data model. Some of the supported commands include:

* create: Create a new instance of a class.
* show: Display the details of a specific instance.
* destroy: Delete an instance.
* update: Modify the attributes of an instance.
* all: Display all instances of a class or all instances across all classes.
* count: Retrieve the number of instances of a class.
_For detailed usage instructions and examples, refer to the documentation or use the help command within the console._

### Examples
Here are some examples of using the command interpreter:

Creating a new user:
```Bash
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907

Showing details of a user:
```Bash
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}

Updating attributes of a user:

```Bash
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Brenda"
[User] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Brenda', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}

Deleting a User:
```Bash
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb)

Confirm deleted user:
```Bash
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
