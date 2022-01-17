import os
import re
import logging
import pandas as pd

logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.info('start of the program')


def getInventory(current_path, current_folder, visited, file_list):
    current_path = current_path + '\\' + current_folder
    visited[current_path] = True
    logging.debug("current path is " + current_path)
    folders = []
    current_path_files = os.listdir(current_path)
    for file_or_folder in current_path_files:
        if os.path.isdir(current_path + '\\' + file_or_folder):
            folders.append(file_or_folder)
        else:
            file_list.append((current_path, file_or_folder))

    logging.debug("file list is")
    for filepath, filename in file_list:
        logging.debug(filepath + " " + filename)
    logging.debug("***************************")
    for child_folder in folders:
        if visited.get(current_path + '\\' + child_folder) is None:
            logging.debug("go down to " + child_folder)
            getInventory(current_path, child_folder, visited, file_list)


# read log contents from given file_path
# return log file as a big string
# completed
def get_log_content(file_path):
    file_object = open(file_path)
    file_content = file_object.read()
    file_object.close()
    return file_content


# get all the user name of the given log file
# return a list of usernames
# comment: need to implement multi-user cases (1/14)
def get_user_name(log_content):
    user_name_regex = re.compile(r".* INFO .*] :(.*) - ")
    user_name_obj = user_name_regex.search(log_content[:1000])
    user_name = user_name_obj.group(1).split('@')
    return [user_name[0]]


# provide a user's log file content given username and log_content
# comment: need to implement split the log content based on the given user name (1/14)
def get_user_log_content(user, log_content):
    return log_content


# input data: user's log content
# split the user's log content based on SAS file
# make a list of pair of SAS file name and the SAS file's log content
# comment: need to implement SAS file line number part here (1/14)
def get_sas_files(user_log_content):
    sas_file_regex = re.compile(r"_SASPROGRAMFILE='(.*)';")
    sas_file_list = sas_file_regex.findall(user_log_content)
    sas_file_list.insert(0, '')

    sas_content_list = user_log_content.split("%LET _SASPROGRAMFILE='")
    sas_content_numbered_list = sas_line_number_counter(sas_content_list)

    zipped_sas_file_content_list = tuple(zip(sas_file_list, sas_content_numbered_list))

    return zipped_sas_file_content_list


def sas_line_number_counter(sas_content_list):
    temp_chunk = ""
    sas_content_numbered_list = []
    for line_num, line in enumerate(sas_content_list[0].splitlines(True)):
        temp_chunk += str(line_num + 1) + "  " + line

    sas_content_numbered_list.append(temp_chunk)

    with open("output\\chunk1.txt", 'w') as text_file:
         text_file.write(temp_chunk)
    test_counter = 2

    temp_chunk = ""
    for sas_content in sas_content_list[1:]:
        line_number_regex = re.compile(r"\n\d\d\d\d-\d\d-.* - (\d+) ")
        line_number_regex_obj = line_number_regex.search(sas_content)
        start_line_number = int(line_number_regex_obj.group(1))

        for line in sas_content.splitlines(True):
            temp_chunk += str(start_line_number - 1) + "  " + line
            start_line_number += 1
        sas_content_numbered_list.append(temp_chunk)

        with open('output\\chunk' + str(test_counter) + '.txt', 'w') as text_file:
            text_file.write(temp_chunk)
        test_counter += 1

        temp_chunk = ""

    return sas_content_numbered_list


def get_sas_file_line_number(record_content):
    sas_file_line_regex = re.compile(r"(.*)  \d\d\d\d-\d\d-\d\d.*\(Total process time\):")
    sas_file_line_obj = sas_file_line_regex.search(record_content)
    if sas_file_line_obj is None:
        return ""
    else:
        return sas_file_line_obj.group(1)


# get input file such as *.csv
# if there is not an input file, then return ""
# completed
def get_input_file_name(sas_file_content):
    input_file_name_regex = re.compile(r"NOTE: The infile '(.*)' is")
    sas_file_list = input_file_name_regex.search(sas_file_content)
    if sas_file_list is not None:
        input_file_name = sas_file_list.group(1)
    else:
        input_file_name = ''

    return input_file_name


