from typing import Annotated

from fastapi import APIRouter, Path, Depends, HTTPException

from api.dependencies import db_dep
from service.helpers import check_last_updated
from service.teams.handlers import get_team_stats_by_metric

from service.teams.helpers import helper_dep

teams_router = APIRouter(prefix='/teams', tags=['teams'], dependencies=[Depends(check_last_updated)])


@teams_router.get('/{club_name}/metrics/{metric}/')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def teams_stats_by_metric(
        club_name: Annotated[str, Path()],
        db: db_dep,
        helper_obj: helper_dep,
):
    if " " in club_name:
        raise HTTPException(status_code=404,
                            detail=f"Wrong path parameter ({club_name}) :: there "
                                   f"shouldn't be any empty substrings. Use this: {club_name.replace(" ", "_")}")

    validated_club_name = club_name.replace("_", " ")
    return await get_team_stats_by_metric(club_name=validated_club_name, helper_obj=helper_obj, db=db)


