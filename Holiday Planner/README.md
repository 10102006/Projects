# Holiday Planner

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

  cg = dh.STATE(
      "Chhattisgarh",
      "A relative backwards state of India has a great potential for providing human resource.",
  )

  tps = []
  for i in range(3):
      tp = dh.TOURISTPLACE(f"Tourist Place-{i}", "lorem ipsum dore")
      [tp.MakeHotels(f"{f + 1} Hotel", (f + 1)*2, (f + 1) * 320) for (f) in range(3)]

      tps.append(tp)

  [cg.AddTouristPlace(touristPlace) for touristPlace in tps]

  print(json.dumps(cg.GetState(), indent=2))

```

---

## OSHandler

Currently only able to make folders for each state in the databse and adding the tourist place as a json file.

* Dump
  * `Activate`
  * `InitialiseStates`
  * `InitialiseTouristPlaces`

``` python

  dump = DUMP(database)
  dump.Activate()

```
