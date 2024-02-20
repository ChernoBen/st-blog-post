from models.post import Post
import datetime

class API:
    def __init__(self, config=None) -> None:
        self.config = config
        
    def add_post(self,post:Post):
        return True
    
    def get_posts(self,start_date:datetime.datetime,end_date:datetime.datetime):
        return [
            Post(
                "Ryan","Secret Project",datetime.datetime(year=2024,month=2,day=1)
            ),
            Post(
                "Benja","Arquitetura do projeto",datetime.datetime(year=2024,month=1,day=1)
            )
        ]
            
            