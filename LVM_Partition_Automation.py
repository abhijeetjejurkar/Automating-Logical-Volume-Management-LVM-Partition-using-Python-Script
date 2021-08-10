import os
import getpass


#welcome part start
os.system("tput setaf 5")
print("\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#os.system("espeak-ng Welcome: I am penuuu")
os.system("clear")


os.system("tput setaf 7")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  || A Python Tool to manage LVM ||  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
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


while True:
		os.system("clear")
		print("""
            Press 1 : To Create LVM Partition
            Press 2 : To Increase or Decrease LVM Partition 
	    	Press 3 : To Exit
	    	""")
		ch = int( input("Enter your Choice"))
	    
		if ch==1 :
			os.system('fdisk -l ')
			disk = input("Enter the Name of Disk You want to Use : ")
			os.system('pvcreate {}'.format(disk))
                
			vg = input("Give the Volume Group Name : ")
			os.system('vgcreate {} {} '.format(vg,disk))
                
			lv = input("Give Logical Volume Name : ")
			size = input("Size of Volume : ")
			os.system('lvcreate --size {} --name {} {}'.format(size,lv,vg))
                
			os.system('mkfs.ext4 /dev/{}/{} '.format(vg,lv))
			
			dirr= input("Give the Path Where you want to mount Partiion")      
                
			print(os.system('mount /dev/{}/{} {} '.format(vg,lv,dirr)))
			
		elif ch==2 :
			print("""
	        	press 1: To Increase
	        	press 2: To Decrease""")
                
			chng = int(input("Enter your Choice"))
			vg = input("Enter the Volume Group Name : ")
			lv = input("Enter the Logical Volume Name : ")
			if chng == 1 :
	            		size = input("Enter the Size you want to Increase : ")
	            		cmd = 'lvextend --resizefs --size +{} /dev/{}/{} '.format(size,vg,lv)
        
	            		os.system(cmd)

			if chng == 2:
	            		size = input("Enter Final Size you want After Decreament : ")
	            		cmd = 'lvreduce --resizefs --size {} /dev/{}/{} '.format(size,vg,lv)
	            		os.system(cmd)
    


		elif ch== 3:
			exit()
print("Bye!,Have a Nice Day")
	    