from pytest import mark
from readlogs.D_CLDASST_Reader import get_user_name
from readlogs.D_CLDASST_Reader import get_input_file_name
from readlogs.D_CLDASST_Reader import get_output_library_table
from readlogs.D_CLDASST_Reader import get_input_library_table
from readlogs.D_CLDASST_Reader import get_sas_step_name
from readlogs.D_CLDASST_Reader import proc_sql_parsing
from readlogs.D_CLDASST_Reader import data_step_parsing
from readlogs.D_CLDASST_Reader import get_ext_db
from readlogs.D_CLDASST_Reader import get_time_info
from readlogs.D_CLDASST_Reader import get_process_time
from readlogs.D_CLDASST_Reader import get_migration_disp

from input_contents import input_case1
from input_contents import input_case2
from input_contents import input_case3
from input_contents import input_case4
from input_contents import input_case5
from input_contents import input_case6
from input_contents import input_case7
from input_contents import input_case8
from input_contents import input_case9
from input_contents import input_case10
from input_contents import input_case11
from input_contents import input_case12
from input_contents import input_case13
from input_contents import input_case14
from input_contents import input_case15
from input_contents import input_case16
from input_contents import input_case17
from input_contents import input_case18
from input_contents import input_case19
from input_contents import input_case20
from input_contents import input_case21
from input_contents import input_case22
from input_contents import input_case23
from input_contents import input_case24

@mark.case1
def test_get_user_name_1(input_case1):
    user_name = get_user_name(input_case1)
    assert user_name == "hxdhiraj"


@mark.case1
def test_get_input_file_name_1(input_case1):
    input_file = get_input_file_name(input_case1)
    assert input_file == "/sasdata/adhoc/Projects/Canada/flat_files/province_weekly_gap.csv"


@mark.case1
def test_get_output_library_table_1(input_case1):
    output_library, output_table = get_output_library_table(input_case1)
    assert output_library == "INSTAGE" and output_table == "PROVINCE_GAP_ANALYSIS"


@mark.case1
def test_get_input_library_table_1(input_case1):
    input_lib, input_table = get_input_library_table(input_case1)
    assert input_lib == "" and input_table == ""


@mark.case1
def test_get_sas_step_name_1(input_case1):
    step, step_name = get_sas_step_name(input_case1)
    assert step == "DATA statement" and step_name == "DATA"


@mark.case1
def test_proc_sql_parsing_1(input_case1):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case1)
    assert input_lib == [] and input_table == [] and output_lib == [] and output_table == [], str(input_lib) + str(
        input_table) + str(output_lib) + str(output_table)


@mark.case1
def test_data_step_parsing_1(input_case1):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case1)
    assert input_lib == [] and input_table == [] and output_lib == ['instage'] and output_table == [
        'province_gap_analysis'], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case1
def test_get_ext_db_1(input_case1):
    ext_db_list = get_ext_db(input_case1)
    assert ext_db_list == []


@mark.case1
def test_get_time_info_1(input_case1):
    exe_date, exe_time = get_time_info(input_case1)
    assert exe_date == '2021-05-15' and exe_time == '08:03:54'


@mark.case1
def test_get_process_time_1(input_case1):
    cpu_time, real_time = get_process_time(input_case1)
    assert real_time == 0.01 and cpu_time == 0.02


@mark.case1
def test_get_migration_disp_1(input_case1):
    rule_id, migration_disp = get_migration_disp(0.02, 0.01, 'DATA statement', 'DATA', input_case1)
    assert rule_id == '2' and migration_disp == "Code Change", migration_disp


@mark.case2
def test_get_user_name_2(input_case2):
    user_name = get_user_name(input_case2)
    assert user_name == "hxdhiraj"


@mark.case2
def test_get_input_file_name_2(input_case2):
    input_file = get_input_file_name(input_case2)
    assert input_file == "/sasdata/adhoc/Projects/Canada/flat_files/product_weekly_gap.csv"


@mark.case2
def test_get_output_library_table_2(input_case2):
    output_library, output_table = get_output_library_table(input_case2)
    assert output_library == "INSTAGE" and output_table == "PRODUCT_GAP_ANALYSIS"


