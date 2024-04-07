#开发者：远渡
#开发时间：2023/5/31 19:42

import sys
import socket
import queue
import threading
import argparse
import re
import ipaddress

def TCP_p0rt_5erver_name(port):#获取TCP端口服务名称函数
    try:
        result=socket.getservbyport(port,"tcp")#获取TCP下指定端口对应的服务名
        return result
    except Exception as e:
        return "None"

def UDP_p0rt_5erver_name(port):#获取UDP端口服务名称函数
    try:
        result=socket.getservbyport(port,"udp")#获取UDP下指定端口对应的服务名
        return result
    except Exception as e:
        return "None"

def C0nnect_UDP_P0rt(DestIP,DestPort,timeout):#UDP端口连接函数，用于向目标端口发送信息，接受回包来判断目标UDP端口是否开启
    buffer=1024#缓冲区
    data="He110 W0r1d".encode("UTF-8")
    try:
        UDP_c0nnect=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP数据报
        UDP_c0nnect.settimeout(timeout)#设置超时时间
        UDP_c0nnect.sendto(data,(DestIP,DestPort))#UDP无协议连接，使用sendto()函数发送信息
        data,(ip,port)=UDP_c0nnect.recvfrom(buffer)#接收返回数据
        UDP_c0nnect.close()
        if data:
            print("回包数据:",data)
            return 0#未出现timeout则视目标UDP端口开放
    except Exception as e:
        UDP_c0nnect.close()
        return -1#出错超时则视目标UDP端口关闭


