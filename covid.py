# importing the required module
import matplotlib.pyplot as plt
import numpy as np

x = ["Feb 15, 2020","Feb 16, 2020","Feb 17, 2020","Feb 18, 2020","Feb 19, 2020","Feb 20, 2020","Feb 21, 2020","Feb 22, 2020","Feb 23, 2020","Feb 24, 2020","Feb 25, 2020","Feb 26, 2020","Feb 27, 2020","Feb 28, 2020","Feb 29, 2020","Mar 01, 2020","Mar 02, 2020","Mar 03, 2020","Mar 04, 2020","Mar 05, 2020","Mar 06, 2020","Mar 07, 2020","Mar 08, 2020","Mar 09, 2020","Mar 10, 2020","Mar 11, 2020","Mar 12, 2020","Mar 13, 2020","Mar 14, 2020","Mar 15, 2020","Mar 16, 2020","Mar 17, 2020","Mar 18, 2020","Mar 19, 2020","Mar 20, 2020","Mar 21, 2020","Mar 22, 2020","Mar 23, 2020","Mar 24, 2020","Mar 25, 2020","Mar 26, 2020","Mar 27, 2020","Mar 28, 2020","Mar 29, 2020","Mar 30, 2020","Mar 31, 2020","Apr 01, 2020","Apr 02, 2020","Apr 03, 2020","Apr 04, 2020","Apr 05, 2020","Apr 06, 2020","Apr 07, 2020","Apr 08, 2020","Apr 09, 2020","Apr 10, 2020","Apr 11, 2020","Apr 12, 2020","Apr 13, 2020","Apr 14, 2020","Apr 15, 2020","Apr 16, 2020","Apr 17, 2020","Apr 18, 2020","Apr 19, 2020","Apr 20, 2020","Apr 21, 2020","Apr 22, 2020","Apr 23, 2020","Apr 24, 2020","Apr 25, 2020","Apr 26, 2020","Apr 27, 2020","Apr 28, 2020","Apr 29, 2020","Apr 30, 2020","May 01, 2020","May 02, 2020","May 03, 2020","May 04, 2020","May 05, 2020","May 06, 2020","May 07, 2020","May 08, 2020","May 09, 2020","May 10, 2020","May 11, 2020","May 12, 2020","May 13, 2020","May 14, 2020","May 15, 2020","May 16, 2020","May 17, 2020","May 18, 2020","May 19, 2020","May 20, 2020","May 21, 2020","May 22, 2020","May 23, 2020","May 24, 2020","May 25, 2020","May 26, 2020","May 27, 2020","May 28, 2020","May 29, 2020","May 30, 2020","May 31, 2020","Jun 01, 2020","Jun 02, 2020","Jun 03, 2020","Jun 04, 2020","Jun 05, 2020","Jun 06, 2020","Jun 07, 2020","Jun 08, 2020","Jun 09, 2020","Jun 10, 2020","Jun 11, 2020","Jun 12, 2020","Jun 13, 2020","Jun 14, 2020","Jun 15, 2020","Jun 16, 2020","Jun 17, 2020","Jun 18, 2020","Jun 19, 2020","Jun 20, 2020","Jun 21, 2020","Jun 22, 2020","Jun 23, 2020","Jun 24, 2020","Jun 25, 2020","Jun 26, 2020","Jun 27, 2020","Jun 28, 2020","Jun 29, 2020","Jun 30, 2020","Jul 01, 2020","Jul 02, 2020","Jul 03, 2020","Jul 04, 2020","Jul 05, 2020","Jul 06, 2020","Jul 07, 2020","Jul 08, 2020","Jul 09, 2020","Jul 10, 2020","Jul 11, 2020","Jul 12, 2020","Jul 13, 2020","Jul 14, 2020","Jul 15, 2020","Jul 16, 2020","Jul 17, 2020","Jul 18, 2020","Jul 19, 2020","Jul 20, 2020","Jul 21, 2020","Jul 22, 2020","Jul 23, 2020","Jul 24, 2020","Jul 25, 2020","Jul 26, 2020","Jul 27, 2020","Jul 28, 2020","Jul 29, 2020","Jul 30, 2020","Jul 31, 2020","Aug 01, 2020","Aug 02, 2020","Aug 03, 2020","Aug 04, 2020","Aug 05, 2020","Aug 06, 2020","Aug 07, 2020","Aug 08, 2020","Aug 09, 2020","Aug 10, 2020","Aug 11, 2020","Aug 12, 2020","Aug 13, 2020","Aug 14, 2020","Aug 15, 2020","Aug 16, 2020","Aug 17, 2020","Aug 18, 2020","Aug 19, 2020","Aug 20, 2020","Aug 21, 2020","Aug 22, 2020","Aug 23, 2020","Aug 24, 2020","Aug 25, 2020","Aug 26, 2020","Aug 27, 2020","Aug 28, 2020","Aug 29, 2020","Aug 30, 2020","Aug 31, 2020","Sep 01, 2020","Sep 02, 2020","Sep 03, 2020","Sep 04, 2020","Sep 05, 2020","Sep 06, 2020","Sep 07, 2020","Sep 08, 2020","Sep 09, 2020","Sep 10, 2020","Sep 11, 2020","Sep 12, 2020","Sep 13, 2020","Sep 14, 2020","Sep 15, 2020","Sep 16, 2020","Sep 17, 2020","Sep 18, 2020","Sep 19, 2020","Sep 20, 2020","Sep 21, 2020","Sep 22, 2020","Sep 23, 2020","Sep 24, 2020","Sep 25, 2020","Sep 26, 2020","Sep 27, 2020","Sep 28, 2020","Sep 29, 2020","Sep 30, 2020","Oct 01, 2020","Oct 02, 2020","Oct 03, 2020","Oct 04, 2020","Oct 05, 2020","Oct 06, 2020","Oct 07, 2020","Oct 08, 2020","Oct 09, 2020","Oct 10, 2020","Oct 11, 2020","Oct 12, 2020","Oct 13, 2020","Oct 14, 2020","Oct 15, 2020","Oct 16, 2020","Oct 17, 2020","Oct 18, 2020","Oct 19, 2020","Oct 20, 2020","Oct 21, 2020","Oct 22, 2020","Oct 23, 2020","Oct 24, 2020","Oct 25, 2020","Oct 26, 2020","Oct 27, 2020","Oct 28, 2020","Oct 29, 2020","Oct 30, 2020","Oct 31, 2020","Nov 01, 2020","Nov 02, 2020","Nov 03, 2020","Nov 04, 2020","Nov 05, 2020","Nov 06, 2020","Nov 07, 2020","Nov 08, 2020","Nov 09, 2020","Nov 10, 2020","Nov 11, 2020","Nov 12, 2020","Nov 13, 2020","Nov 14, 2020","Nov 15, 2020","Nov 16, 2020","Nov 17, 2020","Nov 18, 2020","Nov 19, 2020","Nov 20, 2020","Nov 21, 2020","Nov 22, 2020","Nov 23, 2020","Nov 24, 2020","Nov 25, 2020","Nov 26, 2020","Nov 27, 2020","Nov 28, 2020","Nov 29, 2020","Nov 30, 2020","Dec 01, 2020","Dec 02, 2020","Dec 03, 2020","Dec 04, 2020","Dec 05, 2020","Dec 06, 2020","Dec 07, 2020","Dec 08, 2020","Dec 09, 2020","Dec 10, 2020","Dec 11, 2020","Dec 12, 2020","Dec 13, 2020","Dec 14, 2020","Dec 15, 2020","Dec 16, 2020","Dec 17, 2020","Dec 18, 2020","Dec 19, 2020","Dec 20, 2020","Dec 21, 2020","Dec 22, 2020","Dec 23, 2020","Dec 24, 2020","Dec 25, 2020","Dec 26, 2020","Dec 27, 2020","Dec 28, 2020","Dec 29, 2020","Dec 30, 2020","Dec 31, 2020","Jan 01, 2021","Jan 02, 2021","Jan 03, 2021","Jan 04, 2021","Jan 05, 2021","Jan 06, 2021","Jan 07, 2021","Jan 08, 2021","Jan 09, 2021","Jan 10, 2021","Jan 11, 2021","Jan 12, 2021","Jan 13, 2021","Jan 14, 2021","Jan 15, 2021","Jan 16, 2021","Jan 17, 2021","Jan 18, 2021","Jan 19, 2021","Jan 20, 2021","Jan 21, 2021","Jan 22, 2021","Jan 23, 2021","Jan 24, 2021","Jan 25, 2021","Jan 26, 2021","Jan 27, 2021","Jan 28, 2021","Jan 29, 2021","Jan 30, 2021","Jan 31, 2021","Feb 01, 2021","Feb 02, 2021","Feb 03, 2021","Feb 04, 2021","Feb 05, 2021","Feb 06, 2021","Feb 07, 2021","Feb 08, 2021","Feb 09, 2021","Feb 10, 2021","Feb 11, 2021","Feb 12, 2021","Feb 13, 2021","Feb 14, 2021","Feb 15, 2021","Feb 16, 2021","Feb 17, 2021","Feb 18, 2021","Feb 19, 2021","Feb 20, 2021","Feb 21, 2021","Feb 22, 2021","Feb 23, 2021","Feb 24, 2021","Feb 25, 2021","Feb 26, 2021","Feb 27, 2021","Feb 28, 2021","Mar 01, 2021","Mar 02, 2021","Mar 03, 2021","Mar 04, 2021","Mar 05, 2021","Mar 06, 2021","Mar 07, 2021","Mar 08, 2021","Mar 09, 2021","Mar 10, 2021","Mar 11, 2021","Mar 12, 2021","Mar 13, 2021","Mar 14, 2021","Mar 15, 2021","Mar 16, 2021","Mar 17, 2021","Mar 18, 2021","Mar 19, 2021","Mar 20, 2021","Mar 21, 2021","Mar 22, 2021","Mar 23, 2021","Mar 24, 2021","Mar 25, 2021","Mar 26, 2021","Mar 27, 2021","Mar 28, 2021","Mar 29, 2021","Mar 30, 2021","Mar 31, 2021","Apr 01, 2021","Apr 02, 2021","Apr 03, 2021","Apr 04, 2021","Apr 05, 2021","Apr 06, 2021","Apr 07, 2021","Apr 08, 2021","Apr 09, 2021","Apr 10, 2021","Apr 11, 2021","Apr 12, 2021","Apr 13, 2021","Apr 14, 2021","Apr 15, 2021","Apr 16, 2021","Apr 17, 2021","Apr 18, 2021","Apr 19, 2021","Apr 20, 2021","Apr 21, 2021","Apr 22, 2021","Apr 23, 2021","Apr 24, 2021","Apr 25, 2021","Apr 26, 2021","Apr 27, 2021","Apr 28, 2021","Apr 29, 2021","Apr 30, 2021","May 01, 2021","May 02, 2021","May 03, 2021","May 04, 2021","May 05, 2021","May 06, 2021","May 07, 2021","May 08, 2021","May 09, 2021","May 10, 2021","May 11, 2021","May 12, 2021","May 13, 2021","May 14, 2021","May 15, 2021","May 16, 2021","May 17, 2021","May 18, 2021","May 19, 2021","May 20, 2021","May 21, 2021","May 22, 2021","May 23, 2021","May 24, 2021","May 25, 2021","May 26, 2021","May 27, 2021","May 28, 2021","May 29, 2021","May 30, 2021","May 31, 2021","Jun 01, 2021","Jun 02, 2021","Jun 03, 2021","Jun 04, 2021","Jun 05, 2021","Jun 06, 2021","Jun 07, 2021","Jun 08, 2021","Jun 09, 2021","Jun 10, 2021","Jun 11, 2021","Jun 12, 2021","Jun 13, 2021","Jun 14, 2021","Jun 15, 2021","Jun 16, 2021","Jun 17, 2021","Jun 18, 2021","Jun 19, 2021","Jun 20, 2021","Jun 21, 2021","Jun 22, 2021","Jun 23, 2021","Jun 24, 2021","Jun 25, 2021","Jun 26, 2021","Jun 27, 2021","Jun 28, 2021","Jun 29, 2021","Jun 30, 2021","Jul 01, 2021",
"Jul 02, 2021","Jul 03, 2021","Jul 04, 2021","Jul 05, 2021","Jul 06, 2021","Jul 07, 2021","Jul 08, 2021","Jul 09, 2021","Jul 10, 2021","Jul 11, 2021","Jul 12, 2021","Jul 13, 2021","Jul 14, 2021","Jul 15, 2021","Jul 16, 2021","Jul 17, 2021","Jul 18, 2021","Jul 19, 2021","Jul 20, 2021","Jul 21, 2021","Jul 22, 2021","Jul 23, 2021","Jul 24, 2021","Jul 25, 2021","Jul 26, 2021","Jul 27, 2021","Jul 28, 2021","Jul 29, 2021","Jul 30, 2021","Jul 31, 2021","Aug 01, 2021","Aug 02, 2021","Aug 03, 2021","Aug 04, 2021","Aug 05, 2021","Aug 06, 2021","Aug 07, 2021","Aug 08, 2021","Aug 09, 2021","Aug 10, 2021","Aug 11, 2021","Aug 12, 2021","Aug 13, 2021","Aug 14, 2021","Aug 15, 2021","Aug 16, 2021","Aug 17, 2021","Aug 18, 2021","Aug 19, 2021","Aug 20, 2021","Aug 21, 2021","Aug 22, 2021","Aug 23, 2021","Aug 24, 2021","Aug 25, 2021","Aug 26, 2021","Aug 27, 2021","Aug 28, 2021","Aug 29, 2021","Aug 30, 2021","Aug 31, 2021","Sep 01, 2021","Sep 02, 2021","Sep 03, 2021","Sep 04, 2021","Sep 05, 2021","Sep 06, 2021","Sep 07, 2021","Sep 08, 2021","Sep 09, 2021","Sep 10, 2021","Sep 11, 2021","Sep 12, 2021","Sep 13, 2021","Sep 14, 2021","Sep 15, 2021","Sep 16, 2021","Sep 17, 2021","Sep 18, 2021","Sep 19, 2021","Sep 20, 2021","Sep 21, 2021","Sep 22, 2021","Sep 23, 2021","Sep 24, 2021","Sep 25, 2021","Sep 26, 2021","Sep 27, 2021","Sep 28, 2021","Sep 29, 2021","Sep 30, 2021","Oct 01, 2021","Oct 02, 2021","Oct 03, 2021","Oct 04, 2021","Oct 05, 2021","Oct 06, 2021","Oct 07, 2021","Oct 08, 2021","Oct 09, 2021","Oct 10, 2021","Oct 11, 2021","Oct 12, 2021","Oct 13, 2021","Oct 14, 2021","Oct 15, 2021","Oct 16, 2021","Oct 17, 2021","Oct 18, 2021","Oct 19, 2021","Oct 20, 2021","Oct 21, 2021","Oct 22, 2021","Oct 23, 2021","Oct 24, 2021","Oct 25, 2021","Oct 26, 2021","Oct 27, 2021","Oct 28, 2021","Oct 29, 2021","Oct 30, 2021","Oct 31, 2021","Nov 01, 2021","Nov 02, 2021","Nov 03, 2021","Nov 04, 2021","Nov 05, 2021","Nov 06, 2021","Nov 07, 2021","Nov 08, 2021","Nov 09, 2021","Nov 10, 2021","Nov 11, 2021","Nov 12, 2021","Nov 13, 2021","Nov 14, 2021","Nov 15, 2021","Nov 16, 2021","Nov 17, 2021","Nov 18, 2021","Nov 19, 2021","Nov 20, 2021","Nov 21, 2021","Nov 22, 2021","Nov 23, 2021","Nov 24, 2021","Nov 25, 2021","Nov 26, 2021","Nov 27, 2021","Nov 28, 2021","Nov 29, 2021","Nov 30, 2021","Dec 01, 2021","Dec 02, 2021","Dec 03, 2021","Dec 04, 2021","Dec 05, 2021","Dec 06, 2021","Dec 07, 2021","Dec 08, 2021","Dec 09, 2021","Dec 10, 2021","Dec 11, 2021","Dec 12, 2021","Dec 13, 2021","Dec 14, 2021","Dec 15, 2021","Dec 16, 2021","Dec 17, 2021","Dec 18, 2021","Dec 19, 2021","Dec 20, 2021","Dec 21, 2021","Dec 22, 2021","Dec 23, 2021","Dec 24, 2021","Dec 25, 2021","Dec 26, 2021","Dec 27, 2021","Dec 28, 2021","Dec 29, 2021","Dec 30, 2021","Dec 31, 2021","Jan 01, 2022","Jan 02, 2022","Jan 03, 2022","Jan 04, 2022","Jan 05, 2022","Jan 06, 2022","Jan 07, 2022","Jan 08, 2022","Jan 09, 2022","Jan 10, 2022","Jan 11, 2022","Jan 12, 2022","Jan 13, 2022","Jan 14, 2022","Jan 15, 2022","Jan 16, 2022","Jan 17, 2022","Jan 18, 2022","Jan 19, 2022","Jan 20, 2022","Jan 21, 2022","Jan 22, 2022","Jan 23, 2022","Jan 24, 2022","Jan 25, 2022","Jan 26, 2022","Jan 27, 2022","Jan 28, 2022","Jan 29, 2022","Jan 30, 2022","Jan 31, 2022","Feb 01, 2022","Feb 02, 2022","Feb 03, 2022","Feb 04, 2022","Feb 05, 2022","Feb 06, 2022","Feb 07, 2022","Feb 08, 2022","Feb 09, 2022","Feb 10, 2022","Feb 11, 2022","Feb 12, 2022","Feb 13, 2022","Feb 14, 2022","Feb 15, 2022","Feb 16, 2022","Feb 17, 2022","Feb 18, 2022","Feb 19, 2022","Feb 20, 2022","Feb 21, 2022","Feb 22, 2022","Feb 23, 2022","Feb 24, 2022","Feb 25, 2022","Feb 26, 2022","Feb 27, 2022","Feb 28, 2022","Mar 01, 2022","Mar 02, 2022","Mar 03, 2022","Mar 04, 2022","Mar 05, 2022","Mar 06, 2022","Mar 07, 2022","Mar 08, 2022","Mar 09, 2022","Mar 10, 2022","Mar 11, 2022","Mar 12, 2022","Mar 13, 2022","Mar 14, 2022","Mar 15, 2022","Mar 16, 2022","Mar 17, 2022","Mar 18, 2022","Mar 19, 2022","Mar 20, 2022","Mar 21, 2022","Mar 22, 2022","Mar 23, 2022","Mar 24, 2022","Mar 25, 2022","Mar 26, 2022","Mar 27, 2022","Mar 28, 2022","Mar 29, 2022","Mar 30, 2022","Mar 31, 2022","Apr 01, 2022","Apr 02, 2022","Apr 03, 2022","Apr 04, 2022","Apr 05, 2022","Apr 06, 2022","Apr 07, 2022","Apr 08, 2022","Apr 09, 2022","Apr 10, 2022","Apr 11, 2022","Apr 12, 2022","Apr 13, 2022","Apr 14, 2022","Apr 15, 2022","Apr 16, 2022","Apr 17, 2022","Apr 18, 2022","Apr 19, 2022","Apr 20, 2022","Apr 21, 2022","Apr 22, 2022","Apr 23, 2022","Apr 24, 2022","Apr 25, 2022","Apr 26, 2022","Apr 27, 2022","Apr 28, 2022","Apr 29, 2022","Apr 30, 2022","May 01, 2022","May 02, 2022","May 03, 2022","May 04, 2022","May 05, 2022","May 06, 2022","May 07, 2022","May 08, 2022","May 09, 2022","May 10, 2022","May 11, 2022","May 12, 2022","May 13, 2022","May 14, 2022","May 15, 2022","May 16, 2022","May 17, 2022","May 18, 2022","May 19, 2022","May 20, 2022","May 21, 2022","May 22, 2022","May 23, 2022","May 24, 2022","May 25, 2022","May 26, 2022","May 27, 2022"]

