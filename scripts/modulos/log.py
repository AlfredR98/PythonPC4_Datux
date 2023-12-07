import os
from datetime import datetime
class Log:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'storelog.txt')
    def register_log(self,data):
        try:
            now=datetime.now()
            log_entry=f"log[{now}]-[{data}]\n"
            with open(self.file_path, mode='a') as file_data:
                file_data.write(log_entry)
            print("se registro el log correctamente")
        except Exception as e:
            print("erro in register log",e)