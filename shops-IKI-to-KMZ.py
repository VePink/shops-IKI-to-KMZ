from POIs.functions import pack_attributes

def scrape_IKI(driver):
    driver.get('https://iki.lt/iki-parduotuviu-tinklas/') #open browser

    name_web_elements = driver.find_elements_by_class_name("store-list-item__header")
    address_web_elements = driver.find_elements_by_class_name("store-list-item__row")
    working_hours_web_elements = driver.find_elements_by_class_name("store-list-item__working-hours")

    #create empty lists for storing shops and properties
    names = []
    addresses = []
    working_hours = []

    for i in name_web_elements:
        name = i.get_attribute('innerHTML')
        names.append(name)

    for i in address_web_elements:
        address = i.get_attribute('innerHTML')
        #filter unwanted records
        if (address == "") or (address == "A lygio parduotuvė"):
            pass
        else:
            addresses.append(address)

    for i in working_hours_web_elements:
        timetable = i.text
        working_hours.append(timetable)

    def combineLists ():
        if len(names) == len(addresses) == len(working_hours):
            combined_list = zip(names, addresses, working_hours)
            print("COMBINED list of shop attributes.")
            return list(combined_list)
        else:
            print("Couldn't combine list of shop attributes.")

    shopList = combineLists()

    all_IKI_shops = [] #list for saving shops

    for i in shopList: 
        all_IKI_shops.append(
            pack_attributes(
                i[0], 
                i[1], 
                "not found", 
                "not found", 
                i[2], 
                "", 
                "", 
                "Iki.png")
            )

    return all_IKI_shops   



result_path = (input("Paste path to folder. Result KML will be saved there: ") or "D:\\TMP")
print("Selected result folder: " + result_path)
result_path = (result_path + '\\').replace('\\\\','\\')

api_key = (input("Paste Google Maps Geocoding API key: ") or "AIzaSyABVFtB1GXC-ay7UQRFKTWr5o6bhhHxsEE")
print("key " + api_key + " will be used for geocoding")

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
all_shops = scrape_IKI(driver)
driver.quit() #close browser

from POIs.functions import geolocate
geolocate(api_key, all_shops)

result_filename_prefix = "IKI_"

import datetime
end_timestamp = str(datetime.datetime.now().strftime("%Y%m%d_%H%M"))

from POIs.functions import save_as_KMZ
save_as_KMZ(all_shops, result_path, result_filename_prefix, './Input/IKI.png', end_timestamp)

from POIs.functions import save_as_ZIP
save_as_ZIP(result_path, result_filename_prefix, end_timestamp)

from CLTreport.summary import report_summary
report_summary()