# Daily New Cases
daily_case = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,1,0,0,0,2,0,0,0,0,0,0,7,0,3,0,1,0,7,1,2,3,1,4,0,0,2,5,19,5,6,0,0,0,0,3,0,1,0,1,0,0,1,5,4,12,1,0,11,4,10,8,8,1,10,6,2,4,26,15,4,14,6,1,10,10,0,53,9,36,2,55,15,9,20,19,17,20,44,30,26,29,13,11,6,20,45,4,20,5,26,28,0,43,24,6,14,15,21,30,18,25,28,31,21,19,24,22,62,49,62,53,19,33,56,16,29,21,25,8,26,53,32,19,28,60,56,43,39,27,56,50,41,93,28,28,142,70,78,79,70,83,64,59,77,54,70,80,109,91,45,68,82,61,46,63,61,95,123,78,90,58,76,103,113,90,117,68,86,122,229,213,231,281,167,103,273,234,141,202,148,137,190,168,226,305,268,172,160,91,70,147,100,102,96,145,103,102,157,87,170,134,145,75,95,159,214,110,141,228,189,147,91,175,112,142,110,252,92,119,142,72,81,108,94,92,191,55,69,99,103,133,113,108,66,52,63,94,154,104,56,72,122,71,165,39,80,27,88,69,96,52,120,95,111,82,47,67,81,159,132,142,48,40,101,113,82,139,91,127,72,0,264,77,54,103,45,62,113,157,152,174,341,154,79,125,294,521,879,578,395,662,730,543,735,858,689,895,824,1126,829,623,780,790,363,1274,871,907,1275,597,949,806,800,1173,1055,696,928,488,312,873,951,1054,798,547,1130,426,1109,829,898,677,764,675,517,435,325,677,621,554,578,257,307,481,775,359,602,389,183,179,292,471,359,292,220,0,413,268,255,347,265,148,94,190,153,113,117,132,186,95,0,287,150,194,82,114,108,65,139,35,40,72,180,34,79,56,75,65,67,69,25,81,128,86,74,46,22,50,47,42,60,53,48,19,16,31,21,56,30,28,46,26,29,20,28,46,49,32,21,22,24,18,24,17,22,16,30,15,22,24,27,56,15,55,73,42,54,63,32,31,20,74,40,76,106,77,30,83,113,165,194,244,140,70,198,436,441,534,518,434,284,406,576,801,869,1139,938,737,1458,770,1806,1327,1686,933,1687,1331,1543,1304,1394,2025,1260,1373,1224,1704,2153,1443,1451,1528,1435,1703,2460,1774,2290,2078,1513,1421,1429,1034,1611,1490,1273,653,725,1166,1185,1038,847,931,405,289,1033,694,618,630,510,261,343,528,377,436,731,525,139,190,263,438,312,365,354,138,131,390,108,175,174,187,119,52,221,191,133,102,75,37,49,134,79,90,69,55,36,10,32,90,61,36,31,14,3,19,48,25,36,28,22,6,27,28,15,19,17,5,10,24,21,17,21,25,5,1,17,10,7,10,18,4,10,14,9,14,13,15,1,3,11,8,20,4,8,5,5,25,9,6,5,11,0,4,3,8,9,3,0,9,4,20,46,58,111,105,56,76,120,206,260,379,443,266,113,733,975,1234,1382,1252,541,553,2068,2337,2445,2770,898,527,673,3473,3624,4947,4861,2642,731,918,2975,3594,3301,3031,3117,1010,592,1868,1948,1752,1262,976,284,309,851,667,524,543,440,181,56,240,220,301,199,126,73,16,122,94,100,81,85,30,8,87,60,65,44,50,50,16,48,24,24,26,41,21,17,17,46,16,19,18,2,9,16,17,20,21,14,5,0,10,9,3,3,8,6,0,9,6,6,1,5,4,1,4,5,3,8,6,2,0,5,5,7,5,3,2,1,1,4,3,2,3,13,3,5,3,10,2,7,6,3,6,7,6,1,6,7,1,1,8,4,4,1,2,1,0,13,7,2,10,7,4,10,11,19,15,8,5,5,16,20,7,11,6,14,9,14,26,22,28]

