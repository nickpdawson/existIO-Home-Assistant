from homeassistant import config_entries, core
import asyncio
import logging

from .api import ExistIOAPI
from .coordinator import ExistIODataUpdateCoordinator
from .const import CONF_TOKEN, DOMAIN, PLATFORMS

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
    _LOGGER.info("Setting up ExistIO integration")
    token = entry.data[CONF_TOKEN]
    api = ExistIOAPI(token)
    hass.data[DOMAIN] = {"api": api}
    _LOGGER.info("ExistIOAPI object created")

    coordinator = ExistIODataUpdateCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN]["coordinator"] = coordinator
    _LOGGER.info("ExistIODataUpdateCoordinator object created and data fetched")

    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )
    _LOGGER.info("ExistIO sensor platform setup")

    return True

async def async_unload_entry(hass, entry):
    unload_ok = all(
        await asyncio.gather(
            *[hass.config_entries.async_forward_entry_unload(entry, platform)
              for platform in PLATFORMS]
        )
    )
    if unload_ok:
        hass.data.pop(DOMAIN)

    return unload_ok
