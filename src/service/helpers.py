from typing import Annotated

from fastapi import Header, Request

from auth.dependencies import rcache_dep
from exceptions import no_new_data_exception


async def check_last_updated(
        request: Request,
        last_updated: Annotated[int, Header()],
        rcache: rcache_dep
) -> bool:
    """
    Checks if new data is available by comparing the incoming last-update in header vs last-update
    associated with any params that came in path params. If last_last update value in header
    is more than all the values available in redis - then return a response saying no new data
    available and do not try to attempt to a DB, if ANY of the last_updates in REDIS is more ->
    go to DB and fetch new available data
    :param request:
    :param last_updated:
    :param rcache:
    :return:
    """
    path_params = request.path_params
    keys = [f'{param_name}:{param_value}' for param_name, param_value in path_params.items()]
    if keys:
        last_updates = await rcache.hmget('updates', keys=keys)
        last_updates = list(map(lambda x: int(x), filter(lambda x: x is not None, last_updates)))

        if last_updates and all(map(lambda x: x <= last_updated, last_updates)):
            raise no_new_data_exception

    return True