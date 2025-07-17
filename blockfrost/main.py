from blockfrost import BlockFrostApi, ApiError, ApiUrls

if __name__ == '__main__':
    try:
        api = BlockFrostApi(base_url=ApiUrls.localhost.value)

        health = api.health(return_type='json')
        print(health)

    except Exception as e:
        print(e)