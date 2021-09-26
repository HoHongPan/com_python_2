import logging
import json
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = "["
    for i in range(20):
        result = result + "{"
        c = request.get_json()[i].get("room")
        logging.info("data sent for evaluation {}".format(c))
        result = result + "\"room\":" + str(c) + ","
        a = request.get_json()[i].get("grid")
        logging.info("data sent for evaluation {}".format(a))
        rows_a = len(a)
        columns_a = len(a[0])
        b = request.get_json()[i].get("interestedIndividuals")
        logging.info("data sent for evaluation {}".format(b))
        rows_b = len(b)
        result = result + "\"p1\": { "
        for n in range(rows_b):
            result = result +"\""+ b[n] + "\": "
            if b[n][1] == ',':
                i = int(b[n][0])
                if len(b[n]) == 3:
                    j = int(b[n][2])
                else:
                    j = int(b[n][2])*10 + int(b[n][3])
            else:
                i = int(b[n][0])* 10 + int(b[n][1])
                if len(b[n]) == 4:
                    j = int(b[n][3])
                else:
                    j = int(b[n][3]) * 10 + int(b[n][4])
            if int(a[i][j]) != 1:
                result = result + "-1"
            else:
                list = [[i,j,0]]
                rows, cols = (rows_a, columns_a)
                looked = [[0 for c in range(cols)] for r in range(rows)]
                looked [i][j] = 1
                flag = 0
                while len(list) != 0:
                    if list[0][0] > 0:
                        if int(a[list[0][0]-1][list[0][1]]) == 1:
                            if looked[list[0][0]-1][list[0][1]] == 0:
                                looked[list[0][0] - 1][ list[0][1]] = 1
                                list.append([list[0][0]-1,list[0][1],list[0][2]+1])
                        elif int(a[list[0][0]-1][list[0][1]]) == 3:
                            result = result + str(list[0][2]+1)
                            flag = 1
                            break
                    if list[0][0] < rows_a-1:
                        if int(a[list[0][0] + 1][list[0][1]]) == 1:
                            if looked[list[0][0]+1][list[0][1]] == 0:
                                looked[list[0][0] + 1][list[0][1]] = 1
                                list.append([list[0][0] + 1, list[0][1], list[0][2] + 1])
                        elif int(a[list[0][0] + 1][list[0][1]]) == 3:
                            result = result + str(list[0][2] + 1)
                            flag = 1
                            break
                    if list[0][1] > 0:
                        if int(a[list[0][0]][list[0][1]-1]) == 1:
                            if looked[list[0][0]][list[0][1]-1] == 0:
                                looked[list[0][0]][ list[0][1]-1] = 1
                                list.append([list[0][0]-1,list[0][1],list[0][2]+1])
                        elif int(a[list[0][0]][list[0][1]-1]) == 3:
                            result = result + str(list[0][2]+1)
                            flag = 1
                            break
                    if list[0][1] < columns_a-1:
                        if int(a[list[0][0]][list[0][1] + 1]) == 1:
                            if looked[list[0][0]][list[0][1]+1] == 0:
                                looked[list[0][0]][ list[0][1]+1] = 1
                                list.append([list[0][0], list[0][1] + 1, list[0][2] + 1])
                        elif int(a[list[0][0] ][list[0][1]+ 1]) == 3:
                            result = result + str(list[0][2] + 1)
                            flag = 1
                            break
                    del list[0]
                logging.info("data sent for evaluation {}".format(i))
                logging.info("data sent for evaluation {}".format(j))
                logging.info("data sent for evaluation {}".format(looked))
                if flag == 0:
                    result = result + "-1"
            if n < rows_b-1:
                result = result + ", "
        else:
            result = result + "},"

        result = result + "\"p2\": -1,"
        result = result + "\"p3\": -1,"
        result = result + "\"p4\": -1,"
        result = result + "  }"
    else:
        result = result + "]"
        print (result)
        
    return result

