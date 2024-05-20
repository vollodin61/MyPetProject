from datetime import datetime
from icecream import ic

ice = ic
ice.configureOutput(includeContext=True, prefix=datetime.now().strftime('%Y-%m-%d %H:%M:%S '))
