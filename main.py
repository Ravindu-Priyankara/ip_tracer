#! usr/bin/env python3

try:
    from modules.user_loc import *
    from modules.color_codes import *
except Exception as error:
    print(error.__class__.__name__+":"+error.message)
class Main:
    global cmd
    global banner
    global user_data

    def main():
        #create a banner

        #find my details
        user_data()

    def banner():
        pass
    def user_data():
        user_detail = get_location()

        list = ["ip","city","region","region_code","country_code","country_code_iso3","country_name","country_capital","country_tld","continent_code","in_eu","postal","latitude","longitude","timezone","utc_offset","country_calling_code","currency","currency_name","languages","asn","org"]

        for x in range(len(list)):
            print(f"{BRIGHT_YELLOW} your {list[x]} is: {BRIGHT_MAGENTA}{user_detail[list[x]]}\n")
    
    def cmd():
        pass
    
if __name__ == '__main__':
    mainClass = Main
    mainClass.main()