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
import tkinter as tk
#The built-in python GUI framework

#XML RPC client server interaction: https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server
class MyXMLRPCServer(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)	
	
'''
Function server_details specifies servers' attributes namely IP address, port number and client associated functions.
INPUT: Servers' IP address, port number and client associated functions.
OUTPUT: Server is instantiated and starts running forever.
'''
	
def server_details():
    server = SimpleXMLRPCServer(('127.0.0.1', 2346), requestHandler = MyXMLRPCServer, allow_none = True)
    print("Server up and running on port 2346")
    rpcgui.entry.insert(tk.END, "Server window "+ "\n")
	
    server.register_introspection_functions()
    server.register_function(connected_clients, "connected_clients")
    server.register_function(receive_updates, "receive_updates")
    server.register_function(consistent_files, "consistent_files")
    server.serve_forever()
	
file_update = ''
#A global variable which takes in file updates from the associated client and will be modified in file_update finction

'''
Function connected_clients connects multiple clients to server
INPUT: Unique client name from client
OUTPUT: Server accepts requesting clients displays clients name onto GUI
'''

def connected_clients(client_name):
    print("Connected with " + client_name)
    rpcgui.entry.insert(tk.END, "Connected with " + client_name + "\n")
    return "Connected with server as " + client_name

'''
Function receive_updates receives the file updates from client when the file is modified
INPUT: File updates from clients.
OUTPUT: File updates being accepted and Invalidation requests being sent to clients.
'''
	
def receive_updates(updates):
    global file_update
    file_update = updates
    rpcgui.entry.insert(tk.END, "Update received and Invalidation requests being sent to clients" + "\n")
    return "Invalidation request from server"

'''
Function consistent_files instructs clients to correct their conflicts
OUTPUT: Instruction to clients to correct their conflicts
'''
	
def consistent_files():
    rpcgui.entry.insert(tk.END, "Instructing clients to update" + "\n")
    return(file_update)

'''
Class MyXMLRPCGUI has three functions in it:
init method initialises the Tkinter frame, a entry and packs it
start_XMLRPCServer forks out a thread and to start start_XMLRPCServer method which in-turn starts up my XMLRPC Server
'''
	
class MyXMLRPCGUI(tk.Tk):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entry = tk.Text(self.master)
        self.entry.pack()
		
    def start_XMLRPCServer(self):
        self.new_thread = Thread(target = server_details)
        self.new_thread.start()
	
'''
The main method creates a object rpcgui, for the MyXMLRPCServer class and uses it to start our XMLRPCServer
'''
	
if __name__ == "__main__":
    root = tk.Tk()
    rpcgui = MyXMLRPCGUI(root)
    rpcgui.start_XMLRPCServer()
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