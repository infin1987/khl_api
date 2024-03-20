from fastapi import FastAPI, APIRouter
import uvicorn
from api.router import main_stats_router
from auth.router import auth_router

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
# from .routers import items, users

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

main_auth_router = APIRouter(prefix='/auth', tags=['auth'])
main_app_router = APIRouter(prefix='/api/v1')

main_auth_router.include_router(auth_router)

main_app_router.include_router(main_stats_router)

app.include_router(main_app_router)
app.include_router(main_auth_router)

# app.include_router(api_router, prefix='/api/v1', tags=['api'])
# app.include_router(auth_router, prefix='/auth', tags=['auth'])
# app.include_router(players_router, prefix='/api/v1')


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