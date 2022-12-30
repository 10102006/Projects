# Holiday Planner

Holiday Planner is a CLI application for people wanting to travel as well, guides. It can work as a choosing system for the tourist, and a database maintainer for the guide.

Features:

* Guides
  * Can create a state fldr to store various tourist place.
  * alter the tourist place data.
  * delete a tourist place.
* Tourists
  1. present a list of state to choose from.
  2. seleting the state will present its details.
  3. then a list of tourist place with semi-details.
  4. selecting a tourist place will present its full details

``` shell

1. state1
2. state2
3. state3

> state1

state1
state1 details lorem ipsum dore.

1. tp1: lorem ipsum dore...
2. tp2: lorem ipsum dore...
3. tp3: lorem ipsum dore...

> tp2

tp2
lorem ipsum dore is a whore.

hotels:
  1. ht1: *****/ $20
  2. ht2: ***  / $3

transport:
  1. tp1
  2. tp2

> h1

```

TODO Complete This shit

## Data Handler

This python file handles how the State object is interpret in form of a class, which can be converted in simpler format `__dict__`, latter.

* STATE:
  * `AddTouristPlace()`
  * `GetState()`
* TOURISTPLACE
  * `MakeHotels()`
  * `AddTransport()`

``` python

  touristPlaces = [
    dh.TouristPlace(
      'yo' * i,
      'ha'*i*3,
      [
        ('a', 1, 12), ('b', 5, 12345)
      ],
      [
        ('as', 45), ('qw', 78)
      ]
    ) for i in range(3)
  ]

  cg = dh.State('CG', 'LOL', touristPlaces)
  print(cg.GetState())

```

---

## OS Handler

Currently only able to make folders for each state in the databse and adding the tourist place as a json file.

* Dump
  * `Activate`
  * `InitialiseStates`
  * `InitialiseTouristPlaces`

``` python

  database = {}
  dump = Dumper(database)
  dump.Activate()

```

``` python

    touristPlaces = [
    dh.TouristPlace(
        'yo' * i,
        'ha'*i*3,
        [
        ('a', 1, 12), ('b', 5, 12345)
        ],
        [
        ('as', 45), ('qw', 78)
        ]
    ) for i in range(1, 3)
    ]

    cg = dh.State('CG', 'LOL', touristPlaces)

    touristPlaces = [
    dh.TouristPlace(
        'lol' * i,
        'mwa'+'ha'*i*3,
        [
        ('a', 1, 12), ('b', 5, 12345)
        ],
        [
        ('as', 45), ('qw', 78)
        ]
    ) for i in range(1, 2)
    ]

    mh = dh.State('MH', 'HEH', touristPlaces)

    database = {cg, mh}
    dump = Dumper(database)
    dump.Activate()


```