# Total Cases
total_case = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,3,5,7,7,8,8,8,8,10,10,10,10,10,10,10,17,17,20,20,21,21,28,29,31,34,35,39,39,39,41,46,65,70,76,76,76,76,76,79,79,80,80,81,81,81,82,87,91,103,104,104,115,119,129,137,145,146,156,162,164,168,194,209,213,227,233,234,244,254,254,307,316,352,354,409,424,433,453,472,489,509,553,583,609,638,651,662,668,688,733,737,757,762,788,816,816,859,883,889,903,918,939,969,987,1012,1040,1071,1092,1111,1135,1157,1219,1268,1330,1383,1402,1435,1491,1507,1536,1557,1582,1590,1616,1669,1701,1720,1748,1808,1864,1907,1946,1973,2029,2079,2120,2213,2241,2269,2411,2481,2559,2638,2708,2791,2855,2914,2991,3045,3115,3195,3304,3395,3440,3508,3590,3651,3697,3760,3821,3916,4039,4117,4207,4265,4341,4444,4557,4647,4764,4832,4918,5040,5269,5482,5713,5994,6161,6264,6537,6771,6912,7114,7262,7399,7589,7757,7983,8288,8556,8728,8888,8979,9049,9196,9296,9398,9494,9639,9742,9844,10001,10088,10258,10392,10537,10612,10707,10866,11080,11190,11331,11559,11748,11895,11986,12161,12273,12415,12525,12777,12869,12988,13130,13202,13283,13391,13485,13577,13768,13823,13892,13991,14094,14227,14340,14448,14514,14566,14629,14723,14877,14981,15037,15109,15231,15302,15467,15506,15586,15613,15701,15770,15866,15918,16038,16133,16244,16326,16373,16440,16521,16680,16812,16954,17002,17042,17143,17256,17338,17477,17568,17695,17767,17767,18031,18108,18162,18265,18310,18372,18485,18642,18794,18968,19309,19463,19542,19667,19961,20482,21361,21939,22334,22996,23726,24269,25004,25862,26551,27446,28270,29396,30225,30848,31628,32418,32781,34055,34926,35833,37108,37705,38654,39460,40260,41433,42488,43184,44112,44600,44912,45785,46736,47790,48588,49135,50265,50691,51800,52629,53527,54204,54968,55643,56160,56595,56920,57597,58218,58772,59350,59607,59914,60395,61170,61529,62131,62520,62703,62882,63174,63645,64004,64296,64516,64516,64929,65197,65452,65799,66064,66212,66306,66496,66649,66762,66879,67011,67197,67292,67292,67579,67729,67923,68005,68119,68227,68292,68431,68466,68506,68578,68758,68792,68871,68927,69002,69067,69134,69203,69228,69309,69437,69523,69597,69643,69665,69715,69762,69804,69864,69917,69965,69984,70000,70031,70052,70108,70138,70166,70212,70238,70267,70287,70315,70361,70410,70442,70463,70485,70509,70527,70551,70568,70590,70606,70636,70651,70673,70697,70724,70780,70795,70850,70923,70965,71019,71082,71114,71145,71165,71239,71279,71355,71461,71538,71568,71651,71764,71929,72123,72367,72507,72577,72775,73211,73652,74186,74704,75138,75422,75828,76404,77205,78074,79213,80151,80888,82346,83116,84922,86249,87935,88868,90555,91886,93429,94733,96127,98152,99412,100785,102009,103713,105866,107309,108760,110288,111723,113426,115886,117660,119950,122028,123541,124962,126391,127425,129036,130526,131799,132452,133177,134343,135528,136566,137413,138344,138749,139038,140071,140765,141383,142013,142523,142784,143127,143655,144032,144468,145199,145724,145863,146053,146316,146754,147066,147431,147785,147923,148054,148444,148552,148727,148901,149088,149207,149259,149480,149671,149804,149906,149981,150018,150067,150201,150280,150370,150439,150494,150530,150540,150572,150662,150723,150759,150790,150804,150807,150826,150874,150899,150935,150963,150985,150991,151018,151046,151061,151080,151097,151102,151112,151136,151157,151174,151195,151220,151225,151226,151243,151253,151260,151270,151288,151292,151302,151316,151325,151339,151352,151367,151368,151371,151382,151390,151410,151414,151422,151427,151432,151457,151466,151472,151477,151488,151488,151492,151495,151503,151512,151515,151515,151524,151528,151548,151594,151652,151763,151868,151924,152000,152120,152326,152586,152965,153408,153674,153787,154520,155495,156729,158111,159363,159904,160457,162525,164862,167307,170077,170975,171502,172175,175648,179272,184219,189080,191722,192453,193371,196346,199940,203241,206272,209389,210399,210991,212859,214807,216559,217821,218797,219081,219390,220241,220908,221432,221975,222415,222596,222652,222892,223112,223413,223612,223738,223811,223827,223949,224043,224143,224224,224309,224339,224347,224434,224494,224559,224603,224653,224703,224719,224767,224791,224815,224841,224882,224903,224920,224937,224983,224999,225018,225036,225038,225047,225063,225080,225100,225121,225135,225140,225140,225150,225159,225162,225165,225173,225179,225179,225188,225194,225200,225201,225206,225210,225211,225215,225220,225223,225231,225237,225239,225239,225244,225249,225256,225261,225264,225266,225267,225268,225272,225275,225277,225280,225293,225296,225301,225304,225314,225316,225323,225329,225332,225338,225345,225351,225352,225358,225365,225366,225367,225375,225379,225383,225384,225386,225387,225387,225400,225407,225409,225419,225426,225430,225440,225451,225470,225485,225493,225498,225503,225519,225539,225546,225557,225563,225577,225586,225600,225626,225648,225676]

