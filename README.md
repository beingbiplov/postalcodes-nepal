# postalcodes-nepal


postalcodes-nepal is a python package that helps you to work with postal codes (Zip codes) of Nepal.
Some of the functionality currently supported by postalcodes-nepal are:
  - Query for the postal code of any city of Nepal.
  - Check wheather a postal code is valid code of Nepal. 
  - Find the post office information based on city or postal code.
  - Find postal codes of all post office within a district.
  - Find postal codes of all post office of Nepal

# Installation

Run the following to install:

  ```python
$ pip install postalcodes-nepal
```




## Usage 

Some simple usecases of postalcodes-nepal

 ```python
from postalcodes_nepal.postalcodes import *

#Validate postal code. Checks if the postal code is valid and return True or False accordingly.
validate(44660)

#Find the postal code of particular city. Returns postal code or if the query didnot match any city returns None.
postal_code('Kathmandu')

#Returns the post office informtion of the city ie. District, Post Office, Postal Code and Post Office Type. Returns None if data doesnot match.
city_po_info('Kathmandu')

#Returns the city of the provided postal code. Returns None if data doesnot match.
postalcode_to_city(44600)

#Returns the post office information of the postal code.  Returns None if data doesnot match.
`postalcode_info(44600)

#Returns the city and postal codes of all post office of a district. Returns None if query doesnot match.
district_data('Jhapa')

#Returns the city and postal codes of all post offices of Nepal.
country_data()
```

OR you can alternatively import as follows:
```python
from postalcodes_nepal import postalcodes

postalcodes.validate(44600)

#OR import individually
from postalcodes_nepal.postalcodes import validate

validate(44600)
```
 










   [git-repo-url]: <https://github.com/beingbiplov>
   [biplov]: <https://github.com/beingbiplov>
   