def Get_p0rt_l15t5(_5tart_p0rt,end_p0rt,top=None):#获取常用端口列表函数
    T0p1000_l15t=[1,3,6,9,13,17,19,20,21,22,23,24,25,30,32,37,42,49,53,70,79,80,81,82,83,84,88,89,99,106,109,110,113,
                  119,125,135,139,143,146,161,163,179,199,211,222,254,255,259,264,280,301,306,311,340,366,389,406,416,
                  425,427,443,444,458,464,481,497,500,512,513,514,524,541,543,544,548,554,563,587,593,616,625,631,636,
                  646,648,666,667,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800,808,843,873,880,888,
                  898,900,901,902,911,981,987,990,992,995,999,1000,1001,1007,1009,1010,1021,1022,1023,1024,1025,1026,
                  1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,
                  1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,
                  1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,
                  1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1102,1104,1105,1106,1107,1110,1111,
                  1112,1113,1117,1119,1121,1122,1123,1126,1130,1131,1137,1141,1145,1147,1148,1151,1154,1163,1164,1165,
                  1169,1174,1183,1185,1186,1192,1198,1201,1213,1216,1217,1233,1236,1244,1247,1259,1271,1277,1287,1296,
                  1300,1309,1310,1322,1328,1334,1352,1417,1433,1443,1455,1461,1494,1500,1503,1521,1524,1533,1556,1580,
                  1583,1594,1600,1641,1658,1666,1687,1700,1717,1718,1719,1720,1723,1755,1761,1782,1801,1805,1812,1839,
                  1862,1863,1875,1900,1914,1935,1947,1971,1974,1984,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,
                  2008,2009,2013,2020,2021,2030,2033,2034,2038,2040,2041,2042,2045,2046,2047,2048,2065,2068,2099,2103,
                  2105,2106,2111,2119,2121,2126,2135,2144,2160,2170,2179,2190,2196,2200,2222,2251,2260,2288,2301,2323,
                  2366,2381,2382,2393,2399,2401,2492,2500,2522,2525,2557,2601,2604,2607,2638,2701,2710,2717,2725,2800,
                  2809,2811,2869,2875,2909,2920,2967,2998,3000,3003,3005,3006,3011,3013,3017,3030,3052,3071,3077,3128,
                  3168,3211,3221,3260,3268,3283,3300,3306,3322,3323,3324,3333,3351,3367,3369,3370,3371,3389,3404,3476,
                  3493,3517,3527,3546,3551,3580,3659,3689,3703,3737,3766,3784,3800,3809,3814,3826,3827,3851,3869,3871,
                  3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000,4001,4002,4003,4004,4005,4045,4111,
                  4125,4129,4224,4242,4279,4321,4343,4443,4444,4445,4449,4550,4567,4662,4848,4899,4998,5000,5001,5002,
                  5003,5009,5030,5033,5050,5054,5060,5080,5087,5100,5101,5120,5190,5200,5214,5221,5225,5269,5280,5298,
                  5357,5405,5414,5431,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678,5718,5730,5800,5801,
                  5810,5815,5822,5825,5850,5859,5862,5877,5900,5901,5902,5903,5906,5910,5915,5922,5925,5950,5952,5959,
                  5960,5961,5962,5987,5988,5998,5999,6000,6001,6002,6003,6004,6005,6006,6009,6025,6059,6100,6106,6112,
                  6123,6129,6156,6346,6389,6502,6510,6543,6547,6565,6566,6580,6646,6666,6667,6668,6689,6692,6699,6779,
                  6788,6792,6839,6881,6901,6969,7000,7001,7004,7007,7019,7025,7070,7100,7103,7106,7200,7402,7435,7443,
                  7496,7512,7625,7627,7676,7741,7777,7800,7911,7920,7937,7999,8000,8001,8007,8008,8009,8010,8021,8031,
                  8042,8045,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8093,8099,8180,8192,8193,8200,8222,8254,
                  8290,8291,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651,8654,8701,8800,8873,8888,8899,8994,9000,
                  9001,9002,9009,9010,9040,9050,9071,9080,9090,9099,9100,9101,9102,9110,9200,9207,9220,9290,9415,9418,
                  9485,9500,9502,9535,9575,9593,9594,9618,9666,9876,9877,9898,9900,9917,9929,9943,9968,9998,9999,10000,
                  10001,10002,10003,10009,10012,10024,10082,10180,10215,10243,10566,10616,10621,10626,10628,10778,11110,
                  11967,12000,12174,12265,12345,13456,13722,13782,14000,14238,14441,15000,15002,15003,15660,15742,16000,
                  16012,16016,16018,16080,16113,16992,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,
                  19842,20000,20005,20031,20221,20828,21571,22939,23502,24444,24800,25734,26214,27000,27352,27355,27715,
                  28201,30000,30718,30951,31038,31337,32768,32769,32770,32771,32772,32773,32774,32775,32776,32777,32778,
                  32779,32780,32781,32782,32783,32784,33354,33899,34571,34572,35500,38292,40193,40911,41511,42510,44176,
                  44442,44501,45100,48080,49152,49153,49154,49155,49156,49157,49158,49159,49160,49163,49165,49167,49175,
                  49400,49999,50000,50001,50002,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,
                  54045,54328,55055,55555,55600,56737,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,
                  65000,65129,65389]
    T0p100_l15t=[7,9,13,21,22,25,37,53,79,80,88,106,110,113,119,135,139,143,179,199,389,427,443,444,465,513,514,543,548,
                 554,587,631,646,873,990,993,995,1025,1026,1027,1028,1110,1433,1720,1723,1755,1900,2000,2049,2121,2717,
                 3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000,6646,
                 7070,8000,8008,8080,8443,8888,9100,9999,32768,49152,49153,49154,49155,49156]
    T0p50_l15t=[21,22,25,53,80,110,113,135,139,143,179,199,443,445,465,514,548,554,587,646,993,995,1025,1026,1433,1720,
                1723,2000,3306,3389,5060,5666,5900,6001,8000,8008,8080,8443,8888,10000,32768,49152,49154]
    if (top!=None):#指定了top列表则按top列表返回
        if (top==50):
            return T0p50_l15t
        elif (top==100):
            return T0p100_l15t
        else:
            return T0p1000_l15t
    else:#指定了扫描端口范围则start port-end port
        return list(range(_5tart_p0rt,end_p0rt+1))

def Get_IP_l15t5(_5tart_IP,end_IP):#获取IP地址列表函数
    startIP=ipaddress.ip_address(_5tart_IP)#ip_address()可自动检测是IPv4还是IPv6地址
    endIP=ipaddress.ip_address(end_IP)
    IP_list=[]
    while startIP<=endIP:
        IP_list.append(str(startIP))
        startIP+=1
    return IP_list

