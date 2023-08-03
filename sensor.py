"""
Support for the Exist.io API.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/sensor.existio/
"""
from datetime import timedelta
import logging

from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=60)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Exist.io sensor."""
    api = hass.data[DOMAIN]["api"]
    coordinator = hass.data[DOMAIN]["coordinator"]

    sensors = []
    for attribute in coordinator.data:
        if attribute["active"]:
            sensors.append(ExistIOSensor(coordinator, api, attribute))

    async_add_entities(sensors, True)


class ExistIOSensor(CoordinatorEntity, Entity):
    """Representation of a Exist.io sensor."""

    def __init__(self, coordinator, api, attribute):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.api = api
        self._attr = attribute
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"existio_{self._attr['name']}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {"icon": "mdi:run"}

    async def async_update(self):
        """Fetch new state data for the sensor."""
        _LOGGER.debug("Starting async_update for sensor %s", self.name)
        await self.coordinator.async_request_refresh()
        data = self.coordinator.data
        _LOGGER.debug("Data fetched from coordinator for sensor %s: %s", self.name, data)

        for attribute in data:
            if attribute["name"] == self._attr["name"]:
                self._attr = attribute
                break

        _LOGGER.debug("Attribute data for sensor %s: %s", self.name, self._attr)

        if "values" in self._attr and len(self._attr["values"]) > 0:
            self._state = self._attr["values"][0]["value"]

        _LOGGER.debug("State set for sensor %s: %s", self.name, self._state)
        _LOGGER.debug("Finished async_update for sensor %s", self.name)
