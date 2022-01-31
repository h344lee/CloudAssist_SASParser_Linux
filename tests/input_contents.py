from pytest import fixture


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case1():
    return """
7  2021-05-15T08:03:54,871 INFO  [00000010] :hxdhiraj - 7          
8  2021-05-15T08:03:54,871 INFO  [00000010] :hxdhiraj - 8          ODS _ALL_ CLOSE;
9  2021-05-15T08:03:54,872 INFO  [00000010] :hxdhiraj - 9          OPTIONS DEV=ACTIVEX;
10  2021-05-15T08:03:54,876 INFO  [00000010] :hxdhiraj - 10         GOPTIONS XPIXELS=0 YPIXELS=0;
11  2021-05-15T08:03:54,876 INFO  [00000010] :hxdhiraj - 11         FILENAME EGSR TEMP;
12  2021-05-15T08:03:54,878 INFO  [00000010] :hxdhiraj - 12         ODS tagsets.sasreport13(ID=EGSR) FILE=EGSR
13  2021-05-15T08:03:54,878 INFO  [00000010] :hxdhiraj - 13             STYLE=HtmlBlue
14  2021-05-15T08:03:54,879 INFO  [00000010] :hxdhiraj - 14             STYLESHEET=(URL="file:///C:/Program%20Files/SASHome/SASEnterpriseGuide/7.1/Styles/HtmlBlue.css")
15  2021-05-15T08:03:54,879 INFO  [00000010] :hxdhiraj - 15             NOGTITLE
16  2021-05-15T08:03:54,879 INFO  [00000010] :hxdhiraj - 16             NOGFOOTNOTE
17  2021-05-15T08:03:54,909 INFO  [00000010] :hxdhiraj - 17             GPATH=&sasworklocation
18  2021-05-15T08:03:54,909 INFO  [00000010] :hxdhiraj - 18             ENCODING=UTF8
19  2021-05-15T08:03:54,909 INFO  [00000010] :hxdhiraj - 19             options(rolap="on")
20  2021-05-15T08:03:54,910 INFO  [00000010] :hxdhiraj - 20         ;
21  2021-05-15T08:03:54,910 INFO  [00000010] :hxdhiraj - NOTE: Writing TAGSETS.SASREPORT13(EGSR) Body file: EGSR
22  2021-05-15T08:03:54,911 INFO  [00000010] :hxdhiraj - 21         
23  2021-05-15T08:03:54,911 INFO  [00000010] :hxdhiraj - 22         GOPTIONS ACCESSIBLE;
24  2021-05-15T08:03:54,912 INFO  [00000010] :hxdhiraj - 23         /*-----------------------Province based gap filling-------------------------*/
25  2021-05-15T08:03:54,915 INFO  [00000015] :hxdhiraj - 24         data instage.province_gap_analysis;
26  2021-05-15T08:03:54,915 INFO  [00000015] :hxdhiraj - 25         	infile '/sasdata/adhoc/Projects/Canada/flat_files/province_weekly_gap.csv'
27  2021-05-15T08:03:54,916 INFO  [00000015] :hxdhiraj - 26         		delimiter=','
28  2021-05-15T08:03:54,916 INFO  [00000015] :hxdhiraj - 27         		missover
29  2021-05-15T08:03:54,916 INFO  [00000015] :hxdhiraj - 28         		firstobs=2
30  2021-05-15T08:03:54,916 INFO  [00000015] :hxdhiraj - 29         		DSD
31  2021-05-15T08:03:54,917 INFO  [00000015] :hxdhiraj - 30         		lrecl = 32767;
32  2021-05-15T08:03:54,917 INFO  [00000015] :hxdhiraj - 31          FORMAT
33  2021-05-15T08:03:54,917 INFO  [00000015] :hxdhiraj - 32                 AOP_Customer_Group $CHAR15.
34  2021-05-15T08:03:54,918 INFO  [00000015] :hxdhiraj - 33                 Delivery_Plant   $CHAR10.
35  2021-05-15T08:03:54,918 INFO  [00000015] :hxdhiraj - 34                 Province         $CHAR2.
36  2021-05-15T08:03:54,918 INFO  [00000015] :hxdhiraj - 35                 Lag_Duration     BEST1.
37  2021-05-15T08:03:54,918 INFO  [00000015] :hxdhiraj - 36                 fromdate         DATE9.
38  2021-05-15T08:03:54,919 INFO  [00000015] :hxdhiraj - 37                 todate           DATE9.;
39  2021-05-15T08:03:54,919 INFO  [00000015] :hxdhiraj - 38             INPUT
40  2021-05-15T08:03:54,919 INFO  [00000015] :hxdhiraj - 39                 AOP_Customer_Group : $CHAR15.
41  2021-05-15T08:03:54,920 INFO  [00000015] :hxdhiraj - 40                 Delivery_Plant   : $CHAR10.
42  2021-05-15T08:03:54,920 INFO  [00000015] :hxdhiraj - 41                 Province         : $CHAR2.
43  2021-05-15T08:03:54,920 INFO  [00000015] :hxdhiraj - 42                 Lag_Duration     : BEST1.
44  2021-05-15T08:03:54,920 INFO  [00000015] :hxdhiraj - 43                 fromdate         : DATE9.
45  2021-05-15T08:03:54,920 INFO  [00000015] :hxdhiraj - 44                 todate           : DATE9.;
46  2021-05-15T08:03:54,920 INFO  [00000015] :hxdhiraj - 45         run;
47  2021-05-15T08:03:54,921 INFO  [00000015] :hxdhiraj - 
48  2021-05-15T08:03:54,923 INFO  [00000015] :hxdhiraj - NOTE: The infile '/sasdata/adhoc/Projects/Canada/flat_files/province_weekly_gap.csv' is:
49  2021-05-15T08:03:54,923 INFO  [00000015] :hxdhiraj -       Filename=/sasdata/adhoc/Projects/Canada/flat_files/province_weekly_gap.csv,
50  2021-05-15T08:03:54,923 INFO  [00000015] :hxdhiraj -       Owner Name=hxdhiraj,Group Name=sas,
51  2021-05-15T08:03:54,923 INFO  [00000015] :hxdhiraj -       Access Permission=-rw-------,
52  2021-05-15T08:03:54,924 INFO  [00000015] :hxdhiraj -       Last Modified=19Feb2021:02:18:11,
53  2021-05-15T08:03:54,924 INFO  [00000015] :hxdhiraj -       File Size (bytes)=113
54  2021-05-15T08:03:54,924 INFO  [00000015] :hxdhiraj - 
55  2021-05-15T08:03:54,924 INFO  [00000015] :hxdhiraj - NOTE: 2 records were read from the infile '/sasdata/adhoc/Projects/Canada/flat_files/province_weekly_gap.csv'.
56  2021-05-15T08:03:54,924 INFO  [00000015] :hxdhiraj -       The minimum record length was 14.
57  2021-05-15T08:03:54,924 INFO  [00000015] :hxdhiraj -       The maximum record length was 22.
58  2021-05-15T08:03:54,925 INFO  [00000015] :hxdhiraj - NOTE: The data set INSTAGE.PROVINCE_GAP_ANALYSIS has 2 observations and 6 variables.
59  2021-05-15T08:03:54,925 INFO  [00000015] :hxdhiraj - 2                                                          The SAS System                                 08:02 Friday, May 14, 2021
60  2021-05-15T08:03:54,925 INFO  [00000015] :hxdhiraj - 
61  2021-05-15T08:03:54,925 INFO  [00000015] :hxdhiraj - NOTE: DATA statement used (Total process time):
62  2021-05-15T08:03:54,925 INFO  [00000015] :hxdhiraj -       real time           0.01 seconds
63  2021-05-15T08:03:54,926 INFO  [00000015] :hxdhiraj -       cpu time            0.02 """


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case2():
    return """
65  2021-05-15T08:03:54,927 INFO  [00000010] :hxdhiraj - 
66  2021-05-15T08:03:54,927 INFO  [00000010] :hxdhiraj - 46         
67  2021-05-15T08:03:54,927 INFO  [00000010] :hxdhiraj - 47         
68  2021-05-15T08:03:54,928 INFO  [00000010] :hxdhiraj - 48         /*-----------------------Product based gap filling-------------------------*/
69  2021-05-15T08:03:54,930 INFO  [00000016] :hxdhiraj - 49         data instage.product_gap_analysis;
70  2021-05-15T08:03:54,930 INFO  [00000016] :hxdhiraj - 50         	infile '/sasdata/adhoc/Projects/Canada/flat_files/product_weekly_gap.csv'
71  2021-05-15T08:03:54,931 INFO  [00000016] :hxdhiraj - 51         		delimiter=','
72  2021-05-15T08:03:54,931 INFO  [00000016] :hxdhiraj - 52         		missover
73  2021-05-15T08:03:54,931 INFO  [00000016] :hxdhiraj - 53         		firstobs=2
74  2021-05-15T08:03:54,932 INFO  [00000016] :hxdhiraj - 54         		DSD
75  2021-05-15T08:03:54,932 INFO  [00000016] :hxdhiraj - 55         		lrecl = 32767;
76  2021-05-15T08:03:54,932 INFO  [00000016] :hxdhiraj - 56          FORMAT
77  2021-05-15T08:03:54,932 INFO  [00000016] :hxdhiraj - 57          		Product_Code $CHAR15.
78  2021-05-15T08:03:54,933 INFO  [00000016] :hxdhiraj - 58                 AOP_Customer_Group $CHAR15.
79  2021-05-15T08:03:54,933 INFO  [00000016] :hxdhiraj - 59                 Delivery_Plant   $CHAR10.
80  2021-05-15T08:03:54,933 INFO  [00000016] :hxdhiraj - 60                 Province_code         $CHAR2.
81  2021-05-15T08:03:54,933 INFO  [00000016] :hxdhiraj - 61                 Lag_Duration     BEST1.
82  2021-05-15T08:03:54,934 INFO  [00000016] :hxdhiraj - 62                 fromdate         DATE9.
83  2021-05-15T08:03:54,934 INFO  [00000016] :hxdhiraj - 63                 todate           DATE9.;
84  2021-05-15T08:03:54,934 INFO  [00000016] :hxdhiraj - 64             INPUT
85  2021-05-15T08:03:54,934 INFO  [00000016] :hxdhiraj - 65         		Product_Code 	:$CHAR15.
86  2021-05-15T08:03:54,935 INFO  [00000016] :hxdhiraj - 66                 AOP_Customer_Group : $CHAR15.
87  2021-05-15T08:03:54,935 INFO  [00000016] :hxdhiraj - 67         		Delivery_Plant   : $CHAR10.
88  2021-05-15T08:03:54,935 INFO  [00000016] :hxdhiraj - 68                 Province_code    : $CHAR2.
89  2021-05-15T08:03:54,935 INFO  [00000016] :hxdhiraj - 69                 Lag_Duration     : BEST1.
90  2021-05-15T08:03:54,935 INFO  [00000016] :hxdhiraj - 70                 fromdate         : DATE9.
91  2021-05-15T08:03:54,936 INFO  [00000016] :hxdhiraj - 71                 todate           : DATE9.;
92  2021-05-15T08:03:54,936 INFO  [00000016] :hxdhiraj - 72         run;
93  2021-05-15T08:03:54,936 INFO  [00000016] :hxdhiraj - 
94  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj - NOTE: The infile '/sasdata/adhoc/Projects/Canada/flat_files/product_weekly_gap.csv' is:
95  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj -       Filename=/sasdata/adhoc/Projects/Canada/flat_files/product_weekly_gap.csv,
96  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj -       Owner Name=hxdhiraj,Group Name=sas,
97  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj -       Access Permission=-rw-------,
98  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj -       Last Modified=19Feb2021:02:18:26,
99  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj -       File Size (bytes)=143
100  2021-05-15T08:03:54,938 INFO  [00000016] :hxdhiraj - 
101  2021-05-15T08:03:54,939 INFO  [00000016] :hxdhiraj - NOTE: 2 records were read from the infile '/sasdata/adhoc/Projects/Canada/flat_files/product_weekly_gap.csv'.
102  2021-05-15T08:03:54,939 INFO  [00000016] :hxdhiraj -       The minimum record length was 21.
103  2021-05-15T08:03:54,939 INFO  [00000016] :hxdhiraj -       The maximum record length was 29.
104  2021-05-15T08:03:54,939 INFO  [00000016] :hxdhiraj - NOTE: The data set INSTAGE.PRODUCT_GAP_ANALYSIS has 2 observations and 7 variables.
105  2021-05-15T08:03:54,940 INFO  [00000016] :hxdhiraj - NOTE: DATA statement used (Total process time):
106  2021-05-15T08:03:54,940 INFO  [00000016] :hxdhiraj -       real time           0.01 seconds
107  2021-05-15T08:03:54,940 INFO  [00000016] :hxdhiraj -       cpu time            0.02 
    """


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case3():
    return """
638  2021-05-15T08:06:45,032 INFO  [00000010] :hxdhiraj - 
639  2021-05-15T08:06:45,032 INFO  [00000010] :hxdhiraj - 361        
640  2021-05-15T08:06:45,032 INFO  [00000010] :hxdhiraj - 362        /*	identifying invalid records */
641  2021-05-15T08:06:45,033 INFO  [00000010] :hxdhiraj - 363        
642  2021-05-15T08:06:45,033 INFO  [00000056] :hxdhiraj - 364        proc sql;
643  2021-05-15T08:06:45,034 INFO  [00000056] :hxdhiraj - 365        
644  2021-05-15T08:06:45,034 INFO  [00000056] :hxdhiraj - 366        create table PostFcst.bev_ty_fixed_invalid_records_cn (drop=fromdate todate id) as
645  2021-05-15T08:06:45,035 INFO  [00000056] :hxdhiraj - 367        	select * from work.bev_type_fix_gap_local
646  2021-05-15T08:06:45,035 INFO  [00000056] :hxdhiraj - 368        		WHERE id not IN (SELECT b.id FROM  indata.ORDERABLESKUDIM_GAP_ANALYSIS   as a,work.bev_type_fix_gap_local as B
647  2021-05-15T08:06:45,035 INFO  [00000056] :hxdhiraj - 369        		WHERE
648  2021-05-15T08:06:45,035 INFO  [00000056] :hxdhiraj - 370        			a.beverage_family = b.beverage_family and
649  2021-05-15T08:06:45,035 INFO  [00000056] :hxdhiraj - 371        			a.importbrandflag = b.importbrandflag
650  2021-05-15T08:06:45,036 INFO  [00000056] :hxdhiraj - 372        	);
651  2021-05-15T08:06:45,036 ERROR [00000056] :hxdhiraj - ERROR: File INDATA.ORDERABLESKUDIM_GAP_ANALYSIS.DATA does not exist.
652  2021-05-15T08:06:45,036 INFO  [00000056] :hxdhiraj - NOTE: PROC SQL set option NOEXEC and will continue to check the syntax of statements.
653  2021-05-15T08:06:45,037 INFO  [00000056] :hxdhiraj - 373        run;
654  2021-05-15T08:06:45,037 INFO  [00000056] :hxdhiraj - NOTE: PROC SQL statements are executed immediately; The RUN statement has no effect.
655  2021-05-15T08:06:45,037 INFO  [00000056] :hxdhiraj - 374        
656  2021-05-15T08:06:45,037 INFO  [00000056] :hxdhiraj - 375        
657  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj - 376        /*getting beverage details*/
658  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj - NOTE: The SAS System stopped processing this step because of errors.
659  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj - 12                                                         The SAS System                                 08:02 Friday, May 14, 2021
660  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj - 
661  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj - NOTE: PROCEDURE SQL used (Total process time):
662  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj -       real time           0.00 seconds
663  2021-05-15T08:06:45,038 INFO  [00000056] :hxdhiraj -       cpu time            0.00 
"""


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case4():
    return """
923  2021-05-15T08:06:45,118 INFO  [00000010] :hxdhiraj - 
924  2021-05-15T08:06:45,118 INFO  [00000010] :hxdhiraj - 522        
925  2021-05-15T08:06:45,121 INFO  [00000068] :hxdhiraj - 523        data work.bev_type_month_gap_local;
926  2021-05-15T08:06:45,121 INFO  [00000068] :hxdhiraj - 524        set work.bev_type_month_gap_local;
927  2021-05-15T08:06:45,121 INFO  [00000068] :hxdhiraj - 525        id = uuidgen();
928  2021-05-15T08:06:45,121 INFO  [00000068] :hxdhiraj - 526        run;
929  2021-05-15T08:06:45,121 INFO  [00000068] :hxdhiraj - 
930  2021-05-15T08:06:45,123 INFO  [00000068] :hxdhiraj - NOTE: There were 1 observations read from the data set WORK.BEV_TYPE_MONTH_GAP_LOCAL.
931  2021-05-15T08:06:45,123 INFO  [00000068] :hxdhiraj - NOTE: The data set WORK.BEV_TYPE_MONTH_GAP_LOCAL has 1 observations and 9 variables.
932  2021-05-15T08:06:45,123 INFO  [00000068] :hxdhiraj - NOTE: DATA statement used (Total process time):
933  2021-05-15T08:06:45,123 INFO  [00000068] :hxdhiraj -       real time           0.00 seconds
934  2021-05-15T08:06:45,124 INFO  [00000068] :hxdhiraj -       cpu time            0.00 
"""


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case5():
    return """
1168  2021-05-15T08:06:45,190 INFO  [00000010] :hxdhiraj - 665        data work.bev_type_weekly_gap_all work.bev_type_weekly_gap_local;
1169  2021-05-15T08:06:45,190 INFO  [00000010] :hxdhiraj - 
1170  2021-05-15T08:06:45,193 INFO  [00000078] :hxdhiraj - 666        	set instage.bev_type_weekly_analysis_date_cn;
1171  2021-05-15T08:06:45,194 INFO  [00000078] :hxdhiraj - 667        
1172  2021-05-15T08:06:45,194 INFO  [00000078] :hxdhiraj - 668        	if AOP_Customer_Group eq "ALL" or Delivery_Plant eq "ALL" then
1173  2021-05-15T08:06:45,194 INFO  [00000078] :hxdhiraj - 669        		output work.bev_type_weekly_gap_all;
1174  2021-05-15T08:06:45,194 INFO  [00000078] :hxdhiraj - 670        	else output work.bev_type_weekly_gap_local;
1175  2021-05-15T08:06:45,194 INFO  [00000078] :hxdhiraj - 671        run;
1176  2021-05-15T08:06:45,194 INFO  [00000078] :hxdhiraj - 
1177  2021-05-15T08:06:45,196 INFO  [00000078] :hxdhiraj - NOTE: There were 1 observations read from the data set INSTAGE.BEV_TYPE_WEEKLY_ANALYSIS_DATE_CN.
1178  2021-05-15T08:06:45,196 INFO  [00000078] :hxdhiraj - NOTE: The data set WORK.BEV_TYPE_WEEKLY_GAP_ALL has 1 observations and 8 variables.
1179  2021-05-15T08:06:45,197 INFO  [00000078] :hxdhiraj - NOTE: The data set WORK.BEV_TYPE_WEEKLY_GAP_LOCAL has 0 observations and 8 variables.
1180  2021-05-15T08:06:45,197 INFO  [00000078] :hxdhiraj - NOTE: DATA statement used (Total process time):
1181  2021-05-15T08:06:45,197 INFO  [00000078] :hxdhiraj -       real time           0.00 seconds
1182  2021-05-15T08:06:45,197 INFO  [00000078] :hxdhiraj -       cpu time            0.01 
"""


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case6():
    return """
1184  2021-05-15T08:06:45,199 INFO  [00000010] :hxdhiraj - 
1185  2021-05-15T08:06:45,199 INFO  [00000010] :hxdhiraj - 672        
1186  2021-05-15T08:06:45,202 INFO  [00000079] :hxdhiraj - 673        data work.bev_type_weekly_gap_local;
1187  2021-05-15T08:06:45,202 INFO  [00000079] :hxdhiraj - 674        set work.bev_type_weekly_gap_local;
1188  2021-05-15T08:06:45,202 INFO  [00000079] :hxdhiraj - 675        id = uuidgen();
1189  2021-05-15T08:06:45,202 INFO  [00000079] :hxdhiraj - 676        run;
1190  2021-05-15T08:06:45,202 INFO  [00000079] :hxdhiraj - 
1191  2021-05-15T08:06:45,203 INFO  [00000079] :hxdhiraj - NOTE: There were 0 observations read from the data set WORK.BEV_TYPE_WEEKLY_GAP_LOCAL.
1192  2021-05-15T08:06:45,204 INFO  [00000079] :hxdhiraj - NOTE: The data set WORK.BEV_TYPE_WEEKLY_GAP_LOCAL has 0 observations and 9 variables.
1193  2021-05-15T08:06:45,204 INFO  [00000079] :hxdhiraj - NOTE: DATA statement used (Total process time):
1194  2021-05-15T08:06:45,204 INFO  [00000079] :hxdhiraj -       real time           0.00 seconds
1195  2021-05-15T08:06:45,204 INFO  [00000079] :hxdhiraj -       cpu time            0.00  
"""