# get SAS Step names such as DATA statement, Procedure SQL, SAS Initialization
# return SAS STEP (such as DATA statement) and SAS Step name (ex)sql, Data
# Completed but need to check if there is any other case regarding SAS Step (1/14)
def get_sas_step_name(sas_file_content):
    sas_step_name_regex = re.compile(r"NOTE: (.*) (.*) used")
    sas_step_name_regex_obj = sas_step_name_regex.search(sas_file_content)

    if sas_step_name_regex_obj is None:
        sas_step = ''
        sas_step_name = ''
    elif sas_step_name_regex_obj.group(1) == 'DATA':
        sas_step = sas_step_name_regex_obj.group(1) + ' ' + sas_step_name_regex_obj.group(2)
        sas_step_name = sas_step_name_regex_obj.group(1)
    elif sas_step_name_regex_obj.group(1) == 'PROCEDURE':
        sas_step = 'PROCEDURE Statement'
        sas_step_name = sas_step_name_regex_obj.group(2)
    elif sas_step_name_regex_obj.group(1) == 'SAS':
        sas_step = 'SAS Initialization'
        sas_step_name = ''
    elif sas_step_name_regex_obj.group(1) == 'The SAS':
        sas_step = 'SAS System'
        sas_step_name = ''
    else:
        sas_step = ''
        sas_step_name = ''
    return sas_step, sas_step_name


# get time infomation
# return execution date and execution time
# completed
def get_time_info(sas_file_content):
    time_info_regex = re.compile(r"(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d).*real time")
    time_info_regex_obj = time_info_regex.search(sas_file_content)

    if time_info_regex_obj is None:
        print("time info cannot get regex object")
        exc_date = "error"
        exc_time = "error"
    else:
        exc_date = time_info_regex_obj.group(1)
        exc_time = time_info_regex_obj.group(2)

    return exc_date, exc_time


# get process time for cpu time and real time
# return cpu time and real time as second
# comment: need to update the SAS System time part (1/14)
def get_process_time(sas_file_content):
    cpu_time_regex = re.compile(r"cpu time \s+(\d+.\d+) ")
    cpu_time_regex_obj = cpu_time_regex.search(sas_file_content)
    cpu_time = cpu_time_regex_obj.group(1)

    real_time_regex = re.compile(r"real time \s+(\d+.\d+) ")
    real_time_regex_obj = real_time_regex.search(sas_file_content)
    if real_time_regex_obj is None:
        real_time_regex_ver2 = re.compile(r"real time \s+(\d+:\d+).")
        real_time_regex_obj = real_time_regex_ver2.search(sas_file_content)
    real_time = real_time_regex_obj.group(1)

    return cpu_time, real_time


# get output library and output table from regular log message such as NOTE: ~~
# return output library and output table
# completed for the regular log message
# comment: need to enhance to get information from actual sql query
def get_output_library_table(sas_file_content):
    output_lib_table_regex = re.compile(r"NOTE: The data set (.*)\.(.*) has (\d+) observations and (\d+) "
                                        r"variables.")
    output_lib_table_regex_obj = output_lib_table_regex.search(sas_file_content)
    if output_lib_table_regex_obj is not None:
        output_lib = output_lib_table_regex_obj.group(1)
        output_table = output_lib_table_regex_obj.group(2)
    else:
        output_lib = ''
        output_table = ''

    return output_lib, output_table


# get input library and input table from regular log output such as NOTE: ~
# return input_lib, input_table as string
# Need to enhance to process actual query based process.
def get_input_library_table(sas_file_content):
    input_lib_table_regex = re.compile(r"NOTE: There were (\d+) observations read from the data set (.*)\.(.*).")
    input_lib_table_regex_obj = input_lib_table_regex.search(sas_file_content)
    if input_lib_table_regex_obj is not None:
        input_lib = input_lib_table_regex_obj.group(2)
        input_table = input_lib_table_regex_obj.group(3)
        # print(input_lib)
        # print(input_table)
    else:
        input_lib = ''
        input_table = ''

    return input_lib, input_table


