from aiohttp import ClientSession
from .errors import *
from .models import *


class IntrecoAPI():
    def __init__(self, api_token: str):
        self._api_token: str = api_token
        self._session: ClientSession = None
        self._base: str = "http://100.99.62.154:8080/"

    async def _request(self, method: str, url, headers: dict | None, data: dict | None):
        self._session = ClientSession()
        async with self._session.request(method=method, url=self._base + url, headers=headers, data=data) as r:
            resp = await r.json()

            if r.status != 200:
                if r.status == 403:
                    raise NotAuthorized(resp["detail"])

            return resp

    async def get_user(self) -> User:
        headers = {
            "Authorization": self._api_token
        }

        req = await self._request(method="GET", url=f"/user/", headers=headers, data=None)
        data = req[0]
        return User(data["id"], data["first_name"], data["last_name"], data["email"], data["staff"], data["created_at"])
    
    async def get_devices(self):

        headers = {
            "Authorization": self._api_token
        }

        data = await self._request(method="GET", url=f"/device", headers=headers, data=None)
        print(data)
        devices = []
        for device in data:
            if device["type"] == "temp_hum_sensor":
                devices.append(TempHumSensor(serial_number=device["serial_number"], created_at=device["created_at"], last_updated=device["last_updated"], state=device["state"], activated_at=device["activated_at"], name=device["name"]))

            # Return other device types when added

        return devices
    
    async def get_device(self, serial_number):

        headers = {
            "Authorization": self._api_token
        }

        data = await self._request(method="GET", url=f"/device/{serial_number}", headers=headers, data=None)

        if data["type"] == "temp_hum_sensor":
            return TempHumSensor(serial_number=data["serial_number"], created_at=data["created_at"], last_updated=data["last_updated"], state=data["state"], activated_at=data["activated_at"], name=data["name"])

            # Return other device types when added