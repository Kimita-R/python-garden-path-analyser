# Garden Path Sentences Analyzer
This python script uses the spaCy library to analyse sets of Garden Path Sentences, extracting and identiying their parts of speech. 

## Requirements
* Python 3.x
* spaCy 3.x

## Getting Started 
To get started with this project, follow these steps:

* Clone this repository
* Build the Docker image: docker build -t myproject .
* Run the Docker container: docker run -it --rm myproject
* Run the script by typing python garden.py and pressing enter in the console

## Installation
* Run the requirements.txt file 
OR 
* Install Python 3.x from the official website
* Install spaCy by running pip install spacy on your terminal or command prompt
* Download the en_core_web_sm model for spaCy by running python -m spacy download en_core_web_sm

## Usage
* Clone or download the code from this repository
* Open a terminal or command prompt and navigate to the directory where the code is located
* The script has a list of pre-programmed garden path sentences - to test your own sentences open the script and add new sentences to the "gardenpathSentences" list.
* Run the script by typing python garden.py and pressing enter
* The script will print the parts of speech for each word in each sentence.
