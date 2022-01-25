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