import app
import queue
import random


team_2_players = {}

playing = {}

Q1 = queue.Queue()
Q2 = queue.Queue()
Q3 = queue.Queue()
Q4 = queue.Queue()
Q5 = queue.Queue()
Q6 = queue.Queue()

def court1_q():
    dict_info = app.receive_form_data1
    Q1.put(dict_info)
    return

def court1_dq():
    cur_dict = Q1.get()
    playing[cur_dict] = random.randint(1,50) * 30275
    return

def court2_q():
    dict_info = app.receive_form_data2
    Q2.put(dict_info[0])
    return

def court2_dq():
    cur_dict = Q2.get()
    playing[cur_dict] = random.randint(1,50) * 30275
    return

def court3_q():
    dict_info = app.receive_form_data3
    Q3.put(dict_info[0])
    return

def court3_dq():
    cur_dict = Q3.get()
    playing[cur_dict] = random.randint(1,50) * 30275
    return

def court4_q():
    dict_info = app.receive_form_data4
    Q4.put(dict_info[0])
    return

def court4_dq():
    cur_dict = Q4.get()
    playing[cur_dict] = random.randint(1,50) * 30275
    return

def court5_q():
    dict_info = app.receive_form_data5
    Q5.put(dict_info[0])
    return

def court5_dq():
    cur_dict = Q5.get()
    playing[cur_dict] = random.randint(1,50) * 30275
    return

def court6_q():
    dict_info = app.receive_form_data6
    Q6.put(dict_info[0])
    return

def court6_dq():
    cur_dict = Q6.get()
    playing[cur_dict] = random.randint(1,50) * 30275
    return