@mark.case2
def test_get_input_library_table_2(input_case2):
    input_lib, input_table = get_input_library_table(input_case2)
    assert input_lib == "" and input_table == ""


@mark.case2
def test_get_sas_step_name_2(input_case2):
    step, step_name = get_sas_step_name(input_case2)
    assert step == "DATA statement" and step_name == "DATA"


@mark.case2
def test_proc_sql_parsing_2(input_case2):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case2)
    assert input_lib == [] and input_table == [] and output_lib == [] and output_table == [], str(input_lib) + str(
        input_table) + str(output_lib) + str(output_table)


@mark.case2
def test_data_step_parsing_2(input_case2):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case2)
    assert input_lib == [] and input_table == [] and output_lib == ['instage'] and output_table == [
        'product_gap_analysis'], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case2
def test_get_ext_db_2(input_case2):
    ext_db_list = get_ext_db(input_case2)
    assert ext_db_list == []


@mark.case2
def test_get_time_info_2(input_case2):
    exe_date, exe_time = get_time_info(input_case2)
    assert exe_date == '2021-05-15' and exe_time == '08:03:54'


@mark.case2
def test_get_process_time_2(input_case2):
    cpu_time, real_time = get_process_time(input_case2)
    assert real_time == 0.01 and cpu_time == 0.02


@mark.case2
def test_get_migration_disp_2(input_case2):
    rule_id, migration_disp = get_migration_disp(0.02, 0.01, 'DATA statement', 'DATA', input_case2)
    assert rule_id == '2' and migration_disp == "Code Change", migration_disp


@mark.case3
def test_get_user_name_3(input_case3):
    user_name = get_user_name(input_case3)
    assert user_name == "hxdhiraj"


@mark.case3
def test_get_input_file_name_3(input_case3):
    input_file = get_input_file_name(input_case3)
    assert input_file == "", input_file


@mark.case3
def test_get_output_library_table_3(input_case3):
    output_library, output_table = get_output_library_table(input_case3)
    assert output_library == "" and output_table == "", output_library + output_table


@mark.case3
def test_get_input_library_table_3(input_case3):
    input_lib, input_table = get_input_library_table(input_case3)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case3
def test_get_sas_step_name_3(input_case3):
    step, step_name = get_sas_step_name(input_case3)
    assert step == "PROCEDURE Statement" and step_name == "SQL", step + step_name


@mark.case3
def test_proc_sql_parsing_3(input_case3):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case3)
    assert input_lib == ['work'] and input_table == ['bev_type_fix_gap_local'] and output_lib == ['PostFcst'] and \
           output_table == ['bev_ty_fixed_invalid_records_cn'], str(input_lib) + str(
        input_table) + str(output_lib) + str(output_table)


@mark.case3
def test_data_step_parsing_3(input_case3):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case3)
    assert input_lib == [] and input_table == [] and output_lib == [] and output_table == [], \
        str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case3
def test_get_ext_db_3(input_case3):
    ext_db_list = get_ext_db(input_case3)
    assert ext_db_list == []


@mark.case3
def test_get_time_info_3(input_case3):
    exe_date, exe_time = get_time_info(input_case3)
    assert exe_date == '2021-05-15' and exe_time == '08:06:45'


@mark.case3
def test_get_process_time_3(input_case3):
    cpu_time, real_time = get_process_time(input_case3)
    assert real_time == 0 and cpu_time == 0, str(cpu_time) + " " + str(real_time)


@mark.case3
def test_get_migration_disp_3(input_case3):
    rule_id, migration_disp = get_migration_disp(0, 0, 'PROCEDURE Statement', 'SQL', input_case3)
    assert rule_id == '9' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case4
def test_get_user_name_4(input_case4):
    user_name = get_user_name(input_case4)
    assert user_name == "hxdhiraj"


@mark.case4
def test_get_input_file_name_4(input_case4):
    input_file = get_input_file_name(input_case4)
    assert input_file == "", input_file


@mark.case4
def test_get_output_library_table_4(input_case4):
    output_library, output_table = get_output_library_table(input_case4)
    assert output_library == "WORK" and output_table == "BEV_TYPE_MONTH_GAP_LOCAL", output_library + output_table


