weight = float(input("Please enter weight: "));

groundShippingCost = 20.0;
premiumGroundShippingCost = 125;
droneShippingCost = 0.0;

if (weight <= 2):
    groundShippingCost += (weight * 1.5)
    droneShippingCost += (weight * 4.5)
elif (weight <= 6):
    groundShippingCost += (weight * 3)
    droneShippingCost += (weight * 9)
elif (weight <= 10):
    groundShippingCost += (weight * 4)
    droneShippingCost += (weight * 12)
else:
    groundShippingCost += (weight * 4.75)
    droneShippingCost += (weight * 14.25)

print(f"Ground shipping: {groundShippingCost}");
print(f"Premium Ground Shipping: {premiumGroundShippingCost}");
print(f"Drone Shipping: {droneShippingCost}");

if(groundShippingCost > premiumGroundShippingCost and droneShippingCost > premiumGroundShippingCost):
    print(f"Cheapest shipping is Premium Ground Shipping at {premiumGroundShippingCost}")
elif(groundShippingCost > droneShippingCost):
    print(f"Cheapest shipping is Drone Shipping at {droneShippingCost}")
else:
    print(f"Cheapest shipping is Ground Shipping at {groundShippingCost}")