# Total Deaths
total_death = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,7,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,11,11,11,11,11,11,11,11,11,11,11,11,12,13,14,15,15,15,15,16,16,16,17,19,19,19,19,19,19,19,19,20,20,20,20,21,21,21,21,21,22,23,23,23,25,26,26,26,27,27,28,28,31,31,35,35,35,37,39,39,40,41,43,44,45,49,51,53,54,58,59,59,61,62,64,64,66,66,67,68,68,69,70,71,72,73,73,73,73,74,75,75,78,79,81,82,85,86,88,89,91,91,91,92,93,94,95,95,97,99,99,99,99,99,104,104,110,110,113,116,118,119,120,121,123,124,126,127,128,128,128,129,130,131,131,132,132,133,133,133,136,136,138,139,139,140,142,143,144,145,145,146,147,148,149,150,150,156,156,159,161,162,162,165,166,167,168,169,171,171,172,176,181,187,192,197,201,205,211,216,234,241,249,253,271,283,290,297,305,319,329,336,347,356,363,367,386,403,415,427,436,451,460,465,480,486,501,514,525,535,547,551,561,571,583,587,595,599,606,608,613,613,630,641,653,665,668,674,680,686,693,698,700,707,711,719,722,725,725,732,733,737,740,743,746,747,750,752,753,758,762,764,769,769,775,775,778,782,782,782,785,785,788,789,789,791,791,794,794,794,797,798,798,800,802,805,805,806,807,807,809,814,814,814,814,814,815,815,817,818,819,820,821,823,825,826,826,826,826,826,826,828,828,828,828,831,831,831,831,833,834,834,835,836,836,836,836,836,837,837,837,837,838,839,840,840,840,840,841,841,842,844,844,844,847,848,848,852,857,863,865,867,868,869,872,878,884,885,897,904,912,923,934,939,947,962,982,996,1013,1033,1057,1075,1099,1118,1138,1158,1190,1221,1232,1257,1282,1307,1341,1367,1388,1407,1434,1462,1479,1500,1526,1538,1566,1600,1613,1628,1641,1655,1671,1690,1707,1716,1731,1748,1761,1773,1783,1785,1800,1808,1813,1822,1825,1834,1842,1851,1853,1864,1866,1871,1872,1877,1878,1881,1885,1888,1891,1892,1892,1892,1894,1895,1898,1902,1903,1903,1903,1903,1903,1906,1907,1908,1909,1909,1910,1912,1915,1917,1918,1918,1918,1919,1919,1919,1919,1921,1922,1922,1924,1924,1924,1924,1925,1925,1926,1927,1927,1927,1927,1927,1928,1928,1928,1929,1929,1929,1929,1930,1930,1931,1932,1932,1932,1933,1934,1934,1934,1934,1934,1934,1934,1934,1936,1936,1936,1936,1936,1936,1936,1938,1938,1939,1940,1940,1940,1940,1940,1941,1941,1941,1941,1941,1941,1941,1941,1941,1941,1941,1942,1942,1944,1945,1945,1946,1948,1948,1950,1952,1952,1957,1960,1961,1965,1967,1968,1973,1976,1988,1996,2006,2012,2019,2031,2042,2050,2065,2075,2077,2085,2096,2099,2105,2109,2117,2123,2127,2132,2136,2140,2146,2149,2153,2157,2159,2161,2163,2164,2165,2167,2170,2173,2174,2180,2180,2183,2183,2183,2183,2185,2186,2188,2188,2189,2189,2189,2189,2189,2189,2189,2189,2189,2189,2190,2191,2192,2192,2192,2192,2192,2192,2193,2194,2195,2196,2196,2196,2197,2198,2198,2198,2198,2198,2198,2198,2198,2199,2199,2199,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2200,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2201,2203,2203,2203,2203,2203]

