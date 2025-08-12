#parent class
class browserutils():

    def __init__(self,driver):
        #obj1.driver=driver obj1 thaan enga  object  self thaa class oda object
        self.driver=driver


    def get_title(self):
        return self.driver.title



#| Part                       | Meaning                                      |
#| -------------------------- | -------------------------------------------- |
#| `def`                      | function create panrom                       |
#| `get_title`                | function name                                |
#| `(self)`                   | class object                                 |
#| `return self.driver.title` | browser la irukkura page title return panrom |


#| Word          | Meaning                         |
#| ------------- | ------------------------------- |
#| `self`        | naan (நான்) – ithu class object |
#| `self.name`   | en peru                         |
#| `self.driver` | en browser driver               |


#self = current object (for example: obj)

#So self.driver = obj.driver

#  self.driver=driver