@mark.case4
def test_get_input_library_table_4(input_case4):
    input_lib, input_table = get_input_library_table(input_case4)
    assert input_lib == "WORK" and input_table == "BEV_TYPE_MONTH_GAP_LOCAL", input_lib + input_table


@mark.case4
def test_get_sas_step_name_4(input_case4):
    step, step_name = get_sas_step_name(input_case4)
    assert step == "DATA statement" and step_name == "DATA", step + step_name


@mark.case4
def test_proc_sql_parsing_4(input_case4):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case4)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case4
def test_data_step_parsing_4(input_case4):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case4)
    assert input_lib == ['work'] and input_table == ['bev_type_month_gap_local'] and output_lib == [
        'work'] and output_table == ['bev_type_month_gap_local'], \
        str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case4
def test_get_ext_db_4(input_case4):
    ext_db_list = get_ext_db(input_case4)
    assert ext_db_list == []


@mark.case4
def test_get_time_info_4(input_case4):
    exe_date, exe_time = get_time_info(input_case4)
    assert exe_date == '2021-05-15' and exe_time == '08:06:45'


@mark.case4
def test_get_process_time_4(input_case4):
    cpu_time, real_time = get_process_time(input_case4)
    assert real_time == 0 and cpu_time == 0, str(cpu_time) + " " + str(real_time)


@mark.case4
def test_get_migration_disp_4(input_case4):
    rule_id, migration_disp = get_migration_disp(0, 0, 'PROCEDURE Statement', 'SQL', input_case4)
    assert rule_id == '9' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case5
def test_get_user_name_5(input_case5):
    user_name = get_user_name(input_case5)
    assert user_name == "hxdhiraj"


@mark.case5
def test_get_input_file_name_5(input_case5):
    input_file = get_input_file_name(input_case5)
    assert input_file == "", input_file


@mark.case5
def test_get_output_library_table_5(input_case5):
    output_library, output_table = get_output_library_table(input_case5)
    assert output_library == "WORK;WORK" and output_table == "BEV_TYPE_WEEKLY_GAP_ALL;BEV_TYPE_WEEKLY_GAP_LOCAL", output_library + output_table


@mark.case5
def test_get_input_library_table_5(input_case5):
    input_lib, input_table = get_input_library_table(input_case5)
    assert input_lib == "INSTAGE" and input_table == "BEV_TYPE_WEEKLY_ANALYSIS_DATE_CN", input_lib + input_table


@mark.case5
def test_get_sas_step_name_5(input_case5):
    step, step_name = get_sas_step_name(input_case5)
    assert step == "DATA statement" and step_name == "DATA", step + step_name


@mark.case5
def test_proc_sql_parsing_5(input_case5):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case5)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case5
def test_data_step_parsing_5(input_case5):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case5)
    assert input_lib == ['instage'] and input_table == ['bev_type_weekly_analysis_date_cn'] and output_lib == ['work',
                                                                                                               'work'] \
           and output_table == ['bev_type_weekly_gap_all', 'bev_type_weekly_gap_local'], \
        str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case5
def test_get_ext_db_5(input_case5):
    ext_db_list = get_ext_db(input_case5)
    assert ext_db_list == []


@mark.case5
def test_get_time_info_5(input_case5):
    exe_date, exe_time = get_time_info(input_case5)
    assert exe_date == '2021-05-15' and exe_time == '08:06:45'


@mark.case5
def test_get_process_time_5(input_case5):
    cpu_time, real_time = get_process_time(input_case5)
    assert real_time == 0 and cpu_time == 0.01, str(cpu_time) + " " + str(real_time)


@mark.case5
def test_get_migration_disp_5(input_case5):
    rule_id, migration_disp = get_migration_disp(0.01, 0, 'DATA statement', 'DATA', input_case5)
    assert rule_id == '2' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case6
def test_get_user_name_6(input_case6):
    user_name = get_user_name(input_case6)
    assert user_name == "hxdhiraj"