# mcebelsasd003_30796.log
@fixture(scope='function')
def input_case7():
    return """
1447  2021-05-15T08:06:45,276 INFO  [00000010] :hxdhiraj - 821        proc sql;
1448  2021-05-15T08:06:45,277 INFO  [00000010] :hxdhiraj - 
1449  2021-05-15T08:06:45,278 INFO  [00000090] :hxdhiraj - 822        alter table indata.STRHISTORYDAILY_GAP_CAN
1450  2021-05-15T08:06:45,278 INFO  [00000090] :hxdhiraj - 823        drop column id;
1451  2021-05-15T08:06:45,361 INFO  [00000090] :hxdhiraj - NOTE: Table INDATA.STRHISTORYDAILY_GAP_CAN has been modified, with 12 columns.
1452  2021-05-15T08:06:45,362 INFO  [00000090] :hxdhiraj - 824        run;
1453  2021-05-15T08:06:45,362 INFO  [00000090] :hxdhiraj - NOTE: PROC SQL statements are executed immediately; The RUN statement has no effect.
1454  2021-05-15T08:06:45,362 INFO  [00000090] :hxdhiraj - 825        /*making count of inserted and deleted records for the emailer*/
1455  2021-05-15T08:06:45,363 INFO  [00000090] :hxdhiraj - NOTE: PROCEDURE SQL used (Total process time):
1456  2021-05-15T08:06:45,363 INFO  [00000090] :hxdhiraj -       real time           0.08 seconds
1457  2021-05-15T08:06:45,363 INFO  [00000090] :hxdhiraj -       cpu time            0.09 
"""


