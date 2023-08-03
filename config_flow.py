import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import DOMAIN, CONF_TOKEN

class ExistIoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Exist.io."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Exist.io", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(CONF_TOKEN): str}),
            errors=errors,
        )

    async def async_setup_entry(self, entry):
        """Set up an Exist.io entry."""
        coordinator = get_coordinator(self.hass, entry)
        self.hass.data[DOMAIN] = coordinator
        return await coordinator.async_refresh()

def get_coordinator(hass, entry):
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="Exist.io sensor",
        update_interval=timedelta(hours=1),
    )
    coordinator.update = lambda: update_data(hass, coordinator, entry)
    return coordinator

async def update_data(hass, coordinator, entry):
    exist_io = ExistIO(hass, entry.data[CONF_TOKEN])
    data = await exist_io.async_update()
    return data
