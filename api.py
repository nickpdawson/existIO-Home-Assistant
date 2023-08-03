import logging
import httpx

from .const import API_ENDPOINT

_LOGGER = logging.getLogger(__name__)

class ExistIOAPI:
    def __init__(self, token):
        _LOGGER.info("ExistIOAPI object created")
        self._token = token
        self.headers = {"Authorization": f"Token {self._token}"}
        _LOGGER.info(f"Authorization headers set: {self.headers}")

    async def async_get_data(self):
        _LOGGER.info("Sending request to ExistIO API")
        async with httpx.AsyncClient() as client:
            try:
                _LOGGER.info("Preparing API request")
                response = await client.get(API_ENDPOINT, headers=self.headers)
                _LOGGER.info("API request sent, awaiting response")
                response.raise_for_status()
                _LOGGER.info("API response received and status is OK")
                _LOGGER.info("API request successful, parsing response")
                data = response.json()
                _LOGGER.info(f"API response parsed, data: {data}")
                return data
            except httpx.HTTPStatusError as exception:
                _LOGGER.error(f"HTTP error occurred: {exception}")
                raise
            except Exception as exception:
                _LOGGER.error(f"An error occurred: {exception}")
                raise
