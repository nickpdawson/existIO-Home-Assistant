from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import ExistIOAPI
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

class ExistIODataUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, api: ExistIOAPI):
        self.api = api
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    async def _async_update_data(self):
        try:
            data = await self.api.async_get_data()
            _LOGGER.info(f"Fetched data: {data}")
            return data
        except Exception as exception:
            _LOGGER.error(f"Error occurred while fetching data: {exception}")
            raise UpdateFailed from exception
