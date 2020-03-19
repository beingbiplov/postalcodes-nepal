import json
import pkg_resources

my_data = pkg_resources.resource_filename(__name__, "dataset/postalcodes.json")

with open(my_data) as f:
	NepalData = json.load(f)


def validate(postal_code):
	postal_code = str(postal_code)
	for dict in NepalData:		
		for po_info in dict['data']:
			if po_info['Postal Code'] == postal_code:
				return True
	return False

def postal_code(city):
	city = str(city)
	city = city.capitalize()
	for dict in NepalData:
		for po_info in dict['data']:
			if po_info['Post Office'] == city:
				return po_info['Postal Code']
	return None

def city_po_info(city):
	city = str(city)
	city = city.capitalize()
	for dict in NepalData:
		for po_info in dict['data']:
			if po_info['Post Office'] == city:
				city_po_info = {
					'District' : dict['District'],
					'Post Office' : po_info['Post Office'],
					'Postal Code' : po_info['Postal Code'],
					'Post Office Type' : po_info['Post Office Type'],
				}
				return city_po_info
	return None

def postalcode_to_city(postal_code):
	postal_code = str(postal_code)
	for dict in NepalData:		
		for po_info in dict['data']:
			if po_info['Postal Code'] == postal_code:
				return po_info['Post Office']
	return None

def postalcode_info(postal_code):
	postal_code = str(postal_code)
	for dict in NepalData:		
		for po_info in dict['data']:
			if po_info['Postal Code'] == postal_code:
				city_po_info = {
					'District' : dict['District'],
					'Post Office' : po_info['Post Office'],
					'Postal Code' : po_info['Postal Code'],
					'Post Office Type' : po_info['Post Office Type'],
				}
				return city_po_info
	return None

def district_data(district):
	district = str(district)
	district = district.capitalize()
	district_po_data= []
	for dict in NepalData:
		if dict['District'] == district :
			for po_info in dict['data']:
				district_po_data.append((po_info['Post Office'], po_info['Postal Code']))
			return district_po_data

	return None

def country_data():
	country_po_data = []
	for dict in NepalData:
		for po_info in dict['data']:
			country_po_data.append((po_info['Post Office'], po_info['Postal Code']))
	return country_po_data
