# README

`quantine.py` contains a `class QuantineSQL` which includes
all methods for inserting and reading data.
Use methods `get_canteens_form_four_fifteet_to_six_pm` and `get_canteens_ran_by_rahva_toit(self)`
for retrieving data from database.

All the nessecary files.
`queries.sql` contains all the sql commands for creating and quering the data that is needed
for this exercise.
`scrape.py` file has a scraper that scrapes all the information about diners in Tal Tech and saves it
`curantines.csv` file.
`queries.sql` file also has comments for every sql statement aswell.

## Scraping information
To scrape information it is nessecary to install the dependecies like `bs4` and `requests` libraries.
To do that just run the following:

```
pipenv shell
pipenv install 
```


### Task description

There are 8 diners in different buildings of TalTech:

https://www.ttu.ee/students/university-facilities/canteen/

but IT College diner:

https://www.itcollege.ee/tudengile/oppehoone/kohvik/

is not in this list for unknown reason.

There are 4 service providers in total: Rahva Toit, Baltic Restaurants Estonia AS, TTÜ Sport and Bitstop Kohvik OÜ.

There are different opening hours for every canteen.



Please zip all files (code + readme + SQLite database) and upload to Moodle

Hints: SQLite datatypes: https://www.sqlite.org/datatype3.html


