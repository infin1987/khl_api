from fastapi import APIRouter

from .arenas.routers import arenas_router
from .players.routers import players_router
from .refs.routers import refs_router
from .teams.routers import teams_router
from .tests.routers import tests_router

main_stats_router = APIRouter()
main_tests_router = APIRouter()

main_stats_router.include_router(players_router)
main_stats_router.include_router(teams_router)
main_tests_router.include_router(tests_router)
main_stats_router.include_router(arenas_router)
main_stats_router.include_router(refs_router)
