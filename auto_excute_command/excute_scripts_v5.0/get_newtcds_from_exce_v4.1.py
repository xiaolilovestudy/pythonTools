# coding=utf-8
import csv
import os
import sys
import time
from datetime import datetime
import pandas as pd

dirs = os.getcwd()
all_ids=[]; have_ids=[];total_tcds_list =[];cmdlist_tcds =[]
log_file=""
host1 ="H0701"; host2 = "H0802"; #host = "all"
schedule_testcase_format = """0 ID, 1 Title,2 Category, 3 Priority,4 A:1DPC,5  Schedule,6 testresult,7 sighting,8 owner,9 Duration,10 date,11 config,12 comment"""
schedule_file = r"latest_27.4_CXSH-CS2-SKU1-5600-64GB-MPS-MT-Rev-A(2Rx4).xlsx"
sheet_name = r"Functional (1DPC)"
command_excel = r"CXDIMM-CMDline 2.xlsx"
sheet_command = r"CXDIMM-CMDline 2"
new_command_excel = rf"testcase_running_command.xlsx"
not_find_excel = rf"Not_find_ids_in_schedule_file.xlsx"
TESTER = "Li, DongwangX"


def write_log(message):
    '''定义log函数， 将执行过程中的步骤记录的log文档中，方便后续查看'''
    datet = datetime.now().strftime('%Y-%m-%d')
    global log_file
    log_file = "get_new_cmd_{0}.log".format(datet)
    ctime = time.strftime("%Y-%m-%d %X", time.localtime())
    with open(log_file, 'a', encoding='utf-8') as file:
        file.write("{0}   {1}\n".format(ctime, message))


def all_tcds():
    # ID,Title,Category,Test Schedule,Test owner
    # tcds_list =[]
    data_form = pd.read_excel((schedule_file), sheet_name=sheet_name)
    global total_tcds_list
    for num in range(len(list(data_form.index.values))):
        total_tcds_list.append(list(data_form.loc[num].values))
    write_log(f"Total {len(total_tcds_list)} tcds from schedule excel\n")


def cxsh_command():
    # comlist_tcds =[]
    global comlist_tcds
    command_form = pd.read_excel((command_excel), sheet_name=sheet_command)
    for num in range(len(list(command_form.index.values))):
        cmdlist_tcds.append(list(command_form.loc[num].values))
    write_log(f"Total {len(cmdlist_tcds)} tcds from have command excel\n")


def get_new_excel(schedule=total_tcds_list, cxsh_com=cmdlist_tcds):
    # fileds = ['host', 'weekend', 'owner', 'category', 'priority', 'id', 'title', 'cmd']
    excel_head = pd.DataFrame({'host': [], 'weekend': [], 'owner': [], 'category': [],
         'priority': [], 'id': [], 'title': [],
         'cmd': []})
    excel_head.to_excel(new_command_excel,header=True, index=True)
    null_testcase = pd.DataFrame({'host': ['all'], 'weekend': ['WW52'], 'owner': ['all'], 'category': ['test'],
         'priority': ['P1'], 'id': ['118119120'], 'title': ['TEST_REQUIREMENTS_IS_PASS'],
         'cmd': ['python harness_main.py --loops=1 --test NULL_TEST']})
    null_testcase.to_excel(new_command_excel,index=False)
    num = 0; tcds_num =1
    for numi in range(len(schedule)):
        for numy in range(len(cxsh_com)):
            if schedule[numi][0] ==cxsh_com[numy][0]:# and schedule[numi][8] == TESTER :
                # print(schedule[numi][8])
                host = "all"
                if schedule[numi][8] == TESTER:
                    if num %2 ==0:
                        host = host1
                    else:
                        host = host2
                    num += 1
                df = pd.DataFrame({'host':[host],'weekend':[schedule[numi][5]],'owner':[schedule[numi][8]],'category':[schedule[numi][2]],'priority':[schedule[numi][3]],'id':[schedule[numi][0]],'title':[schedule[numi][1]],'cmd':[cxsh_com[numy][2]]})
                with pd.ExcelWriter(new_command_excel, engine="openpyxl", mode="a",if_sheet_exists="overlay") as writer:
                    df.to_excel(writer,sheet_name="Sheet1",startrow=writer.sheets['Sheet1'].max_row, header=False, index=False)
                write_log(f"Add {tcds_num} tcds in need run command successfully. info: {schedule[numi]} \n")
                tcds_num +=1
    write_log(f"Total add {tcds_num -1} tcds")
                # data_columns = {"Host":[host],"Weekend":[all_tcds()[numi][5]],"Owner":[all_tcds()[numi][8]],"Category":[all_tcds()[numi][2]],"Priority":[all_tcds()[numi][3]],"ID":[all_tcds()[numi][1]],"Title":[all_tcds()[numi][2]],"CMD":[cxsh_command[numy][2]] }
                # data_frame = pd.DataFrame(data_columns)
                # data_frame.to_excel(r"testcase_command.xlsx",index=False)


def compare_tcds(schedule=total_tcds_list, cxsh_command=cmdlist_tcds):
    write_log(" begin compare ids")
    num = 1; schedule_ids =[]; cmdlist_ids =[]
    excel_head = pd.DataFrame({'num':[],'host': [], 'weekend': [], 'owner': [], 'category': [],
                               'priority': [], 'id': [], 'title': [],
                               'cmd': []})
    excel_head.to_excel(not_find_excel, header=True, index=False)
    for numi in range(len(schedule)):
        schedule_ids.append(schedule[numi][0])
    for numy in range(len(cxsh_command)):
        cmdlist_ids.append(cxsh_command[numy][0])
    for i in range(len(schedule_ids)):
        if schedule_ids[i] not in cmdlist_ids:
            for j in range(len(schedule)):
                if schedule_ids[i] == schedule[j][0]:
                    df = pd.DataFrame({'num': num ,'host': "Not Find", 'weekend': [schedule[j][5]], 'owner': [schedule[j][8]],
                                   'category': [schedule[j][2]], 'priority': [schedule[j][3]],
                                   'id': [schedule[j][0]], 'title': [schedule[j][1]], 'cmd': "cmd not find"})
                    with pd.ExcelWriter(not_find_excel, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                        df.to_excel(writer, sheet_name="Sheet1", startrow=writer.sheets['Sheet1'].max_row, header=False,
                            index=False)
                    write_log(f"Add {num} tcds not find. info: {schedule[j]} \n")
                    num +=1
    write_log("end compare ids")


if __name__ == '__main__':
    all_tcds()  # get all schedule tcd
    cxsh_command() # get have command tcd
    get_new_excel()
    compare_tcds()


