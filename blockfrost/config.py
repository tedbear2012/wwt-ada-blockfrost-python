from enum import Enum
try:
    from importlib.metadata import version
except ImportError: # for Python<3.8
    from importlib_metadata import version

class ApiUrls(Enum):
    localhost = 'http://localhost:3000'
    mainnet = 'https://cardano-mainnet.blockfrost.io/api'
    preprod = 'https://cardano-preprod.blockfrost.io/api'
    preview = 'https://cardano-preview.blockfrost.io/api'
    testnet = 'https://cardano-testnet.blockfrost.io/api'
    ipfs = 'https://ipfs.blockfrost.io/api'


DEFAULT_API_VERSION = ''
DEFAULT_ORDER = 'asc'
DEFAULT_PAGINATION_PAGE_COUNT = 1
DEFAULT_PAGINATION_PAGE_ITEMS_COUNT = 100

ADDRESS_GAP_LIMIT = 20

package_name = 'blockfrost-python'
version = version(package_name)
USER_AGENT = f'{package_name} {version}'