@mark.case6
def test_get_input_file_name_6(input_case6):
    input_file = get_input_file_name(input_case6)
    assert input_file == "", input_file


@mark.case6
def test_get_output_library_table_6(input_case6):
    output_library, output_table = get_output_library_table(input_case6)
    assert output_library == "WORK" and output_table == "BEV_TYPE_WEEKLY_GAP_LOCAL", output_library + output_table


@mark.case6
def test_get_input_library_table_6(input_case6):
    input_lib, input_table = get_input_library_table(input_case6)
    assert input_lib == "WORK" and input_table == "BEV_TYPE_WEEKLY_GAP_LOCAL", input_lib + input_table


@mark.case6
def test_get_sas_step_name_6(input_case6):
    step, step_name = get_sas_step_name(input_case6)
    assert step == "DATA statement" and step_name == "DATA", step + step_name


@mark.case6
def test_proc_sql_parsing_6(input_case6):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case6)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case6
def test_data_step_parsing_6(input_case6):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case6)
    assert input_lib == ['work'] and input_table == ['bev_type_weekly_gap_local'] and output_lib == ['work'] \
           and output_table == ['bev_type_weekly_gap_local'], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case6
def test_get_ext_db_6(input_case6):
    ext_db_list = get_ext_db(input_case6)
    assert ext_db_list == []


@mark.case6
def test_get_time_info_6(input_case6):
    exe_date, exe_time = get_time_info(input_case6)
    assert exe_date == '2021-05-15' and exe_time == '08:06:45'


@mark.case6
def test_get_process_time_6(input_case6):
    cpu_time, real_time = get_process_time(input_case6)
    assert real_time == 0 and cpu_time == 0, str(cpu_time) + " " + str(real_time)


@mark.case6
def test_get_migration_disp_6(input_case6):
    rule_id, migration_disp = get_migration_disp(0, 0, 'DATA statement', 'DATA', input_case6)
    assert rule_id == '' and migration_disp == "Lift and Shift", rule_id + " " + migration_disp


@mark.case7
def test_get_user_name_7(input_case7):
    user_name = get_user_name(input_case7)
    assert user_name == "hxdhiraj"


@mark.case7
def test_get_input_file_name_7(input_case7):
    input_file = get_input_file_name(input_case7)
    assert input_file == "", input_file


@mark.case7
def test_get_output_library_table_7(input_case7):
    output_library, output_table = get_output_library_table(input_case7)
    assert output_library == "" and output_table == "", output_library + output_table


@mark.case7
def test_get_input_library_table_7(input_case7):
    input_lib, input_table = get_input_library_table(input_case7)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case7
def test_get_sas_step_name_7(input_case7):
    step, step_name = get_sas_step_name(input_case7)
    assert step == "PROCEDURE Statement" and step_name == "SQL", step + step_name


@mark.case7
def test_proc_sql_parsing_7(input_case7):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case7)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case7
def test_data_step_parsing_7(input_case7):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case7)
    assert input_lib == [] and input_table == [] and output_lib == [] \
           and output_table == [], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case7
def test_get_ext_db_7(input_case7):
    ext_db_list = get_ext_db(input_case7)
    assert ext_db_list == []


@mark.case7
def test_get_time_info_7(input_case7):
    exe_date, exe_time = get_time_info(input_case7)
    assert exe_date == '2021-05-15' and exe_time == '08:06:45'


@mark.case7
def test_get_process_time_7(input_case7):
    cpu_time, real_time = get_process_time(input_case7)
    assert real_time == 0.08 and cpu_time == 0.09, str(cpu_time) + " " + str(real_time)


@mark.case7
def test_get_migration_disp_7(input_case7):
    rule_id, migration_disp = get_migration_disp(0.09, 0.08, 'PROCEDURE Statement', 'SQL', input_case7)
    assert rule_id == '2' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case8
def test_get_user_name_8(input_case8):
    user_name = get_user_name(input_case8)
    assert user_name == "Bank2BU"


@mark.case8
def test_get_input_file_name_8(input_case8):
    input_file = get_input_file_name(input_case8)
    assert input_file == "", input_file


