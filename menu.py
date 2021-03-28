# import all modules
import os
import getpass


#welcome part start
os.system("tput setaf 5")
print("\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#os.system("espeak-ng Welcome: I am penuuu")
os.system("clear")


os.system("tput setaf 7")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || A Python Tool : PYMENUUU ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
os.system("tput setaf 5")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\n\n")
os.system("tput setaf 3")


#authentication part start
password = getpass.getpass("Enter Password : ")
if password != "123":
	print("Incorrect Password..Try again!!")
	exit()
else:
	print("\n\t\t\t\t\tWelcome,Now You can use all our services...\n\n")


#select option locally or remote
print("\t\t\tWhere you want to use the service : locally or remotly")
print("\t\t\tFor Local  : Press l\n\t\t\tFor Remote : Press r\n")
while True:
	option=input()
	if (option!= "l" and option!= "r"):
		print("Nor Supported Option... Again Press(l or r)!! ")
		continue;
	else:
		
		while True:
			os.system("clear")
			os.system("tput setaf 5")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			os.system("tput setaf 7")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || A Python Tool : PYMENUUU ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			os.system("tput setaf 5")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("\n\n\n")
			os.system("tput setaf 5")

			print('''
            \t\t\t\t\t\tPress 1 : To Perform tasks on Linux
            \t\t\t\t\t\tPress 2 : To Use Hadoop Services
            \t\t\t\t\t\tPress 3 : To Use Docker Services
            \t\t\t\t\t\tPress 4 : To Use Cloud Services
            \t\t\t\t\t\tPress 5 : Exit'''
			)
			os.system("tput setaf 3")



			ch=input("Enter Your choice : ")
			if option == "l":
				if int(ch) == 1:
				# linux part
   	 
					while True:

						os.system("clear")
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
						os.system("tput setaf 7")  
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || PYMENUUU : Use Linux OS ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
						print("\n\n\n")
						os.system("tput setaf 6")
    

						# write linux menu
        
						print("""
                               \t\t\t Press 1  : To Configure Yum (Please attach rhel iso image cd/dvd for this)
                               \t\t\t Press 2  : To Setup HTTP Server
                               \t\t\t Press 3  : To Open Text Editor
                               \t\t\t Press 4  : To Start or Stop Firewall Service
                               \t\t\t Press 5  : To Start or Stop SElinux Service
                               \t\t\t Press 6  : To Launch Firefox
                               \t\t\t Press 7  : To Show Calender
                               \t\t\t Press 8  : To Show Date
                               \t\t\t Press 9  : To Open Youtube
                               \t\t\t Press 10 : To Shutdown  
                               \t\t\t Press 11 : To Create LVM Partition
                               \t\t\t Press 12 : To Increase or Decrease LVM Partition 
                               \t\t\t Press 13 : To Exit Local System
	    	               """)

						os.system("tput setaf 3")
						chl=int(input("Enter Your choice : "))
                        
                        #if-condition for linux part

						if chl==1:
							cmd="""wget -O /etc/yum.repos.d/ https://abhihadoop.s3.ap-south-1.amazonaws.com/linux/my.repo?versionId=A8_CXYGNtTwjxTq_aw6dZatONtwhuEjk"""
							print(os.system(cmd))
							print(os.system('yum repolist'))


						elif chl==2:
							print("""****Installing HTTPD****""")
							print(os.system('yum install httpd'))
							print("""****Stoping SElinux*****""")
							print(os.system('setenforce 0'))			
							print("""****Starting Server****""")
							print(os.system('systemctl start httpd'))

						elif chl==3:
							os.system('gedit &')

						elif chl==4:
							st= input("""

                            Press 1 : To Start
                            Press 2 : To Stop

                                """)
							if st==1 :
								print("""****Starting Firewall****""")
								print(os.system('systemctl start firewalld'))

							if st==2 :
								print("""****Stoping Firewall****""")
								print(os.system('systemctl stop firewalld'))

						elif chl==5:
							st= input("""

                            Press 1 : To Start
                            Press 2 : TO Stop

                                """)
							if st==1 :
								print("""****Starting SElinux****""")
								print(os.system('setenforce 1'))

							if st==2 :
								print("""****Stoping SElinux****""")
								print(os.system('setenforce 0'))

						elif chl==6:
							os.system('firefox &')

						elif chl==7:
							os.system('cal ')
							input("Press Enter to Continue")
		
						elif chl==8:
							os.system('date &')
							input("Press Enter to Continue")
		
						elif chl==9:
							os.system('firefox youtube.com &')

						elif chl==10:		
							os.system('sudo init 0')

						elif chl==11:
							os.system('fdisk -l ')
							disk = input("Enter the Name of Disk You want to Use : ")
							os.system('pvcreate {}'.format(disk))
		
							vg = input("Give the Volume Group Name : ")
							os.system('vgcreate {} {} '.format(disk,vg))

							lv = input("Give Logical Volume Name : ")
							size = input("Size of Volume : ")
							os.system('lvcreate --size {} --name {} {}'.format(size,lv,vg))

							os.system('mkfs.ext4 /dev/{}/{} '.format(vg,lv))

							dirr= input("Give the Path Where you want to mount Partiion")      

							print(os.system('mount /dev/{}/{} {} '.format(vg,lv,dirr)))

						elif chl==12 :
							print("""
     		                           press 1: To Increase
                       		         press 2: To Decrease""")
		
							vg = input("Enter the Volume Group Name : ")
							lv = input("Enter the Logical Volume Name : ")

							if chng == 1 :
								size = input("Enter the Size you want to Increase : ")
								cmd = 'lvextend --resizefs --size +{} /dev/{}/{} '.format(size,vg,lv)

								os.system(cmd)

							elif chng == 2:
								size = input("Enter Final Size you want to After Decreament : ")
								cmd = 'lvreduce --resizefs --size {} /dev/{}/{} '.format(size,vg,lv)
								os.system(cmd)

                                        
                                        
						elif chl==13:
							break;
                            
						else:
							print("option not supported")
							input("\nPlease, Enter To Continue...")
							
						input("Press Enter To Continue...")
			






				elif int(ch) == 2:
						#hadoop part starting ...
	
						#desinging -part of hadooop..
					while True:
						os.system("clear")
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
						os.system("tput setaf 7")  
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || PYMENUUU : Use Hadoop Service ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	                        
						print("\n\n\n")
						os.system("tput setaf 6")
    

						# menu for the cloud
						print('''
	                     \t\t\t\tPress 1  : To Create Hadoop Cluster
                        \t\t\t\tPress 2  : To Increase or Decrease the Size of Hadoop DataNode
                        \t\t\t\tPress 3  : To Configure this System as NameNode
                        \t\t\t\tPress 4  : To Configure this System as Client
                        \t\t\t\tPress 5  : To Configure this System as DataNode
                        \t\t\t\tPress 6  : To Exit From the Hadoop service
                        ''')
						chh = int(input("Enter your Choice"))
                        
    
						if chh == 1 :
							print("""Setting up NameNode""")
							#Getting IP form master node
							mip = input("Enter the Ip of NameNode : ")

							#Getting Password from Master node 
							mpass=getpass.getpass("Enter the Password of Master node IP : ")
							cmd = 'ssh {} yum install sshpass -y'.format(mip)
							os.system(cmd)
						
					
							print("""
							*****Download Software on namenode*****
							""")
							input("Press Enter To Continue...")
							
							#Downloading softwares on Master node 
							cmd ='sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/hadoop-1.2.1-1.x86_64.rpm'.format(mpass,mip)
							os.system(cmd)

							cmd="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/jdk-8u171-linux-x64.rpm""".format(mpass,mip)
							os.system(cmd)
					
					
							#Installing Software on Master node
							print("""
							*****Install Software on namenode*****
							 """)
							input("Press Enter To Continue...")  
							cmd = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(mpass,mip)
							print(os.system(cmd))
					
							cmd='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(mpass,mip)
							print(os.system(cmd))


							#Configuring hadoop files for namenode
							print("*****Configuring Hadoop Files for Namenode*****")
							cmd="""sshpass -p {} ssh {} wget -O /etc/hadoop/core-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/core-site.xml""".format(mpass,mip)
							os.system(cmd)

							cmd="""sshpass -p {} ssh {} wget -O /etc/hadoop/hdfs-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/hdfs-site.xml""".format(mpass,mip)
							os.system(cmd)
							cmd ="""sshpass -p {} ssh {} mkdir /nn """.format(mpass,mip)
							os.system(cmd)


							#Stopping Firewall on NameNode
							print("*****Stopping firewall on NameNode*****")
							cmd="""sshpass -p {} ssh {} systemctl stop firewalld""".format(mpass,mip)
							os.system(cmd)

							#Disable Firewall on NameNode
							#cmd='sshpass -p {} ssh {} systemctl disable	firewalld'.format(mpass,mip)
							#os.system(cmd)		

							#Formating Namenode
							print("*****Formating Namenode*****")
							cmd='sshpass -p {} ssh {} hadoop namenode -format'.format(mpass,mip)
							os.system(cmd)

							#Starting Namenode
							cmd='sshpass -p {} ssh {} hadoop-daemon.sh start namenode'.format(mpass,mip)
							os.system(cmd)
							
							print("""
							*****NameNode Started*****
							""")
							input("Press Enter To Continue...")



							print("""

						Setting up Client

						""")
							
							#Getting IP of Client 
							cip = input("Enter the Ip of Client : ")
	
							#Getting Password from client 
							cpass=getpass.getpass("Enter the Password of Client IP : ")
							cmd = 'ssh {} yum install sshpass -y'.format(cip)
							os.system(cmd)


							#Downloading softwares on Client
							print("""
							*****Download Software on Client*****
							""")
							input("Press Enter To Continue...") 
							cmd ="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/hadoop-1.2.1-1.x86_64.rpm""".format(cpass,cip)
							os.system(cmd)

							cmd="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/jdk-8u171-linux-x64.rpm""".format(cpass,cip)
							os.system(cmd)
							input("Press Enter To Continue...")


							#Installing Software on Client
							print("""
							*****Install Software on Client***** 
							""")
							input("Press Enter To Continue...")  
							cmd = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(cpass,cip)
							print(os.system(cmd))

							cmd='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(cpass,cip)
							print(os.system(cmd))
							input("Press Enter To Continue...")

                                #Configuring hadoop files for Client
							print("*****Configuring Hadoop Files for Client*****")
							cmd="""wget -O /core-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/core-site.xml"""
							os.system(cmd)

							with open('/core-site.xml') as f:
								newText=f.read().replace('0.0.0.0', mip)
							with open('/core-site.xml',"w") as f:
								f.write(newText)

							os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(cpass,cip))
							
							print("""
							***Client Configuration Completed***
							""")
							input("Press Enter To Continue...")



							print("""

                            Setting up DataNode

					""")
							dno=int(input("How Many Data Nodes You Have"))
							dnip=[]	
							dnpass=[]
							for i in range(0,dno) :
								dip=input("Enter the Ip of DataNode {} ".format(i+1))
								dnip.append(dip)
								dpass=getpass.getpass("Enter Password of DataNode {} ".format(i+1))
								dnpass.append(dpass)

                                        #Downloading Software on DataNode
								print("""
								*****Download Software on DataNode*****
								""")
								input("Press Enter To Continue...")
								
								cmd="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/hadoop-1.2.1-1.x86_64.rpm""".format(dpass,dip)
								os.system(cmd)
	
								cmd="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/jdk-8u171-linux-x64.rpm""".format(dpass,dip)
								os.system(cmd)
								
								
											
                                        #Installing Software on DataNode
								print("""
								*****Install Software on DataNode*****
								""")
								input("Press Enter To Continue...")
								cmd = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(dpass,dip)
								print(os.system(cmd))
		
								cmd='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(dpass,dip)
								print(os.system(cmd))	
								

			
								print("""How Much Space Should be given by this DataNode to Cluster
                                                Press 1 : Use the Same Disk of System
                                                Press 2 : Attach new disk""")
								alc = int(input("Enter Choice : "))

								if alc == 1 :
									os.system('sshpass -p {} ssh {} rm -rf /data '.format(dpass,dip))
									os.system('sshpass -p {} ssh {} mkdir /data '.format(dpass,dip))
							
								elif alc == 2 :
									os.system('sshpass -p {} ssh {} fdisk -l '.format(dpass,dip))
									disk = input("Enter the Name of Disk You want to Use : ")
									os.system('sshpass -p {} ssh {} pvcreate {}'.format(dpass,dip,disk))

									vg = input("Give the Volume Group Name : ")
									os.system('sshpass -p {} ssh {} vgcreate {} {} '.format(dpass,dip,disk,vg))

									lv = input("Give Logical Volume name Name : ")
									size = input("Size of Volume : ")
									os.system('sshpass -p {} ssh {} lvcreate --size {} --name {} {}'.format(dpass,dip,size,lv,vg))

									os.system('sshpass -p {} ssh {}  mkfs.ext4 /dev/{}/{} '.format(dpass,dip,vg,lv))

									os.system('sshpass -p {} ssh {} rm -rf /data '.format(dpass,dip))
									os.system('sshpass -p {} ssh {} mkdir /data'.format(dpass,dip))


									os.system('sshpass -p {} ssh {} mount /dev/{}/{} /data '.format(dpass,dip,vg,lv))


									#Configuring hadoop file on DataNode
								print("*****Configuring hadoop file on DataNode*****")
								os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(dpass,dip))

								os.system('sshpass -p {} ssh {} rm -rf /data '.format(dpass,dip))
								os.system('sshpass -p {} ssh {} mkdir /data '.format(dpass,dip)) 
								cmd="""sshpass -p {} ssh {} wget -O /etc/hadoop/hdfs-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/DataNode/hdfs-site.xml""".format(dpass,dip)				
								os.system(cmd)

								#Stopping Firewall of DataNode
								print("*****Stopping Firewall of DataNode*****")
								os.system('sshpass -p {} ssh {} systemctl stop firewalld'.format(dpass,dip))

								#Disable Firewall of DataNode
								#os.system('sshpass -p {} ssh {} systemctl disable firewalld'.format(dpass,dip))		

								#Starting DataNode
								print("*****Starting DataNode*****")
								os.system('sshpass -p {} ssh {} hadoop-daemon.sh start datanode'.format(dpass,dip))
								print("""
								***DataNode Started***
								""")
								input("Press Enter To Continue...")
							
							print("""
							
							***Hadoop Cluster Created***
							
							""")	
							input("Press Enter To Continue...")


	    
						elif chh == 2 :
							print("""
							press 1: To Increase
							press 2: To Decrease """)
					
							chng=int(input("Enter your choice : "))
							dip=input("Enter the Ip of DataNode : ")
							dpass=getpass.getpass("Enter Password of DataNode : ")
							cmd = 'ssh {} yum install sshpass -y'.format(dip)
							os.system(cmd)

							vg = input("Enter the Volume Group Name : ")
							lv = input("Enter the Logical Volume Name : ")

							if chng == 1 :
								size = input("Enter the Size you want to Increase : ")
								cmd = 'sshpass -p {} ssh {} lvextend --resizefs --size +{} /dev/{}/{} '.format(dpass,dip,size,vg,lv)

								os.system(cmd)

							if chng == 2:
								size = input("Enter Final Size you want to After Decreament : ")
								cmd = 'sshpass -p {} ssh {} lvreduce --resizefs --size {} /dev/{}/{} '.format(dpass,dip,size,vg,lv)
								os.system(cmd)
								
							input("Press Enter To Continue...")


    
						elif chh == 3 :
							#Downloading softwares on Master node 
					
							print("*****Downloading Software*****")
							cmd ="""wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/hadoop-1.2.1-1.x86_64.rpm"""
							os.system(cmd)

							cmd="""wget -O /root/jdk-8u171-linux-x64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/jdk-8u171-linux-x64.rpm"""
							os.system(cmd)
        
        
							#Installing Software on Master node
							print("*****Installing Software***** ")  
							cmd = 'rpm -ivh /root/jdk-8u171-linux-x64.rpm'
							print(os.system(cmd))

							cmd='rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'
							print(os.system(cmd))
							#Configuring hadoop files for namenode
							print("*****Configuring Hadoop Files for Namenode*****")
							cmd="""wget -O /etc/hadoop/core-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/core-site.xml"""
							os.system(cmd)
							cmd="""wget -O /etc/hadoop/hdfs-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/hdfs-site.xml"""			
							os.system(cmd)

							cmd ="""mkdir /nn """
							os.system(cmd)

							#Stopping Firewall on NameNode
							print("*****Stopping firewall on NameNode*****")
							cmd="""systemctl stop firewalld"""
							os.system(cmd)

							#Disable Firewall on NameNode
							#cmd='systemctl disable firewalld'.format(mpass,mip)
							#os.system(cmd)		

							#Formating Namenode
							print("*****Formating Namenode*****")
							cmd='hadoop namenode -format'
							os.system(cmd)
        
							#Starting Namenode
							cmd='hadoop-daemon.sh start namenode'
							os.system(cmd)
							
							input("Press Enter To Continue...")



    
	               
        
						elif chh == 4 :
							#Downloading softwares on Client
							print("*****Downloading Software*****") 
							cmd ="""wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/hadoop-1.2.1-1.x86_64.rpm"""
							os.system(cmd)

							cmd="""wget -O /root/jdk-8u171-linux-x64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/jdk-8u171-linux-x64.rpm"""
							os.system(cmd)
        
        
							#Installing Software on Client
							print("*****Installing Software***** ")  
							cmd = 'rpm -ivh /root/jdk-8u171-linux-x64.rpm'
							print(os.system(cmd))

							cmd='rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'
							print(os.system(cmd))

							#Configuring hadoop files for Client
							print("*****Configuring Hadoop Files for Client*****")
							cmd="""wget -O /etc/hadoop/core-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/core-site.xml"""
							os.system(cmd)

							mip = input("Enter the IP of NameNode : ")
							with open('/etc/hadoop/core-site.xml') as f:
								newText=f.read().replace('0.0.0.0', mip)
							with open('/etc/hadoop/core-site.xml',"w") as f:
								f.write(newText)
					
							input("Press Enter To Continue...")						
					
					
						elif chh == 5 :
							#Downloading Software on DataNode
							print("""
							*****Download Software*****
							""")
							input("Press Enter To Continue...")
							cmd="""wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/hadoop-1.2.1-1.x86_64.rpm"""
							os.system(cmd)
            
							cmd="""wget -O /root/jdk-8u171-linux-x64.rpm https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/software/jdk-8u171-linux-x64.rpm"""
							os.system(cmd)			

							#Installing Software on DataNode
							print("""
							*****Install Software*****
							""")
							input("Press Enter To Continue...")
							cmd = 'rpm -ivh /root/jdk-8u171-linux-x64.rpm'
							print(os.system(cmd))
		
							cmd='rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'
							print(os.system(cmd))	
		
							print("""How Much Space Should be given by this DataNode to Cluster
	        	                        Press 1 : Use the Same Disk of System
	        	                        Press 2 : Attach new disk""")
							alc = int(input("Enter Choice : "))
						
							if alc == 1:
								os.system('rm -rf /data ')
								os.system('mkdir /data')							
							
							elif alc == 2 :
								os.system('fdisk -l ')
								disk = input("Enter the Name of Disk You want to Use : ")
								os.system('pvcreate {}'.format(disk))

								vg = input("Give the Volume Group Name : ")
								os.system('vgcreate {} {} '.format(disk,vg))

								lv = input("Give Logical Volume name Name : ")
								size = input("Size of Volume : ")
								os.system('lvcreate --size {} --name {} {}'.format(size,lv,vg))

								os.system('mkfs.ext4 /dev/{}/{} '.format(vg,lv))

								os.system('rm -rf /data ')
								os.system('mkdir /data')

								os.system('mount /dev/{}/{} /data '.format(vg,lv))
		

							#Configuring hadoop file on DataNode
							print("*****Configuring hadoop file on DataNode*****")
							cmd="""wget -O /etc/hadoop/core-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/NameNode/core-site.xml"""
							os.system(cmd)
					
							mip = input("Enter the IP of NameNode : ")
							with open('/etc/hadoop/core-site.xml') as f:
								newText=f.read().replace('0.0.0.0', mip)
							with open('/etc/hadoop/core-site.xml',"w") as f:
								f.write(newText)
            
							cmd="""wget -O /etc/hadoop/hdfs-site.xml https://abhihadoop.s3.ap-south-1.amazonaws.com/hadoop/DataNode/hdfs-site.xml"""
							os.system(cmd)
            
							#Stopping firewall of DataNode
							print("*****Stopping Firewall of DataNode*****")
							os.system('systemctl stop firewalld')
			
							#Disable Firewall of DataNode
							#os.system('systemctl disable firewalld')		
		
							#Starting DataNode
							print("*****Starting DataNode*****")
							os.system('hadoop-daemon.sh start datanode')
							
							print("""
							***Datanode Started***
							""")
							
							input("Press Enter To Continue...")
            
						elif chh == 6 :
							break;
						else:
							print("option not supported")
							input("\nPlease, Enter To Continue...")
						input("Press Enter To Continue...")
                            
            
                
                
				elif int(ch) == 3 :
					#docker code started here...
					while True:
	
						os.system("clear")
						os.system("tput setaf 6")

						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
						os.system("tput setaf 7")  
				
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || PYMENUUU : Use Docker Service ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
						print("\n\n\n")
						os.system("tput setaf 6")
					

						# menu for docker code
						print('''
                        \t\t\t\tPress 1 : To See running Docker container 
                        \t\t\t\tPress 2 : To See All Docker container Present
                        \t\t\t\tPress 3 : To See images present 
                        \t\t\t\tPress 4 : To Launch a Docker container
                        \t\t\t\tPress 5 : To Remove a running Docker Container 
                        \t\t\t\tPress 6 : To Delete a image
                        \t\t\t\tPress 7 : To download image from Docker Hub
                        \t\t\t\tPress 8 : To Configure Web server inside Docker Container
                        \t\t\t\tPress 9 : To fetch the logs of container
                        \t\t\t\tPress 10: Exit From Docker Service''')

						os.system("tput setaf 3")
						chd=input("Enter Your choice : ")
						#if-condition for docker service

						if int(chd) == 1:
							# see the container
							os.system("docker ps")
		                        
						elif int(chd) == 2:
							#see all docker container
							os.system("docker ps -a")
		                        
						elif int(chd) == 3:
							#to see image present
							os.system("docker images")
		                        
						elif int(chd) == 4:
							#to launch a docker container
							name = input("Enter the name of container: ")
							print("\t\t\tAvaliable Imges :-")
							print(os.system("docker images"))
							img = input("Enter the image name: ")
							print(""" \t\t\t Where You want to launch the docker container :
                                Background : Press 'b' 
                                Foreground : Press 'f' """)
							optiond = input("choose a option: ")
                            
							if optiond == 'b':
								os.system("docker run -dit --name {0} {1}".format(name,img))
							elif optiond == 'f' :
								os.system("docker run -it --name {0} {1}".format(name,img))
							else:
								print("Incorrect option..")
                           
						elif int(chd) == 5:
							#to remove a runnning docker container
							print("\t\t\tRunning Containers")
							os.system("docker ps")
							name=input("Enter Container name you want to remove :")
							os.system("docker rm -f {0}".format(name))
		                           
		                           
						elif int(chd) == 6:
							#to remove a image
							printf("\t\tImage Present in system")
							os.system("docker images")
							name=input("Enter Image name you want to remove :")								
							os.system("docker rmi -f {0}".format(name))
							
					
						elif int(chd) == 7:
						#to pull a docker image
							name=input("Enter image name ")
							os.system("docker pull {0}".format(name))
                           
						elif int(chd) == 8:
							#to fetch the logs of container
							print("\t\tRunning Container: ")
							os.system("docker ps")
							name=input("Enter the Container Name :")
							os.system("docker logs {0}".format(name))
                           
                            
						elif int(chd) == 9:
							#to configure web server inside docker container
							print("will update soon...")
		                       
		                            
						elif int(chd) == 10:
							break;
						else:
							print("option not supported")
							input("\nPlease, Enter To Continue...")
						
						input("\nPlease, Enter To Continue...")
		
                
            
				elif int(ch) == 4:
					#cloud part starting ..
					#desinging part of cloud
						while True:
		
							os.system("clear")
							os.system("tput setaf 6")
							print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
							os.system("tput setaf 7")  
							print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || PYMENUUU : Use Cloud Service ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
							os.system("tput setaf 6")
							print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        
							print("\n\n\n")
							os.system("tput setaf 6")
    

							# menu for the cloud
							print('''
                        \t\t\t\tPress 1  : To login in AWS account 
                        \t\t\t\tPress 2  : To launch a EC instance
                        \t\t\t\tPress 3  : To create security Pair
                        \t\t\t\tPress 4  : To create Key-Pair
                        \t\t\t\tPress 5  : To create a EBS Volume
                        \t\t\t\tPress 6  : To attach EBS with EC2 instance
                        \t\t\t\tPress 7  : To create S3 Bucket
                        \t\t\t\tPress 8  : To upload object in S3 Bucket
                        \t\t\t\tPress 9  : To create CloudFront Distribution
                        \t\t\t\tPress 10 : To show EC2 instances 
                        \t\t\t\tPress 11 : To show EBS Volume
                        \t\t\t\tPress 12 : To show security-pair
                        \t\t\t\tPress 13 : To show key-pair
                        \t\t\t\tPress 14 : To show bucket present in S3 
                        \t\t\t\tPress 15 : To create IAM User
                        \t\t\t\tPress 16 : Exit From Cloud Service''')

							os.system("tput setaf 3")
							cch=input("Enter Your choice : ")
               
							#if-condition for cloud part

							if int(cch) == 1:
								#login in aws 
								os.system("aws configure")
		                        
							elif int(cch)== 2:
								#launch instance
								print('''
                            \t\t\tAvailabe AMI :--
                            \t\t\t1. Amazon Linux 2 AMI : Press 'a'
                            \t\t\t2. Red Hat Enterprise Linux 8  : Press 'b'
                            \t\t\t3. Microsoft Windows Server 2019 Base : Press 'c'       
         		                   ''')
								imcode=input("give code  of AMI(a/b/c) : ")
								if imcode=="a":
									img="ami-0e306788ff2473ccb"
								elif imcode=="b":
									img="ami-052c08d70def0ac62"
								else:
									img="ami-0b2f6494ff0b07a0e"
								instype=input("Give instance type : ")
								count=input("How many instance you want to launch : ")
								keypair=input("Give name of key-pair : ")
								sg=input("give name of secutity-group : ")
								os.system("aws ec2 run-instances  --image-id  {0}  --instance-type  {1}  --key-name {2} --count {3} --security-group-ids {4}".format(img,instype,keypair,count,sg))                              
                        
							elif int(cch)== 3:
								#create security group
								sgname=input("Enter Security group name :")
								sgdesc=input("Enter Security Description :")

								os.system("aws ec2 create-security-group  --group-name {0} --description {1}".format(sgname,sgdesc))

							elif int(cch)== 4:
         		                   #create key pair
								keyname=input("Enter Key name :")
								os.system("aws ec2 create-key-pair --key-name {0}".format(keyname)) 
                            

							elif int(cch)== 5:
								#create EBS volume
								size=input("Enter the size of volume in GB :")
								az=input("Enter Availability-zone :")
								os.system("aws ec2 create-volume --size {0}  --availability-zone  {1}".format(size,az))
                        
							elif int(cch)== 6:
								#attach EBS with EC2
								instid=input("Enter Instance Id :")
								volid=input("Enter Volume Id :")
								dev=input("Enter Device name :")
								os.system("aws ec2 attach-volume  --instance-id {0}  --volume-id {1}  --device {2}".format(instid,volid,dev))
                            
							elif int(cch)== 7:
								#create s3 bucket
								bucketname = input("Enter Bucket name :")
								os.system("aws s3 mb s3://{0}".format(bucketname))
                        
							elif int(cch) == 8:
								#upload object in s3
								#not complete ...soon complete
								filelocation = input("Enter path of files :")
								bucketname = input("Enter Bucket name :")
								extension = input("Extension of file wants to add :")
								#os.system("aws s3 cp {0}  s3://{1}/ --recursive --include "*.jpg"  --acl public-read-write")
                        
							elif int(cch)== 9:
								#create cloudfront distribution
								print("code here")
         		               
							elif int(cch)== 10:
								#show ec2 instance
								instid = input("Enter instance id :")
								os.system("aws ec2 describe-instances --instance-ids {0}".format(instid))
                        
							elif int(cch)== 11:
								#show ebs volume
								volid = input("Enter EBS Volume id :")
								os.system("aws ec2 describe-volumes --volume-ids {0}".format(volid))
                            
                        
							elif int(cch)== 12:
								#show secutiy pair
								sgname = input("Enter security-group name :")
								os.system("aws ec2 describe-security-groups  --group-name {0}".format(sgname))

                        
							elif int(cch)== 13:
								#show key pair
								keyname = input("Enter keyname :")
								os.system("aws ec2 describe-key-pairs --key-names {0}".format(keyname))
						
							elif int(cch)== 14:
								#show bucket present in s3
								os.system("aws s3 ls")
		
							elif int(cch)== 15:
								#To create IAM User
								print("will update soon...")
		
							elif int(cch) == 16:
								break;
							else:
								print("option not supported")
								input("\nPlease, Enter To Continue...")
							input("\nPlease, Enter To Continue...")
		
		
		                    
		
				elif int(ch) == 5:
						#exit
						exit()
			        
				else:
						print("Choose again..Option Not supported!!")
						input("Press Enter To Continue...")
		
				input("Press Enter To Continue...")
				
				#remote login code started here...  
		            
			else:
				if int(ch) == 1:
					dip=input("Enter the IP : ")
					dpass=getpass.getpass("Enter Password : ")
					cmd = 'ssh {} yum install sshpass -y'.format(dip)
					os.system(cmd)
				# linux code
					while True:

						os.system("clear")
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
						os.system("tput setaf 7")  
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || PYMENUUU : Use Linux OS (Remote) ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					
						os.system("tput setaf 6")
						print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					
						print("\n\n\n")
						os.system("tput setaf 6")
    

						os.system("tput setaf 3")
						
					
					
						# write linux menu
						print("""
                               \t\t\t Press 1  : To Configure Yum (Please attach rhel iso image cd/dvd for this)
                               \t\t\t Press 2  : To Setup HTTP Server
                               \t\t\t Press 3  : To Start or Stop Firewall Service
                               \t\t\t Press 4  : To Show Calender
                               \t\t\t Press 5  : To Show Date
                               \t\t\t Press 6  : To Shutdown  
                               \t\t\t Press 7  : To Create LVM Partition
                               \t\t\t Press 8  : To Increase or Decrease LVM Partition 
                               \t\t\t Press 9 : To Exit Remote System
					""")

        
                        

					
                        
						chr = int( input("Enter your Choice"))
		        	

						if chr==1:
							cmd="""sshpass -p {} ssh {}  wget -O /etc/yum.repos.d/ https://abhihadoop.s3.ap-south-1.amazonaws.com/linux/my.repo?versionId=A8_CXYGNtTwjxTq_aw6dZatONtwhuEjk""".format(dpass,dip)
							print(os.system(cmd))
							print(os.system('sshpass -p {} ssh {} yum repolist'.format(dpass,dip)))


						elif chr==2:
							print("""****Installing HTTPD****""")
							print(os.system('sshpass -p {} ssh {} yum install httpd'.format(dpass,dip)))
							print("""****Stoping SElinux*****""")
							print(os.system('sshpass -p {} ssh {} setenforce 0'.format(dpass,dip)))			
							print("""****Starting Server****""")
							print(os.system('sshpass -p {} ssh {} systemctl start httpd'.format(dpass,dip)))
	
						elif chr==3:
							st= input("""
	
								Press 1 : To Start
								Press 2 : To Stop

							""")
							if st==1 :
								print("""****Starting Firewall****""")
								print(os.system('sshpass -p {} ssh {} systemctl start firewalld'.format(dpass,dip)))

							if st==2 :
								print("""****Stoping Firewall****""")
								print(os.system('sshpass -p {} ssh {} systemctl stop firewalld'.format(dpass,dip)))

						elif chr==4:
							print(os.system('sshpass -p {} ssh {} cal '.format(dpass,dip)))
							
						elif chr==5:
							print(os.system('sshpass -p {} ssh {} date &'.format(dpass,dip)))
							
						elif chr==6:
							print(os.system('sshpass -p {} ssh {} sudo init 0'.format(dpass,dip)))

						elif chr==7:
							os.system('sshpass -p {} ssh {} fdisk -l '.format(dpass,dip))
							disk = input("Enter the Name of Disk You want to Use : ")
							os.system('sshpass -p {} ssh {} pvcreate {}'.format(dpass,dip,disk))

							vg = input("Give the Volume Group Name : ")
							os.system('sshpass -p {} ssh {} vgcreate {} {} '.format(dpass,dip,disk,vg))
	
							lv = input("Give Logical Volume Name : ")
							size = input("Size of Volume : ")
							os.system('sshpass -p {} ssh {} lvcreate --size {} --name {} {}'.format(dpass,dip,size,lv,vg))
	
							os.system('sshpass -p {} ssh {} mkfs.ext4 /dev/{}/{} '.format(dpass,dip,vg,lv))

							dirr= input("Give the Path Where you want to mount Partiion")      

							print(os.system('sshpass -p {} ssh {} mount /dev/{}/{} {} '.format(dpass,dip,vg,lv,dirr)))

						elif chr==8 :
							print("""
	                                press 1: To Increase
	                                press 2: To Decrease""")
	
							vg = input("Enter the Volume Group Name : ")
							lv = input("Enter the Logical Volume Name : ")
	
							if chng == 1 :
								size = input("Enter the Size you want to Increase : ")
								cmd = 'sshpass -p {} ssh {} lvextend --resizefs --size +{} /dev/{}/{} '.format(dpass,dip,size,vg,lv)
	
								os.system(cmd)
	
							if chng == 2:
								size = input("Enter Final Size you want to After Decreament : ")
								cmd = 'sshpass -p {} ssh {} lvreduce --resizefs --size {} /dev/{}/{} '.format(dpass,dip,size,vg,lv)
								os.system(cmd)
	
	
	
						elif chr==9:
							break;
						else:
							print("Choose again..Option Not supported!!")
		

							input("\nPlease,Enter To Continue....")
						input("Press Enter To Continue...")
	                            
	
	
	
				elif int(ch) == 2:
					#hadoop code here.
					print("remote hadoop code here")
	
				elif int(ch) == 3:
					#docker code 
					print("remote docker task")
	
				elif int(ch) == 4:
					#cloud 
					print("In cloud no use of remote : Press l to continue..")
	
				elif int(ch) == 5:
					#exit
					exit();
	        
				else:
					print("Choose again..Option Not supported!!")
	
	
					input("\nPlease,Enter To Continue....")

				input("Press Enter To Continue...")




    


