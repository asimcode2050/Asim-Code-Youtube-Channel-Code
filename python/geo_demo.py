from pygeocoder import Geocoder
results = Geocoder.geocode("Mountain View")
print(results.coordinates)
print(results.country)
print(results.postal_code)
print(results.latitude)
print(results.longitude)
results = Geocoder.reverse_geocode(results.latitude,results.longitude)
print(results.formatted_address)
print("--------------------------")