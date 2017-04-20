from apistar import App, Route

from data_store import DATA_STORE


def welcome():
    return {'message': 'Welcome to EasyTrip APIs!'}

def attraction_list():
    return DATA_STORE['attraction']

def attraction_instance(instance_id: int = 1):
    attraction = DATA_STORE['attraction'][instance_id]
    return attraction

app = App(routes=[
    Route('/', 'GET', welcome),
    Route('/attraction/', 'GET', attraction_list),
    Route('/attraction/{instance_id}/', 'GET', attraction_instance)
])
