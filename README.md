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
* Users request tickets for the shuttle in point A based on the arrival of the shuttle to point A
* We produce outputs for every user an averages

## simV4

* From point A to Point B
* One shuttle with the both go and return trip set as *random normal distributions with the mean as a parameter and std = 1*
* Users are generated *with a random poisson distribution with a lamnda as given parameter* 
* Users request tickets for the shuttle in point A based on the arrival of the shuttle to point A
* We produce outputs for every user an averages