# SASBAP_30420.log
@fixture(scope='function')
def input_case8():
    return """
19087  2021-05-14T06:46:03,905 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   data stg_wtch.fsc_entity_watch_list_dim(
19088  2021-05-14T06:46:03,906 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   keep=entity_watch_list_key entity_watch_list_number watch_list_name tax_id date_of_birth year_of_birth first_name last_name middle_name entity_name match_code_individual match_code_organization 
19089  2021-05-14T06:46:03,906 INFO  [00001214] :Bank2BU@SASBAP - match_code_addr_lines match_code_city match_code_state match_code_country match_code_full_address index=(entity_watch_list_key) compress=yes) stg_wtch.wl_ind_name(
19090  2021-05-14T06:46:03,906 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   keep=entity_watch_list_key last_name rename=(last_name=in_last_name) compress=yes) stg_wtch.wl_ind_match(
19091  2021-05-14T06:46:03,906 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   keep=entity_watch_list_key match_code_individual rename=(match_code_individual=im_match_code_individual) compress=yes) stg_wtch.wl_org_name(
19092  2021-05-14T06:46:03,908 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   keep=entity_watch_list_key entity_name rename=(entity_name=on_organization_name) compress=yes) stg_wtch.wl_org_match(
19093  2021-05-14T06:46:03,908 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   keep=entity_watch_list_key match_code_organization rename=(match_code_organization=om_match_code_organization) compress=yes) ;
19094  2021-05-14T06:46:03,946 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   set seg_kc.fsc_entity_watch_list_dim(keep=entity_watch_list_key entity_watch_list_number watch_list_name type_desc tax_id date_of_birth year_of_birth first_name last_name middle_name 
19095  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - entity_name match_code_individual match_code_organization match_code_addr_lines match_code_city match_code_state match_code_country match_code_full_address exclude_ind change_current_ind where=(upcase(change_current_ind) eq 'Y' and upcase(exclude_ind) eq 
19096  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - 'N')) end=eof;
19097  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   if upcase(type_desc) eq 'INDIVIDUAL' and not missing(last_name) then do;
19098  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   last_name=upcase(compbl(kstrip(last_name)));
19099  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   output stg_wtch.fsc_entity_watch_list_dim stg_wtch.wl_ind_name stg_wtch.wl_ind_match;
19100  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   end;
19101  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   else if upcase(type_desc) eq 'ORGANIZATION' and not missing(entity_name) then do;
19102  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   entity_name=upcase(compbl(kstrip(entity_name)));
19103  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   output stg_wtch.fsc_entity_watch_list_dim stg_wtch.wl_org_name stg_wtch.wl_org_match;
19104  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   end;
19105  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_AGP.FCF_RUN_GENERATED_HEADERS):   run;
19106  2021-05-14T06:46:03,947 INFO  [00001214] :Bank2BU@SASBAP - 
19107  2021-05-14T06:46:03,988 INFO  [00001214] :Bank2BU@SASBAP - NOTE: There were 0 observations read from the data set SEG_KC.FSC_ENTITY_WATCH_LIST_DIM.
19108  2021-05-14T06:46:03,988 INFO  [00001214] :Bank2BU@SASBAP -       WHERE (UPCASE(change_current_ind)='Y') and (UPCASE(exclude_ind)='N');
19109  2021-05-14T06:46:03,996 INFO  [00001214] :Bank2BU@SASBAP - NOTE: The data set STG_WTCH.FSC_ENTITY_WATCH_LIST_DIM has 0 observations and 17 variables.
19110  2021-05-14T06:46:04,017 INFO  [00001214] :Bank2BU@SASBAP - NOTE: The data set STG_WTCH.WL_IND_NAME has 0 observations and 2 variables.
19111  2021-05-14T06:46:04,022 INFO  [00001214] :Bank2BU@SASBAP - NOTE: The data set STG_WTCH.WL_IND_MATCH has 0 observations and 2 variables.
19112  2021-05-14T06:46:04,026 INFO  [00001214] :Bank2BU@SASBAP - NOTE: The data set STG_WTCH.WL_ORG_NAME has 0 observations and 2 variables.
19113  2021-05-14T06:46:04,038 INFO  [00001214] :Bank2BU@SASBAP - NOTE: The data set STG_WTCH.WL_ORG_MATCH has 0 observations and 2 variables.
19114  2021-05-14T06:46:04,041 INFO  [00001214] :Bank2BU@SASBAP - NOTE: DATA statement used (Total process time):
19115  2021-05-14T06:46:04,041 INFO  [00001214] :Bank2BU@SASBAP -       real time           0.13 seconds
19116  2021-05-14T06:46:04,041 INFO  [00001214] :Bank2BU@SASBAP -       cpu time            0.06 
"""