# Daily New Deaths
daily_death = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,2,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,2,1,0,0,1,0,1,0,3,0,4,0,0,2,2,0,1,1,2,1,1,4,2,2,1,4,1,0,2,1,2,0,2,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,3,1,2,1,3,1,2,1,2,0,0,1,1,1,1,0,2,2,0,0,0,0,5,0,6,0,3,3,2,1,1,1,2,1,2,1,1,0,0,1,1,1,0,1,0,1,0,0,3,0,2,1,0,1,2,1,1,1,0,1,1,1,1,1,0,6,0,3,2,1,0,3,1,1,1,1,2,0,1,4,5,6,5,5,4,4,6,5,18,7,8,4,18,12,7,7,8,14,10,7,11,9,7,4,19,17,12,12,9,15,9,5,15,6,15,13,11,10,12,4,10,10,12,4,8,4,7,2,5,0,17,11,12,12,3,6,6,6,7,5,2,7,4,8,3,3,0,7,1,4,3,3,3,1,3,2,1,5,4,2,5,0,6,0,3,4,0,0,3,0,3,1,0,2,0,3,0,0,3,1,0,2,2,3,0,1,1,0,2,5,0,0,0,0,1,0,2,1,1,1,1,2,2,1,0,0,0,0,0,2,0,0,0,3,0,0,0,2,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,2,0,0,3,1,0,4,5,6,2,2,1,1,3,6,6,1,12,7,8,11,11,5,8,15,20,14,17,20,24,18,24,19,20,20,32,31,11,25,25,25,34,26,21,19,27,28,17,21,26,12,28,34,13,15,13,14,16,19,17,9,15,17,13,12,10,2,15,8,5,9,3,9,8,9,2,11,2,5,1,5,1,3,4,3,3,1,0,0,2,1,3,4,1,0,0,0,0,3,1,1,1,0,1,2,3,2,1,0,0,1,0,0,0,2,1,0,2,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,2,1,0,1,2,0,2,2,0,5,3,1,4,2,1,5,3,12,8,10,6,7,12,11,8,15,10,2,8,11,3,6,4,8,6,4,5,4,4,6,3,4,4,2,2,2,1,1,2,3,3,1,6,0,3,0,0,0,2,1,2,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0]

