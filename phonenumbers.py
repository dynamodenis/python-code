#pip install phonenumbers
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

#Enter phone number with country code

phone_number = phonenumbers.parse('+254758818394')

#this prints the counrty name
print(geocoder.description_for_number(phone_number,'en'))

#this prints the service
print(carrier.name_for_number,'en')