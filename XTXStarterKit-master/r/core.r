
DATA_ROW_IN_TRANSIT <<- FALSE


# Receives a line of data from standard input
#
# Standard input is fed into your algorithm
# ONLY after a prediction for the previous
# row of data is received.
get_next_data_as_string <- function() {
  
  if (DATA_ROW_IN_TRANSIT) {
    stop("get_next_data_as_string() can only be called once for every prediction made.")
  }

  data <- readLines(input, n=1)
  DATA_ROW_IN_TRANSIT <<- TRUE

  return(data)
}

get_next_data_as_list <- function() {

  if (DATA_ROW_IN_TRANSIT) {
    stop("get_next_data_as_list() can only be called once for every prediction made.")
  }

  raw_data <- readLines(input, n=1)
  data <- strsplit(raw_data, ',')[[1]]
  DATA_ROW_IN_TRANSIT <<- TRUE

  return(data)
}

get_next_data_as_dataframe <- function() {

  if (DATA_ROW_IN_TRANSIT) {
    stop("get_next_data_as_dataframe() can only be called once for every prediction made.")
  }

  raw_data <- readLines(input, n=1)
  data <- read.csv(text=raw_data, sep=',', header=FALSE)
  DATA_ROW_IN_TRANSIT <<- TRUE

  return(data)
}

get_next_data_as_matrix <- function() {

  if (DATA_ROW_IN_TRANSIT) {
    stop("get_next_data_as_matrix() can only be called once for every prediction made.")
  }

  raw_data <- readLines(input, n=1)
  data_frame <- read.csv(text=raw_data, sep=',', header=FALSE)
  data <- as.matrix(data_frame)
  DATA_ROW_IN_TRANSIT <<- TRUE

  return(data)
}

# Prints prediction standard out
#
# Use this function for submitting
# your actual prediction
submit_prediction <- function(pred) {
  enable_print()
  write(pred, stdout()) 
  disable_print()

  DATA_ROW_IN_TRANSIT <<- FALSE
}

# Prints to standard error
# 
# Use this for development / debugging
# Output sent to standard error will not
# be scored.
debug_print <- function(msg) {
  message(paste0(capture.output(msg), collapse = "\n"))
}

enable_print <- function() {
  sink()
}

disable_print <- function() {
  if (Sys.info()["sysname"] == "Windows") {
    sink("NUL")
  } else {
    sink("/dev/null")
  }
}

init <- function() {
  disable_print()
}
