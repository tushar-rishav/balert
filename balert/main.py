#! /usr/bin/python
from multiprocessing.dummy import Pool as ThreadPool
from sys import argv, exit


from Bsettings import bpath,SetLevel
from Voice import voice
from BatteryStatus import battery

import argparse,logging


def main():

    parser = argparse.ArgumentParser(description=" \
             Listen the voice of your battery whenever she is low!",epilog="Author:\
             tushar.rishav@gmail.com")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--rate", help="Rate of speaking.(100-200)",
                       type=int)
    group.add_argument("-v", "--vol", help="Volume of speaking.(1.0)",
                       type=str)
    group.add_argument("-l", "--lang", help="Language speaking.(1.0)",
                       type=str)
    group.add_argument("-m", "--msg", help="Alert message of your own",
                       type=str)
    group.add_argument("-c", "--charge", help="Decide the critical charge level",
                       type=int, default=20)
    args = parser.parse_args()
    
    if len(argv) == 1:
        pass
    
    al = voice()
        
    if args.rate:
        al.set_rate(args.rate)
    elif args.vol:
        al.set_vol(args.vol)
    elif args.lang:
        al.set_lang(args.lang)
    elif args.msg:
        al.msg = args.msg
    elif args.charge:
        SetLevel.CHARGE = args.charge
        
    __ = battery()
    _ = __.get_low_battery_warning_level()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(_)
    if _[0] == 0 and _[1]:
        al.msg+="All cool! %d Percent remaining" %_[1]
    elif _[0] == 1:
        al.msg+="Low Battery! %d Percent remaining" %_[1]
    else:
        al.msg+=" Battrey is Charging!"
    print al.msg
    al.speak()




if __name__ == "__main__":
    main()




    
