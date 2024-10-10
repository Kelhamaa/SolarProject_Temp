from typing import Union
from fastapi import FastAPI,Request
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.models import OpenAPI, Response
from fastapi.staticfiles import StaticFiles
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from setting import TORTOISE_ORM

from maininterface import maininterface
from structure import struc


from request import req
from router import router,custom_swagger_ui_html,redoc_html,get_openapi

app=FastAPI()
# "/static" is path, has nothing to do with directory name, can call it what you want
#app.mount("/static",StaticFiles(directory="statics"))

# forget this and cannot connect with database, big idiot
# orm: object related mapper. class in python -- tables in database
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # if database is empty, automatically create. Do not open this in development environment
    # add_exception_handlers=True, #Do not open this in development environment

)

app.include_router(maininterface,tags=["maininterface"])
app.include_router(struc,tags=["structure"])

app.include_router(req,tags=["request"])

app.include_router(router)
app.add_route("/docs", custom_swagger_ui_html, methods=["GET"])
app.add_route("/redoc", redoc_html, methods=["GET"])
app.add_route("/openapi.json", get_openapi, methods=["GET"])

@app.middleware("http")
async def middleware2(request:Request,call_next):
    # request code
    print("m2 request")
    response=await call_next(request)
    # response code
    print("m2 response")
    response.headers["editer"] = "yuju"
    return response

@app.middleware("http")
async def middleware1(request:Request,call_next):
    # request code
    print("m1 request")
    # if request.url.path in ["/density"]:
    #     return Response(content="forbidden",status_code=403)
    response=await call_next(request)
    # response code
    print("m1 response")
    response.headers["editer"] = "yuju"
    return response





@app.get("/")
async def get_home():
    return {"message": "Hello World"}




if __name__=="__main__":
    uvicorn.run('main:app',port=8080,reload=False)





