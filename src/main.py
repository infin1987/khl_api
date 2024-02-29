from fastapi import FastAPI
import uvicorn
from api.router import api_router
from auth.router import auth_router

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
# from .routers import items, users

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()
app.include_router(api_router, prefix='/api', tags=['api'])
app.include_router(auth_router, prefix='/auth', tags=['auth'])


# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )
#

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}

if __name__=="__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)