def Port_judge(port):#端口合法性判断函数
    if port in range(0,65536):
        return True
    else:
        print("Port is invalid!")
        return False

def IP_judge(ip):#IP地址合法性判断函数
    pattern=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')#re正则匹配IP地址
    if pattern.match(ip):
        return True
    else:
        return False

class Multi_p0rt_mode_P0rt5caner(object):#多端口模式扫描类
    class P0rt5can(threading.Thread):#继承了threading模块的Thread类，对run方法进行了重写
        def __init__(self, port_queue, ip, timeout=3):#初始化参数
            threading.Thread.__init__(self)
            self.__port_queue=port_queue
            self.__ip=ip
            self.__timeout=timeout
        def run(self):#一旦此类被调用，此方法中的代码自动运行
            while True:
                if self.__port_queue.empty():#如果port队列不空则继续运行
                    break
                p0rt=self.__port_queue.get(timeout=0.5)#从port队列中取出队首的port
                IP=self.__ip
                t1me0ut=self.__timeout
                try:
                    TCP_c0nnect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#TCP流
                    TCP_c0nnect.settimeout(t1me0ut)#设置超时时间
                    re5u1t_c0de_TCP=TCP_c0nnect.connect_ex((IP,p0rt))#TCP端口开启情况
                    re5u1t_c0de_UDP=C0nnect_UDP_P0rt(IP,p0rt,t1me0ut)#UDP端口开启情况
                    if re5u1t_c0de_TCP==0 and re5u1t_c0de_UDP!=0:#TCP端口开启，UDP端口关闭
                        s1="% 6d [OPEN]       TCP\n"%p0rt
                        TCP_5erver_name=TCP_p0rt_5erver_name(p0rt)
                        s2="                    %s\n"%TCP_5erver_name
                        sys.stdout.write(s1)
                        sys.stdout.write(s2)
                    if re5u1t_c0de_TCP!=0 and re5u1t_c0de_UDP==0:#TCP端口关闭，UDP端口开启
                        s1="% 6d [OPEN]               UDP\n"%p0rt
                        UDP_5erver_name=UDP_p0rt_5erver_name(p0rt)
                        s2="                          %s\n"%UDP_5erver_name
                        sys.stdout.write(s1)
                        sys.stdout.write(s2)
                    if re5u1t_c0de_TCP==0 and re5u1t_c0de_UDP==0:#TCP端口和UDP端口均开启
                        s1="% 6d [OPEN]      TCP      UDP\n"%p0rt
                        TCP_5erver_name=TCP_p0rt_5erver_name(p0rt)
                        UDP_5erver_name=UDP_p0rt_5erver_name(p0rt)
                        s2="                  {0}       {1}\n".format(TCP_5erver_name,UDP_5erver_name)
                        sys.stdout.write(s1)
                        sys.stdout.write(s2)
                    if re5u1t_c0de_TCP!=0 and re5u1t_c0de_UDP!=0:#TCP端口和UDP端口均关闭
                        s1="% 6d [CLOSE]                  \n"%p0rt
                        sys.stdout.write(s1)
                except Exception as e:
                    print(e)
                    break
                finally:
                    TCP_c0nnect.close()