# SASBAP_30420.log
@fixture(scope='function')
def input_case9():
    return """
266  2021-05-14T06:45:18,222 INFO  [00000011] :Bank2BU@SASBAP - 
267  2021-05-14T06:45:18,227 INFO  [00000080] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   proc sql noprint;
268  2021-05-14T06:45:18,228 INFO  [00000080] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
269  2021-05-14T06:45:18,228 INFO  [00000080] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable PBEGINDATE resolves to 20181026
270  2021-05-14T06:45:18,228 INFO  [00000080] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   create table mst_prep.DORMANT_ACCOUNT_TRANSACTIONS as ( select b.account_number, a.dorm_days, c.currency_amount , input(put(c.date_key,8.),yymmdd8.) as date_key, c.transaction_key from work.dormprepaccts a, 
271  2021-05-14T06:45:18,228 INFO  [00000080] :Bank2BU@SASBAP - seg_kc.fsc_account_dim b, seg_kc.fsc_cash_flow_fact c where b.account_key = c.account_key and c.date_key <= 20181102 and c.date_key >= 20181026 and b.account_number = a.account_number and a.dorm_days <= 60 ) order by account_number, date_key;
272  2021-05-14T06:45:19,229 INFO  [00000080] :Bank2BU@SASBAP - NOTE: Table MST_PREP.DORMANT_ACCOUNT_TRANSACTIONS created, with 0 rows and 5 columns.
273  2021-05-14T06:45:19,229 INFO  [00000080] :Bank2BU@SASBAP - 
274  2021-05-14T06:45:19,229 INFO  [00000080] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   quit;
275  2021-05-14T06:45:19,229 INFO  [00000080] :Bank2BU@SASBAP - NOTE: PROCEDURE SQL used (Total process time):
276  2021-05-14T06:45:19,229 INFO  [00000080] :Bank2BU@SASBAP -       real time           1.00 seconds
277  2021-05-14T06:45:19,229 INFO  [00000080] :Bank2BU@SASBAP -       cpu time            0.03 
"""


# SASBAP_30420.log
@fixture(scope='function')
def input_case10():
    return """
746  2021-05-14T06:45:23,253 INFO  [00000011] :Bank2BU@SASBAP - 
747  2021-05-14T06:45:23,253 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
748  2021-05-14T06:45:23,253 INFO  [00000011] :Bank2BU@SASBAP - runasofdate=20181102
749  2021-05-14T06:45:23,253 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable FIRST_JOB_CALENDAR_DATE resolves to        21185
750  2021-05-14T06:45:23,253 INFO  [00000011] :Bank2BU@SASBAP - first_job_calendar_date=       21185
751  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   proc sql;
752  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DBFLAVOR resolves to oracle
753  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DBFLAVOR resolves to oracle
754  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCAUTHDOMAIN resolves to BANK2BU Segmented Knowledge Center
755  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCDBCONNOPTS resolves to path=sasbap
756  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Some characters in the above value which were subject to macro quoting have been unquoted for printing.
757  2021-05-14T06:45:23,256 INFO  [00000141] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   connect to oracle as oracle (authdomain="BANK2BU Segmented Knowledge Center" path=sasbap);
758  2021-05-14T06:45:23,257 DEBUG [00004009] :Bank2BU@SASBAP - IOM CALL svcGetOption(): opt=SELFTEST not found
759  2021-05-14T06:45:23,257 DEBUG [00000003] :Bank2BU@SASBAP - IOM LOGIC ENTRY {class:2ad8b6955e0}->OMIProxyClassNew()
760  2021-05-14T06:45:23,257 DEBUG [00000003] :Bank2BU@SASBAP - IOM NEW OMIProxy (compRef:2ad8be2c380, comp:2ad8b694820)
761  2021-05-14T06:45:23,257 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c380}->OMIProxy::ProxyInit()
762  2021-05-14T06:45:23,257 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c380}->OMIProxy::ProxyInit()
763  2021-05-14T06:45:23,259 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c380}->OMIProxy::ProxyPEInfo()
764  2021-05-14T06:45:23,259 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c380}->OMIProxy::ProxyPEInfo()
765  2021-05-14T06:45:23,259 DEBUG [00000003] :Bank2BU@SASBAP - IOM LOGIC ENTRY {class:2ad8b695720}->SecurityProxyClassNew()
766  2021-05-14T06:45:23,259 DEBUG [00000003] :Bank2BU@SASBAP - IOM NEW SecurityProxy (compRef:2ad8be2c4c0, comp:2ad8b6967e0)
767  2021-05-14T06:45:23,259 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c4c0}->SecurityProxy::ProxyInit()
768  2021-05-14T06:45:23,259 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c4c0}->SecurityProxy::ProxyInit()
769  2021-05-14T06:45:23,260 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c4c0}->SecurityProxy::GetCredentials()
770  2021-05-14T06:45:23,291 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c4c0}->SecurityProxy::GetCredentials()
771  2021-05-14T06:45:23,291 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c4c0}->SecurityProxy::GetInfo()
772  2021-05-14T06:45:23,293 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c4c0}->SecurityProxy::GetInfo()
773  2021-05-14T06:45:23,293 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c4c0}->SecurityProxy::FreeCredentials()
774  2021-05-14T06:45:23,294 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c4c0}->SecurityProxy::FreeCredentials()
775  2021-05-14T06:45:23,294 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c380}->OMIProxy::ProxyPEInfo()
776  2021-05-14T06:45:23,294 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c380}->OMIProxy::ProxyPEInfo()
777  2021-05-14T06:45:23,294 DEBUG [00000003] :Bank2BU@SASBAP - IOM LOGIC ENTRY {class:2ad8b695a00}->ServerProxyClassNew()
778  2021-05-14T06:45:23,294 DEBUG [00000003] :Bank2BU@SASBAP - IOM NEW ServerProxy (compRef:2ad8be2c5e0, comp:2ad8b831480)
779  2021-05-14T06:45:23,295 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c5e0}->ServerProxy::ProxyInit()
780  2021-05-14T06:45:23,295 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c5e0}->ServerProxy::ProxyInit()
781  2021-05-14T06:45:23,295 DEBUG [00000003] :Bank2BU@SASBAP - IOM CALL {compRef:2ad8be2c4c0}->SecurityProxy::GetLoginForAuthDomain()
782  2021-05-14T06:45:23,323 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN 0={compRef:2ad8be2c4c0}->SecurityProxy::GetLoginForAuthDomain()
783  2021-05-14T06:45:23,326 INFO  [00000141] :Bank2BU@SASBAP - NOTE:  Credential obtained from SAS metadata server.
784  2021-05-14T06:45:23,326 DEBUG [00000003] :Bank2BU@SASBAP - IOM ENTRY ServerProxy {compRef:2ad8be2c5e0}->CompDtor()
785  2021-05-14T06:45:23,326 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN ServerProxy 0={compRef:2ad8be2c5e0}->CompDtor()
786  2021-05-14T06:45:23,326 DEBUG [00000003] :Bank2BU@SASBAP - IOM ENTRY OMIProxy {compRef:2ad8be2c380}->CompDtor()
787  2021-05-14T06:45:23,328 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN OMIProxy 0={compRef:2ad8be2c380}->CompDtor()
788  2021-05-14T06:45:23,328 DEBUG [00000003] :Bank2BU@SASBAP - IOM ENTRY SecurityProxy {compRef:2ad8be2c4c0}->CompDtor()
789  2021-05-14T06:45:23,328 DEBUG [00000003] :Bank2BU@SASBAP - IOM RETURN SecurityProxy 0={compRef:2ad8be2c4c0}->CompDtor()
790  2021-05-14T06:45:23,523 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
791  2021-05-14T06:45:23,523 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
792  2021-05-14T06:45:23,523 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DBFLAVOR resolves to oracle
793  2021-05-14T06:45:23,523 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
794  2021-05-14T06:45:23,523 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
795  2021-05-14T06:45:23,523 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
796  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
797  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
798  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
799  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
800  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
801  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
802  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
803  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
804  2021-05-14T06:45:23,524 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
805  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
806  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
807  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
808  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
809  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
810  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
811  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
812  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
813  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
814  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable SEGKCSCHEMA resolves to BANK2BU
815  2021-05-14T06:45:23,526 INFO  [00000141] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   create table mst_prep.account_trans20181102 as select account_number length=50, account_type_desc length=20, currency_based_account_ind length=1, account_tax_state_code length=3, party_number length=50, 
816  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - acc_entity_segment_id, pty_entity_segment_id, annual_income_amount length=8, last_susp_actv_rpt_date length=8, last_cash_trans_rpt_date length=8, politically_exposed_person_ind length=1, customer_since_date length=8, input("20181102",yymmdd8.) as date_key 
817  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - format=yymmdd8. length=5, transaction_cdi_code length=1, primary_medium_desc length=20, secondary_medium_desc length=20, mechanism_desc length=20, street_state_code length=3, branch_number length=25, branch_type_desc length=10, country_code_3 length=3, 
818  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - currency_code length=3, status_desc length=20, status_reason_desc length=35, currency_amount length=8, transaction_key length=8, risk_classification length=3, associate_number length=20, expected_incoming_amount length=8, expected_outgoing_amount 
819  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - length=8, expected_incoming_count length=8, expected_outgoing_count length=8, increased_behavior_credit_amt length=8 , increased_behavior_debit_amt length=8, increased_behavior_credit_cnt length=8, increased_behavior_debit_cnt length=8, 
820  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - expected_credit_ceiling_amount length=8, expected_debit_ceiling_amount length=8 from connection to oracle (select Innr.*, AA.expected_incoming_amount, AA.expected_outgoing_amount, AA.expected_incoming_count, AA.expected_outgoing_count, 
821  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - AA.increased_behavior_credit_amt , AA.increased_behavior_debit_amt, AA.increased_behavior_credit_cnt, AA.increased_behavior_debit_cnt , AA.expected_credit_ceiling_amount, AA.expected_debit_ceiling_amount from (select A.account_number, A.account_type_desc, 
822  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - A.currency_based_account_ind, A.account_tax_state_code, B.party_number, A.entity_segment_id as acc_entity_segment_id, B.entity_segment_id as pty_entity_segment_id, B.annual_income_amount, B.last_susp_actv_rpt_date, B.last_cash_trans_rpt_date, 
823  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - B.politically_exposed_person_ind, B.customer_since_date, B.risk_classification, C.transaction_cdi_code, C.primary_medium_desc, C.secondary_medium_desc, C.mechanism_desc, D.street_state_code, D.branch_number, D.branch_type_desc, E.country_code_3, 
824  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - F.currency_code, G.status_desc, G.status_reason_desc, I.currency_amount, I.transaction_key, L.associate_number from BANK2BU.fsc_account_dim A, BANK2BU.fsc_party_dim B, BANK2BU.fsc_transaction_type_dim C, BANK2BU.fsc_branch_dim D, BANK2BU.fsc_country_dim 
825  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - E, BANK2BU.fsc_currency_dim F, BANK2BU.fsc_transaction_status_dim G, BANK2BU.fsc_party_account_bridge H, BANK2BU.fsc_cash_flow_fact I, BANK2BU.fsc_associate_dim L where I.account_key = A.account_key and A.account_key = H.account_key and B.party_key = 
826  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - H.party_key and I.transaction_type_key = C.transaction_type_key and I.transaction_status_key = G.transaction_status_key and I.country_key = E.country_key and I.branch_key = D.branch_key and I.transaction_currency_key = F.currency_key and I.date_key = 
827  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - 20181102 and H.role_key = 1 and H.change_current_ind = 'Y' and I.associate_key = L.associate_key ) Innr left join BANK2BU.fsc_account_analysis_dim AA on AA.account_number=Innr.account_number union all select Innr.*, AA.expected_incoming_amount, 
828  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - AA.expected_outgoing_amount, AA.expected_incoming_count, AA.expected_outgoing_count, AA.increased_behavior_credit_amt , AA.increased_behavior_debit_amt, AA.increased_behavior_credit_cnt, AA.increased_behavior_debit_cnt , AA.expected_credit_ceiling_amount, 
829  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - AA.expected_debit_ceiling_amount from (select A.account_number, A.account_type_desc, A.currency_based_account_ind, A.account_tax_state_code, B.party_number, A.entity_segment_id as acc_entity_segment_id, B.entity_segment_id as pty_entity_segment_id, 
830  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - B.annual_income_amount, B.last_susp_actv_rpt_date, B.last_cash_trans_rpt_date, B.politically_exposed_person_ind, B.customer_since_date, B.risk_classification, C.transaction_cdi_code, C.primary_medium_desc, C.secondary_medium_desc, C.mechanism_desc, 
831  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - D.street_state_code, D.branch_number, D.branch_type_desc, E.country_code_3, '' as currency_code, G.status_desc, G.status_reason_desc, 0 as currency_amount, I.transaction_key, 'UNKNOWN' as associate_number from BANK2BU.fsc_account_dim A, 
832  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - BANK2BU.fsc_party_dim B, BANK2BU.fsc_transaction_type_dim C, BANK2BU.fsc_branch_dim D, BANK2BU.fsc_country_dim E, BANK2BU.fsc_transaction_status_dim G, BANK2BU.fsc_party_account_bridge H, BANK2BU.fsc_account_event_fact I where I.account_key = 
833  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - A.account_key and A.account_key = H.account_key and B.party_key = H.party_key and I.transaction_type_key = C.transaction_type_key and I.transaction_status_key = G.transaction_status_key and I.country_key = E.country_key and I.branch_key = D.branch_key and 
834  2021-05-14T06:45:23,527 INFO  [00000141] :Bank2BU@SASBAP - I.date_key = 20181102 and H.role_key = 1 and H.change_current_ind = 'Y' ) Innr left join BANK2BU.fsc_account_analysis_dim AA on AA.account_number=Innr.account_number ) order by account_number, date_key;
835  2021-05-14T06:45:23,937 INFO  [00000141] :Bank2BU@SASBAP - NOTE: Table MST_PREP.ACCOUNT_TRANS20181102 created, with 0 rows and 38 columns.
836  2021-05-14T06:45:23,937 INFO  [00000141] :Bank2BU@SASBAP - 
837  2021-05-14T06:45:23,939 INFO  [00000141] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DBFLAVOR resolves to oracle
838  2021-05-14T06:45:23,939 INFO  [00000141] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   disconnect from oracle;
839  2021-05-14T06:45:23,943 INFO  [00000141] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP):   quit;
840  2021-05-14T06:45:23,943 INFO  [00000141] :Bank2BU@SASBAP - NOTE: PROCEDURE SQL used (Total process time):
841  2021-05-14T06:45:23,943 INFO  [00000141] :Bank2BU@SASBAP -       real time           0.68 seconds
842  2021-05-14T06:45:23,943 INFO  [00000141] :Bank2BU@SASBAP -       cpu time            0.01 
"""


