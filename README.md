# IKI-shops-geolocator
Tool for getting geographic locations of "IKI" shops from official website and saving dataset as KML file for later use in variuos geospatial analysis software.

<img src="/images/thumbnail.png" width="500"/>

Data source - official IKI website: https://iki.lt/iki-parduotuviu-tinklas/

## Prerequisites:
* Google Geocoding API from Google Cloud (more info: https://developers.google.com/maps/documentation/geocoding/get-api-key). You must ENABE geocoding API and ADD BILLING to your Google Cloud project (https://cloud.google.com/)

## Usage:
1. Download [tool](https://github.com/VePink/IKI-shops-geolocator/blob/main/dist/IKI_to_KML.exe?) to your PC.
1. Run tool
1. Enter path to folder (e.g.: C:\Users\Ve\Documents\Results). KML file will be saved there. Press Enter.
1. Tool asks for API key. Copy the key and press "Enter".
2. Result file will be saved on provided directory both as KML and ZIP file.

## Result example:
https://github.com/VePink/IKI-shops-geolocator/tree/main/Output
