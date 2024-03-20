from typing import Annotated

from fastapi import Depends

from service.teams.helpers import ModelSchemaHelper

helper_dep = Annotated[ModelSchemaHelper, Depends(ModelSchemaHelper('teams', 'tms'))]

'pl_goals_api_'