# SASBAP_30420.log
@fixture(scope='function')
def input_case11():
    return """
857  2021-05-14T06:45:23,960 INFO  [00000011] :Bank2BU@SASBAP - 
858  2021-05-14T06:45:23,961 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  Beginning execution.
859  2021-05-14T06:45:23,965 INFO  [00000143] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   proc sql noprint;
860  2021-05-14T06:45:23,965 INFO  [00000143] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   select max(input(sp.parm_value,best32.)) into :numdays from seg_kc.fsk_header h, seg_kc.fsk_scenario s, seg_kc.fsk_scenario_parameter sp where h.header_id=s.header_id and 
861  2021-05-14T06:45:23,965 INFO  [00000143] :Bank2BU@SASBAP - upcase(h.denorm_table_name) = "ACCOUNT_TRANSACTIONS" and upcase(s.scenario_status_code) = "ACT" and upcase(s.current_ind) = "Y" and upcase(s.logical_delete_ind) ne 'Y' and s.scenario_id = sp.scenario_id and sp.parm_name like 'p%_num_days' ;
862  2021-05-14T06:45:24,210 INFO  [00000143] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   quit;
863  2021-05-14T06:45:24,210 INFO  [00000143] :Bank2BU@SASBAP - NOTE: PROCEDURE SQL used (Total process time):
864  2021-05-14T06:45:24,210 INFO  [00000143] :Bank2BU@SASBAP -       real time           0.24 seconds
865  2021-05-14T06:45:24,210 INFO  [00000143] :Bank2BU@SASBAP -       cpu time            0.04 
"""


