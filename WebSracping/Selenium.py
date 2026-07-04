import os
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

os.makedirs("flipkart_pages", exist_ok=True)

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

options.add_experimental_option(
    "excludeSwitches",
    ["enable-automation"]
)

options.add_experimental_option(
    "useAutomationExtension",
    False
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.execute_script("""
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
})
""")

driver.maximize_window()


base_url = r"https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_5_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_5_0_na_na_na&as-pos=5&as-type=TRENDING&suggestionId=mobiles&requestId=232774c7-b593-436e-893f-9c7688393cd7&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3D6%2BGB&p%5B%5D=facets.ram%255B%255D%3D8%2BGB%2Band%2BAbove&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.brand%255B%255D%3DNothing&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DTecno&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DPeace&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DMicromax&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DGIONEE&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DXOLO&p%5B%5D=facets.brand%255B%255D%3DCMF%2Bby%2BNothing&p%5B%5D=facets.brand%255B%255D%3DBlackZone&p%5B%5D=facets.brand%255B%255D%3DMaplin&p%5B%5D=facets.brand%255B%255D%3DCoolpad&p%5B%5D=facets.brand%255B%255D%3DGOLY&p%5B%5D=facets.brand%255B%255D%3DLeEco&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DSmartron&p%5B%5D=facets.brand%255B%255D%3DBlackBerry&p%5B%5D=facets.brand%255B%255D%3Dhmd&p%5B%5D=facets.brand%255B%255D%3DAcerpure&p%5B%5D=facets.brand%255B%255D%3DHMD&p%5B%5D=facets.brand%255B%255D%3Dringme&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DAi%252B&p%5B%5D=facets.brand%255B%255D%3Ditel&p%5B%5D=facets.brand%255B%255D%3DKechaoda&p%5B%5D=facets.brand%255B%255D%3DSIAVANTAGE&p%5B%5D=facets.brand%255B%255D%3DXOME&p%5B%5D=facets.brand%255B%255D%3DGFive&p%5B%5D=facets.brand%255B%255D%3DSnexan&p%5B%5D=facets.brand%255B%255D%3DAlcatel&p%5B%5D=facets.brand%255B%255D%3DI%2BKall&p%5B%5D=facets.brand%255B%255D%3DYU&p%5B%5D=facets.brand%255B%255D%3DWobble"

START_PAGE = 1
END_PAGE = 42

for page in range(START_PAGE, END_PAGE + 1):

    try:
        print(f"\nDownloading Page {page}")
        driver.get(base_url + f"&page={page}")
        wait_time = random.uniform(4, 8)
        time.sleep(wait_time)
        html = driver.page_source
        if "Access Denied" in html or "captcha" in html.lower():
            print("Flipkart blocked the request.")
            break

        file_path = f"flipkart_pages/page_{page}.html"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Saved {file_path}")

        if page % 15 == 0:
            pause = random.uniform(20, 40)
            print(f"Taking a {pause:.1f} second break...")
            time.sleep(pause)

    except Exception as e:
        print(f"Error on page {page}")
        print(e)

        time.sleep(10)
        continue
input("Press Enter to close browser...")
driver.quit()