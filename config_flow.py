"""Config flow for Exist.io."""
import logging
from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow
import voluptuous as vol

from .const import DOMAIN


class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow to handle Exist.io OAuth2 authentication."""

    DOMAIN = DOMAIN
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    async def async_step_user(self, user_input=None):
        """Handle a flow start."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        fields = {
            vol.Required("token"): str,
        }

        return self.async_show_form(step_id="user", data_schema=vol.Schema(fields))