@mark.case8
def test_get_output_library_table_8(input_case8):
    output_library, output_table = get_output_library_table(input_case8)
    assert output_library == "STG_WTCH;STG_WTCH;STG_WTCH;STG_WTCH;STG_WTCH" and output_table == "FSC_ENTITY_WATCH_LIST_DIM;WL_IND_NAME;WL_IND_MATCH;WL_ORG_NAME;WL_ORG_MATCH", output_library + output_table


@mark.case8
def test_get_input_library_table_8(input_case8):
    input_lib, input_table = get_input_library_table(input_case8)
    assert input_lib == "SEG_KC" and input_table == "FSC_ENTITY_WATCH_LIST_DIM", input_lib + input_table


@mark.case8
def test_get_sas_step_name_8(input_case8):
    step, step_name = get_sas_step_name(input_case8)
    assert step == "DATA statement" and step_name == "DATA", step + step_name


@mark.case8
def test_proc_sql_parsing_8(input_case8):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case8)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case8
def test_data_step_parsing_8(input_case8):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case8)
    assert input_lib == ['seg_kc'] and input_table == ['fsc_entity_watch_list_dim'] and output_lib == ['stg_wtch', 'stg_wtch', 'stg_wtch', 'stg_wtch', 'stg_wtch'] \
           and output_table == ['fsc_entity_watch_list_dim', 'wl_ind_name', 'wl_ind_match', 'wl_org_name', 'wl_org_match'], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case8
def test_get_ext_db_8(input_case8):
    ext_db_list = get_ext_db(input_case8)
    assert ext_db_list == []


@mark.case8
def test_get_time_info_8(input_case8):
    exe_date, exe_time = get_time_info(input_case8)
    assert exe_date == '2021-05-14' and exe_time == '06:46:04'


@mark.case8
def test_get_process_time_8(input_case8):
    cpu_time, real_time = get_process_time(input_case8)
    assert real_time == 0.13 and cpu_time == 0.06, str(cpu_time) + " " + str(real_time)


@mark.case8
def test_get_migration_disp_8(input_case8):
    rule_id, migration_disp = get_migration_disp(0.06, 0.13, 'DATA statement', 'DATA', input_case8)
    assert rule_id == '15' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case9
def test_get_user_name_9(input_case9):
    user_name = get_user_name(input_case9)
    assert user_name == "Bank2BU"


@mark.case9
def test_get_input_file_name_9(input_case9):
    input_file = get_input_file_name(input_case9)
    assert input_file == "", input_file


@mark.case9
def test_get_output_library_table_9(input_case9):
    output_library, output_table = get_output_library_table(input_case9)
    assert output_library == "MST_PREP" and output_table == "DORMANT_ACCOUNT_TRANSACTIONS", output_library + output_table


@mark.case9
def test_get_input_library_table_9(input_case9):
    input_lib, input_table = get_input_library_table(input_case9)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case9
def test_get_sas_step_name_9(input_case9):
    step, step_name = get_sas_step_name(input_case9)
    assert step == "PROCEDURE Statement" and step_name == "SQL", step + step_name


@mark.case9
def test_proc_sql_parsing_9(input_case9):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case9)
    assert input_lib == [] and input_table == [] and output_lib == ['mst_prep'] and \
           output_table == ['DORMANT_ACCOUNT_TRANSACTIONS'], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case9
def test_data_step_parsing_9(input_case9):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case9)
    assert input_lib == [] and input_table == [] and output_lib == [] \
           and output_table == [], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case9
def test_get_ext_db_9(input_case9):
    ext_db_list = get_ext_db(input_case9)
    assert ext_db_list == []


@mark.case9
def test_get_time_info_9(input_case9):
    exe_date, exe_time = get_time_info(input_case9)
    assert exe_date == '2021-05-14' and exe_time == '06:45:19'


@mark.case9
def test_get_process_time_9(input_case9):
    cpu_time, real_time = get_process_time(input_case9)
    assert real_time == 1 and cpu_time == 0.03, str(cpu_time) + " " + str(real_time)


@mark.case9
def test_get_migration_disp_9(input_case9):
    rule_id, migration_disp = get_migration_disp(0.03, 1, 'PROCEDURE Statement', 'SQL', input_case9)
    assert rule_id == '9' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case10
