''' The goal for your program is to safely land the "Mars Lander" shuttle, the
landing ship which contains the Opportunity rover. Mars Lander is guided by a
program, and right now the failure rate for landing on the NASA simulator is
unacceptable.
Note that it may look like a difficult problem, but in reality the problem is
easy to solve. This puzzle is the first level among three, therefore, we need
to present you some controls you won't need in order to complete this first
level. '''
surface_n = int(input())

for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if y < 1250:
        print("0 4")
    else:
        print("0 3")