# Daily Active Cases
active_case = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,3,5,7,7,8,8,8,8,10,10,10,9,9,9,9,16,16,18,18,19,19,26,27,29,32,31,31,31,31,33,37,53,58,64,64,64,64,64,67,61,61,61,62,60,57,55,53,57,69,70,70,80,77,86,93,101,102,108,114,116,120,143,137,141,155,149,148,152,161,155,207,205,236,233,281,295,300,315,332,343,362,400,429,449,474,487,483,487,507,547,551,546,537,562,588,588,626,648,651,649,663,684,706,723,727,752,726,743,758,777,784,841,886,946,999,996,1017,1009,991,1019,1023,1043,1047,1062,1065,1094,1107,1121,1159,1212,1250,1279,1283,1249,1286,1310,1371,1393,1413,1535,1554,1589,1604,1614,1636,1673,1699,1727,1735,1715,1769,1810,1872,1758,1678,1642,1662,1621,1660,1698,1723,1846,1922,1811,1728,1736,1802,1833,1904,1973,1944,1988,2100,2274,2423,2495,2688,2729,2722,2876,3106,3130,3005,2863,2790,2887,2934,3118,3393,3292,3435,3253,3320,3249,3278,3126,2973,2614,2660,2502,2571,2592,2466,2305,2284,2250,2277,2361,2278,2169,2105,2087,2252,2432,2566,2647,2819,2902,2539,2433,2249,2340,2456,2597,2412,2205,2117,2111,1897,2064,2065,2045,1928,1856,1879,1725,1830,1799,1802,1756,1754,1703,1707,1762,1754,1696,1715,1819,1747,1780,1806,1841,1861,1720,1756,1745,1657,1695,1761,1800,1618,1667,1748,1877,1994,1853,1781,1757,1854,1827,1879,1966,1813,1761,1761,1860,1937,1894,1985,1970,1771,1731,1813,1947,2116,2375,2464,2302,2354,2330,2822,3653,4212,4514,4625,5239,5706,6417,7113,7703,8317,8885,9641,10432,10700,11329,11555,11451,12383,12096,12736,13193,13397,14332,14481,14847,15533,16388,16536,16871,16978,17009,17491,17855,17165,17058,17104,18031,18197,18987,19211,19152,19232,19460,19781,19337,18419,18442,18308,17799,17381,17613,17541,16452,15725,16220,14965,15151,15406,15411,14453,14016,14318,14347,13760,13411,13411,13353,13088,12352,12668,12794,12783,12677,12558,12094,11914,11047,11082,11158,11152,11152,10395,10119,10304,10258,10213,10211,9581,9583,9549,9381,9406,9063,8600,8176,8161,7096,7082,7129,7112,6113,6184,6290,6324,6383,6384,6357,5979,4500,4449,4509,3190,2268,2238,1860,1872,1891,1593,1612,1596,1604,1614,1557,1414,1175,1048,874,891,904,908,904,854,875,892,661,675,686,624,612,630,389,437,434,467,532,487,530,589,615,620,639,690,699,637,743,816,838,872,921,1057,1249,1479,1610,1488,1634,2054,2437,2750,3238,3189,3403,3770,4321,4830,5698,6688,7613,7809,9019,9745,11534,12408,14074,14269,15679,16662,18004,18758,19927,20784,21578,22808,22514,22465,23872,23778,24887,26239,25423,26006,28096,29016,30462,32214,31234,27668,28445,24987,26165,27085,27810,27882,24116,24186,19832,18964,18778,19238,18583,17748,16874,16782,16863,16880,16057,14943,15006,13990,13991,12378,12723,12961,12479,11803,10878,10488,9764,9921,9279,8711,8282,7864,7344,6195,6048,6046,5923,5187,5204,5004,3027,2990,2696,2509,2505,2413,2284,2308,2159,2093,2067,2042,1817,1781,1837,1560,1475,1489,1305,1302,1314,1133,1167,1191,1187,1112,1056,1058,1071,1056,1073,989,711,626,636,636,625,647,637,632,335,330,149,132,149,153,160,136,140,137,121,135,135,116,99,107,127,130,133,123,93,118,123,129,122,133,113,94,96,102,105,104,104,99,95,93,115,173,247,352,408,484,604,802,1023,1080,1511,1772,1878,2586,3534,4575,5924,6982,7517,8021,10051,11679,14105,16822,17718,18229,17627,20646,23553,28492,30504,33134,33250,32660,34737,36737,35905,38926,41652,39224,38003,37222,37141,36842,36024,35684,35964,28189,24960,24139,22436,21523,20720,18279,15220,14338,12833,12479,12051,12007,9571,8286,6358,6417,6476,6106,5237,5044,4797,4770,4633,4420,4204,4201,4236,4097,4020,3908,3797,3752,3782,3803,3625,3584,3513,3510,3506,3524,3525,3425,3233,3024,3043,3029,3042,3047,3047,1458,1098,1022,1012,1020,1026,1009,1001,1007,1012,994,988,986,980,977,975,978,976,976,976,969,47,51,58,63,66,68,51,47,51,54,30,33,46,49,43,46,54,45,52,58,52,49,56,62,47,53,60,59,60,64,65,69,70,52,48,43,44,47,45,55,61,60,59,64,81,94,102,107,85,94,110,71,77,83,97,80,78,104,126,152]