# SASBAP_30420.log
@fixture(scope='function')
def input_case12():
    return """
884  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - 
885  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  %LET (variable name is DEFAULT_NUM_DAYS_ZERO)
886  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DEFAULT_NUM_DAYS_ZERO resolves to        5
887  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DEFAULT_NUM_DAYS_ZERO resolves to 5
888  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  %IF condition &default_num_days_zero eq . is FALSE
889  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  %PUT Account_header scenarios with default number of days equal to zero: &default_num_days_zero
890  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DEFAULT_NUM_DAYS_ZERO resolves to 5
891  2021-05-14T06:45:24,250 INFO  [00000011] :Bank2BU@SASBAP - Account_header scenarios with default number of days equal to zero: 5
892  2021-05-14T06:45:24,252 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable DEFAULT_NUM_DAYS_ZERO resolves to 5
893  2021-05-14T06:45:24,252 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  %IF condition &default_num_days_zero gt 0 is TRUE
894  2021-05-14T06:45:24,252 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  %PUT These scenarios need month-to-runasofdate number of days of transactions.
895  2021-05-14T06:45:24,252 INFO  [00000011] :Bank2BU@SASBAP - These scenarios need month-to-runasofdate number of days of transactions.
896  2021-05-14T06:45:24,252 INFO  [00000011] :Bank2BU@SASBAP - MLOGIC(FCF_CREATE_ACCT_TRANS_VIEW):  %PUT Adjust numdays if necessary.
897  2021-05-14T06:45:24,252 INFO  [00000011] :Bank2BU@SASBAP - Adjust numdays if necessary.
898  2021-05-14T06:45:24,255 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   data _null_;
899  2021-05-14T06:45:24,255 INFO  [00000145] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181102
900  2021-05-14T06:45:24,270 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   runasofdate = input(put(20181102,8.),yymmdd8.);
901  2021-05-14T06:45:24,272 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   put 'runasofdate: ' runasofdate nldate.;
902  2021-05-14T06:45:24,272 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   startmonth = runasofdate - day(runasofdate) + 1;
903  2021-05-14T06:45:24,272 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   put 'Start of month: ' startmonth nldate.;
904  2021-05-14T06:45:24,272 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   num_days = runasofdate - startmonth + 1;
905  2021-05-14T06:45:24,273 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   put 'Days month-to-runasofdate: ' num_days;
906  2021-05-14T06:45:24,273 INFO  [00000145] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable NUMDAYS resolves to 20
907  2021-05-14T06:45:24,273 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   final_num_days = max(num_days, 20);
908  2021-05-14T06:45:24,273 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   call symput('numdays',kstrip(put(final_num_days, best32.)));
909  2021-05-14T06:45:24,273 INFO  [00000145] :Bank2BU@SASBAP - MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ACCT_TRANS_VIEW):   run;
910  2021-05-14T06:45:24,273 INFO  [00000145] :Bank2BU@SASBAP - 
911  2021-05-14T06:45:24,277 INFO  [00000145] :Bank2BU@SASBAP - runasofdate: November 02, 2018   
912  2021-05-14T06:45:24,277 INFO  [00000145] :Bank2BU@SASBAP - Start of month: November 01, 2018   
913  2021-05-14T06:45:24,277 INFO  [00000145] :Bank2BU@SASBAP - Days month-to-runasofdate: 2
914  2021-05-14T06:45:24,277 INFO  [00000145] :Bank2BU@SASBAP - NOTE: DATA statement used (Total process time):
915  2021-05-14T06:45:24,277 INFO  [00000145] :Bank2BU@SASBAP -       real time           0.02 seconds
916  2021-05-14T06:45:24,277 INFO  [00000145] :Bank2BU@SASBAP -       cpu time            0.03 
"""


# SASBAP_25212.log
@fixture(scope='function')
def input_case13():
    return """
77  2021-05-14T07:49:39,496 INFO  [00000011] :Bank2BU@SASBAP - 
78  2021-05-14T07:49:39,497 INFO  [00000011] :Bank2BU@SASBAP - SYMBOLGEN:  Macro variable RUNASOFDATE resolves to 20181105
79  2021-05-14T07:49:39,499 INFO  [00000011] :Bank2BU@SASBAP - 29         %put NOTE: FCF: runasofdate=&runasofdate;
80  2021-05-14T07:49:39,499 INFO  [00000011] :Bank2BU@SASBAP - NOTE: FCF: runasofdate=20181105
81  2021-05-14T07:49:39,499 INFO  [00000011] :Bank2BU@SASBAP - 30         
82  2021-05-14T07:49:39,501 INFO  [00000022] :Bank2BU@SASBAP - 31         proc sql;
83  2021-05-14T07:49:39,501 INFO  [00000022] :Bank2BU@SASBAP - 32               update db_kc.fsk_job_calendar set status_ind ='N';
84  2021-05-14T07:49:41,379 INFO  [00000022] :Bank2BU@SASBAP - NOTE: 7304 rows were updated in DB_KC.FSK_JOB_CALENDAR.
85  2021-05-14T07:49:41,379 INFO  [00000022] :Bank2BU@SASBAP - 
86  2021-05-14T07:49:41,385 INFO  [00000022] :Bank2BU@SASBAP - 33         
87  2021-05-14T07:49:41,385 INFO  [00000022] :Bank2BU@SASBAP - 34               update db_kc.fsk_job_calendar set status_ind='Y'
88  2021-05-14T07:49:41,385 INFO  [00000022] :Bank2BU@SASBAP - 35               where datepart(calendar_date) lt "02Nov2018"d;
89  2021-05-14T07:49:41,532 INFO  [00000022] :Bank2BU@SASBAP - NOTE: 305 rows were updated in DB_KC.FSK_JOB_CALENDAR.
90  2021-05-14T07:49:41,532 INFO  [00000022] :Bank2BU@SASBAP - 
91  2021-05-14T07:49:41,537 INFO  [00000022] :Bank2BU@SASBAP - 36         quit;
92  2021-05-14T07:49:41,537 INFO  [00000022] :Bank2BU@SASBAP - NOTE: PROCEDURE SQL used (Total process time):
93  2021-05-14T07:49:41,537 INFO  [00000022] :Bank2BU@SASBAP -       real time           2.03 seconds
94  2021-05-14T07:49:41,537 INFO  [00000022] :Bank2BU@SASBAP -       cpu time            0.73 
"""


# SASBAP_25212.log
@fixture(scope='function')
def input_case14():
    return """
461  2021-05-14T07:50:09,278 INFO  [00000011] :Bank2BU@SASBAP - 
462  2021-05-14T07:50:09,285 INFO  [00000025] :Bank2BU@SASBAP - MPRINT(CLEAR_CORE_KC):   proc sql;
463  2021-05-14T07:50:09,287 INFO  [00000025] :Bank2BU@SASBAP - MPRINT(CLEAR_CORE_KC):   delete from db_kc.FSK_CASH_FLOW_ALERT where FSK_CASH_FLOW_ALERT.ALERT_ID>=0 ;
464  2021-05-14T07:50:09,386 INFO  [00000025] :Bank2BU@SASBAP - NOTE: No rows were deleted from DB_KC.FSK_CASH_FLOW_ALERT.
465  2021-05-14T07:50:09,386 INFO  [00000025] :Bank2BU@SASBAP - 
466  2021-05-14T07:50:09,390 INFO  [00000025] :Bank2BU@SASBAP - MPRINT(CLEAR_CORE_KC):   quit;
467  2021-05-14T07:50:09,390 INFO  [00000025] :Bank2BU@SASBAP - NOTE: PROCEDURE SQL used (Total process time):
468  2021-05-14T07:50:09,390 INFO  [00000025] :Bank2BU@SASBAP -       real time           0.10 seconds
469  2021-05-14T07:50:09,390 INFO  [00000025] :Bank2BU@SASBAP -       cpu time            0.03 
"""


# 2124.log
@fixture(scope='function')
def input_case15():
    return """
1776  2021-05-05T04:37:35,389 INFO  [00000014] :hxdhiraj - 
1777  2021-05-05T04:37:35,389 INFO  [00000014] :hxdhiraj - 164       +
1778  2021-05-05T04:37:35,389 INFO  [00000014] :hxdhiraj - 165       +
1779  2021-05-05T04:37:35,393 INFO  [00000019] :hxdhiraj - 166       +proc sql;
1780  2021-05-05T04:37:35,394 INFO  [00000019] :hxdhiraj - 167       +
1781  2021-05-05T04:37:35,395 INFO  [00000019] :hxdhiraj - 168       +create table work.&SASDATASET as
1782  2021-05-05T04:37:35,395 INFO  [00000019] :hxdhiraj - 169       +  select
1783  2021-05-05T04:37:35,396 INFO  [00000019] :hxdhiraj - 170       +    MonWeekStartDate,
1784  2021-05-05T04:37:35,396 INFO  [00000019] :hxdhiraj - 171       +    CalendarMonthStartDate,
1785  2021-05-05T04:37:35,397 INFO  [00000019] :hxdhiraj - 172       +    ShipToDistributorNbr,
1786  2021-05-05T04:37:35,397 INFO  [00000019] :hxdhiraj - 173       +    OrderableSKUId,
1787  2021-05-05T04:37:35,398 INFO  [00000019] :hxdhiraj - 174       +    ModifyDts,
1788  2021-05-05T04:37:35,398 INFO  [00000019] :hxdhiraj -                                                                                           The SAS System
1789  2021-05-05T04:37:35,398 INFO  [00000019] :hxdhiraj - 
1790  2021-05-05T04:37:35,399 INFO  [00000019] :hxdhiraj - 175       +    BarrelQty
1791  2021-05-05T04:37:35,399 INFO  [00000019] :hxdhiraj - 176       +   from
1792  2021-05-05T04:37:35,399 INFO  [00000019] :hxdhiraj - 177       +     indata.&SASDATASET;
1793  2021-05-05T04:37:44,303 INFO  [00000019] :hxdhiraj - NOTE: Table WORK.STRHISTORYWEEKLY created, with 12507689 rows and 6 columns.
1794  2021-05-05T04:37:44,304 INFO  [00000019] :hxdhiraj - 
1795  2021-05-05T04:37:44,304 INFO  [00000019] :hxdhiraj - 178       +quit;
1796  2021-05-05T04:37:44,305 INFO  [00000019] :hxdhiraj - NOTE: PROCEDURE SQL used (Total process time):
1797  2021-05-05T04:37:44,305 INFO  [00000019] :hxdhiraj -       real time           8.91 seconds
1798  2021-05-05T04:37:44,305 INFO  [00000019] :hxdhiraj -       cpu time            5.50 
"""


