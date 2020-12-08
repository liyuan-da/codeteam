import matplotlib.pyplot as py

xlabel = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
ylabel = [80, 60, 70, 30, 30, 40, 30]
y2label = [60, 50, 30, 10, 20, 10, 40]
y3label = [20, 10, 0, 10, 10, 20, 30]
py.ylim((0, 100))
py.xlabel('Day')
py.ylabel('Probability(%)')
py.title('Probability of Raining')
py.plot(xlabel, ylabel, color = 'skyblue', label = 'Taipei')
py.plot(xlabel, y2label, color = 'orange', label = "Taichung")
py.plot(xlabel, y3label, color = 'g', label = "Tainan")
py.legend() 
py.show()