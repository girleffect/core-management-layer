"""
This module manages the common permission-related information in convenient
formats.

In order to prevent repeated API lookups, data can be loaded when the
application is started and refreshed as necessary. We typically store
dictionaries where the key is the id of the entity, and the value is the entity
itself, as well as a dictionary which maps the text identifier of the entity
to its id.

While the use of globals to store these values can be problematic in the case
where an application is multi-threaded, the same is not true when the application
uses an event loop, since it is single-threaded in nature.

The values stored in the global dictionaries are refreshed when a scheduled
job calls one of the refresh_* functions. Typically a refresh will use a cached
value from Memcache, but, if the value is not in memcache or it expired, the
API will be queried and the cache updated.

If multiple instances of the management-layer is running, typically only one
will have to refresh memcache, after which the rest will use the cached values.

"""
import json
import logging

from typing import Callable, Tuple, List, Dict, TypeVar, Awaitable

import aiomcache
import time
from aiohttp import web

from management_layer import transformations
from management_layer.settings import CACHE_TIME
from management_layer.sentry import sentry

logger = logging.getLogger(__name__)

# Internal copies of definitions. These are mappings of ids to dictionaries.
DOMAINS = {}  # type: Dict[int, Dict]
PERMISSIONS = {}  # type: Dict[int, Dict]
RESOURCES = {}  # type: Dict[int, Dict]
ROLES = {}  # type: Dict[int, Dict]
SITES = {}  # type: Dict[int, Dict]

# Name/label to id mappings.
DOMAIN_NAME_TO_ID_MAP = {}  # type: Dict[str, int]
PERMISSION_NAME_TO_ID_MAP = {}  # type: Dict[str, int]
RESOURCE_URN_TO_ID_MAP = {}  # type: Dict[str, int]
ROLE_LABEL_TO_ID_MAP = {}  # type: Dict[str, int]
SITE_NAME_TO_ID_MAP = {}  # type: Dict[str, int]
SITE_CLIENT_ID_TO_ID_MAP = {}  # type: Dict[str, int]

# Custom convenience type
T = TypeVar("T")


async def _load(
    api_call: Callable[..., Awaitable[List[T]]],
    memcache: aiomcache.Client, transform: transformations.Transformation,
    key: bytes, name_field: str, nocache: bool=False
) -> Tuple[Dict[int, T], Dict[str, int]]:
    """
    Generic function to load permission-related information from the cache
    or Access Control component.

    :param api_call: The API call that returns the needed information
    :param memcache: The memcache client to use
    :param transform: The transformation to apply to results
    :param key: The cache key to use
    :param name_field: The name of the field in which the text name can be found
    :param nocache: Optional flag to bypass the cache for reading values
    :return: A tuple containing the an id->entity map, as well as a str->id
        mapping.
    """
    items = None if nocache else await memcache.get(key)
    if not items:
        logger.debug("Loading from API")
        items_by_id = {}  # type: Dict[int, T]
        offset = 0
        items = await api_call(offset=offset, limit=20)
        while items:
            for item in items:
                items_by_id[item.id] = transform.apply(item.to_dict())
            # Check if there are more items
            offset += len(items)
            items = await api_call(offset=offset)

        await memcache.set(key, json.dumps(items_by_id).encode("utf8"), CACHE_TIME)
    else:
        logger.debug("Loaded from cache")
        items_by_id = json.loads(items, encoding="utf8")

    name_to_id_map = {
        item[name_field]: id_ for id_, item in items_by_id.items()
    }  # type: Dict[str, int]

    return items_by_id, name_to_id_map


async def refresh_domains(app: web.Application, nocache: bool=False):
    """Refresh the global domain information"""
    logger.info("Refreshing domains")
    global DOMAINS
    global DOMAIN_NAME_TO_ID_MAP
    start_time = time.time()
    try:
        DOMAINS, DOMAIN_NAME_TO_ID_MAP = await _load(
            app["access_control_api"].domain_list, app["memcache"], transformations.DOMAIN,
            bytes(f"{__name__}:domains", encoding="utf8"), "name", nocache
        )
        total_time = (time.time() - start_time) * 1000
        logger.info(f"Refreshed in {total_time:.3f} ms")
    except Exception as e:
        sentry.captureException()
        logger.error(e)


async def refresh_permissions(app: web.Application, nocache: bool=False):
    """Refresh the global permission information"""
    logger.info("Refreshing permissions")
    global PERMISSIONS
    global PERMISSION_NAME_TO_ID_MAP
    start_time = time.time()
    try:
        PERMISSIONS, PERMISSION_NAME_TO_ID_MAP = await _load(
            app["access_control_api"].permission_list, app["memcache"], transformations.PERMISSION,
            bytes(f"{__name__}:permissions", encoding="utf8"), "name", nocache
        )
        total_time = (time.time() - start_time) * 1000
        logger.info(f"Refreshed in {total_time:.3f} ms")
    except Exception as e:
        sentry.captureException()
        logger.error(e)


async def refresh_resources(app: web.Application, nocache: bool=False):
    """Refresh the global resources information"""
    logger.info("Refreshing resources")
    global RESOURCES
    global RESOURCE_URN_TO_ID_MAP
    start_time = time.time()
    try:
        RESOURCES, RESOURCE_URN_TO_ID_MAP = await _load(
            app["access_control_api"].resource_list, app["memcache"], transformations.RESOURCE,
            bytes(f"{__name__}:resources", encoding="utf8"), "urn", nocache
        )
        total_time = (time.time() - start_time) * 1000
        logger.info(f"Refreshed in {total_time:.3f} ms")
    except Exception as e:
        sentry.captureException()
        logger.error(e)


async def refresh_roles(app: web.Application, nocache: bool=False):
    """Refresh the global roles information"""
    logger.info("Refreshing roles")
    global ROLES
    global ROLE_LABEL_TO_ID_MAP
    start_time = time.time()
    try:
        ROLES, ROLE_LABEL_TO_ID_MAP = await _load(
            app["access_control_api"].role_list, app["memcache"], transformations.ROLE,
            bytes(f"{__name__}:roles", encoding="utf8"), "label", nocache
        )
        total_time = (time.time() - start_time) * 1000
        logger.info(f"Refreshed in {total_time:.3f} ms")
    except Exception as e:
        sentry.captureException()
        logger.error(e)


async def refresh_sites(app: web.Application, nocache: bool=False):
    """Refresh the global sites information"""
    logger.info("Refreshing sites")
    global SITES
    global SITE_NAME_TO_ID_MAP
    start_time = time.time()
    try:
        SITES, SITE_NAME_TO_ID_MAP = await _load(
            app["access_control_api"].site_list, app["memcache"], transformations.SITE,
            bytes(f"{__name__}:sites", encoding="utf8"), "name", nocache
        )
        global SITE_CLIENT_ID_TO_ID_MAP
        SITE_CLIENT_ID_TO_ID_MAP = {
            detail["client_id"]: id_ for id_, detail in SITES.items()
        }
        total_time = (time.time() - start_time) * 1000
        logger.info(f"Refreshed in {total_time:.3f} ms")
    except Exception as e:
        sentry.captureException()
        logger.error(e)


async def refresh_all(app: web.Application, nocache: bool=False):
    """
    Refresh all data mappings
    """
    logger.info("Refreshing all mappings")
    await refresh_domains(app, nocache)
    await refresh_permissions(app, nocache)
    await refresh_resources(app, nocache)
    await refresh_roles(app, nocache)
    await refresh_sites(app, nocache)