class Multi_IP_mode_P0rt5caner(object):#多主机模式扫描类
    class P0rt5can(threading.Thread):#继承了threading模块的Thread类，对run方法进行了重写
        def __init__(self, ip_queue, port_list, timeout=3):#初始化参数
            threading.Thread.__init__(self)
            self.__ip_queue=ip_queue
            self.__port=port_list
            self.__timeout=timeout
        def run(self):#一旦此类被调用，此方法中的代码自动运行
            while True:
                if self.__ip_queue.empty():#如果IP队列不空则继续运行
                    break
                IP=self.__ip_queue.get(timeout=0.5)#从IP队列中取出队首的IP
                p0rt_list=self.__port
                t1me0ut=self.__timeout
                for p0rt in p0rt_list:
                    try:
                        TCP_c0nnect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#TCP流
                        TCP_c0nnect.settimeout(t1me0ut)#设置超时时间
                        re5u1t_c0de_TCP=TCP_c0nnect.connect_ex((IP,p0rt))#TCP端口开启情况
                        re5u1t_c0de_UDP=C0nnect_UDP_P0rt(IP,p0rt,t1me0ut)##UDP端口开启情况
                        if re5u1t_c0de_TCP==0 and re5u1t_c0de_UDP!=0:#TCP端口开启，UDP端口关闭
                            s1=" {0} [OPEN]    {1}     TCP\n".format(IP,p0rt)
                            TCP_5erver_name=TCP_p0rt_5erver_name(p0rt)
                            s2="                                 %s\n"%TCP_5erver_name
                            sys.stdout.write(s1)
                            sys.stdout.write(s2)
                        if re5u1t_c0de_TCP!=0 and re5u1t_c0de_UDP==0:#TCP端口关闭，UDP端口开启
                            s1=" {0} [OPEN]   {1}             UDP\n".format(IP,p0rt)
                            UDP_5erver_name=UDP_p0rt_5erver_name(p0rt)
                            s2="                                        %s\n"%UDP_5erver_name
                            sys.stdout.write(s1)
                            sys.stdout.write(s2)
                        if re5u1t_c0de_TCP==0 and re5u1t_c0de_UDP==0:#TCP端口和UDP端口均开启
                            s1=" {0} [OPEN]   {1}     TCP     UDP\n".format(IP,p0rt)
                            TCP_5erver_name=TCP_p0rt_5erver_name(p0rt)
                            UDP_5erver_name=UDP_p0rt_5erver_name(p0rt)
                            s2="                                {0}     {1}\n".format(TCP_5erver_name,UDP_5erver_name)
                            sys.stdout.write(s1)
                            sys.stdout.write(s2)
                        if re5u1t_c0de_TCP!=0 and re5u1t_c0de_UDP!=0:#TCP端口和UDP端口均关闭
                            s1=" {0} [CLOSE]   {1}                \n".format(IP,p0rt)
                            sys.stdout.write(s1)
                    except Exception as e:
                        print(e)
                        break
                    finally:
                        TCP_c0nnect.close()


