import re
import csv
import operator

def Error_Messages_Report(logfile):
    Error_Msg = {}
    pattern = re.compile(r'.*ERROR ([a-zA-z ]+.+) \([a-zA-z]+\)$')
    try:
        with open(logfile) as file:
            for line in file.readlines():
                match = pattern.search(line)
                if match :
                    errormsg = match.group(1)
                    Error_Msg[errormsg] = Error_Msg.get(errormsg,0) + 1
            file.close()
    except FileNotFoundError:
        print("The provided Log File {} does not exist".format(logfile))
    except Exception as err:
        print("An Error occured {} while processing the log file \n {}".format(type(err),err))
    return Error_Msg


def populate_ErrorMessage_and_UserStatistics_dict():
    Error_Msg = {}
    user_usage = {}

    pattern = re.compile(r'.* ticky: (ERROR|INFO) ([a-zA-z ]+.+) \((.*)\)$')
    try:
        with open('.\\TextFiles\\ServiceLogfile.txt') as file:
            for line in file.readlines():
                match = pattern.search(line)
                msg_type = match.group(1)
                username = match.group(3)
                if msg_type == "ERROR" :
                    errormsg = match.group(2)
                    Error_Msg[errormsg] = Error_Msg.get(errormsg,0) + 1
                    if username in user_usage.keys():
                        user_usage.setdefault(username, {})['error_count'] = user_usage[username].get('error_count',0) + 1
                    else:
                        user_usage.setdefault(username, {})['error_count'] = 1
                elif msg_type == "INFO":
                    if username in user_usage.keys():
                        user_usage.setdefault(username, {})['info_count'] = user_usage[username].get('info_count',0) + 1
                    else :
                        user_usage.setdefault(username, {})['info_count'] = 1
    except FileNotFoundError:
        print("The provided Log File does not exist")
    except Exception as err:
        print("An Error occured {} while processing the log file \n {}".format(type(err),err))
    return Error_Msg,user_usage


def generate_UserStatistics_Report(dictionary, report_file):
    sorted_dict = sorted(dictionary.items(),key=operator.itemgetter(0))
    sorted_dict.insert(0,("Username","INFO","ERROR"))
    try:
        with open(report_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(sorted_dict[0])
            for key,value in sorted_dict[1:]:
                writer.writerow([key,value.get('info_count',0),value.get('error_count',0)])
    except IOError:
        print("Input Output Error")
    except Exception as err:
        print("An Exception Occured while Writing to the File {}",type(err))


def generate_ErrorCount_Report(dictionary, report_file):
    sorted_dict = sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)
    sorted_dict.insert(0,("Error","Count"))
    try:
        with open(report_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(sorted_dict)
    except IOError:
        print("Input Output Error")
    except Exception as err:
        print("An Exception Occured while Writing to the File {}",type(err))
    

def main():
    error_dict,user_usage_dict = populate_ErrorMessage_and_UserStatistics_dict()
    generate_ErrorCount_Report(error_dict,"error_message.csv")
    generate_UserStatistics_Report(user_usage_dict,"user_statistics.csv")

if __name__=="__main__":
    main()