# get number of rows write and output library and output table.
# got the information from three regular log output
# return a list of [rows, libs, tbls] ex) [row1;row2, lib1;lib2, table1; table2]
def get_sas_row_write(record_content):
    rows = libs = tbls = ""

    sas_row_write_regex_case_one = re.compile(r"NOTE: (\d+) rows were updated in (.*)\.(.*).")
    sas_row_write_regex_case_one_list = sas_row_write_regex_case_one.findall(record_content)
    if len(sas_row_write_regex_case_one_list) != 0:
        sas_row_write_regex_case_one_list = sas_row_write_regex_case_one_list[-1]

    sas_row_write_regex_case_two = re.compile(r"NOTE: Table (.*)\.(.*) created, with (\d+) rows")
    sas_row_write_regex_case_two_list = sas_row_write_regex_case_two.findall(record_content)
    sas_row_write_regex_case_two_list = [(record[2], record[0], record[1]) for record in
                                         sas_row_write_regex_case_two_list]

    sas_row_write_regex_case_three = re.compile(r"NOTE: (\d+) rows were deleted from (.*)\.(.*).")
    sas_row_write_regex_case_three_list = sas_row_write_regex_case_three.findall(record_content)
    if len(sas_row_write_regex_case_three_list) != 0:
        sas_row_write_regex_case_three_list = sas_row_write_regex_case_three_list[-1]
        if sas_row_write_regex_case_three_list[0] == 'No':
            sas_row_write_regex_case_three_list[0] = '0'
        rows = str(sas_row_write_regex_case_three_list[0])
        libs = str(sas_row_write_regex_case_three_list[1])
        tbls = str(sas_row_write_regex_case_three_list[2])

    for record in sas_row_write_regex_case_two_list:
        rows = ';'.join([rows, str(record[0])])
        libs = ';'.join([libs, str(record[1])])
        tbls = ';'.join([tbls, str(record[2])])

    if len(sas_row_write_regex_case_one_list) != 0:
        rows = ';'.join([rows, str(sas_row_write_regex_case_one_list[0])])
        libs = ';'.join([libs, str(sas_row_write_regex_case_one_list[1])])
        tbls = ';'.join([tbls, str(sas_row_write_regex_case_one_list[2])])

    if rows == "":
        return []
    else:
        if rows[0] == ';':
            return [rows[1:], libs[1:], tbls[1:]]
        else:
            return [rows, libs, tbls]


# update a row of record to the given dataframe 'log_df'
def save_record_to_df(log_df, extracted_record):
    updated_log_df = log_df.append(pd.Series(extracted_record, index=log_df.columns), ignore_index=True)
    return updated_log_df


# save the dataframe to an excel file
def save_df_to_xlsx(log_df):
    # check "\output" folder and make it if it is not exist
    if not os.path.isdir('output'):
        os.makedirs('output')
    log_df.to_excel("output\\output.xlsx", index=False)