# Total Recovered
total_recovered = []
for i in range (0, len(daily_case)):
   total_recovered.append(total_case[i] - total_death[i] - active_case[i])

# Daily Recovered
daily_recovered = []
daily_recovered.append(total_recovered[0])
for i in range(0, len(total_recovered)-1):
    a = total_recovered[i+1]-total_recovered[i]
    daily_recovered.append(a)

# Reproduction Number
rep_number = [0]
for i in range(1, len(x)):
   try:
      rt = daily_case[i]/daily_recovered[i]
      rep_number.append(rt)
   except:
      rep_number.append(rep_number[i-1])

# Jangka Waktu Tertentu
tgl_js = []
totcase_js = []
totreco_js = []
daycase_js = []
dayreco_js = []
rt_js = []
dc_js = []
Re = []
for i in range(len(x)):
   for j in range(len(x)):
      if x[i] == 'Dec 01, 2021':
         if x[j] == 'Feb 13, 2022':
            for k in range(i, j+1):
               tgl_js.append(x[k])
               totcase_js.append(total_case[k])
               totreco_js.append(total_recovered[k])
               daycase_js.append(daily_case[k])
               dayreco_js.append(daily_recovered[k])
               dc_js.append(daily_case[k])
               rt_js.append(rep_number[k])
               Re.append(1)

