# The AirBnB Clone Project
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

---
### Description of the Project

---
- This is the first step towards building my first full web application: the AirBnB clone. This first step is very important because I will use what I build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

- Each task is linked and will help me to:

1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of my future instances
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4. create the first abstracted storage engine of the project: File storage.5. create all unittests to validate all our classes and storage engine

---
### Description of the Command Interpreter

---
A python command interpreter program built using the python module cmd. Contains to create, update, delete and print a class instance or all instaces created.

## Getting Started
To start the command interpreter type in these commands in your terminal:

```bash
Cloning the repo and starting the console:
==========================================

git clone https://github.com/Prof-Percival/AirBnB_clone.git
cd AirBnB_clone
./console.py
```

---
## Usage
Here is how it can be used. This will show the available commands:

```bash
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
You can get help for specific command by specifing help <command>. For example
(htnb) help create
Usage: create BaseModel
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
```
## Usage and Examples
```bash
./console.py
# Create a BaseModel instance and print its id
(htnb) create BaseModel
53be0422-79fb-4221-80fd-3551589a5940
# to print the instance
(htnb) show BaseModel 53be0422-79fb-4221-80fd-3551589a5940
[BaseModel] (53be0422-79fb-4221-80fd-3551589a5940) {'id': '53be0422-79fb-4221-80fd-3551589a5940', 'created_at': datetime.datetime(2023, 7, 16, 15, 17, 51, 543688), 'updated_at': datetime.datetime(2023, 7, 16, 15, 17, 51, 543688)}
# to print all object created previously
(htnb) all
["[BaseModel] (53be0422-79fb-4221-80fd-3551589a5940) {\'id\': \'53be0422-79fb-4221-80fd-3551589a5940\', \'created_at\': datetime.datetime(2023, 7, 16, 15, 17, 51, 543688), \'updated_at\': datetime.datetime(2023, 7, 16, 15, 25, 14, 443863), \'first_name\': \'"Betty"\'}', "[BaseModel] (f182d7f1-2460-40b8-906f-b61babbec9e2) {'id': 'f182d7f1-2460-40b8-906f-b61babbec9e2', 'created_at': datetime.datetime(2023, 7, 16, 15, 26, 24, 972213), 'updated_at': datetime.datetime(2023, 7, 16, 15, 26, 24, 972213)}"]
```
---
### AUTHORS:
<details>
    <summary>Phadima Maredi</summary>
    <ul>
        <li>
            <a href="https://github.com/Prof-Percival">GitHub</a>
        </li>
        <li>
            <a href="mailto:percival.mrd921@yahoo.com" title="Phadima Email Address">Email Phadima</a>
        </li>
    </ul>
  </details>
  
<details>
    <summary>GEOFFREY ONYANGO ODUOR</summary>
    <ul>
        <li>
            <a href="https://github.com/luckyhope1">GitHub</a>
        </li>
        <li>
            <a href="https://twitter.com/TomGeoffry">Twitter</a>
        </li>
        <li>
            <a href="mailto:geoffrytom@gmail.com" title="Geoffrey Email Address">Email Geoffrey</a>
        </li>
    </ul>
  </details>
---
### God Above All  :pray:
___
All of the work in this project was conducted as part of the ALX-SE program's curriculum. ALX Africa is an online full-stack software engineering school that uses project-based peer learning to educate students for careers in the IT industry. Visit this <a href="https://www.alxafrica.com/software-engineering-2022">website</a> for further information.
