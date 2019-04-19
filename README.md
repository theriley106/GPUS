# GPUS

### Using public NHTSA data to reduce the probability of a vehicle accident in real time 


## Inspiration
There's a long stretch of road in Greenville, SC where accidents are extremely common.  It is particularly difficult to know which parts are worse than others if you're not familiar with the area. Knowing in real-time how dangerous the road in which you're driving on has been can allow the driver to adjust speed accordingly.

## What it does
Using your current Longitude/Latitude, we quantify the amount of car accidents that have happened within a specified distance to quantify how dangerous the road you're driving on is.

In the event of an accident the system will send a text message to specified contacts and emergency responders telling them your current location.

## How we built it
We are using Google's BigQuery in order to process the data surrounding the location of the Dragon board device. We are using a motion detector that is attached to the dragon board in order to detect accidents in the vehicle. 

## Challenges we ran into
We had lots of issues using the Dragonboard. There is lots of incompatibilies between the software as well as the motion detectors. The Dragonboard's capabilities are similar to that of a Raspberry Pi but are slightly different. Not enough people have experience with the system in order to provide a good community surrounding the device for troubleshooting issues like this.

## Accomplishments that we're proud of
We were able to get the motion sensor working and the GPS working on the Dragonboard.

## What we learned
We learned how the GPS works as well as the motion sensor that is separate from the device.