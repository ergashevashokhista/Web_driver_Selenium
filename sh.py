import time, os, selenium, requests, re

from selenium import webdriver

#Create a browser object
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get("https://sourceforge.net/directory/") # Get webpage
browser.implicitly_wait(10) # Wait 10 seconds for browser to load the page

category = 'Blockchain'
operating_system = 'Mac'

args = { 'category': 'Software Development', 'os': 'Linux' }

#Clear all filters
browser.find_element_by_link_text('Clear All Filters').click()

#select category you want i.e Software Development
browser.find_element_by_css_selector("[data-toggle=facet-os]").click()
browser.find_element_by_partial_link_text(operating_system).click() #select os

browser.find_element_by_partial_link_text(category).click()

# retrieve all the results
next_button = browser.find_element_by_class_name("pagination-next")
overall_search_res = []
while True:
    search_results = browser.find_elements_by_xpath("//div[contains(@class,'result-heading-texts')]")
    #get the title of each an every result (program & description)
    for res_text in search_results:
        overall_search_res.append(res_text.text)

    #Check if its the end of the results or not
    if 'disabled' in next_button.get_attribute('class') : break

    #Get next page with list of results (programs)
    next_button.click()
    next_button = browser.find_element_by_class_name("pagination-next")

args = { 'category': 'Security', 'os': 'Virtualization' }

def get_prog_list(args, browser):
    #get main page and clear all filters
    browser.get("https://sourceforge.net/directory/")
    try :
        browser.find_element_by_link_text('Clear All Filters').click()
    except:
        pass

    #select category you want i.e Software Development
    browser.find_element_by_css_selector("[data-toggle=facet-os]").click()
    print(args.get('os','Linux'))
    browser.find_element_by_partial_link_text(args.get('os','Linux')).click() #select os

    element = browser.find_element_by_partial_link_text(args.get('category','Software Development'))
    element.click()

    try:
        next_button = browser.find_element_by_class_name("pagination-next")
        next_button_status = next_button.get_attribute('class')
    except :
        next_button_status = 'disabled'

    overall_search_res = []
    while True:
        search_results = browser.find_elements_by_xpath("//div[contains(@class,'result-heading-texts')]")
        #get the title of each an every result (program & description)
        for res_text in search_results:
            overall_search_res.append(res_text.text)

        #Check if its the end of the results or not
        if 'disabled' in next_button_status : break

        #Get next page with list of results (programs)
        next_button.click()
        next_button = browser.find_element_by_class_name("pagination-next")
        next_button_status = next_button.get_attribute('class')

    return overall_search_res

rr = get_prog_list({ 'category': 'Security', 'os': 'Virtualization' } ,browser)

res_text = '\n'.join([f'{j}. '+i.split('\n')[0] for j,i in enumerate(rr,1)])
print(res_text)

with open('list_Security.txt','w+') as file:
    file.write(res_text)

browser.quit()

# import numpy as np
# Recall = np.array([0.,0.111,0.111,0.111,0.222,0.222,0.222,0.333,0.333,0.444,0.444,0.444])
# precision = np.array([0.,0.5,0.,0.,0.4,0.,0.,0.375,0.,0.4,0.,0.])
# len(precision) == len(Recall)
# r_level = np.arange(0,1.1,0.1)
# r_level
# interpolated = np.zeros(11)
#
# for r in r_level:
#     mask = np.where(Recall >= r)[0]
#     if mask.size == 0: print(0)
#     else : print(precision[mask].max())
