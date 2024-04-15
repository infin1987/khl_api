from fastapi import APIRouter
from .players.routers import players_router
from .teams.routers import teams_router
from .tests.routers import tests_router

main_stats_router = APIRouter()
main_tests_router = APIRouter()

main_stats_router.include_router(players_router)
main_stats_router.include_router(teams_router)
main_tests_router.include_router(tests_router)
