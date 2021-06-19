from .category import Category

class Task():
    """
    Object for every task.
    """
    id:int

    complete:bool
    name:str
    description:str
    category:Category

    expiration_day:int
    expiration_month:int
    expiration_year:int

    creation_day:int
    creation_month:int
    creation_year:int

    def __init__(self):
        pass
        

    #Setters
    def set_id(self, id:int):
        self.id = id

    def set_name(self, name:str):
        self.name = name
    
    def set_description(self, description:str):
        self.description = description
    
    def set_category(self, category:Category):
        self.category = category
    
    def set_expiration_date(self, expiration_day:int, expiration_month:int, expiration_year:int):
        self.expiration_day = expiration_day
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
    
    #Date
    def set_expiration_date_list(self, expiration_date:list[int]):
        """
        (DAY,MONTH,YEAR)
        """
        self.expiration_day = expiration_date[0]
        self.expiration_month = expiration_date[1]
        self.expiration_year = expiration_date[2]
    
    def set_expiration_date_dict(self, expiration_date:dict[str,int]):
        """
        {"day":int, "month":int, "year":int}
        """
        self.expiration_day = expiration_date["day"]
        self.expiration_month = expiration_date["month"]
        self.expiration_year = expiration_date["year"]

    def set_expiration_day(self, expiration_day:int):
        self.expiration_day = expiration_day
    
    def set_expiration_month(self, expiration_month:int):
        self.expiration_month = expiration_month
    
    def set_expiration_year(self, expiration_year:int):
        self.expiration_year = expiration_year

    def stringify(self):
        

    def testerror():
        pass

