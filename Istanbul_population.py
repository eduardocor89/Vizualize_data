"""
Let's say I work at the UN in urban planning and I'm intersted in tracking population growth across metropolitan regions.
I'm hoping that by looking at historical population numbers that I can predict future growth and 
help my team make decisions about resourcing. 
"""

# Let's start with some variables
city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_1950 = 983000
pop_2000 = 8831800
pop_2017 = 15029231

# Using these variables, I'm gonna write a script
# that calculates the annual percentage growth rate
# where the rate is the population change over
# that certain period of time. 

pop_change = pop_2017 - pop_1927

# I'll now calculate the percentage growth rage by 
# subtracting the past from the present population,
# dividing it by the past population and to get the percentage, I'll multiply by 100. 

percentage_gr = (pop_change/pop_1927) * 100

# Now let's get the annual percentage growth. 
# I'll do that by taking the result of the percentage_gr
# and dividing it by the number of years elapsed
annual_gr = percentage_gr/(90)

# Let's make this into a funciton so that I can reuse this calculation in the future. 

def population_growth(year_one, year_two,population_one,population_two):
  growth_rate = (((population_two - population_one)/population_one)*100)/(year_two - year_one)

  return growth_rate

# Let's see if my population_growth function worked.

print(annual_gr)
set_one = population_growth(1927,2017,pop_1927,pop_2017)
print(set_one)

# Let's see if we can zeron in on the growth from the 50s to 2000

set_two = population_growth(1950,2000,pop_1950,pop_2000)
print(set_two)
print()

# Now let's create a report into a variable called report. 

report = "The population change Instabul, Turkey from 1927 to 2017 went from " + str(pop_1927) + " to " + str(pop_2017) + " marking a " + str(round(set_one,2)) + "% annual growth rate between those years. That is, Istanbul grew it's size by almost a quarter EACH year!"

print(report)
