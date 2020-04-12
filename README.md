# HW nr 3

## Using the files.


## Homework description

Koduülesande eesmärk on harjutada graafilise keskkonna ja andmetega töötamist ning erinevatest allikatest pärit andmete kokkuliitmist. Samuti on eesmärgiks  pakettide paigaldamise õppimine keerulisematel juhtumitel.

Ülesandeks on Tallinnast väljuvate otselendude joonistamine Euroopa kaardile. OpenFlights Airports Database-s https://openflights.org/data.html on üle 14000 lennujaama üle kogu maailma, kuid regulaarlennud Tallinnast toimuvad ainult mõnekümnesse.

Lennujaamade andmed koos geograafiliste koordinaatidega
https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat (ilma veerupealkirjadeta)
või
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat (veerupealkirjadega).

Tallinnast väljuvad otselennud:
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud.csv

Nende kahe tabeli põhjal ning Pythoni kartograafia- (nt. cartopy) ja joonestuspakettide (nt. matplotlib) kasutamisega tuleb luua Euroopa kaart ning kaardile kuvada lennujaamad, kuhu saab Tallinnast lennata koos lennuteekondadega sinna. Tähelepanu tasub pöörata sellele, et tulenevalt maakera kumeruse kujutamise iseärasustest ei ole geograafiline otsetee kahemõõtmelisel kaardil sirgjoon, vaid kõver.
Loodud programm peab joonestama kaardi nii ekraanile kui ka salvestama failina (png, jpg, pdf või mõni muu formaat) sarnaselt näidisele: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.png Kaardil peab olema ka pealkiri. Muu kujundus on omal valikul.

Samad andme- ja näidisfailid asuvad kokkupakituna ka ülesande lisas.
------
Kuidas teha?

Ilmselt on otstarbekas Tallinnast väljuvate otselendude tabelile lisada koordinaadid.
Üks võimalus seda teha on kasutada 'pandas' library-t, selleks tuleb csv failid importida (pandas.read_csv) ja seejärel kokku 'mergeda'. Ühine väli kannab nime 'IATA'. Tasub tähele panna, et ühes failis on väljade eraldaja koma, teises semikoolon.
Pandas csv importimine https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

Kokkutõstetud andmetega tabeli näidis on: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.txt

Mõningad viited:

https://scitools.org.uk/cartopy/docs/latest/installing.html
Cartopy installeerimine Conda abiga.


Maakaartide (kontuurkaardid jne) joonistamine. Lennuteekondade joonistamine.
https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html

Veel lisalugemist:
https://matplotlib.org/basemap/users/geography.html
https://matplotlib.org/basemap/users/installing.html
https://matplotlib.org/basemap/users/intro.html
https://towardsdatascience.com/planning-to-travel-around-the-world-with-python-42fac1d21a6e

https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py