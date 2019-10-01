#!/usr/bin/Rscript
source("core.r")

init()  # do NOT remove this code, place logic & imports below this line

# R submission
#
# Implement the model below
# This sample algorithm naively sends 1 as the prediction for every line of data
#
###################################################### OVERVIEW ######################################################
# 
# 1. Use get_next_data_as_string() OR get_next_data_as_list() OR get_next_data_as_dataframe() OR get_next_data_as_matrix() to
#    receive a row of data
# 2. Use the predict method to write the prediction logic, and return a float representing your prediction
# 3. Submit a prediction using submit_prediction
#
######################################################################################################################
#
################################################## OVERVIEW OF DATA ##################################################
# 
# 1. get_next_data_as_string() accepts no input and returns a String representing a row of data extracted from data.csv
#    Example output: [1] "1618.0,1618.5,1619.5,1620.0,1620.5,1621.0,1621.5,1622.0,1622.5,1623.0,1623.5,1624.0,1624.5
#                         1625.0,1626.0,1.0,1.0,3.0,10.0,5.0,24.0,8.0,152.0,4.0,10.0,2.0,24.0,2.0,82.0,10.0,1615.5,
#                         1615.0,1614.5,1614.0,1613.5,1613.0,1612.5,1612.0,1611.5,1611.0,1610.5,1610.0,1609.5,1608.5,
#                         1608.0,3.0,94.0,2.0,11.0,4.0,1.0,3.0,10.0,7.0,20.0,4.0,4.0,2.0,2.0,1.0"
#
# 2. get_next_data_as_list() accepts no input and returns a list representing a row of data extracted from data.csv
#    Example output:  [1] "1619.5" "1620.0" "1621.0" ""       ""       ""       ""       ""
#                     [9] ""       ""       ""       ""       ""       ""       ""       "1.0"
#                     [17] "10.0"   "24.0"   ""       ""       ""       ""       ""       ""
#                     [25] ""       ""       ""       ""       ""       ""       "1615.0" "1614.0"
#                     [33] "1613.0" "1612.0" "1611.0" "1610.0" "1607.0" "1606.0" "1605.0" "1604.0"
#                     [41] "1603.0" "1602.0" "1601.5" "1601.0" "1600.0" "7.0"    "10.0"   "1.0"
#                     [49] "10.0"   "20.0"   "3.0"    "20.0"   "27.0"   "11.0"   "14.0"   "35.0"
#                     [57] "10.0"   "1.0"    "10.0"   "13.0"
#
# 3. get_next_data_as_dataframe() accepts no input and returns a dataframe representing a row of data extracted from data.csv
#    Example output:       V1   V2   V3 V4 V5 V6 V7 V8 V9 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19
#                    1 1619.5 1620 1621 NA NA NA NA NA NA  NA  NA  NA  NA  NA  NA   1  10  24  NA
#                      V20 V21 V22 V23 V24 V25 V26 V27 V28 V29 V30  V31  V32  V33  V34  V35  V36
#                    1  NA  NA  NA  NA  NA  NA  NA  NA  NA  NA  NA 1615 1614 1613 1612 1611 1610
#                      V37  V38  V39  V40  V41  V42    V43  V44  V45 V46 V47 V48 V49 V50 V51 V52
#                    1 1607 1606 1605 1604 1603 1602 1601.5 1601 1600   7  10   1  10  20   3  20
#                      V53 V54 V55 V56 V57 V58 V59 V60
#                    1  27  11  14  35  10   1  10  13
#
# 4. get_next_data_as_matrix() accepts no input and returns a matrix representing a row of data extracted from data.csv
#    Example output:          V1   V2   V3 V4 V5 V6 V7 V8 V9 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19
#                    [1,] 1619.5 1620 1621 NA NA NA NA NA NA  NA  NA  NA  NA  NA  NA   1  10  24  NA
#                         V20 V21 V22 V23 V24 V25 V26 V27 V28 V29 V30  V31  V32  V33  V34  V35  V36
#                    [1,]  NA  NA  NA  NA  NA  NA  NA  NA  NA  NA  NA 1615 1614 1613 1612 1611 1610
#                          V37  V38  V39  V40  V41  V42    V43  V44  V45 V46 V47 V48 V49 V50 V51 V52
#[                   [1,] 1607 1606 1605 1604 1603 1602 1601.5 1601 1600   7  10   1  10  20   3  20
#                         V53 V54 V55 V56 V57 V58 V59 V60
#                    [1,]  27  11  14  35  10   1  10  13

######################################################################################################################
#
###################################################### IMPORTANT ######################################################
# 
# 1. One of the methods get_next_data_as_string(), get_next_data_as_dataframe(), get_next_data_as_list(),
#    or get_next_data_as_matrix() MUST be used and _prediction(pred) MUST be used to submit below in the solution
#    implementation for the submission to work correctly.
# 2. get_next_data_as_string(), get_next_data_as_dataframe(), get_next_data_as_list(), or get_next_data_as_matrix()
#    CANNOT be called more then once in a row without calling self.submit_prediction(pred).
# 3. In order to debug by printing do NOT call the default method `print(...)`, rather call debug_print(...)
#
######################################################################################################################


input <- file('stdin')
open(input, 'rb')

# get_prediction(data) expects a row of data from data.csv as input and should return a float that represents a
#     prediction for the supplied row of data 
get_prediction <- function(data) {
  split_data <- unlist(strsplit(data, "[,]"))
  bidSize0 = as.numeric(split_data[46])
  askSize0 = as.numeric(split_data[16])
  if(is.null(bidSize0)){
    bidSize0 = 0
  }
  if(is.null(askSize0)){
    askSize0 = 0
  }
  return(0.0025 * (bidSize0-askSize0))
}

debug_print("Use the print function `debug_print(...)` for debugging purposes, do NOT use the default `print(...)`")

while (TRUE) {
    tryCatch({
    # NOTE: Only one of (get_next_data_as_string, get_next_data_as_dataframe, get_next_data_as_list,
	  #             get_next_data_as_matrix) can be used to get the row of data, please refer to the
	  #             `OVERVIEW OF DATA` section above.
	  #
	  #		Uncomment the one that will be used, and comment the others.
    #data <- get_next_data_as_dataframe()
    #data <- get_next_data_as_list()
    #data <- get_next_data_as_matrix()
    data <- get_next_data_as_string()
    
    # Write prediction logic in get_prediction(...)
    prediction <- get_prediction(data)
    
    # submit_prediction(pred) MUST be used submit your 
    # prediction for the current row of data
  
    submit_prediction(prediction)
  }, error=function(e){
    if (grepl("ignoring SIGPIPE signal", e)) {
      quit()
    } else {
      stop(e)
    }
  })
}
