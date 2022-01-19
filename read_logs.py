import os
import re
import logging
import pandas as pd

logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.info('start of the program')


def init_proc_cat_prod(cat_prod_dict):
    cat_prod_dict["ACECLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ADAPTIVEREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["AGGREGATION"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["ALLELE"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["ANOM"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["ANOVA"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["APPEND"] = ("Base SAS", "Data Management")
    cat_prod_dict["APPSRV"] = ("SAS/IntrNet", "SAS ENV")
    cat_prod_dict["ARIMA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["AUTHLIB"] = ("Base SAS", "Data Management")
    cat_prod_dict["AUTOREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["BCHOICE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BGLIMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BINNING"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["BLIMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BMDP"] = ("Base SAS", "Data Management")
    cat_prod_dict["BOM"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["BOXPLOT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BOXPLOT"] = ("SAS/STAT", "Advanced Analytics")
    cat_prod_dict["BTL"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["BUILD"] = ("SAS/AF", "SAS ENV")
    cat_prod_dict["CALENDAR"] = ("Base SAS", "Data Management")
    cat_prod_dict["CALIS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CALLRFC"] = ("Base SAS", "Data Management")
    cat_prod_dict["CANCORR"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CANDISC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAPABILITY"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["CARDINALITY"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["CARIMA"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CASECONTROL"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["CATALOG"] = ("Base SAS", "Data Management")
    cat_prod_dict["CATMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAUSALGRAPH"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAUSALMED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAUSALTRT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CCDM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CCOPULA"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CDISC"] = ("Base SAS", "Data Management")
    cat_prod_dict["CESM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CHART"] = ("Base SAS", "Reporting")
    cat_prod_dict["CIMPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["CLP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["CLUSTER"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CNTSELECT"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["COMPARE"] = ("Base SAS", "Data Management")
    cat_prod_dict["COMPILE"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["COMPUTAB"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["CONTENTS"] = ("Base SAS", "Data Management")
    cat_prod_dict["CONVERT"] = ("Base SAS", "Data Management")
    cat_prod_dict["COPULA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["COPY"] = ("Base SAS", "Data Management")
    cat_prod_dict["CORR"] = ("Base SAS", "Data Management")
    cat_prod_dict["CORRELATION"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["CORRESP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["COUNTREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["CPANEL"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CPM"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["CPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["CQLIM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CSPATIALREG"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CUSUM"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["CV2VIEW"] = ("Base SAS", "Data Management")
    cat_prod_dict["DATASETS"] = ("Base SAS", "Data Management")
    cat_prod_dict["DATASOURCE"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["DATEKEYS"] = ("Base SAS", "Data Management")
    cat_prod_dict["DB2EXT"] = ("Base SAS", "Data Management")
    cat_prod_dict["DB2UTIL"] = ("Base SAS", "Data Management")
    cat_prod_dict["DBCSTAB"] = ("Base SAS", "Data Management")
    cat_prod_dict["DBF"] = ("Base SAS", "Data Management")
    cat_prod_dict["DBLOAD"] = ("Base SAS", "Data Management")
    cat_prod_dict["DCBSTAB"] = ("Base SAS", "Data Management")
    cat_prod_dict["DELETE"] = ("Base SAS", "Data Management")
    cat_prod_dict["DIF"] = ("Base SAS", "Data Management")
    cat_prod_dict["DISCRIM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["DISPLAY"] = ("Base SAS", "Data Management")
    cat_prod_dict["DISTANCE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["DISTANCE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["DMSRVADM"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DMSRVDATASVC"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DMSRVPROCESSSVC"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DMSSRVPROCESSSVC"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DOCPARSE"] = ("SAS Text Miner", "Analytics")
    cat_prod_dict["DOCUMENT"] = ("Base SAS", "Data Management")
    cat_prod_dict["DOWNLOAD"] = ("SAS/CONNECT", "SAS ENV")
    cat_prod_dict["DQLOCLST"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DQMATCH"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DQSCHEME"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DS2"] = ("Base SAS", "Advanced Data Management")
    cat_prod_dict["DSTODS2"] = ("Base SAS", "Data Management")
    cat_prod_dict["DTREE"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["ECM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["ENTROPY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["ESM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["EXPAND"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["EXPLODE"] = ("Base SAS", "Data Management")
    cat_prod_dict["EXPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["FACTEX"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["FACTOR"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FAMILY"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["FASTCLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FCMP"] = ("Base SAS", "Data Management")
    cat_prod_dict["FEDSQL"] = ("Base SAS", "Data Management")
    cat_prod_dict["FMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FONTREG"] = ("Base SAS", "Data Management")
    cat_prod_dict["FORECAST"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["FORMAT"] = ("Base SAS", "Data Management")
    cat_prod_dict["FORMS"] = ("Base SAS", "Data Management")
    cat_prod_dict["FREQ"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FREQTAB"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["FSBROWSE"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["FSEDIT"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["FSLETTER"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["FSLIST"] = ("Base SAS", "Data Management")
    cat_prod_dict["FSVIEW"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["G3D"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["G3GRID"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GA"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["GAM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GAMMOD"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["GAMPL"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GAMSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["GANNO"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GANTT"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["GAREABAR"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GBARLINE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GCHART"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GCONTOUR"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GDEVICE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GEE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GENESELECT"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["GENMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GEOCODE"] = ("Base SAS", "Reporting")
    cat_prod_dict["GFONT"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GINSIDE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GIS"] = ("SAS/GIS", "Advanced Analytics")
    cat_prod_dict["GKPI"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GLIMMIX"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLMMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLMPOWER"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLMSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GMAP"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GOPTIONS"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GPLOT"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GPROJECT"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GRADAR"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GREDUCE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GREMOVE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GREPLAY"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GROOVY"] = ("Base SAS", "Data Management")
    cat_prod_dict["GSLIDE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GTILE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["HADOOP"] = ("Base SAS", "Data Management")
    cat_prod_dict["HAPLOTYPE"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["HDMD"] = ("Base SAS", "Data Management")
    cat_prod_dict["HP4SCORE"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPBIN"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPBNET"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPBOOLRULE"] = ("SAS Text Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPCANDISC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPCDM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPCLUS"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPCOPULA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPCORR"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPCOUNTREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPDECIDE"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPDMDB"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPDS2"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPEXPORT"] = ("SAS High-Performance Risk", "Advanced Analytics")
    cat_prod_dict["HPF"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFARIMASPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFDIAGNOSE"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFENGINE"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFESMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFEVENTS"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFEXMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFIDMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPFOREST"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPFRECONCILE"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFREPOSITORY"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFSELECT"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFTEMPRECON"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFUCMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPGENSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPIMPUTE"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPLMIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPLOGISTIC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPMIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPNEURAL"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPNLMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPPANEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPPLS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPPRINCOMP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPQLIM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPQUANTSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPREDUCE"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPRISK"] = ("SAS High-Performance Risk", "Advanced Analytics")
    cat_prod_dict["HPSAMPLE"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPSEVERITY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPSPLIT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPSUMMARY"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPSVM"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPTMINE"] = ("SAS Text Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPTMSCORE"] = ("SAS Text Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HTSNP"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["HTTP"] = ("Base SAS", "Data Management")
    cat_prod_dict["ICA"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["ICLIFETEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ICPHREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["IML"] = ("SAS/IML", "Advanced Analytics")
    cat_prod_dict["IMPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["IMSTAT"] = ("SAS LASR Analytic Server", "Advanced Data Management")
    cat_prod_dict["IMXFER"] = ("SAS LASR Analytic Server", "Advanced Data Management")
    cat_prod_dict["INBREED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["INFOMAPS"] = ("Base SAS", "Reporting")
    cat_prod_dict["IOMOPERATE"] = ("SAS Integration Technologies", "SAS ENV")
    cat_prod_dict["IRT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ISHIKAWA"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["ITEMS"] = ("Base SAS", "Data Management")
    cat_prod_dict["JAVAINFO"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["JSON"] = ("Base SAS", "Data Management")
    cat_prod_dict["KCLUS"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["KDE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["KRIGE2D"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LASR"] = ("SAS LASR Analytic Server", "Advanced Analytics")
    cat_prod_dict["LATTICE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LIFEREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LIFETEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LMIXED"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["LOAN"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["LOCALEDATA"] = ("Base SAS", "Data Management")
    cat_prod_dict["LOESS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LOGISTIC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LOGSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["LUA"] = ("Base SAS", "Data Management")
    cat_prod_dict["MACONTROL"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["MAPIMPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["MBC"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["MCMC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MDC"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["MDDB"] = ("SAS/MDDB Server", "Reporting")
    cat_prod_dict["MDS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MEANS"] = ("Base SAS", "Analytics")
    cat_prod_dict["METADATA"] = ("Base SAS", "Data Management")
    cat_prod_dict["METALIB"] = ("Base SAS", "Data Management")
    cat_prod_dict["METAOPERATE"] = ("Base SAS", "Data Management")
    cat_prod_dict["MI"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MIANALYZE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MIGRATE"] = ("Base SAS", "Data Management")
    cat_prod_dict["MIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MODECLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MODEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["MODELMATRIX"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["MULTTEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MVPDIAGNOSE"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["MVPMODEL"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["MVPMONITOR"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["NESTED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["NETDRAW"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["NLIN"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["NLMIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["NLMOD"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["NMF"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["NPAR1WAY"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ODSLIST"] = ("Base SAS", "Reporting")
    cat_prod_dict["ODSTABLE"] = ("Base SAS", "Reporting")
    cat_prod_dict["ODSTEXT"] = ("Base SAS", "Reporting")
    cat_prod_dict["OLAP"] = ("SAS OLAP Server", "Reporting")
    cat_prod_dict["OLAPCONTENTS"] = ("SAS OLAP Server", "Reporting")
    cat_prod_dict["OLAPOPERATE"] = ("SAS OLAP Server", "Reporting")
    cat_prod_dict["OPERATE"] = ("SAS/SHARE", "SAS ENV")
    cat_prod_dict["OPTEX"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["OPTGRAPH"] = ("SAS OPTGRAPH Procedure", "Advanced Analytics")
    cat_prod_dict["OPTIONS"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["OPTLOAD"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["OPTLP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTLSO"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["OPTMILP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTMODEL"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTNET"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["OPTNETWORK"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTQP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTSAVE"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["ORTHOREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PANEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["PARETO"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["PARTITION"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PCA"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PDLREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["PDS"] = ("Base SAS", "Data Management")
    cat_prod_dict["PDSCOPY"] = ("Base SAS", "Data Management")
    cat_prod_dict["PHREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PHSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PLAN"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PLM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PLOT"] = ("Base SAS", "Data Management")
    cat_prod_dict["PLS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PLSMOD"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PM"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["PMENU"] = ("Base SAS", "Data Management")
    cat_prod_dict["POWER"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRESENV"] = ("Base SAS", "Data Management")
    cat_prod_dict["PRINCOMP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRINQUAL"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRINT"] = ("Base SAS", "Reporting")
    cat_prod_dict["PRINTTO"] = ("Base SAS", "Reporting")
    cat_prod_dict["PROBIT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRODUCT_STATUS"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["PROTO"] = ("Base SAS", "Data Management")
    cat_prod_dict["PRTDEF"] = ("Base SAS", "Data Management")
    cat_prod_dict["PRTEXP"] = ("Base SAS", "Data Management")
    cat_prod_dict["PSMATCH"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PSMOOTH"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["PWENCODE"] = ("Base SAS", "Data Management")
    cat_prod_dict["QDEVICE"] = ("Base SAS", "Data Management")
    cat_prod_dict["QLIM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["QTRSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["QUANTLIFE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["QUANTREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["QUANTSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["QUEST"] = ("SAS/ACCESS", "Data Management")
    cat_prod_dict["RANK"] = ("Base SAS", "Data Management")
    cat_prod_dict["RAREEVENTS"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["RDC"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RDPOOL"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RDSEC"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RECOMMEND"] = ("SAS LASR Analytic Server", "Advanced Analytics")
    cat_prod_dict["REG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["REGISTRY"] = ("Base SAS", "Data Management")
    cat_prod_dict["REGSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["RELEASE"] = ("Base SAS", "Data Management")
    cat_prod_dict["RELIABILITY"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["REPORT"] = ("Base SAS", "Reporting")
    cat_prod_dict["RISK"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RMSTREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ROBUSTREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["RSREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["S3"] = ("Base SAS", "Data Management")
    cat_prod_dict["SANDWICH"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["SCA"] = ("Base SAS", "Data Management")
    cat_prod_dict["SCAPROC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SCORE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SCOREACCEL"] = ("Base SAS", "Analytics")
    cat_prod_dict["SEQDESIGN"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SEQTEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SERVER"] = ("SAS/SHARE", "SAS ENV")
    cat_prod_dict["SEVERITY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SEVSELECT"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["SGDESIGN"] = ("Base SAS", "Analytics")
    cat_prod_dict["SGMAP"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGPANEL"] = ("Base SAS", "Analytics")
    cat_prod_dict["SGPIE"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGPLOT"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGRENDER"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGSCATTER"] = ("Base SAS", "Reporting")
    cat_prod_dict["SHEWHART"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["SIM2D"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SIMILARITY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SIMLIN"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SIMNORMAL"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SIMSYSTEM"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["SOAP"] = ("Base SAS", "Data Management")
    cat_prod_dict["SORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["SOURCE"] = ("Base SAS", "Data Management")
    cat_prod_dict["SPATIALREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SPC"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["SPDO"] = ("SAS Scalable Performance Data Server", "Data Management")
    cat_prod_dict["SPECTRA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SPP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SQL"] = ("Base SAS", "Data Management")
    cat_prod_dict["SQOOP"] = ("Base SAS", "Data Management")
    cat_prod_dict["SSM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["STANDARD"] = ("Base SAS", "Data Management")
    cat_prod_dict["STATESPACE"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["STDIZE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["STDRATE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["STEPDISC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["STP"] = ("SAS Integration Technologies", "SAS ENV")
    cat_prod_dict["STREAM"] = ("Base SAS", "Data Management")
    cat_prod_dict["SUMMARY"] = ("Base SAS", "Analytics")
    cat_prod_dict["SURVEYFREQ"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYIMPUTE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYLOGISTIC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYMEANS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYPHREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SYSLIN"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TABULATE"] = ("Base SAS", "Reporting")
    cat_prod_dict["TAPECOPY"] = ("Base SAS", "Data Management")
    cat_prod_dict["TAPELABEL"] = ("Base SAS", "Data Management")
    cat_prod_dict["TEMPLATE"] = ("Base SAS", "Data Management")
    cat_prod_dict["TIMEDATA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TIMEID"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TIMEPLOT"] = ("Base SAS", "Analytics")
    cat_prod_dict["TIMESERIES"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TMODEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TPSPLINE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["TRANSPOSE"] = ("Base SAS", "Analytics")
    cat_prod_dict["TRANSREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["TRANTAB"] = ("Base SAS", "Data Management")
    cat_prod_dict["TREE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["TREESPLIT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["TSCSREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TTEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["UCM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["UNIVARIATE"] = ("Base SAS", "Analytics")
    cat_prod_dict["UPLOAD"] = ("SAS/CONNECT", "SAS ENV")
    cat_prod_dict["VARCLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["VARCOMP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["VARIMPUTE"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["VARIOGRAM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["VARMAX"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["VARREDUCE"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["VASMP"] = ("SAS LASR Analytic Server", "Advanced Analytics")
    cat_prod_dict["X11"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["X12"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["X13"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["XSL"] = ("Base SAS", "Data Management")

    # proc_df = pd.read_excel('proc.xls')
    # proc_list = proc_df.values.tolist()
    #
    # for step, proc, prod in proc_list:
    #     print('cat_prod_dict["' + step.encode('utf-8', 'ignore').strip() + '"]=("' + proc.encode('utf-8',
    #     'ignore').strip() + '", "' + prod.encode('utf-8', 'ignore').strip() + '")')

    return cat_prod_dict


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

    # with open("output\\chunk1.txt", 'w') as text_file:
    #      text_file.write(temp_chunk)
    # test_counter = 2

    temp_chunk = ""
    for sas_content in sas_content_list[1:]:
        line_number_regex = re.compile(r"\n\d\d\d\d-\d\d-.* - (\d+) ")
        line_number_regex_obj = line_number_regex.search(sas_content)
        start_line_number = int(line_number_regex_obj.group(1))

        for line in sas_content.splitlines(True):
            temp_chunk += str(start_line_number - 1) + "  " + line
            start_line_number += 1
        sas_content_numbered_list.append(temp_chunk)

        # with open('output\\chunk' + str(test_counter) + '.txt', 'w') as text_file:
        #     text_file.write(temp_chunk)
        # test_counter += 1

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

    return float(cpu_time), float(real_time)


# get output library and output table from regular log message such as NOTE: ~~
# return output library and output table
# completed for the regular log message
# comment: need to enhance to get information from actual sql query
def get_output_library_table(sas_file_content):
    output_lib_table_regex_1 = re.compile(r"NOTE: The data set (.*)\.(.*) has \d+ observations and \d+ "
                                          r"variables.")
    output_lib_table_list_1 = output_lib_table_regex_1.findall(sas_file_content)

    output_lib_table_regex_2 = re.compile(r"NOTE: SQL view (.*)\.(.*) has been defined.")
    output_lib_table_list_2 = output_lib_table_regex_2.findall(sas_file_content)

    output_lib_table_list = output_lib_table_list_1 + output_lib_table_list_2

    output_lib = ''
    output_table = ''

    if len(output_lib_table_list) != 0:
        for idx, record in enumerate(output_lib_table_list):
            if idx == 0:
                output_lib += record[0]
                output_table += record[1]
            else:
                output_lib += ';' + record[0]
                output_table += ';' + record[1]

    return output_lib, output_table


# get input library and input table from regular log output such as NOTE: ~
# return input_lib, input_table as string
# Need to enhance to process actual query based process.
def get_input_library_table(sas_file_content):
    input_lib_table_regex = re.compile(r"NOTE: There were \d+ observations read from the data set (.*)\.(.*).")
    input_lib_table_list = input_lib_table_regex.findall(sas_file_content)

    input_lib = ''
    input_table = ''

    if len(input_lib_table_list) != 0:
        for idx, record in enumerate(input_lib_table_list):
            if idx == 0:
                input_lib += record[0]
                input_table += record[1]
            else:
                input_lib += ';' + record[0]
                input_table += ';' + record[1]

    return input_lib, input_table

    # if input_lib_table_regex_obj is not None:
    #     input_lib = input_lib_table_regex_obj.group(2)
    #     input_table = input_lib_table_regex_obj.group(3)
    #     # print(input_lib)
    #     # print(input_table)
    # else:
    #     input_lib = ''
    #     input_table = ''
    #
    # return input_lib, input_table


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


def proc_sql_parsing(record_content):
    proc_sql_regex = re.compile(r"(.*proc sql)(.+)((?:\n.+)+)(quit|run)", re.MULTILINE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)

    if len(proc_sql_regex_list) != 0:
        # print(proc_sql_regex_list[0])
        # print(proc_sql_regex_list[0][1])
        # print(proc_sql_regex_list[0][2])

        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)
        print(proc_sql)


def get_proc_sql(sql_block):
    # +proc sql case: hiragana - 874       +proc sql;
    sql_block_regex = re.compile(r"(.* - \d+ \s+\+)(.*)")
    sql_lines = ""
    for sql_block_line in sql_block.splitlines():
        if 'connect to' in sql_block_line:
            sql_lines = 'pass through'
            break
        filtered_line = sql_block_regex.findall(sql_block_line)
        # print(filtered_line)
        if len(filtered_line) == 1 and len(filtered_line[0]) == 2 and filtered_line[0][1] != '':
            sql_lines += filtered_line[0][1].strip() + " "

    # MPRINT proc sql case: MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ASC_TRANS_VIEW):   proc sql noprint;
    if sql_lines == "":
        proc_sql_mprint_regex = re.compile(r"(MPRINT\(.*\)\:)(.+)((?:\n.+)+)(NOTE|quit)", re.MULTILINE)
        proc_sql_mprint_regex_list = proc_sql_mprint_regex.findall(sql_block)
        if len(proc_sql_mprint_regex_list) >= 1:
            sql_lines = proc_sql_mprint_regex_list[0][1].strip() + " "

            mprint_regex = re.compile(r".* - MPRINT\(.*\)\:\s+(.*)")
            general_regex = re.compile(r".* - (.*)")

            mprint_block = proc_sql_mprint_regex_list[0][2]
            for mprint_block_line in mprint_block.splitlines():

                if 'connect to' in mprint_block_line:
                    sql_lines = 'pass through'
                    break

                if re.match(mprint_regex, mprint_block_line) is not None:
                    mprint_block_line_list = mprint_regex.findall(mprint_block_line)
                else:
                    mprint_block_line_list = general_regex.findall(mprint_block_line)
                # print(mprint_block_line_list)
                if len(mprint_block_line_list) == 1 and mprint_block_line_list != '' and mprint_block_line_list[0][:4] != 'NOTE' and mprint_block_line_list[0][:4] != 'SYMB':
                    sql_lines += mprint_block_line_list[0]

    # number proc sql case: Bank2BU@SASBAP - 31         proc sql
    if sql_lines == "":

        proc_sql_num_regex = re.compile(r".* - \d+\s+(.*)")
        for sql_block_line in sql_block.splitlines():
            if 'connect to' in sql_block_line:
                sql_lines = 'pass through'
                break
            filtered_line = proc_sql_num_regex.findall(sql_block_line)

            if len(filtered_line) == 1 and filtered_line[0] != '':
                sql_lines += filtered_line[0].strip() + " "

    return sql_lines


# update a row of record to the given dataframe 'log_df'
def save_record_to_df(log_df, extracted_record):
    updated_log_df = log_df.append(pd.Series(extracted_record, index=log_df.columns), ignore_index=True)
    return updated_log_df


# save the dataframe to an excel file
def save_df_to_xlsx(log_df):
    # check "\output" folder and make it if it is not exist
    if not os.path.isdir('output'):
        os.makedirs('output')
    log_df.to_excel("output\\output.xlsx", float_format="%0.2f", index=False)


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
    # ==========================
    FILE_SAS_PROC_CAT = ""
    FILE_SAS_PROC_PROD = ""
    FILE_SAS_MIGR_DISP = ""
    FILE_SAS_MIGR_RUL_ID = ""
    FILE_SAS_MIGR_REC_ACT = ""
    FILE_SAS_PROC_INMEM_FLG = 0
    FILE_SAS_PROC_ELT_FLG = 0
    FILE_SAS_PROC_GRID_FLG = 0
    FILE_SAS_PROC_INDB_FLG = 0
    FILE_SAS_SRC_TYP = "SAS"
    FILE_SAS_ENV_NAME = "SAS GRID PROD"

    log_df = pd.DataFrame(columns=['FILE_ID', 'FILE_PTH', 'FILE_NM', 'FILE_USR_NM', 'FILE_SAS_F_ID',
                                   'FILE_SAS_F_LOC', 'FILE_SAS_F_NM', 'FILE_SAS_STP',
                                   'FILE_SAS_STP_NM', 'FILE_LN_NUM', 'FILE_SAS_INP_LIB',
                                   'FILE_SAS_INP_TBL', 'FILE_SAS_INP_FIL_NM', 'FILE_SAS_INP_ROW_RD',
                                   'FILE_SAS_OUT_LIB', 'FILE_SAS_OUT_TBL', 'FILE_SAS_ROW_WRT',
                                   'FILE_SAS_INP_MUL_FLG', 'FILE_SAS_INP_MUL_TBLS', 'FILE_EXC_DT',
                                   'FILE_SAS_EXC_TM', 'FILE_SAS_EXC_CPU_TM', 'FILE_SAS_EXC_RL_TM',
                                   'FILE_SAS_PROC_CAT', 'FILE_SAS_PROC_PROD', 'FILE_SAS_MIGR_DISP',
                                   'FILE_SAS_MIGR_RUL_ID', 'FILE_SAS_MIGR_REC_ACT', 'FILE_SAS_PROC_INMEM_FLG',
                                   'FILE_SAS_PROC_ELT_FLG', 'FILE_SAS_PROC_GRID_FLG', 'FILE_SAS_PROC_INDB_FLG',
                                   'FILE_SAS_SRC_TYP', 'FILE_SAS_ENV_NAME'])

    current_path = os.getcwd()
    current_folder = 'logs_test'
    visited = dict()
    file_list = []
    cat_prod_dict = dict()
    cat_prod_dict = init_proc_cat_prod(cat_prod_dict)
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

                    if FILE_SAS_STP == "PROCEDURE Statement":
                        proc_sql_parsing(record_content)
                    else:
                        pass  # data_step_parsing(record_content)

                    if FILE_SAS_STP_NM == 'DATA':
                        FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = 'Base SAS', 'Data Management'
                    elif FILE_SAS_STP_NM == '':
                        pass
                    else:
                        FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = cat_prod_dict[FILE_SAS_STP_NM.upper()]

                    FILE_ID = 'LOG_' + str(file_id_counter)
                    file_id_counter += 1
                    extracted_record = [FILE_ID, FILE_PTH, FILE_NM, FILE_USR_NM, FILE_SAS_F_ID, FILE_SAS_F_LOC,
                                        FILE_SAS_F_NM, FILE_SAS_STP, FILE_SAS_STP_NM, FILE_LN_NUM, FILE_SAS_INP_LIB,
                                        FILE_SAS_INP_TBL, FILE_SAS_INP_FIL_NM, FILE_SAS_INP_ROW_RD, FILE_SAS_OUT_LIB,
                                        FILE_SAS_OUT_TBL, FILE_SAS_ROW_WRT, FILE_SAS_INP_MUL_FLG, FILE_SAS_INP_MUL_TBLS,
                                        FILE_EXC_DT, FILE_SAS_EXC_TM, FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM,
                                        FILE_SAS_PROC_CAT, FILE_SAS_PROC_PROD, FILE_SAS_MIGR_DISP, FILE_SAS_MIGR_RUL_ID,
                                        FILE_SAS_MIGR_REC_ACT, FILE_SAS_PROC_INMEM_FLG, FILE_SAS_PROC_ELT_FLG,
                                        FILE_SAS_PROC_GRID_FLG, FILE_SAS_PROC_INDB_FLG, FILE_SAS_SRC_TYP,
                                        FILE_SAS_ENV_NAME]

                    log_df = save_record_to_df(log_df, extracted_record)

                    # Data initialization
                    FILE_SAS_ROW_WRT = FILE_SAS_OUT_LIB = FILE_SAS_OUT_TBL = sas_row_write_data = ""

        save_df_to_xlsx(log_df)

logging.info('end of the program')
