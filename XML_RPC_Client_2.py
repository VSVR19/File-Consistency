'''
Student Name: Venkata Ramana Voddam Pudi Sankar
Student ID: 1001614404
'''

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
#imports for XML RPC Client and Server functionallity 
import os
from threading import Thread
import time
import tkinter as tk
#The built-in python GUI framework
import sys

#XML RPC client server interaction: https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
class MyXMLRPCClient(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
	
client_name = 'Client 2'
#Unique client name for this client which will be displayed at the server

'''
Function client_details reads data from clients and it pauses for a 10 second interval.
It then again reads the file
If any diffrence, its propagted to server and process it.
INPUT: Update made to the tect file by user
OUTPUT: Updates propagated to the serevr and files made consistent
'''
	
def client_details():
    try:
        s = xmlrpc.client.ServerProxy('http://localhost:2346')
		#Client connects at localhost, port 2346
        rpcgui.entry.insert(tk.END, "Client 2 welcomes you! "+ "\n")
        rpcgui.entry.insert(tk.END, s.connected_clients(client_name) + "\n")
		#The clients name is transmitted to server here.
    
        while True:
            f = open("C:\\Users\\Venkat\\Desktop\\DS Assignment 2\\Client 2\\AS2_File.txt", "r")
            file_data = f.read()
			#The clients' file is read here for the first time.
		
            while True:
                time.sleep(10)
				#Pausing the code for 10 seconds
			
                f_sleep = open("C:\\Users\\Venkat\\Desktop\\DS Assignment 2\\Client 2\\AS2_File.txt", "r")
                file_data_sleep = f_sleep.read()
				#The clients' file is read here after sleep for any updates                
			
                if file_data == file_data_sleep:
                    rpcgui.entry.insert(tk.END, "No modifications made to the file" + "\n")
                elif file_data != file_data_sleep:
                    rpcgui.entry.insert(tk.END,"Modifications made to the file" + "\n")
                #This if block determines whether the file has been updated or not    
                    rpcgui.entry.insert(tk.END,s.receive_updates(file_data_sleep) + "\n")
					#The file updates are sent to server here.
				
                    rpcgui.entry.insert(tk.END,"Pulling updates from server" + "\n")
                    update_from_server = s.consistent_files()
					#Client pulls updates from server
				
                    rpcgui.entry.insert(tk.END,"Updating local copy" + "\n")
					#The clients local copy is to be updated
				
                    for i in range(1, 4):
                        f = open("C:\\Users\\Venkat\\Desktop\\DS Assignment 2\\Client " + str(i) + "\\AS2_File.txt", "r+")
                        f.write(update_from_server)
                        f.truncate()
						#Truncating makes sure that updates are overwritten, not simply appended
                        f.close()
				
                    break
				
                break
            
    except:
        print("Errors caught")
        sys.exit(0)
		#Exception handler to catch any errors
		
'''
Class MyXMLRPCGUI has three functions in it:
init method initialises the Tkinter frame, entry and packs it
start_XMLRPCClient forks out a thread and to start start_XMLRPCClient method which in-turn starts up my XMLRPC Client
disconnect_XMLRPCClient methods disconnects this particular client from server
'''
		
class MyXMLRPCGUI(tk.Tk):
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entry = tk.Text(self.master)
        self.entry.pack()        
        self.master.protocol('WM_DELETE_WINDOW', self.disconnect_XMLRPCClient)
		#init method initialises the Tkinter frame, entry and packs it
		
    def start_XMLRPCClient(self):
        self.new_thread = Thread(target = client_details)
        self.new_thread.start()
		#start_XMLRPCClient forks out a thread and to start start_XMLRPCClient method which in-turn starts up my XMLRPC Client
		
    def disconnect_XMLRPCClient(self):        
        self.master.destroy()
        sys.exit(0)
		#disconnect_XMLRPCClient methods disconnects this particular client from server
		
'''
Class MyXMLRPCGUI has three functions in it:
init method initialises the Tkinter frame, a entry and packs it
start_XMLRPCClient forks out a thread and to start start_XMLRPCClient method which in-turn starts up my XMLRPC Client
disconnect_XMLRPCClient methods disconnects this particular client from server
'''
		
if __name__ == "__main__":
    root = tk.Tk()
    rpcgui = MyXMLRPCGUI(root)
    rpcgui.start_XMLRPCClient()
    root.mainloop()
	
'''
REFERENCES:
https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch09s07.html
https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
https://scorython.wordpress.com/2016/06/27/multithreading-with-tkinter/
https://docs.python.org/3/library/_thread.html
http://thepythonguru.com/python-strings/
https://automatetheboringstuff.com/chapter8/
https://www.reddit.com/r/learnpython/comments/2rpk0k/how_to_update_your_gui_in_tkinter_after_using/
https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
https://stackoverflow.com/questions/5503445/why-cant-xmlrpc-client-append-item-to-list-accessable-via-xmlrpc-server-procedu#
https://docs.python.org/3/library/xmlrpc.html
https://www.guru99.com/reading-and-writing-files-in-python.html
https://stackoverflow.com/questions/11469228/python-replace-and-overwrite-instead-of-appending#
http://stupidpythonideas.blogspot.com/2013/10/why-your-gui-app-freezes.html
https://www.odoo.com/forum/help-1/question/error-while-trying-to-connect-to-xml-rpc-solved-94868
https://stackoverflow.com/questions/49220464/passing-arguments-in-tkinters-protocolwm-delete-window-function-on-python#
'''