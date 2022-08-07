from selenium import webdriver
import time

web = webdriver.Chrome('/Users/kareem/auto/chromedriver')
web.get('https://debbiedingell.house.gov/forms/writeyourrep/?zip5=48126&zip4=')
time.sleep(1)


streetadd = web.find_element("xpath",'//*[@id="ctl00_ctl16_Street"]')
streetadd.send_keys('19855 W Outer Dr')

city = web.find_element("xpath",'//*[@id="ctl00_ctl16_City"]')
city.send_keys('Dearborn')

zipnum= web.find_element("xpath",'//*[@id="ctl00_ctl16_Zip"]')
zipnum.send_keys('48124')

phonenum = web.find_element("xpath",'//*[@id="ctl00_ctl16_Phone"]')
phonenum.send_keys('000-000-0000')

emailinfo = web.find_element("xpath",'//*[@id="ctl00_ctl16_Email"]')
emailinfo.send_keys('Handalacoalition@gmail.com')

subject = web.find_element("xpath",'//*[@id="ctl00_ctl16_Subject"]')
subject.send_keys('WE DEMAND THAT YOU SPEAK UP FOR MASAFER YATTA, PROTECT PALESTINIAN AMERICANS, AND STOP OUR TAX DOLLARS FROM MURDERING PALESTINIANS')

commenttext = web.find_element("xpath",'//*[@id="ctl00_ctl16_Body"]')
commenttext.send_keys("Dear Debbie Dingell,\n\n- We demand that you join Congresswoman Cori Bush in sending a letter to the Biden administration calling out Israeli war crimes and demanding that the U.S. push for Israel's demolitions and displacement to end.\n\n- We demand that you call out Israel's racist 97 page directive policy aimed in isolating, surveilling, and discriminating  Palestinian Americans trying to visit their family and land.\n\n- We demand that you stop receiving contributions from war mongering weapon manufacturers like Lockheed Martin \n\n- We demand that you fight against our tax dollars being used to murder Palestinians and instead used to invest in our communities.\n\nIsrael’s High Court has just ruled that over 1,000 Palestinians can be forcibly evicted from their land in the Occupied West Bank. The Court’s decision is a devastating blow to twelve of the villages situated in Masafer Yatta, in the South Hebron Hills, and yet another clear example of Israeli apartheid in action.\n\nWe demand an urgent response from you to prevent this ethnic cleansing of Palestinians.\n\nIn May 2022 the Coordination of Government Activities in the Territories, known as COGAT, the unit of Israel’s Defense Ministry tasked with administering civilian issues in the Palestinian territories that Israel illegally occupies issued  a 97-page document. This document introduced a slate of severe restrictions on international travel to the occupied West Bank. These policies are racist, degrading, violates our right to privacy and collects data that is used to help them further illegally occupy Palestinian land.\n\nWe DEMAND that you take action and speak up for Palestinian Americans that are vulnerable under such policy.\n\nOn Aug 5 2022, Israel bombs Gaza without warning murdering at least 9 Palestinians and 44 wounded. Israel has one of the most powerful militaries in the world and is attacking a largely defenseless entrapped civilian population. We are tired of our tax dollars being used to bomb one of the most densely populated places in the world. We demand that you do your part as our representative and speak out against our hard earned tax dollars  being used to commit massacres overseas.\n\nPlease respond accordingly,\n\nYour constituents ")