def running(args,mode):#运行函数
    if mode=="00" or mode=="01":#单主机扫描模式
        if mode=="00":#单主机指定端口号扫描
            IP=args.IP#获取指定IP
            top=args.top_list
            if top!=None:#指定了top则优先使用top
                p0rt_list=Get_p0rt_l15t5(0,65535,top)#根据top获取端口list
            else:
                p0rt_list=args.port#获取指定端口列表
            t1me0ut=3#设置超时时间
            for p0rt in p0rt_list:
                if Port_judge(p0rt)!=1:#如果用户输入的端口不合法则不扫描该端口
                    sys.stdout.write("%d端口不合法"%p0rt)
                else:
                    try:
                        TCP_c0nnect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#TCP流
                        TCP_c0nnect.settimeout(t1me0ut)
                        re5u1t_c0de_TCP=TCP_c0nnect.connect_ex((IP,p0rt))#TCP端口开启情况
                        re5u1t_c0de_UDP=C0nnect_UDP_P0rt(IP,p0rt,t1me0ut)#UDP端口开启情况
                        if re5u1t_c0de_TCP==0 and re5u1t_c0de_UDP!=0:#TCP端口开启，UDP端口关闭
                            s1="% 6d [OPEN]       TCP\n"%p0rt
                            TCP_5erver_name=TCP_p0rt_5erver_name(p0rt)
                            s2="                    %s\n"%TCP_5erver_name
                            sys.stdout.write(s1)
                            sys.stdout.write(s2)
                        if re5u1t_c0de_TCP!=0 and re5u1t_c0de_UDP==0:#TCP端口关闭，UDP端口开启
                            s1="% 6d [OPEN]               UDP\n"%p0rt
                            UDP_5erver_name=UDP_p0rt_5erver_name(p0rt)
                            s2="                           %s\n"%UDP_5erver_name
                            sys.stdout.write(s1)
                            sys.stdout.write(s2)
                        if re5u1t_c0de_TCP==0 and re5u1t_c0de_UDP==0:#TCP端口和UDP端口均开启
                            s1="% 6d [OPEN]      TCP      UDP\n"%p0rt
                            TCP_5erver_name=TCP_p0rt_5erver_name(p0rt)
                            UDP_5erver_name=UDP_p0rt_5erver_name(p0rt)
                            s2="                   {0}       {1}\n".format(TCP_5erver_name,UDP_5erver_name)
                            sys.stdout.write(s1)
                            sys.stdout.write(s2)
                        if re5u1t_c0de_TCP!=0 and re5u1t_c0de_UDP!=0:#TCP端口和UDP端口均关闭
                            s1="% 6d [CLOSE]                   \n"%p0rt
                            sys.stdout.write(s1)
                    except Exception as e:
                        print(e)
                    finally:
                        TCP_c0nnect.close()
        elif mode=="01":#单主机指定端口段扫描
            p0rt_5cner=Multi_p0rt_mode_P0rt5caner()#实例化一个Multi_p0rt_mode_P0rt5caner()类
            p0rt_queue=queue.Queue()#实例化一个Queue()类
            thread_num=args.thread#线程数量
            threads=[]#保存新线程
            ip=args.IP#扫描的IP
            _5tart_p0rt=args.start_port#起始端口
            end_p0rt=args.end_port#结束端口
            top=args.top_list#取端口top数
            if top!=None:#指定了top则优先使用top
                port_list=Get_p0rt_l15t5(_5tart_p0rt,end_p0rt,top)#根据top获取端口list
            elif Port_judge(_5tart_p0rt) and Port_judge(end_p0rt):#如果起始端口和结束端口均合法
                port_list=Get_p0rt_l15t5(_5tart_p0rt,end_p0rt,top)#根据起始端口号和结束端口号获取端口list
            else:#若起始端口和结束端口任意一个非法则终止程序
                print("Program was terminated unexpectedly!")
                exit()
            for port in port_list:#对port列表进行遍历，将先遍历到的先入队
                p0rt_queue.put(port)
            for t in range(thread_num):
                threads.append(p0rt_5cner.P0rt5can(p0rt_queue,ip,timeout=3))#将实例化后的P0rt5can加入到threads列表中
            for thread in threads:#启动线程
                thread.start()
                thread.join(0.01)#设置阻塞时间（单位:s，默认阻塞到主进程结束），此处阻塞时间短时同一端口显示在一起，阻塞时间长时同一IP显示在一起
    elif mode=="10" or mode=="11":#多主机扫描模式
        if mode=="10":#多主机指定端口号扫描
            p0rt_5cner=Multi_IP_mode_P0rt5caner()#实例化一个Multi_IP_mode_P0rt5caner()类
            IP_queue=queue.Queue()#实例化一个Queue()类
            thread_num=args.thread#线程数量
            threads=[]#保存新线程
            top=args.top_list  #取端口top数
            if top!=None:#指定了top则优先使用top
                p0rt_list=Get_p0rt_l15t5(0,65535,top)#根据top获取端口list
            else:
                p0rt_list=args.port#获取端口列表
            start_IP=args.start_multi_IP#获取起始IP
            end_IP=args.end_multi_IP#获取结束IP
            if IP_judge(start_IP) and IP_judge(end_IP):#如果起始IP地址和结束IP地址均合法
                IP_list=Get_IP_l15t5(start_IP,end_IP)#根据起始IP地址和结束IP地址获取IP地址列表
            else: #若起始IP地址和结束IP地址任意一个非法则终止程序
                print("Program was terminated unexpectedly!")
                exit()
            for IP in IP_list:#对IP列表进行遍历，将先遍历到的先入队
                IP_queue.put(IP)
            for t in range(thread_num):
                threads.append(p0rt_5cner.P0rt5can(IP_queue,p0rt_list,timeout=3))#将实例化后的P0rt5can加入到threads列表中
            for thread in threads:#启动线程
                thread.start()
                thread.join(0.1)#测试了一下，这里0.1最适合，设置阻塞时间（单位:s，默认阻塞到主进程结束），用于确保扫描完一个IP再去扫描下一个IP。作用不大，因为影响程序运行时间的主要为目标端口。
        elif mode=="11":#多主机指定端口段扫描
            start_IP=args.start_multi_IP#起始IP地址
            end_IP=args.end_multi_IP#结束IP地址
            if IP_judge(start_IP) and IP_judge(end_IP):#如果起始IP地址和结束IP地址均合法，则获取IP地址列表
                IP_list=Get_IP_l15t5(start_IP,end_IP)
            for IP in IP_list:#这里采取以IP地址为准对每个端口进行线程扫描
                sys.stdout.write("Scanning IP address : %s\n"%IP)
                p0rt_5cner=Multi_p0rt_mode_P0rt5caner()#实例化一个Multi_p0rt_mode_P0rt5caner()类
                p0rt_queue=queue.Queue()#实例化一个Queue()类
                thread_num=args.thread#线程数量
                threads=[]#保存新线程
                top=args.top_list#取端口top数
                _5tart_p0rt=args.start_port#起始端口
                end_p0rt=args.end_port#结束端口
                if top!=None:#指定了top则优先使用top
                    port_list=Get_p0rt_l15t5(_5tart_p0rt,end_p0rt,top)#根据top获取总端口list
                elif Port_judge(_5tart_p0rt) and Port_judge(end_p0rt):#如果起始端口和结束端口均合法
                    port_list=Get_p0rt_l15t5(_5tart_p0rt,end_p0rt,top)#根据参数获取总端口list
                else:#若起始端口和结束端口任意一个非法则终止程序
                    print("Program was terminated unexpectedly!")
                    exit()
                for port in port_list:#对port列表进行遍历，将先遍历到的先入队
                    p0rt_queue.put(port)
                for t in range(thread_num):
                    threads.append(p0rt_5cner.P0rt5can(p0rt_queue,IP,timeout=3))
                for thread in threads:#启动线程
                    thread.start()
                    thread.join()#这里如果不使用默认阻塞会导致子程序都没结束主程序就全部开始，输出会非常混乱。设置阻塞时间（单位:s，默认阻塞到主进程结束），用于确保扫描完一个IP再去扫描下一个IP。作用不大，因为影响程序运行时间的主要为目标端口回应速度


