from random import sample, randint, shuffle
from fractions import Fraction

question_template = "Six shipments of machine parts were shipped from a factory on two trucks, with each shipment entirely on one of the trucks. Each shipment was labeled either S1, S2, S3, S4, S5, or S6. The table shows the value of each shipment as a fraction of the total value of the six shipments. If the shipments on the first truck had a value greater than of the total value of the six shipments, was S3 shipped on the first truck?"
table = {"Shipments":["S1","S2","S3","S4","S5","S6"], "Fraction of the Total Value of the Six Shipments": [Fraction(1,4), Fraction(1,5), Fraction(1,6),Fraction(3,20),Fraction(2,15),Fraction(1,10)]}
statement1 = "S2 and S4 were shipped on the first truck."
statement2 = "S1 and S6 were shipped on the second truck"



forced_shipments = sample([0,1,2,3,4,5], k=2)
total = randint(30,100)