# plot kurva untuk lama waktu recovery 
time1 = []     # day of thehighest number new cases
time2 = []     # day of the highest number daily recovery
for i in range(len(daycase_js)):
   if daycase_js[i] == max(daycase_js):
      tgl_daycase = tgl_js[i]
      time1 = i+1
      break
for j in range(len(dayreco_js)):
   if dayreco_js[j] == max(dayreco_js):
      tgl_dayreco = tgl_js[j]
      time2 = j+1
      break

# Menghitung lama waktu recovery 
recov_time = []
y1 = []
y2 = []
for i in range(time1-1, time2):
   recov_time.append(tgl_js[i])
   y1.append(totcase_js[time1-1])
   y2.append(max(dayreco_js))

# plot kurva x = Jan 03, 2022
rtx = []
rty = [max(rt_js), min(rt_js)-50]
rtf = 0
for i in range(len(tgl_js)):
   if tgl_js[i] == "Jan 03, 2022":
      rtf += rt_js[i]
      rtx.append(tgl_js[i])
      rtx.append(tgl_js[i])
rt_final = '%.1f'%rtf

#! FIRST GRAPH 
#? Lama Waktu Recovery dari Covid (Total Cases VS Total Recovery) dalam periode tertentu
fig, axs0 = plt.subplots()
ax1 = axs0.twinx()

axs0.plot(tgl_js, totcase_js, 'r', label='total cases')
ax1.plot(tgl_js, totreco_js, 'g', label='total recovery')
plt.plot(recov_time, y1, 'm--', label='recovered in %d days'%(time2-time1))
axs0.legend(loc="upper right")
ax1.legend(loc="upper left")
plt.xticks(np.linspace(0, len(tgl_js)+1,10))
axs0.set_xlabel('Date')
axs0.set_ylabel('Total Cases', color='r')
ax1.set_ylabel('Total Recovery', color='g')
axs0.tick_params(axis='y', colors='r')
ax1.tick_params(axis='y', colors='g')
plt.title('Total Cases VS Total Recovery')
axs0.grid(linestyle = '--', linewidth=0.5)
plt.show()

#! SECOND GRAPH
#? Lama Waktu Recovery dari Covid (Daily New Cases VS Daily Recovery) dalam periode tertentu
fig, axs2 = plt.subplots()
ax3 = axs2.twinx()

axs2.plot(tgl_js, daycase_js, 'r', label='Daily Cases')
ax3.plot(tgl_js, dayreco_js, 'g', label='Daily Recovery')
plt.plot(recov_time, y2, 'm--', label='recovered in %d days'%(time2-time1))
axs2.legend(loc="upper right")
ax3.legend(loc="upper left")
plt.xticks(np.linspace(0, len(tgl_js)+1,10))
axs2.set_xlabel('Date')
axs2.set_ylabel('Daily Cases', color='r')
ax3.set_ylabel('Daily Recovery', color='g')
axs2.tick_params(axis='y', colors='r')
ax3.tick_params(axis='y', colors='g')
plt.title('Daily New Cases VS Daily Recovered')
axs2.grid(linestyle = '--', linewidth=0.5)
plt.show()

#! THIRD GRAPH
#? Reproduction Number (Laju Penyebaran) dalam periode tertentu
fig, axs4 = plt.subplots()
ax5 = axs4.twinx()

ax5.plot(tgl_js, dc_js, '#1d1066', label='Daily Cases')
axs4.plot(tgl_js, rt_js, 'r', label='Rt')
axs4.plot(tgl_js, Re, 'b--', label="I/R ratio = Re")
axs4.plot(rtx, rty, 'g--', label="I/R = %s"%rt_final)
axs4.legend(loc="upper left")
ax5.legend()
plt.xticks(np.linspace(0, len(tgl_js)+1,10))
axs4.set_xlabel('Date')
axs4.set_ylabel('Rt', color='r')
ax5.set_ylabel('Daily Cases', color='#1d1066')
axs4.tick_params(axis='y', colors='r')
ax5.tick_params(axis='y', colors='#1d1066')
plt.title('Mozambique Covid-19 Daily New Case')
axs4.grid(linestyle = '--', linewidth=0.5)
plt.show()
