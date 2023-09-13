# 1) Display and read a prompt for building number
building_number = int(input("Enter a number of buildings: "))
# 2) Display and read a prompt for the number of electrical boxes
electrical_boxes = int(input("Enter a number of electrical boxes: "))
# 3) Calculate building revenue
building_revenue = building_number * 125
# 4) Calculate electrical box revenue
electrical_boxes_revenue = electrical_boxes * 51
# 5) Calculate total revenue
total_revenue = building_revenue + electrical_boxes_revenue
# 6) Display the total to the screen
print("If {} boxes were installed in {} buildings Ms. Power would generate ${:,.2f}.".format(electrical_boxes, building_number, total_revenue))