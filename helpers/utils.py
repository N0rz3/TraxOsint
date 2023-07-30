import httpx

class Requests:
    """
    Requests function with httpx

    Parameters of the requests in __init__(url, headers, params)
    Asynchrone function: sender() - for sending the requests

    An asynchrone HTTP client is created to send all requests with the provided headers and parameters.
    """
    def __init__(self, 
                url: str, 
                headers=None,
                params=None
                ):
        """
        Parameters:
            url (str)      : url used for send a requests
            headers (None) : headers used if desired 
            params (None)  : parameters used if desired 
        """
        self.url = url
        self.head = headers
        self.p = params

    async def sender(self):
        try:
            async with httpx.AsyncClient() as client:
                return await client.get(url=self.url, headers=self.head, params=self.p)

        except httpx.HTTPError as e:
            print("[-] HTTP error. ({})".format(e))