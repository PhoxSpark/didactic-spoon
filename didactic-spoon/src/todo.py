import os
import argparse
import logging
from calendar import monthrange
from .model.task import Task
from .model.category import Category

def start(args:argparse.ArgumentParser, log:logging.Logger):
    """
    """
    log.debug("To-Do called.")
    
    categories:dict[int,Category] = dict()
    tasks:dict[int, Task] = dict()
    user_input:int = 0
    data_exists:bool = os.path.isfile("tasks.json")
    
    if data_exists:
        log.debug("Previous data found. Reading it.")
    else:
        log.debug("No previous data found. JSON file will be created.")
        open('tasks.json', 'x').close()
    
    # Menu
    while user_input is not 6:
        print("Select an option:")
        print("1. Create new task")
        print("2. Create new category")
        print("3. Modify task")
        print("4. Modify category")
        print("5. List tasks and categories.")
        print("6. Exit")
        
        try:
            user_input = int(input("Enter a value: "))
        except:
            log.warning("Exception handled. Invalid input.")

        if user_input == 1:
            new_task = create_task(log, tasks, categories)
            tasks[new_task.id] = new_task
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            for task in tasks:
                print(tasks[task].stringify())
        elif user_input == 6:
            pass
        else:
            print("Please, enter a valid number.")

def create_task(log:logging.Logger, tasks:dict[int, Task],
                categories:dict[int, Category]):
    """
    Asks user for values of the task to create and create a new object
    with given data. Category should be handled by the object, so just the
    name is ok.
    """
    task_id:int = check_id(log, tasks)
    task_name:str = input("Enter task name: ")
    task_description:str = input("Enter description: ")
    task_category:str = input("Enter category (if not exisist you'll be prompted): ")
    new_task:Task = Task()
 
    task_exp_day:int = 0
    task_exp_month:int = 0
    task_exp_year:int = 0
 
    #Input and validation of expiration date.
    while task_exp_year > 2100 or task_exp_year < 2010:
        task_exp_year = int(input("Enter expiration year: "))
        if task_exp_year > 2100 or task_exp_year < 2010:
            log.warning("Invalid year.")
            print("Try again, invalid year.")

    while task_exp_month > 12 or task_exp_month < 1:
        task_exp_month = int(input("Enter expiration month: "))
        if task_exp_month > 12 or task_exp_month < 1:
            log.warning("Invalid month.")
            print("Try again, invalid month.")

    month_days = monthrange(task_exp_year, task_exp_month)
    while task_exp_day < 1 or task_exp_day > int(month_days[1]):
        task_exp_day = int(input("Enter expiration day: "))
        if task_exp_day < 1 or task_exp_day > int(month_days[1]):
            log.warning("Invalid day.")
            print("Day must be between 1 and " + str(month_days[1]))

    new_task.set_id(task_id)
    new_task.set_name(task_name)
    new_task.set_description(task_description)
    new_task.set_category(Category())
    new_task.set_expiration_date(task_exp_day, task_exp_month, task_exp_year)

    return new_task

def check_id(log:logging.Logger, dict_to_check:dict[int, Task]):
    """
    Check if Tasks dictionary is empty. If empty, ID will be set to 0.
    """
    next_available_id:int = 0
    if bool(dict_to_check): #Check if empty, return true if not.
        for key in dict_to_check:
            if next_available_id == key:
                log.debug("ID {key} is taken.")
                next_available_id += 1
    log.info("ID will be set to {next_available_id}.")
    return next_available_id

def read_json(log:logging.Logger):
    pass

def create_example_json(log:logging.Logger):
    pass