import os
import re
import logging
import pandas as pd

# logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start of the program')


# get log file from \logs folder. If there is not a log, it raises Exception
# return absolute path of the log file and filename pair of list
# comment: need to enhance to get all the log files regardless of folder structure (1/14)
def get_log_file_list():
    # check log folder exists
    if not os.path.isdir('logs'):
        os.makedirs('logs')
        logging.debug('"logs" folder is just created on current location.\nplease put log files in the directory')
        logging.debug('the location is ' + str(os.getcwd()) + "\\logs")
        raise Exception('please put log files in the "\\logs" folder')

    log_file_list = []
    for filename in os.listdir('logs_test'):
        if os.path.isfile(os.path.join('logs_test', filename)):
            log_file_list.append([os.path.abspath('logs_test'), filename])
    return log_file_list


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
    zipped_sas_file_content_list = tuple(zip(sas_file_list, sas_content_list))

    return zipped_sas_file_content_list



def get_input_file_name(sas_file_content):
    input_file_name_regex = re.compile(r"NOTE: The infile '(.*)' is")
    sas_file_list = input_file_name_regex.search(sas_file_content)
    if sas_file_list is not None:
        input_file_name = sas_file_list.group(1)
    else:
        input_file_name = ''

    return input_file_name


# need to implement cases such as DATA statement, Procedure SQL, SAS Initialization
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


def save_record_to_df(log_df, extracted_record):
    # print(log_df)

    updated_log_df = log_df.append(pd.Series(extracted_record, index=log_df.columns), ignore_index=True)

    # print(updated_log_df)

    return updated_log_df


def save_df_to_xlsx(log_df):
    # check "\output" folder and make it if it is not exist
    if not os.path.isdir('output'):
        os.makedirs('output')
    log_df.to_excel("output\\output.xlsx", index=False)


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

    extracted_record = [FILE_ID, FILE_PTH, FILE_NM, FILE_USR_NM, FILE_SAS_F_ID, FILE_SAS_F_LOC, FILE_SAS_F_NM,
                        FILE_SAS_STP, FILE_SAS_STP_NM, FILE_LN_NUM, FILE_SAS_INP_LIB, FILE_SAS_INP_TBL,
                        FILE_SAS_INP_FIL_NM, FILE_SAS_INP_ROW_RD, FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL, FILE_SAS_ROW_WRT,
                        FILE_SAS_INP_MUL_FLG, FILE_SAS_INP_MUL_TBLS, FILE_EXC_DT, FILE_SAS_EXC_TM, FILE_SAS_EXC_CPU_TM,
                        FILE_SAS_EXC_RL_TM]

    log_df = pd.DataFrame(columns=['FILE_ID', 'FILE_PTH', 'FILE_NM', 'FILE_USR_NM', 'FILE_SAS_F_ID',
                                   'FILE_SAS_F_LOC', 'FILE_SAS_F_NM', 'FILE_SAS_STP',
                                   'FILE_SAS_STP_NM', 'FILE_LN_NUM', 'FILE_SAS_INP_LIB',
                                   'FILE_SAS_INP_TBL', 'FILE_SAS_INP_FIL_NM', 'FILE_SAS_INP_ROW_RD',
                                   'FILE_SAS_OUT_LIB', 'FILE_SAS_OUT_TBL', 'FILE_SAS_ROW_WRT',
                                   'FILE_SAS_INP_MUL_FLG', 'FILE_SAS_INP_MUL_TBLS', 'FILE_EXC_DT',
                                   'FILE_SAS_EXC_TM', 'FILE_SAS_EXC_CPU_TM', 'FILE_SAS_EXC_RL_TM'])

    log_file_path_list = get_log_file_list()

    file_id_counter = 1
    sas_file_id_counter = 1
    sas_file_dict = dict()  # key: sas_file_abs_path, value: FILE_SAS_F_ID

    for file_path, file_name in log_file_path_list:
        file_full_path = file_path + '\\' + file_name
        log_content = get_log_content(file_full_path)

        FILE_PTH = file_full_path
        FILE_NM = file_name
        user_names = get_user_name(log_content)  # need to update later

        print(user_names)

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
                    if record_content[-25:-17] != 'cpu time':
                        continue
                    # print("*") * 50
                    # print("start of content :" + record_content[:50])
                    # print("end of content :" + record_content[-50:])
                    # print("*") * 50
                    #
                    # print(record_content[-25:-17])
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
                    # FILE_SAS_INP_ROW_RD

                    FILE_SAS_STP, FILE_SAS_STP_NM = get_sas_step_name(record_content)
                    FILE_EXC_DT, FILE_SAS_EXC_TM = get_time_info(record_content)
                    FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM = get_process_time(record_content)

                    sas_row_write_data = get_sas_row_write(record_content)

                    if len(sas_row_write_data) != 0:
                        # print(sas_row_write_data)
                        FILE_SAS_ROW_WRT = sas_row_write_data[0]
                        if FILE_SAS_OUT_LIB == "":
                            FILE_SAS_OUT_LIB = sas_row_write_data[1]
                        else:
                            FILE_SAS_OUT_LIB = ';'.join([FILE_SAS_OUT_LIB, str(sas_row_write_data[1])])
                        if FILE_SAS_OUT_TBL == "":
                            FILE_SAS_OUT_TBL = sas_row_write_data[2]
                        else:
                            FILE_SAS_OUT_TBL = ';'.join([FILE_SAS_OUT_TBL, str(sas_row_write_data[2])])

                    # more data extractions here

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

                    FILE_SAS_ROW_WRT = FILE_SAS_OUT_LIB = FILE_SAS_OUT_TBL = sas_row_write_data = ""

        save_df_to_xlsx(log_df)
        # print("total record :" + str(test_record_content_sum))
logging.debug('end of the program')
