# AirBnB clone - The console

<img src="./assets/hbnb_header.png" alt="ALX AirBnB header">

## Background Context

### First step: Write a command interpreter to manage your AirBnB objects.

<p>This is the first step towards building your first full web application: the AirBnB clone, the famous online platform that enables people to book unique accommodations around the world. It collectively covers the fundamental concepts of higher level programming. </p>

<p>This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration</p>

<p>The website allows users to search for various types of accommodations, such as apartments, villas, hotels, and hostels, and book them online.</p>
<p>The project is suitable for developers who want to improve their web development skills, especially in front-end development, back-end development, and database management.</p>

## The Console

<p>A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).</p>
<p>This is the command interpreter for the Airbnb clone website, implementing a back-end system that can interpret user commands and manipulate data without a visual interface. It is a custom shell or command-line interface (CLI) that allows developers to interact with the website's database directly.</p>
<p>The console should provide a set of commands that developers can use to manipulate data in the database, such as creating new listings, updating existing ones, deleting listings, and querying for information about specific listings
It is built using the Python3 programming language</p>

<hr>

## Environment:

> - This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.10.6)

<hr>

### Installation

> - Clone this repository: `git clone "https://github.com/odoublea/AirBnB_clone.git"`
> - Access AirBnb directory: `cd AirBnB_clone`
> - Run hbnb(interactively): `./console` and enter command
> - Run hbnb(non-interactively): `echo "<command>" | ./console.py`

<hr>

### Execution

shell should work like this in interactive mode:

```shell script
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

<hr>

# Author

> - [AbdulQudus Oladega](https://github.com/odoublea)
