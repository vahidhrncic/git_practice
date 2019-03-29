#SalsShipping
def cost_ground_shipping(weight):
  if weight < 2:
    return weight * 1.5 + 20
  elif weight <= 6 and weight > 2:
    return weight * 3 + 20
  elif weight > 6 and weight < 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20
  
  
def cost_drone_shipping(weight):
  if weight < 2:
    return weight * 4.5 
  elif weight <= 6 and weight > 2:
    return weight * 9 
  elif weight > 6 and weight < 10:
    return weight * 12 
  else:
    return weight * 14.25 
  
  
flate_charge = 125
  
def cheapest_shipping(weight):
  if cost_drone_shipping(weight) > cost_ground_shipping(weight) \
  	and cost_ground_shipping(weight) < flate_charge:
    return "Use Ground Shipping it costs: " + str(cost_ground_shipping(weight))
  
  elif cost_drone_shipping(weight) < cost_ground_shipping(weight) \
  	and cost_ground_shipping(weight) > flate_charge:
    return "Use Drone Shipping it costs: " + str(cost_drone_shipping(weight))
  else:
    return "Use Premium Shipping it costs: " + str(flate_charge)
    
 
  
print(cheapest_shipping(4.8))