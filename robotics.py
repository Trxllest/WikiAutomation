from RPA.Browser.Selenium import Selenium
from datetime import datetime
import re
from SeleniumLibrary import errors as SeleniumErrors
br = Selenium()


class Robot:
    """`RPA.Browser.Selenium`-based software robot class"""
    
    def __init__(self, name):
        """
        Initializes the Robot object.

        Args:
            name (str): The name of the robot.
        """       
        self.name = name
        self.summaries = []
        
    def say_hello(self):
        """
        Prints a greeting message.
        """
        print("Hello, my name is " + self.name)
        print("I will provide key information about important scientists for you!")
        print("Information will be provided to you below!")
        
    def say_goodbye(self):
        """
        Prints a farewell message.
        """
        print("I have completed my task! I hope the info was usefull!")
        print("Goodbye, my name is " + self.name)

    def extract_info(self):
        """
        Retrieves the infobox-data from the Wikipedia page.

        Returns:
            list: A list containing the birth date, death date, first paragraph,
                  and age of the scientist.
        """  
        info = []
        try :
            birth_date = self.get_date("//td[@class='infobox-data' and ../th[@class='infobox-label' and .='Born']]")
            birth_date = datetime.strptime(birth_date, '%d %B %Y').date()
        except SeleniumErrors.ElementNotFound:
            birth_date = None
            info.append('???')
            
        try:
            death_date = self.get_date("//td[@class='infobox-data' and ../th[@class='infobox-label' and .='Died']]")
            death_date = datetime.strptime(death_date, '%d %B %Y').date()
        except SeleniumErrors.ElementNotFound:
            death_date = None
            info.append('???')
            
        try:
            first_paragraph = br.get_text("//div[@class='mw-parser-output']/p[not(@class)][1]")
        except SeleniumErrors.ElementNotFound:
            info.append('???')
        
        if birth_date and death_date:
            age = (death_date - birth_date).days // 365
        else:
            age = '???'
            
        info.append(birth_date)
        info.append(death_date)
        info.append(first_paragraph)
        info.append(age)
        
        self.summaries.append(info)
        return info
        
    def get_date(self, locator):
        """
        Process and extract the date using the specified locator.

        Args:
            locator (str): The locator string used to find the date element.

        Returns:
            str | None: The extracted date string, or None if not found.
        """
        pattern = r"\b\d{1,2} \w+ \d{4}\b"
        raw_result = None
        try:
            raw_result = br.find_element(locator).text
        except SeleniumErrors.ElementNotFound:
            return None

        check_date = re.search(pattern,raw_result)
        if check_date:
            date = check_date.group()
            # print(date)
            return date
        else:
            print("No date found")

    def open_webpage(self, scientists):
        """
        Opens the Wikipedia page for each scientist and extracts the information.

        Args:
            scientists (list): A list of scientist names.
        """
        br.open_available_browser()
        
        
        for scientist in scientists:
            search = f"{scientist} Wikipedia"
            br.go_to("https://www.google.com")
            br.input_text("id=APjFqb", search) 
            br.press_keys("id=APjFqb", "ENTER")
            br.wait_until_page_contains_element("class=yuRUbf", '15s')
            
            br.click_link('class=yuRUbf a')
            
            print(f'Here is the info for {scientist}:')
            
            info = self.extract_info()

            print(f"\nScientist: {scientist}")
            print(f"Birth Date: {info[0].strftime('%d %B %Y')}")
            print(f"Death Date: {info[1].strftime('%d %B %Y')}")
            print(f"Age: {info[3]} years")
            print(f"First Paragraph: {info[2]}")
            