# 2124.log
@fixture(scope='function')
def input_case16():
    return """
1800  2021-05-05T04:37:44,306 INFO  [00000014] :hxdhiraj - 
1801  2021-05-05T04:37:44,307 INFO  [00000014] :hxdhiraj - 179       +
1802  2021-05-05T04:37:44,307 INFO  [00000014] :hxdhiraj - 180       +data &_OUTPUT0;
1803  2021-05-05T04:37:44,312 INFO  [00000020] :hxdhiraj - 181       +   set work.&SASDATASET;
1804  2021-05-05T04:37:44,313 INFO  [00000020] :hxdhiraj - 182       +run;
1805  2021-05-05T04:37:44,313 INFO  [00000020] :hxdhiraj - 
1806  2021-05-05T04:37:46,423 INFO  [00000020] :hxdhiraj - NOTE: There were 12507689 observations read from the data set WORK.STRHISTORYWEEKLY.
1807  2021-05-05T04:37:46,424 INFO  [00000020] :hxdhiraj - NOTE: The data set WORK.W17OV4L6I has 12507689 observations and 6 variables.
1808  2021-05-05T04:37:46,425 INFO  [00000020] :hxdhiraj - NOTE: DATA statement used (Total process time):
1809  2021-05-05T04:37:46,425 INFO  [00000020] :hxdhiraj -       real time           2.11 seconds
1810  2021-05-05T04:37:46,425 INFO  [00000020] :hxdhiraj -       cpu time            2.11 
"""


# 2124.log
@fixture(scope='function')
def input_case17():
    return """
2483  2021-05-05T04:37:47,951 INFO  [00000014] :hxdhiraj - 
2484  2021-05-05T04:37:47,951 INFO  [00000014] :hxdhiraj - 758       +
2485  2021-05-05T04:37:47,952 INFO  [00000028] :hxdhiraj - 759       +proc sql;
2486  2021-05-05T04:37:47,953 INFO  [00000028] :hxdhiraj - 760       +   create view work.W3HPGFA3 as
2487  2021-05-05T04:37:47,953 INFO  [00000028] :hxdhiraj - 761       +   select
2488  2021-05-05T04:37:47,954 INFO  [00000028] :hxdhiraj - 762       +      W66KBMFQ.etls_source_row length = 8
2489  2021-05-05T04:37:47,954 INFO  [00000028] :hxdhiraj - 763       +         label = 'The row number in the source table',
2490  2021-05-05T04:37:47,954 INFO  [00000028] :hxdhiraj - 764       +      W66KBMFQ.etls_lookup_table length = 41
2491  2021-05-05T04:37:47,955 INFO  [00000028] :hxdhiraj - 765       +         label = 'The name of the lookup table',
2492  2021-05-05T04:37:47,955 INFO  [00000028] :hxdhiraj - 766       +      W66KBMFQ.etls_exception_cond length = 32
2493  2021-05-05T04:37:47,956 INFO  [00000028] :hxdhiraj - 767       +         label = 'The name of the condition that caused this exception',
2494  2021-05-05T04:37:47,956 INFO  [00000028] :hxdhiraj - 768       +      W66KBMFQ.etls_exception_action length = 32
2495  2021-05-05T04:37:47,956 INFO  [00000028] :hxdhiraj - 769       +         label = 'The name of the action to take for this exception',
2496  2021-05-05T04:37:47,957 INFO  [00000028] :hxdhiraj - 770       +      W66KBMFI.ANALYSIS_ID length = 32,
2497  2021-05-05T04:37:47,957 INFO  [00000028] :hxdhiraj - 771       +      W66KBMFI.TYPE_ID length = 32,
2498  2021-05-05T04:37:47,957 INFO  [00000028] :hxdhiraj - 772       +      W66KBMFI.AFFECTED_TIME_PERIOD_ID length = 32,
2499  2021-05-05T04:37:47,958 INFO  [00000028] :hxdhiraj - 773       +      W66KBMFI.SPLIT_WK_DATE length = 32,
2500  2021-05-05T04:37:47,958 INFO  [00000028] :hxdhiraj - 774       +      W66KBMFI.TIME_SPLIT_WK length = 32,
2501  2021-05-05T04:37:47,958 INFO  [00000028] :hxdhiraj - 775       +      W66KBMFI.SHIPTODIST_ID length = 32,
2502  2021-05-05T04:37:47,959 INFO  [00000028] :hxdhiraj - 776       +      W66KBMFI.OSKU_ID length = 32,
2503  2021-05-05T04:37:47,959 INFO  [00000028] :hxdhiraj - 777       +      W66KBMFI.GL_ACCOUT_ID length = 32,
2504  2021-05-05T04:37:47,959 INFO  [00000028] :hxdhiraj - 778       +      W66KBMFI.TRANSACTION_DT length = 8
2505  2021-05-05T04:37:47,959 INFO  [00000028] :hxdhiraj - 779       +         format = DATE9.
2506  2021-05-05T04:37:47,960 INFO  [00000028] :hxdhiraj - 780       +         informat = DATE9.
2507  2021-05-05T04:37:47,960 INFO  [00000028] :hxdhiraj - 781       +         label = 'Transaction Date',
2508  2021-05-05T04:37:47,960 INFO  [00000028] :hxdhiraj -                                                                                           The SAS System
2509  2021-05-05T04:37:47,961 INFO  [00000028] :hxdhiraj - 
2510  2021-05-05T04:37:47,961 INFO  [00000028] :hxdhiraj - 782       +      W66KBMFI.TRANSACTION_AMT length = 8
2511  2021-05-05T04:37:47,961 INFO  [00000028] :hxdhiraj - 783       +   from
2512  2021-05-05T04:37:47,962 INFO  [00000028] :hxdhiraj - 784       +      work.W66KBMFI,
2513  2021-05-05T04:37:47,962 INFO  [00000028] :hxdhiraj - 785       +      work.W66KBMFQ
2514  2021-05-05T04:37:47,962 INFO  [00000028] :hxdhiraj - 786       +   where
2515  2021-05-05T04:37:47,963 INFO  [00000028] :hxdhiraj - 787       +      W66KBMFI.etls_source_row = W66KBMFQ.etls_source_row
2516  2021-05-05T04:37:47,963 INFO  [00000028] :hxdhiraj - 788       +   ;
2517  2021-05-05T04:37:47,965 INFO  [00000028] :hxdhiraj - NOTE: SQL view WORK.W3HPGFA3 has been defined.
2518  2021-05-05T04:37:47,965 INFO  [00000028] :hxdhiraj - 789       +quit;
2519  2021-05-05T04:37:47,966 INFO  [00000028] :hxdhiraj - NOTE: PROCEDURE SQL used (Total process time):
2520  2021-05-05T04:37:47,966 INFO  [00000028] :hxdhiraj -       real time           0.01 seconds
2521  2021-05-05T04:37:47,966 INFO  [00000028] :hxdhiraj -       cpu time            0.01 
"""


# 2124.log
@fixture(scope='function')
def input_case18():
    return """
2564  2021-05-05T04:37:47,982 INFO  [00000014] :hxdhiraj - 
2565  2021-05-05T04:37:47,982 INFO  [00000014] :hxdhiraj - 823       +
2566  2021-05-05T04:37:47,983 INFO  [00000014] :hxdhiraj - 824       +%put %str(NOTE: Mapping columns ...);
2567  2021-05-05T04:37:47,983 INFO  [00000014] :hxdhiraj - NOTE: Mapping columns ...
2568  2021-05-05T04:37:47,984 INFO  [00000030] :hxdhiraj - 825       +proc sql;
2569  2021-05-05T04:37:47,985 INFO  [00000030] :hxdhiraj - 826       +   create view work.W5D32RTX as
2570  2021-05-05T04:37:47,985 INFO  [00000030] :hxdhiraj - 827       +      select
2571  2021-05-05T04:37:47,986 INFO  [00000030] :hxdhiraj - 828       +         SHIPTODIST_ID,
2572  2021-05-05T04:37:47,986 INFO  [00000030] :hxdhiraj - 829       +         OSKU_ID
2573  2021-05-05T04:37:47,986 INFO  [00000030] :hxdhiraj - 830       +   from &SYSLAST
2574  2021-05-05T04:37:47,987 INFO  [00000030] :hxdhiraj - 831       +      where etls_lookup_table = 'IncomFM.GEOBRANDSUP_LKUP'
2575  2021-05-05T04:37:47,987 INFO  [00000030] :hxdhiraj - 832       +   order by
2576  2021-05-05T04:37:47,988 INFO  [00000030] :hxdhiraj - 833       +      SHIPTODIST_ID,
2577  2021-05-05T04:37:47,988 INFO  [00000030] :hxdhiraj - 834       +      OSKU_ID
2578  2021-05-05T04:37:47,988 INFO  [00000030] :hxdhiraj - 835       +   ;
2579  2021-05-05T04:37:47,990 INFO  [00000030] :hxdhiraj - NOTE: SQL view WORK.W5D32RTX has been defined.
2580  2021-05-05T04:37:47,990 INFO  [00000030] :hxdhiraj - 836       +quit;
2581  2021-05-05T04:37:47,991 INFO  [00000030] :hxdhiraj - NOTE: PROCEDURE SQL used (Total process time):
2582  2021-05-05T04:37:47,991 INFO  [00000030] :hxdhiraj -       real time           0.00 seconds
2583  2021-05-05T04:37:47,992 INFO  [00000030] :hxdhiraj -       cpu time            0.01 
"""


