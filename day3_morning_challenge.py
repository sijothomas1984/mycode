import os

def multilineinput():
    print("Please paste your multi-line input.\n"
          "To end, press ctrl+d on Linux/Mac, ctrl+z on Windows")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return lines

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("nslookup" + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def main():
    switchlist = multilineinput()   # CUSTOMIZE THIS LIST WITH IPs to PING

    ## Use a loop to check each device for ICMP responses
    print("\n***** STARTING ICMP CHECKING *****")
    for x in switchlist:
        if ping_router(x):
            print(f"IP address {x} is responding to ICMP")
        else:
            print(f"IP address {x} is not responding to ICMP")

if __name__ == "__main__":
    main()
