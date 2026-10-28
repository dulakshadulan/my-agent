from abc import ABC, abstractmethod

class ProviderClass(ABC):
    @abstractmethod
    async def model_call(
        self,
        message : dict):
        pass