# 2124.log
@fixture(scope='function')
def input_case19():
    return """
2697  2021-05-05T04:37:48,031 INFO  [00000014] :hxdhiraj - 
2698  2021-05-05T04:37:48,031 INFO  [00000014] :hxdhiraj - 925       +
2699  2021-05-05T04:37:48,035 INFO  [00000034] :hxdhiraj - 926       +data _null_;
2700  2021-05-05T04:37:48,035 INFO  [00000034] :hxdhiraj - 927       +   put "NOTE: The following column(s) do not have a column mapping, so the"
2701  2021-05-05T04:37:48,036 INFO  [00000034] :hxdhiraj - 928       +        " value(s) will be set to missing: GeoBrandSup_ID, GeoBrandSupplier";
2702  2021-05-05T04:37:48,036 INFO  [00000034] :hxdhiraj - 929       +run;
2703  2021-05-05T04:37:48,036 INFO  [00000034] :hxdhiraj - 
2704  2021-05-05T04:37:48,037 INFO  [00000034] :hxdhiraj - NOTE: DATA statement used (Total process time):
2705  2021-05-05T04:37:48,037 INFO  [00000034] :hxdhiraj -       real time           0.00 seconds
2706  2021-05-05T04:37:48,037 INFO  [00000034] :hxdhiraj -       cpu time            0.00 
"""


# 2124.log
@fixture(scope='function')
def input_case20():
    return """
3010  2021-05-05T04:37:48,184 INFO  [00000014] :hxdhiraj - 
3011  2021-05-05T04:37:48,188 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   data _null_;
3012  2021-05-05T04:37:48,189 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   putlog
3013  2021-05-05T04:37:48,190 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   "NOTE: DATA VALIDATION SUMMARY: Total rows - SOURCE = 0";
3014  2021-05-05T04:37:48,190 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   putlog
3015  2021-05-05T04:37:48,191 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   "NOTE: DATA VALIDATION SUMMARY: Total rows - VALID RECORDS = 0";
3016  2021-05-05T04:37:48,191 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   putlog
3017  2021-05-05T04:37:48,191 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   "NOTE: DATA VALIDATION SUMMARY: Total rows - ERROR = 0";
3018  2021-05-05T04:37:48,191 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   putlog
3019  2021-05-05T04:37:48,192 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   "NOTE: DATA VALIDATION SUMMARY: Total rows - EXCEPTION = 0";
3020  2021-05-05T04:37:48,192 INFO  [00000040] :hxdhiraj - MPRINT(ETLS_VALIDATE):   run;
3021  2021-05-05T04:37:48,192 INFO  [00000040] :hxdhiraj - 
3022  2021-05-05T04:37:48,193 INFO  [00000040] :hxdhiraj - NOTE: DATA statement used (Total process time):
3023  2021-05-05T04:37:48,193 INFO  [00000040] :hxdhiraj -       real time           0.00 seconds
3024  2021-05-05T04:37:48,193 INFO  [00000040] :hxdhiraj -       cpu time            0.02
"""


# 2124.log
@fixture(scope='function')
def input_case21():
    return """
3026  2021-05-05T04:37:48,194 INFO  [00000014] :hxdhiraj - 
3027  2021-05-05T04:37:48,196 INFO  [00000041] :hxdhiraj - MPRINT(ETLS_VALIDATE):   proc append base=work.WA6LR3AU data=etls_target force;
3028  2021-05-05T04:37:48,196 INFO  [00000041] :hxdhiraj -                                                                                           The SAS System
3029  2021-05-05T04:37:48,196 INFO  [00000041] :hxdhiraj - 
3030  2021-05-05T04:37:48,196 INFO  [00000041] :hxdhiraj - MPRINT(ETLS_VALIDATE):   run;
3031  2021-05-05T04:37:48,197 INFO  [00000041] :hxdhiraj - 
3032  2021-05-05T04:37:48,197 INFO  [00000041] :hxdhiraj - NOTE: The data set WORK.WA6LR3AU has 0 observations and 0 variables.
3033  2021-05-05T04:37:48,198 INFO  [00000041] :hxdhiraj - NOTE: PROCEDURE APPEND used (Total process time):
3034  2021-05-05T04:37:48,198 INFO  [00000041] :hxdhiraj -       real time           0.00 seconds
3035  2021-05-05T04:37:48,198 INFO  [00000041] :hxdhiraj -       cpu time            0.00 
"""


# 2124.log
@fixture(scope='function')
def input_case22():
    return """
3056  2021-05-05T04:37:48,207 INFO  [00000014] :hxdhiraj - 
3057  2021-05-05T04:37:48,208 INFO  [00000044] :hxdhiraj - MPRINT(ETLS_VALIDATE):   proc datasets library=work memtype=(data view) nolist nowarn;
3058  2021-05-05T04:37:48,209 INFO  [00000044] :hxdhiraj - MPRINT(ETLS_VALIDATE):   delete etls_Source;
3059  2021-05-05T04:37:48,209 INFO  [00000044] :hxdhiraj - MPRINT(ETLS_VALIDATE):   quit;
3060  2021-05-05T04:37:48,209 INFO  [00000044] :hxdhiraj - 
3061  2021-05-05T04:37:48,210 INFO  [00000044] :hxdhiraj - NOTE: PROCEDURE DATASETS used (Total process time):
3062  2021-05-05T04:37:48,210 INFO  [00000044] :hxdhiraj -       real time           0.00 seconds
3063  2021-05-05T04:37:48,210 INFO  [00000044] :hxdhiraj -       cpu time            0.00 
"""


# 2124.log
@fixture(scope='function')
def input_case23():
    return """
3285  2021-05-05T04:37:48,276 INFO  [00000014] :hxdhiraj - 
3286  2021-05-05T04:37:48,276 INFO  [00000014] :hxdhiraj - NOTE: Mapping columns ...
3287  2021-05-05T04:37:48,277 INFO  [00000046] :hxdhiraj - MPRINT(ETLS_LOADER):   proc sql;
3288  2021-05-05T04:37:48,278 INFO  [00000046] :hxdhiraj - MPRINT(ETLS_LOADER):   create view work.WUTZHY5 as select MarketCountryCd as Country_Code length = 32 format = $32. informat = $32., (SUBSTR(TrademarkBrandFamilyName,1,32)) as Brand_Family 
3289  2021-05-05T04:37:48,278 INFO  [00000046] :hxdhiraj - length = 32 format = $32. informat = $32., GeoBrandSup_ID, GeoBrandSupplier from WORK.WA6LR3AU ;
3290  2021-05-05T04:37:48,279 INFO  [00000046] :hxdhiraj - NOTE: SQL view WORK.WUTZHY5 has been defined.
3291  2021-05-05T04:37:48,280 INFO  [00000046] :hxdhiraj - MPRINT(ETLS_LOADER):   quit;
3292  2021-05-05T04:37:48,280 INFO  [00000046] :hxdhiraj - NOTE: PROCEDURE SQL used (Total process time):
3293  2021-05-05T04:37:48,280 INFO  [00000046] :hxdhiraj -       real time           0.00 seconds
3294  2021-05-05T04:37:48,281 INFO  [00000046] :hxdhiraj -       cpu time            0.00 
"""


# 2124.log
@fixture(scope='function')
def input_case24():
    return """
3507  2021-05-05T04:37:48,396 INFO  [00000014] :hxdhiraj - 
3508  2021-05-05T04:37:48,396 INFO  [00000014] :hxdhiraj -                                                                                           The SAS System
3509  2021-05-05T04:37:48,397 INFO  [00000014] :hxdhiraj - 
3510  2021-05-05T04:37:48,397 INFO  [00000014] :hxdhiraj - MPRINT(MAILCHK):  ;
3511  2021-05-05T04:37:48,397 INFO  [00000014] :hxdhiraj - 1351      +
3512  2021-05-05T04:37:48,398 INFO  [00000014] :hxdhiraj - 1352      +/*append us records to DmdMgt.GEOBRANDSUPPLIERMAP*/
3513  2021-05-05T04:37:48,401 INFO  [00000061] :hxdhiraj - 1353      +data work.USGEOBRANDSUPADDS;
3514  2021-05-05T04:37:48,401 INFO  [00000061] :hxdhiraj - 1354      +set DmdMgt.GEOBRANDSUPADDS(where=(country_code='US'));
3515  2021-05-05T04:37:48,401 INFO  [00000061] :hxdhiraj - 1355      +run;
3516  2021-05-05T04:37:48,401 INFO  [00000061] :hxdhiraj - 
3517  2021-05-05T04:37:48,402 INFO  [00000061] :hxdhiraj - NOTE: The data set WORK.USGEOBRANDSUPADDS has 0 observations and 4 variables.
3518  2021-05-05T04:37:48,403 INFO  [00000061] :hxdhiraj - NOTE: DATA statement used (Total process time):
3519  2021-05-05T04:37:48,403 INFO  [00000061] :hxdhiraj -       real time           0.00 seconds
3520  2021-05-05T04:37:48,404 INFO  [00000061] :hxdhiraj -       cpu time            0.01 
"""
