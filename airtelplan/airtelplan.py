import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window
driver.get('https://www.airtel.in/myplan-infinity/')

# Collecting Price Details
price=driver.find_elements(By.CLASS_NAME,"price")
prices=[]
for i in price:
    pric=i.text
    prices.append(pric)


# collecting Validity data
valid=driver.find_elements(By.XPATH,"//div[@class='cart_head'][1]")
validity=[]
for i in valid:
     v=i.text
     validity.append(v)



#collecting Data value
dataget=driver.find_elements(By.XPATH,"//div[@class='border-bottom'][1]")
data=[]
for i in dataget:
    da=i.text
    data.append(da)



# Collecting SMS data
smspack=driver.find_elements(By.XPATH,"//div[@class='border-bottom'][2]")
sms=[]
for i in smspack:
    sms1=i.text
    sms.append(sms1)



# collecting Call details
calling=[]
call=driver.find_elements(By.XPATH,"//div[@class='border-bottom'][3]")
for i in call:
    ca=i.text
    calling.append(ca)



# collecting Amazon details 
amazon_status=[]
amazon=driver.find_elements(By.XPATH,"//div[@class='border-bottom'][4]")
for i in amazon:
    am=i.text
    amazon_status.append(am)




# benefit Avilable
airtelthanks=driver.find_elements(By.XPATH,"//p[@class='additional-benefits-title'][1]")
airtel=[]
for i in airtelthanks:
    air=i.text
    airtel.append(air)
print(airtel)




mydb = mysql.connector.connect(
  host="localhost",
  user="alok",
  password="root",
  database="airtel project"
)
mycursor = mydb.cursor()

add_news = ("INSERT INTO plan_airtelplan"
                "(prices,validity, data, sms, calldetails, amazon,benifit) "
                "VALUES ( %s, %s, %s, %s, %s , %s , %s )")
for i in range(len(prices)):   
    data_news = (prices[i],validity[i], data[i], sms[i], calling[i], amazon_status[i], airtel[i])
    mycursor.execute(add_news,data_news)
    mydb.commit()
mycursor.close()
mydb.close()

print(mydb)
