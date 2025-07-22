import logging
from datetime import datetime

class DBHandler(logging.Handler):
    def emit(self, record):
        try:
            from .models import Logs
            log = Logs(
                date = datetime.now().date(),
                time = datetime.now().time(),
                level = record.levelname,
                message = record.getMessage()
            )
            log.save()
        except Exception:
            pass # Siently ignore error