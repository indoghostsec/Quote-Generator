#!usr/bin/env/python2.7
#coding:utf-8

"""
OPEN SOURCE : Jika ingin membuat sebuah quote dengan melihat kode ini
 Saya selaku pembuat tools ini mengizinkan anda untuk berkarya lebih
 tools ini sengaja tidak dienkripsi agar kalian bisa kembangkan
 sendiri jika ada kesalahan kinerja hubungi : 081223617054



 Author		:	SuhandiGhost
 Team		:	INDOGHOSTSEC
 Website	:	http://www.indoghostsec.my.id
 Support	:	X-Revan-AR, Ghost666include, Hz3666ghost & All Members
 Contact	:	ghostsuhandi@gmail.com

"""


import os, sys, time, re
try:
	import requests
	
except:
	os.system("pip2 install requests")
	


logo = """  \033[1;97m                                         
               `:+shdmNMMMMNmdhs+:`               
           `/ymNds+:-.`    `.-:+sdNNy/`           
        `/dMdo-                    -odMd/`        
      `oNNo.                          .oNNo`      
     :NN+                                +Nm:     
    oMh`                                  `hMo    
   oMy           +oooo+    +oooo+           yMo   
  :Md           `NMMMMN`  `NMMMMN`           dM:  
  hM:           `NMMMMN`  `NMMMMN`           :Mh  
  NM            `NMMMMN`  `NMMMMN`            MN  
  NM               .MMm      .MMm             MN  
  hM:             `dMM+     `dMM+            :Mh  
  :Md            sNMN+     sNMN+             dM:  
   oMy          `Nmo`     `Nmo`             yMo   
    oMd.         `         `              `hMo    
     :mNo`                               +Nm:     
       +mNs.                          .oNNo`      
         :hMd                      -odMd/         
          -Md     //-.`    `.-:+sdNmy/`           
         `mM-  `/mNhdmNNMMNNmdhs+:`               
        `dMo:+hNmo`\033[101m\033[1;77m:: Coded By Suhandi ::\033[0m\033[1;97m
       -mMNmds+.                                  """
       
       
def Main():
	os.system("clear")
	print(logo)
	print("\n------------------------------------")
	Tanya()
	
def Tanya():
	nama = raw_input("\033[1;97m[+] Nama Kamu : \033[1;93m")
	if nama == "index":
		print("\033[1;97m[\033[1;91m!\033[1;97m] Nama index tidak diizinkan!")
		Tanya()
	else:
		link = raw_input("\033[1;97m[+] Link Gambar : \033[1;93m")
		quote = raw_input("\033[1;97m[+] Quote Kamu : \033[1;93m")
		ck = nama.replace(" ", "-")
		file = ck + ".html"
		print("\033[1;97m\n------------------------------------")
		print("[+] Memuat Link Url ...")
		time.sleep(3)
		print("[+] Mengirim Data Strings..")
		time.sleep(3)
		a = []
		c = "1"
		requests.post("https://qoutes-online.000webhostapp.com/index.php?nama="+nama+"&quote="+quote+"&link="+link+"&buat=")
		for i in range(100):
			a.append(c)
			sys.stdout.write("\r\033[1;97m[+] Uploading .. : \033[1;93m" + str(len(a)) + "%")
			sys.stdout.flush()
			time.sleep(0.09)
			
		print("\033[1;97m\n[+] Upload Succes!")
		print("[+] Link Quote : \033[1;93mhttps://qoutes-online.000webhostapp.com/hasil/" + file)
		index = '''

<!doctype html>
<html lang="en">
  <head> <!-- https://quotes-online.000webhostapp.com -->
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.75, shrink-to-fit=no">
    <meta name="description" content="quote online generators">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Mali:400i,700i" rel="stylesheet" type="text/css">
    <link rel="icon" href="https://images4.alphacoders.com/220/220444.jpg" type="image/jpg">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <title>''' + nama + '''</title>
    <style>
    	html,body,.container{
    		background: url('''+ link +''') no-repeat center center/cover;
    		position: fixed;
    		margin: auto; 
    		height: 100%;
    		top: 0; bottom: 0; left: 0; right:0;
    	}
    	.page{
    		position: absolute;
    		margin: auto;
    		height: 50%;
    		top: 0; bottom: 0; left: 0; right:0;
    	}
    	.mek{
    		background-color:rgba(0,0,0,0.4);
    	}
    	h1{
    		transform:rotate(-12deg); 
    		-moz-transform:rotate(-12deg); 
    		-webkit-transform:rotate(-12deg); 
    		-o-transform:rotate(-12deg);
    		font-family: "Mali";
    		font-size: 2em;
    		font-weight: bold;
    		margin-bottom: 15%;
    	}
    	h5{
    		font-family: "Mali";
    	}
    	.logo{
    		text-decoration: none;
    		color: white;
    		font-size: 22px;
    		margin: 10px;
    	}
    	.logo:hover{
    		text-decoration: none;
    		color: white;
    		cursor: pointer;
    	}
    	.hastag{
    		text-decoration: none;
    		color: white;
    	}
    	#footer{ 
    		text-decoration: none;
    		padding-top: 150%;
    		color: white;
    		margin: auto;
    		font-family: "Mali";
    		position: fixed;
    	}
    </style>
  </head>
  <body>
    <div class="container">
    	<div class="page">
    		<h1 class="text-center text-white">- ''' + nama + ''' -</h1>
    		
    		<div class="mek">
    		<h5 class="text-center text-white mb-3"><hr>''' + quote + '''<hr></h5>
    	</div>
    	<footer><center> 
    		<a class="logo" href="">
    			<i class="fab fa-whatsapp"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fab fa-hackerrank"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fab fa-github"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fas fa-globe"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fab fa-blogger"></i>
    		</a>
    		</center></footer>
    </div>
<div id="footer">©2k20 INDOGHOSTSEC</div>
</html>'''
		vm = open(file, "w")
		vm.write(index)
		vm.close()
		print("\033[1;97m[+] Downloading file ..")
		time.sleep(5)
		print("[+] File : \033[1;93m/sdcard/"+ file)
		os.system("cp -f "+file+" /sdcard")
		print("\n\033[1;97m------------------------------------")
		sys.exit()
	
	
	
try:
	Main()
except KeyboardInterrupt:
	sys.sexit()
except EOFError:
	sys.exit()
except requests.exceptions.ConnectionError:
	print("\033[1;97m[!] Koneksi anda tidak stabil")
	sys.exit()
