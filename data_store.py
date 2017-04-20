from box import Box

REVIEW = {'id': 1, 'comment': 'Banana is a fruit, Apple also a fruit. Both are fruit naja'}

ATTRACTION = {
    'id': 1,
    'name': 'Sriracha Tiger Zoo',
    'rating': [1, 5, 2, 4, 0, 5],
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
    'reviews': [REVIEW, REVIEW, REVIEW],
}

DATA_STORE = Box({
    'attraction': [
        ATTRACTION,
        ATTRACTION
    ]
})