def test_get_user_name_10(input_case10):
    user_name = get_user_name(input_case10)
    assert user_name == "Bank2BU"


@mark.case10
def test_get_input_file_name_10(input_case10):
    input_file = get_input_file_name(input_case10)
    assert input_file == "", input_file


@mark.case10
def test_get_output_library_table_10(input_case10):
    output_library, output_table = get_output_library_table(input_case10)
    assert output_library == "MST_PREP" and output_table == "ACCOUNT_TRANS20181102", output_library + output_table


@mark.case10
def test_get_input_library_table_10(input_case10):
    input_lib, input_table = get_input_library_table(input_case10)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case10
def test_get_sas_step_name_10(input_case10):
    step, step_name = get_sas_step_name(input_case10)
    assert step == "PROCEDURE Statement" and step_name == "SQL", step + step_name


@mark.case10
def test_proc_sql_parsing_10(input_case10):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case10)
    assert input_lib == [] and input_table == [] and output_lib == ['mst_prep'] and \
           output_table == ['account_trans20181102'], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case10
def test_data_step_parsing_10(input_case10):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case10)
    assert input_lib == [] and input_table == [] and output_lib == [] \
           and output_table == [], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case10
def test_get_ext_db_10(input_case10):
    ext_db_list = get_ext_db(input_case10)
    assert ext_db_list == ['oracle']


@mark.case10
def test_get_time_info_10(input_case10):
    exe_date, exe_time = get_time_info(input_case10)
    assert exe_date == '2021-05-14' and exe_time == '06:45:23'


@mark.case10
def test_get_process_time_10(input_case10):
    cpu_time, real_time = get_process_time(input_case10)
    assert real_time == 0.68 and cpu_time == 0.01, str(cpu_time) + " " + str(real_time)


@mark.case10
def test_get_migration_disp_10(input_case10):
    rule_id, migration_disp = get_migration_disp(0.01, 0.68, 'PROCEDURE Statement', 'SQL', input_case10)
    assert rule_id == '9' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case11
def test_get_user_name_11(input_case11):
    user_name = get_user_name(input_case11)
    assert user_name == "Bank2BU"


@mark.case11
def test_get_input_file_name_11(input_case11):
    input_file = get_input_file_name(input_case11)
    assert input_file == "", input_file


@mark.case11
def test_get_output_library_table_11(input_case11):
    output_library, output_table = get_output_library_table(input_case11)
    assert output_library == "" and output_table == "", output_library + output_table


@mark.case11
def test_get_input_library_table_11(input_case11):
    input_lib, input_table = get_input_library_table(input_case11)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case11
def test_get_sas_step_name_11(input_case11):
    step, step_name = get_sas_step_name(input_case11)
    assert step == "PROCEDURE Statement" and step_name == "SQL", step + step_name


@mark.case11
def test_proc_sql_parsing_11(input_case11):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case11)
    assert input_lib == ['seg_kc','seg_kc','seg_kc'] and input_table == ['fsk_header', 'fsk_scenario', 'fsk_scenario_parameter'] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case11
def test_data_step_parsing_11(input_case11):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case11)
    assert input_lib == [] and input_table == [] and output_lib == [] \
           and output_table == [], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case11
def test_get_ext_db_11(input_case11):
    ext_db_list = get_ext_db(input_case11)
    assert ext_db_list == []


@mark.case11
def test_get_time_info_11(input_case11):
    exe_date, exe_time = get_time_info(input_case11)
    assert exe_date == '2021-05-14' and exe_time == '06:45:24'


@mark.case11
def test_get_process_time_11(input_case11):
    cpu_time, real_time = get_process_time(input_case11)
    assert real_time == 0.24 and cpu_time == 0.04, str(cpu_time) + " " + str(real_time)


@mark.case11
def test_get_migration_disp_11(input_case11):
    rule_id, migration_disp = get_migration_disp(0.04, 0.24, 'PROCEDURE Statement', 'SQL', input_case11)
    assert rule_id == '9' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case12
