# HW nr 3

[Link to additional files](http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/)


## Using the files.

Make sure to  have Anaconda installed on the machine.
Installation [link](https://www.anaconda.com/distribution/)

```
conda create --name flight python=3.7 pandas cartopy jupyter -y
conda activate flight
```
[More info about conda enviromnents](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Setting up data science stuff on vscode [Link](https://code.visualstudio.com/docs/python/data-science-tutorial)

cleaning up after. Uninstalling the conda environment.
```
conda deactivate flight

conda remove --name flight --all -y
```

## Homework description

The aim of the homework is to practice working with a graphical environment and data, and to combine data from different sources. The aim is also to learn how to install packages in more complex cases. This is probably the most difficult homework, as installing packages can be quite complicated and may require a lot of time and additional reading.

The task is to draw direct flights departing from Tallinn on a map of Europe. The OpenFlights Airports Database https://openflights.org/data.html has over 14,000 airports around the world, but scheduled flights from Tallinn to only a few dozen (before Corona-crisis).

Airport data with geographical coordinates
https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat (without column headers)
or
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat (with column headers).

Direct flights departing from Tallinn:
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud.csv

Based on these two tables, and using Python's cartography (eg cartopy) and drawing packages (eg matplotlib), a map of Europe must be created and the airports displayed on the map, where you can fly on direct routes from Tallinn. It is worth noting that due to the peculiarities of depicting the curvature of the globe, a geographical shortcut on a two-dimensional map is not a straight line, but a curve.
The created program must draw the map both on the screen and save it as a file (png, jpg, pdf or some other format) similar to the example: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.png The map must have also the title. Other designs are on your choice.

The same data and sample files are also compressed in the task attachment.
------
How to do this homework?

It is probably useful to add coordinates to the table of direct flights departing from Tallinn.
One way to do this is to use the 'pandas' library by importing the csv files (pandas.read_csv) and then to merge. The common field is called 'IATA'. Note that one file has a field separator comma, the other a semicolon.
Importing Pandas csv https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

An example of a table with aggregated data is: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.txt (Don't use it in homework!)

Some references:

https://scitools.org.uk/cartopy/docs/latest/installing.html
Installing Cartopy with Conda.

Drawing maps (contour maps, etc.). Drawing flight paths.
https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html

More reading:
https://matplotlib.org/basemap/users/geography.html
https://matplotlib.org/basemap/users/installing.html
https://matplotlib.org/basemap/users/intro.html
https://towardsdatascience.com/planning-to-travel-around-the-world-with-python-42fac1d21a6e

https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
