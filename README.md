
## Table of contents:
- [Introduction](#intro)
- [Technologies](#tech)
- [project Setup](#projo)
- [Illustrations](#illus)
- [Project Information](#info)
- [Contributing](#contri)
- [Acknowledgments](#know)

<INTRODUCTION>

<h1 id="intro">File Search</h1>

## Ingredient info search script (Soup )
After creating an Ingredient() class and learning about OOP, it's time to make something useful with your new knowledge.

For this project, you'll build an ingredient info search script. Your Python code should do the following:

Implement the Ingredient() class, where each ingredient has at least a .name and an .amount attribute.
Add an instance method called .get_info() that takes the .name attribute of an Ingredient() and creates a Wikipedia URL.
The .get_info() method should then automatically open the corresponding Wikipedia page in your web browser:
Wikipedia page of 'carrot'

To complete this project, you'll need to create a new instance method, as well as read up on how you can use Python to open up your local web browser at a certain URL. To help you get started, check out the documentation of the webbrowser module in Python's standard library.

You'll also need to think about how to create the right URL to find the page you're looking for. Go to Wikipedia and search for a page. Then take a look at the URL. What can you see?

https://en.wikipedia.org/wiki/Carrot
What happens when you change to a different page? How can you implement this in your .get_info() method, and what potential challenges could you encounter? If you want to challenge yourself, you can even try to write some code to tackle some of these challenges.

As always, you're encouraged to map out the plan for your program in your notebook. Scribble, draw, draft, and revisit. Convert your handwritten notes to pseudocode. Only then you should start writing your functional code.

Tasks
What other methods can you think to implement in your Ingredient() class?
What type of webbrowser call could you add to your .cook() method?
Think about the organization of your class and practice working with self to get a better understanding of how Python classes work internally.

When you are done with this project, you can move on to the next project where you'll improve your CLI game with object-oriented concepts.


________________________________________________________________________________________________________________________________________________________________________

For this project, you'll create a custom Soup() class that can take Ingredient() and Spice() objects, and use them to look up soup recipes on the Internet.

Your Soup() objects should at least be able to:

take an unlimited number of Ingredient() or Spice() objects during instantiation
have a .cook() method that returns a search result for a soup recipe using all the added ingredients
Keep in mind that you're building an abstraction for your users. You can hide a lot of the inner workings of your Soup() instances from them to present them with a simple interface




<TECHNOLOGIES>

<h1 id="tech">Technologies</h1>

## Builth With
- Python
- Beautifulsoup4
- requests


<PROJECT-SETUP>

<h1 id="projo">Project Setup</h1>


## Hardware Requirements
- You will need a desktop or a laptop computer
- RAM: A minimum of 4GB RAM is recommended
- Disk Space: You should have at least 5GB free of space on your working hard drive

## Software Requirements

## Prerequisites

To get this project up and running locally, you must already have python plus the necessary packages installed on your computer

**simple steps to set up on your local machine**

```
- $ git clone `$ git clone https://github.com/symonkipkemei/scrape.git`
- $ git checkout develop
- Run `python main.py`
```

- [Live Version](https://replit.com/@symonkipkemei/scrape#scrape.py)


<PROJECT-INFORMATION>

<h1 id="info">Project Information</h1>

## Project Status
- In development

## Features
- Analysis of recipes
- Allow users to retrive a particular recipe

## TODO




<CONTRIBUTING>

<h1 id="contri">🤝 Contributing</h1>

Contributions, issues and feature requests are always welcome!

I love meeting other developers, interacting and sharing.

Feel free to check the [issues page](https://github.com/symonkipkemei/scrape/issues).

### How to Contribute

To get a local copy up and running follow these simple example steps.

```
- Fork the repository
- git clone https://github.com/your_username/scrape
- git checkout develop
- git checkout -b branch name
- git remote add upstream https://github.com/symonkipkemei/scrape
- git pull upstream develop
- git commit -m "commit message"
- git push -u origin HEAD
```


<ACKNOWLEDGMENTS>

<h1 id="know">Acknowledgements</h1>

## Author

👤 **Symon Kipkemei**

- Github: [symonkipkemei](https://github.com/symonkipkemei)
- Twitter: [@symon_kipkemei](https://twitter.com/symon_kipkemei)
- LinkedIn: [Symon kipkemei](https://www.linkedin.com/in/symon-kipkemei/)


## Show your support

Be strong, be fearless, be beautiful. And believe that anything is possible when you have the right people there to support you. ~ Misty Copeland


## Acknowledgments

- [codingnomads](https://codingnomads.co/).
