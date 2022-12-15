from flask import Flask, render_template, request
from algorithms.bf import *
from algorithms.nn import *
from algorithms.dp import *
import math
import time

app = Flask(__name__)


@app.route('/')
def calc_distance():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def table():
    if request.form["btn"] == "Submit":
        number = int(request.form['text'])
        names = []
        first = ["city"]
        for i in range(1, number+1):
            first.append(str(i))
        names.append(first)

        i = 1
        for j in range(1, number+1):
            lst = [str(j)]
            for _ in range(1, number+1):
                lst.append(str(i))
                i = i+1
            names.append(lst)
        return render_template('index.html', number=number+1, names = names)
    
    if request.form["btn"] == "Calculate":
        dic = {}
        numberOfElements = int(request.form['elements'])
        numberOfCities = int(math.sqrt(numberOfElements))
        cities = [i for i in range(1, numberOfCities+1)]
        distances = []
        k = 1
        for i in range(numberOfCities):
            distanceRow = []
            for j in range(numberOfCities):
                distanceRow.append(int(request.form[str(k)]))
                k+=1
            distances.append(distanceRow)
        

        # cities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # distances = [[0, 225, 304, 236, 213, 339, 187, 197, 226],
        #              [225, 0, 140, 153, 15, 175, 84, 160, 110],
        #              [304, 140, 0, 152, 132, 41, 121, 190, 108],
        #              [236, 153, 152, 0, 143, 188, 70, 73, 63],
        #              [213, 15, 132, 143, 0, 166, 74, 145, 102],
        #              [339, 175, 41, 188, 166, 0, 157, 226, 144],
        #              [187, 84, 121, 70, 74, 157, 0, 81, 43],
        #              [197, 160, 190, 73, 145, 226, 81, 0, 90],
        #              [226, 110, 108, 63, 102, 144, 43, 90, 0]]
        
        

        details = []

        start = time.process_time()
        best_tour, best_distance = dp(cities, distances)
        end = time.process_time()

        details.append(best_tour)
        details.append(best_distance)
        details.append((end-start)*1000)

        dic['Dynamic Programming'] = details

        details = []

        start = time.process_time()
        best_tour, best_distance = bf(cities, distances)
        end = time.process_time()

        details.append(best_tour)
        details.append(best_distance)
        details.append((end-start)*1000)

        dic['Brute Force'] = details

        details = []

        start = time.process_time()
        best_tour, best_distance = nn(cities, distances)
        end = time.process_time()

        details.append(best_tour)
        details.append(best_distance)
        details.append((end-start)*1000)

        dic['Nearest Neighbor'] = details

        print(dic)

        return render_template('result.html', data=dic)



if __name__ == "__main__":
    app.run(debug=True)