# main function
if __name__ == "__main__":

    FILE_ID = ""
    FILE_PTH = ""
    FILE_NM = ""
    FILE_USR_NM = ""
    FILE_SAS_F_ID = ""
    FILE_SAS_F_LOC = ""
    FILE_SAS_F_NM = ""
    FILE_SAS_STP = ""
    FILE_SAS_STP_NM = ""
    FILE_LN_NUM = ""
    FILE_SAS_INP_LIB = ""
    FILE_SAS_INP_TBL = ""
    FILE_SAS_INP_FIL_NM = ""
    FILE_SAS_INP_ROW_RD = ""
    FILE_SAS_OUT_LIB = ""
    FILE_SAS_OUT_TBL = ""
    FILE_SAS_ROW_WRT = ""
    FILE_SAS_INP_MUL_FLG = ""
    FILE_SAS_INP_MUL_TBLS = ""
    FILE_EXC_DT = ""
    FILE_SAS_EXC_TM = ""
    FILE_SAS_EXC_CPU_TM = ""
    FILE_SAS_EXC_RL_TM = ""

    log_df = pd.DataFrame(columns=['FILE_ID', 'FILE_PTH', 'FILE_NM', 'FILE_USR_NM', 'FILE_SAS_F_ID',
                                   'FILE_SAS_F_LOC', 'FILE_SAS_F_NM', 'FILE_SAS_STP',
                                   'FILE_SAS_STP_NM', 'FILE_LN_NUM', 'FILE_SAS_INP_LIB',
                                   'FILE_SAS_INP_TBL', 'FILE_SAS_INP_FIL_NM', 'FILE_SAS_INP_ROW_RD',
                                   'FILE_SAS_OUT_LIB', 'FILE_SAS_OUT_TBL', 'FILE_SAS_ROW_WRT',
                                   'FILE_SAS_INP_MUL_FLG', 'FILE_SAS_INP_MUL_TBLS', 'FILE_EXC_DT',
                                   'FILE_SAS_EXC_TM', 'FILE_SAS_EXC_CPU_TM', 'FILE_SAS_EXC_RL_TM'])

    current_path = os.getcwd()
    current_folder = 'logs_test'
    visited = dict()
    file_list = []

    getInventory(current_path, current_folder, visited, file_list)

    #    log_file_path_list = get_log_file_list()

    file_id_counter = 1
    sas_file_id_counter = 1
    sas_file_dict = dict()  # key: sas_file_abs_path, value: FILE_SAS_F_ID

    for file_path, file_name in file_list:
        file_full_path = file_path + '\\' + file_name
        log_content = get_log_content(file_full_path)

        FILE_PTH = file_full_path
        FILE_NM = file_name
        user_names = get_user_name(log_content)  # need to update later
        test_record_content_sum = 0

        for user in user_names:
            FILE_USR_NM = user
            user_log_content = get_user_log_content(user, log_content)
            sas_file_content_list = get_sas_files(user_log_content)
            for sas_file_abs_path, sas_file_content in sas_file_content_list:

                record_content_list = re.split(r"seconds\n.* -       \n", sas_file_content)
                # print("number of content : " + str(len(record_content_list)))
                test_record_content_sum += len(record_content_list)
                for record_content in record_content_list:
                    # drop if it is the end of the log content which does not have meaningful information
                    if record_content[-25:-17] != 'cpu time':
                        continue
                    # update sas file id and sas file name and path if it is updated.
                    if sas_file_abs_path != '':
                        if sas_file_dict.get(sas_file_abs_path) is None:
                            sas_file_dict[sas_file_abs_path] = 'SF_' + str(sas_file_id_counter)
                            sas_file_id_counter += 1
                        FILE_SAS_F_ID = sas_file_dict.get(sas_file_abs_path)
                        sas_file_norm_path = os.path.normpath(sas_file_abs_path)
                        FILE_SAS_F_NM = sas_file_norm_path.split(os.sep)[-1]

                    FILE_SAS_F_LOC = sas_file_abs_path
                    FILE_SAS_INP_FIL_NM = get_input_file_name(record_content)
                    FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL = get_output_library_table(record_content)
                    FILE_SAS_INP_LIB, FILE_SAS_INP_TBL = get_input_library_table(record_content)
                    # FILE_SAS_INP_ROW_RD  # Need to get some example to implement
                    if FILE_SAS_F_LOC == "":
                        FILE_LN_NUM = ""
                    else:
                        FILE_LN_NUM = get_sas_file_line_number(record_content)

                    FILE_SAS_STP, FILE_SAS_STP_NM = get_sas_step_name(record_content)
                    if FILE_SAS_STP == 'SAS Initialization' or FILE_SAS_STP == 'SAS System':
                        continue

                    FILE_EXC_DT, FILE_SAS_EXC_TM = get_time_info(record_content)
                    FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM = get_process_time(record_content)

                    sas_row_write_data = get_sas_row_write(record_content)

                    if len(sas_row_write_data) != 0:
                        FILE_SAS_ROW_WRT = sas_row_write_data[0]
                        if FILE_SAS_OUT_LIB == "":
                            FILE_SAS_OUT_LIB = sas_row_write_data[1]
                        else:
                            FILE_SAS_OUT_LIB = ';'.join([FILE_SAS_OUT_LIB, str(sas_row_write_data[1])])
                        if FILE_SAS_OUT_TBL == "":
                            FILE_SAS_OUT_TBL = sas_row_write_data[2]
                        else:
                            FILE_SAS_OUT_TBL = ';'.join([FILE_SAS_OUT_TBL, str(sas_row_write_data[2])])

                    # more data extractions needed to be here

                    FILE_ID = 'LOG_' + str(file_id_counter)
                    file_id_counter += 1
                    extracted_record = [FILE_ID, FILE_PTH, FILE_NM, FILE_USR_NM, FILE_SAS_F_ID, FILE_SAS_F_LOC,
                                        FILE_SAS_F_NM,
                                        FILE_SAS_STP, FILE_SAS_STP_NM, FILE_LN_NUM, FILE_SAS_INP_LIB, FILE_SAS_INP_TBL,
                                        FILE_SAS_INP_FIL_NM, FILE_SAS_INP_ROW_RD, FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL,
                                        FILE_SAS_ROW_WRT,
                                        FILE_SAS_INP_MUL_FLG, FILE_SAS_INP_MUL_TBLS, FILE_EXC_DT, FILE_SAS_EXC_TM,
                                        FILE_SAS_EXC_CPU_TM,
                                        FILE_SAS_EXC_RL_TM]

                    log_df = save_record_to_df(log_df, extracted_record)

                    # Data initialization
                    FILE_SAS_ROW_WRT = FILE_SAS_OUT_LIB = FILE_SAS_OUT_TBL = sas_row_write_data = ""

        save_df_to_xlsx(log_df)

logging.info('end of the program')
