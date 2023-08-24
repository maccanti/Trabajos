class Todo:
    def __init__(self, code_id:int, title:str, description:str ):
        self.code_id:int=code_id
        self.title:str=title
        self.descripion:str=description
        self.completed:bool=False
        self.tags:list=[]
    
    def mark_completed(self):
        self.completed=True

    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def __str__(self):
        return "{}-{}".format(self.code_id,self.title)
    
class TodoBook:
    def __init__(self):
        self.todos:dict={}
    
    def add_todo(self,title:str, description:str)->int:
        id=len(self.todos)+1
        todo=Todo(id, title, description)
        self.todos[id]=todo
        return id
    
    def pendings_todo(self)-> list[Todo]:
        lista_tareapend=[todo for todo in self.todos.values() if not todo.completed]
        return lista_tareapend