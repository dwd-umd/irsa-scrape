"""
STAGE 0
This approach downloads the bare html then triggers the JS in our python script to populate the full html
"""

import os
import sys
import time
import typing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the url for the javascript-enriched webpage
irsa_url: str = 'https://irsa.ipac.caltech.edu/applications/wise/#id=Hydra_wise_wise_5&RequestClass=ServerRequest&DoSearch=true&subsize=0.16666666800000002&cat_overlay=_none_&schema=allsky-4band&band=1,2,3,4&obj_name=606%20Brangane&obj_naifid=2000606&obj_prim_designation=2000606&preliminary_data=no&projectId=wise&searchName=wise_5&shortDesc=Solar%20System%20Object/Orbit&isBookmarkAble=true&isDrillDownRoot=true&isSearchResult=true'

# Choose between phantomjs- and chrome- browser drivers
driver: typing.Any
options: typing.Any = Options()
if len(sys.argv) > 1 and sys.argv[1] == 'headless':
    options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


# Get the web page with Chrome; Chrome will execute the automatically triggered JS as normal
driver.get(irsa_url)

# Start a loop to check when the table-view button becomes available then click it
# Checks every second and maxes out at 100s
isLooping = True
count = 0
while isLooping:
    count += 1
    if count > 100:
        isLooping = False
    try:
        # Try clicking button; leave loop if succesful
        div = driver.find_element_by_class_name('selectable-view')
        time.sleep(1)
        div.click()
        isLooping = False
    except:
        # Sleep if no button was found
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)


time.sleep(1)

# Click 'title="Edit Table Options"' div to reveal Page Size input field
driver.find_element_by_xpath('//*[@title="Edit Table Options"]').click()

time.sleep(1)

# Set the 'Page Size input field' to max permitted value (=3000)
input = driver.find_element_by_class_name('firefly-inputfield-valid')
input.clear()
driver.execute_script(
    "console.log(arguments[0]);arguments[0].setAttribute('value', '3000')", input)
input.send_keys('3000')  # Type 3000
input.send_keys(u'\ue007')  # Type Enter

time.sleep(4)

# Extract html as it now stands in Chrome browser
html_source: str = driver.page_source

# Close Chrome now that we're done
driver.quit()

# Save extracted javascript-enriched html to output file
dir_path: str = os.path.dirname(os.path.realpath(__file__))
output_file: str = dir_path+'/data1/enriched.html'
with open(output_file, 'w') as the_file:
    the_file.write(html_source)
