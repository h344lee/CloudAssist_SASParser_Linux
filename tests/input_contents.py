from pytest import fixture


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


@fixture(scope='function')
def input_case10():
    return """
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


