# World Temperature  

The purpose of this project is to revisit the OpenWeatherMap API to try and calculate average temperatures by date.


### Goals  
1. Create a random list of locations around the world by randomly generating a list of latitude and longitudes
2. Use the Citipy library to find the name of the nearest city to each lat/lon pair
3. Use the OpenWeatherMap API to find the temperature at each location at a certain date
4. Calculate the average global temperature for that date

### Limitations  
If we want to calculate an average global temperature, we'll need a lot of data points. This will mean lots of API calls - and the OpenWeatherMap API free tier has a limit of 60 calls per minute or 1,000 per day.

- We could count calls on the website and reroute to a 'closed' message when the daily rate limit is hit; or,

- We could pull all historical data once and load it into a database. This would give a higher limit on web requests.
