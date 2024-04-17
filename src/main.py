from fastapi import FastAPI, APIRouter
import uvicorn
from api.router import main_stats_router, main_tests_router
from auth.router import auth_router

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
# from .routers import items, users

# app = FastAPI(dependencies=[Depends(get_query_token)])

app = FastAPI()

main_auth_router = APIRouter(prefix='/auth', tags=['auth'])
main_app_router = APIRouter(prefix='/api/v1')
tests_router = APIRouter(prefix='/tests')

main_auth_router.include_router(auth_router)
main_app_router.include_router(main_stats_router)
tests_router.include_router(main_tests_router)

app.include_router(main_app_router)
app.include_router(main_auth_router)
app.include_router(tests_router)


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