def test_get_user_name_12(input_case12):
    user_name = get_user_name(input_case12)
    assert user_name == "Bank2BU"


@mark.case12
def test_get_input_file_name_12(input_case12):
    input_file = get_input_file_name(input_case12)
    assert input_file == "", input_file


@mark.case12
def test_get_output_library_table_12(input_case12):
    output_library, output_table = get_output_library_table(input_case12)
    assert output_library == "" and output_table == "", output_library + output_table


@mark.case12
def test_get_input_library_table_12(input_case12):
    input_lib, input_table = get_input_library_table(input_case12)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case12
def test_get_sas_step_name_12(input_case12):
    step, step_name = get_sas_step_name(input_case12)
    assert step == "DATA statement" and step_name == "DATA", step + step_name


@mark.case12
def test_proc_sql_parsing_12(input_case12):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case12)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case12
def test_data_step_parsing_12(input_case12):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case12)
    assert input_lib == [] and input_table == [] and output_lib == [] \
           and output_table == [], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case12
def test_get_ext_db_12(input_case12):
    ext_db_list = get_ext_db(input_case12)
    assert ext_db_list == []


@mark.case12
def test_get_time_info_12(input_case12):
    exe_date, exe_time = get_time_info(input_case12)
    assert exe_date == '2021-05-14' and exe_time == '06:45:24'


@mark.case12
def test_get_process_time_12(input_case12):
    cpu_time, real_time = get_process_time(input_case12)
    assert real_time == 0.02 and cpu_time == 0.03, str(cpu_time) + " " + str(real_time)


@mark.case12
def test_get_migration_disp_12(input_case12):
    rule_id, migration_disp = get_migration_disp(0.02, 0.03, 'DATA statement', 'DATA', input_case12)
    assert rule_id == '20' and migration_disp == "Code Change", rule_id + " " + migration_disp


@mark.case13
def test_get_user_name_13(input_case13):
    user_name = get_user_name(input_case13)
    assert user_name == "Bank2BU"


@mark.case13
def test_get_input_file_name_13(input_case13):
    input_file = get_input_file_name(input_case13)
    assert input_file == "", input_file


@mark.case13
def test_get_output_library_table_13(input_case13):
    output_library, output_table = get_output_library_table(input_case13)
    assert output_library == "DB_KC" and output_table == "FSK_JOB_CALENDAR", output_library + output_table


@mark.case13
def test_get_input_library_table_13(input_case13):
    input_lib, input_table = get_input_library_table(input_case13)
    assert input_lib == "" and input_table == "", input_lib + input_table


@mark.case13
def test_get_sas_step_name_13(input_case13):
    step, step_name = get_sas_step_name(input_case13)
    assert step == "DATA statement" and step_name == "DATA", step + step_name


@mark.case13
def test_proc_sql_parsing_13(input_case13):
    input_lib, input_table, output_lib, output_table = proc_sql_parsing(input_case13)
    assert input_lib == [] and input_table == [] and output_lib == [] and \
           output_table == [], str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case13
def test_data_step_parsing_13(input_case13):
    input_lib, input_table, output_lib, output_table = data_step_parsing(input_case13)
    assert input_lib == [] and input_table == [] and output_lib == [] \
           and output_table == [], \
           str(input_lib) + str(input_table) + str(output_lib) + str(output_table)


@mark.case13
def test_get_ext_db_13(input_case13):
    ext_db_list = get_ext_db(input_case13)
    assert ext_db_list == []


@mark.case13
def test_get_time_info_13(input_case13):
    exe_date, exe_time = get_time_info(input_case13)
    assert exe_date == '2021-05-14' and exe_time == '06:45:24'


@mark.case13
def test_get_process_time_13(input_case13):
    cpu_time, real_time = get_process_time(input_case13)
    assert real_time == 0.02 and cpu_time == 0.03, str(cpu_time) + " " + str(real_time)


@mark.case13
def test_get_migration_disp_13(input_case13):
    rule_id, migration_disp = get_migration_disp(0.02, 0.03, 'DATA statement', 'DATA', input_case13)
    assert rule_id == '20' and migration_disp == "Code Change", rule_id + " " + migration_disp

