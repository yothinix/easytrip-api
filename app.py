from apistar import App, Route
from box import Box

ATTRACTION = {
    'id': 1,
    'name': 'Sriracha Tiger Zoo',
    'rating': [0, 1, 2, 3, 4, 5],
    'address': '341 ตำบล หนองขาม Amphoe Si Racha. Chang Wat Chon Buri 20110',
    'details': """
        The Sriracha Tiger Zoo is a zoo in Sri Racha, a city on the outskirts of Pattaya, a seaside city in Chonburi Province. Thailand.
        It is about 97 km (60 mi) from Bangkok. The zoo claims a population of 200 tigers and around 10,000... crocodiles. the largest
        such populations in the world.[citation needed] Admission in 2009 (2552) was THB350 for foreigners and THB120 for Thais.
        """,
    'opening hours': '8AM - 6PM',
    'phone': '038 296 556',
    'photos': [
        'link1',
        'link2',
        'link3'
    ],
    'reviews': [
        {
            'id': 1,
            'comment': 'Banana is a fruit, Apple also a fruit. Both are fruit naja'
        }
    ]
}

DATA_STORE = Box({
    'attraction': [
        ATTRACTION,
        ATTRACTION
    ]
})

def welcome():
    return {'message': 'Welcome to EasyTrip APIs!'}

def attraction_list():
    return DATA_STORE.attraction

def attraction_instance(instance_id: int = 1):
    attraction = DATA_STORE.attraction[instance_id]
    return attraction

app = App(routes=[
    Route('/', 'GET', welcome),
    Route('/attraction/', 'GET', attraction_list),
    Route('/attraction/{instance_id}/', 'GET', attraction_instance)
])
