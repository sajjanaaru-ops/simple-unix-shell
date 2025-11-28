import sys #used to get the standard output"$""
import os #used to read,write,check the files and directories
import subprocess #used to run the programs
import shlex #used for parsing the command ,a better form of string.spilt().
def command_location(text):
    path=os.environ.get('PATH')
    strip=text.strip()
    if strip.startswith('type'):
        text=strip[5:]
    if not path:
        if strip.startswith('type'):
            print(f'{strip[5:]}: not found')
            
        #print(f'{text}: not found')
        return
    path_dir=path.split(os.pathsep)
    ex_dir=['.exe','.cmd','.bat','.com']
    for d in path_dir:
        if not d:   #to skip empty directories i.e if the path ends with a separator.
            continue
        fullpath=os.path.join(d,text)
        if os.path.exists(fullpath) and os.access(fullpath,os.X_OK):
            if strip.startswith('type'):
                print(f'{strip[5:]} is {fullpath}')
            
            #print(f'{text} is {fullpath}')
            return fullpath

        for ext in ex_dir:
            fullpath_with_ext=fullpath+ext
            if os.path.exists(fullpath_with_ext) and os.access(fullpath_with_ext,os.X_OK):
                if strip.startswith('type'):
                    print(f'{strip[5:]} is {fullpath_with_ext}')
                
                #print(f'{text} is {fullpath_with_ext}')
                return fullpath_with_ext       
    if strip.startswith('type'):
        print(f'{strip[5:]}: not found')

def exe_external_command(command_parts):#commandparts is a list containing the program name and arguments
    program_name=command_parts[0]
    if '/' in program_name:
        exe_path=program_name
    else:
        exe_path=command_location(program_name)
    if exe_path:
        try:
            subprocess.run(command_parts,check=False)
        except Exception as e:
            print(f'shell: execution error: {e}',file=os.sys.stderr)
    else:
        print(f'{program_name}: command not found')        







builtin=['type','echo','exit','pwd','cd']
def main():
    while True:
        sys.stdout.write("$ ")
        pass
        command = input()
        k=command.strip()
        parts=shlex.split(command)
        command_parts=shlex.split(command)
    
        
        if k.startswith('echo'):
            if k.startswith("echo '") or k.startswith('echo "'):
                text=shlex.split(command)
                m=' '.join(text[1:])
                print(m)
                
            else:
                t=command.split()
                m=' '.join(t[1:]) 
                print(m)  
        elif k.startswith('exit'):
            sys.exit()
        elif k.startswith('type'):
            text=k[5:]
            if k[5:] in builtin:
                print(f'{text} is a shell builtin') 
            else:
                command_location(command)
        elif command_parts[0] not in builtin :
            exe_external_command(command_parts)
        elif k.startswith('pwd'):
            sys.stdout.write(os.getcwd() + "\n")
            sys.stdout.flush() 
        elif k.startswith('cd'):
            pathdir=k[3:]
            if pathdir=='~':
                HOME=os.path.expanduser('~')
                os.chdir(HOME)
            
            elif os.path.isdir(pathdir):
                os.chdir(pathdir)
                
            else:
                print(f'cd: {pathdir}: No such file or directory')    
        else:
            errormsg(command)   

       
        
        
        
        

        
def errormsg(command):
    print(f"{command}: command not found")
            
       

if __name__ == "__main__":
    main()
