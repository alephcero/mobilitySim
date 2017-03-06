# mobilitySim
Simulation for transport demand 

* [Documentation](https://simpy.readthedocs.io/en/latest/)

## First simulation

* From point A to Point B
* One shuttle with fixed schedule (every 15 minutes get from A to B, and 15 from B to A. In station A every 30 minutes)
* Users are generated only in Point A every 2 minutes fixed
* Users request a ticket in point A based only in a fixed time (30 minutes) not when the shuttles arrives (when ever that is)


## Second simulation

* From point A to Point B
* One shuttle with fixed schedule (every 15 minutes get from A to B, and 15 from B to A. In station A every 30 minutes)
* Users are generated *with a random poisson distribution with a lamnda as given parameter* 
* Users request a ticket in point A based only in a fixed time (30 minutes) not when the shuttles arrives (when ever that is)

## Third simulation

* From point A to Point B
* One shuttle with fixed schedule (every 15 minutes get from A to B, and 15 from B to A. In station A every 30 minutes)
* Users are generated *with a random poisson distribution with a lamnda as given parameter* 
* Working on syncronize the request for a ticket with the arrival of the shuttle to point A based on the actual arrival of the shuttle and not based on the clock.
