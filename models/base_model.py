#!/usr/bin/python3

"""base class that defines all common attributes/methods for other classes"""

import uuid
import datetime

class BaseModel():

"""defining a class base model"""

def __init__ (self):
    self.id = str(uuid4())
    self.created_at = datetime 
