
import os


jackal_logo = '''
   __  ______  ______  __  __  ______  __        
  /\\ \\/\\  __ \\/\\  ___\\/\\ \\/ / /\\  __ \\/\\ \\       
 _\\_\\ \\ \\  __ \\ \\ \\___\\ \\  _"-\\ \\  __ \\ \\ \\____  
/\\_____\\ \\_\\ \\_\\ \\_____\\ \\_\\ \\_\\ \\_\\ \\_\\ \\_____\\ 
\\/_____/\\/_/\\/_/\\/_____/\\/_/\\/_/\\/_/\\/_/\\/_____/ 
                                                 
'''

welcome_test = '''
Let's get started with the Jackal System Installer.

For more information or to get in touch with Jackal\nLabs please head to https://jackalprotocol.com'''

version = "0.0.1"

options = '''
1) Set up full node
2) Set up Storage Provider
'''

def prereqs():
    os.system("apt-get install wget -y")

def fullnode():
    prereqs()
    os.system("wget https://go.dev/dl/go1.18.2.linux-amd64.tar.gz")
    os.system("rm -rf /usr/local/go && tar -C /usr/local -xzf go1.18.2.linux-amd64.tar.gz")
    os.system("echo 'export PATH=$PATH:/usr/local/go/bin' >> /etc/profile")
    os.system("source /etc/profile")
    os.system("go version")
    os.system("git clone https://github.com/JackalLabs/canine-chain.git")
    os.system("cd canine-chain && make install")

option_dict = {
    "1": fullnode
}

def ask():
    print(welcome_test)

    print(options)

    choice = input("> ")

    option_dict[choice]()



    

def main():

    os.system('clear')

    print(jackal_logo)

    ask()


if __name__ == "__main__":
    main()