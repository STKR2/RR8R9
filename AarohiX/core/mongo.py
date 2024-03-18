from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info(" يتم تشغيل البيانات ...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Adisa
    LOGGER(__name__).info(" تم تشغيل البيانات .")
except:
    LOGGER(__name__).error("خطا .")
    exit()