def _0rDer5_Get():#获取用户命令函数
    parser=argparse.ArgumentParser(description="Usage of program")
    parser.add_argument("-m","--mode",metavar="MODE",type=str,default="00",choices=["00","01","10","11"],required=True,help="Running mode(00:Single Host-Single Port;01:Single Host-Multi Port;10:Multi Host-Single Port;11:Multi Host-Multi Port)")
    parser.add_argument("-ip","--IP",metavar="IPADRESS",type=str,default="127.0.0.1",help="Single Host scaning mode destination IP address")
    parser.add_argument("-smip","--start_multi_IP",metavar="START_MULTI_IP_ADDRESS",type=str,default="192.168.0.0",help="Multi Host scaning mode,Start destination IP address")
    parser.add_argument("-emip","--end_multi_IP",metavar="END_MULTI_IP_ADDRESS",type=str,default="192.168.255.255",help="Multi Host scaning mode,End destination IP address")
    parser.add_argument("-p","--port",metavar="PORT",type=int,default=80,nargs='*',help="Single Port scaning mode,Destination host port")
    parser.add_argument("-sp","--start_port",metavar="START_PORT",type=int,default=1,help="Multi Port scaning mode,Start destination port (1~65534)")
    parser.add_argument("-ep","--end_port",metavar="END_PORT",type=int,default=65535,help="Multi Port scaning mode,End destination port (2~65535)")
    parser.add_argument("-t","--thread",metavar="THREAD",type=int,default=100,help="The number of threads")
    parser.add_argument("-top","--top_list",metavar="TOP",type=int,default=None,choices=[50,100,1000],help="Top port lists")
    args=parser.parse_args()
    return args

def main():#主函数
    print("===============Welcome to use port scaner===============")
    args=_0rDer5_Get()#获取用户命令
    running(args,args.mode)


if __name__=='__main__':
    main()