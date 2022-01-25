from pytest import mark
from readlogs.read_logs import get_user_name
from readlogs.read_logs import get_input_file_name
from readlogs.read_logs import get_output_library_table
from readlogs.read_logs import get_input_library_table
from readlogs.read_logs import get_sas_step_name
from readlogs.read_logs import proc_sql_parsing
from readlogs.read_logs import data_step_parsing
from readlogs.read_logs import get_ext_db
from readlogs.read_logs import get_time_info
from readlogs.read_logs import get_process_time
from readlogs.read_logs import get_migration_disp

from input_contents import input_case1
from input_contents import input_case2
from input_contents import input_case3
from input_contents import input_case4
from input_contents import input_case5
from input_contents import input_case6
from input_contents import input_case7


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
    assert input_lib == ['work'] and input_table == ['bev_type_month_gap_local'] and output_lib == ['work'] and output_table == ['bev_type_month_gap_local'], \
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
    assert input_lib == ['instage'] and input_table == ['bev_type_weekly_analysis_date_cn'] and output_lib == ['work', 'work'] \
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
    rule_id, migration_disp = get_migration_disp(0, 0, 'DATA statement', 'DATA', input_case5)
    assert rule_id == '' and migration_disp == "Lift and Shift", rule_id + " " + migration_disp




