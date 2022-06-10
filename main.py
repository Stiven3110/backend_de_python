from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/registro")
def registro():
    return {"su cuenta ha sido registrada"}

@app.get("/iniciar_sesion")
def iniciar_sesion():
    return {"has iniciado sesion"}

@app.get("/registro_servicio")
def registro_servicio():
    return {"servicio registrado"}

@app.get("/consultar_servicio")
def consultar_servicio():
    return {"consulta de servicio"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #   return {"item_id": item_id, "q": q}
 #estuve revisando y para mostrar los ejemplos de python mas facil