import sys
import datetime

if __name__ == '__main__':

    #enter name and word 'date'/'time'/'datetime' . you will get greeting and date/time/datetime

    if len(sys.argv)!=3:
        print('invalid count of arguents',file=sys.stderr)
        sys.exit(1)
    else:
        print(f"hello,{sys.argv[1]}")
        if sys.argv[2]=='date':
            print(datetime.date.today())

        elif sys.argv[2]=='datetime':
            print(datetime.datetime.now())
        else:
            print('invalid 2nd arg',file=sys.stderr)
            sys.exit(1)

