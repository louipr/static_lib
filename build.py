import sys
import os

def clean():
    files = [
        "*.exe",
        "*.obj"
    ]
    for fname in files:
        cmd = "rm %s"%(fname)
        print(cmd)
        if(os.system(cmd)):
            print("Aborting clean process")

def compile(compile_list):
    for src_file in compile_list:
        obj_name = src_file.split(".")[0] + ".obj"
        cmd = "gcc -c -g %s -o %s"%(src_file,obj_name)
        print(cmd)
        if(os.system(cmd)):
            print("Aborting compile process!")
            sys.exit(1)

def staticlib(obj_file):
    cmd = "ar rcs libout.a %s %s"%(obj_file,"C:\cygwin64\lib\libc.a")
    print(cmd)
    if(os.system(cmd)):
        print("Aborting staticlib process!")
        sys.exit(1)        

def link(obj_list):
    link_str = " ".join(obj_list)
    cmd = "ld -o out.exe " + link_str
    print(cmd)
    if(os.system(cmd)):
        print("Aborting link process")
        sys.exit(1)


def main():
    clean()
    compile_list = [
        "main.c"
        # "add.c",
        # "sum.c"
    ]
    compile(compile_list)
    # staticlib("main.obj")

    obj_list = [src_file.split(".c")[0] + ".obj" for src_file in compile_list]
    # obj_list = [obj_file for obj_file in obj_list if obj_file != "main.obj"]
    obj_list.append("-L/usr/lib/gcc/x86_64-pc-cygwin/7.3.0")
    #obj_list.append("-L/usr/x86_64-pc-cygwin/lib")
    #obj_list.append("-L/usr/lib")
    obj_list.append("-L/lib")
    obj_list.append("-lc")
    obj_list.append("-lgcc_s")
    obj_list.append("-lgcc")
    obj_list.append("-lcygwin")
    obj_list.append("-ladvapi32")
    obj_list.append("-lshell32")
    obj_list.append("-luser32")
    obj_list.append("-lkernel32")
    # obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/../../../../lib/default-manifest.o")
    # obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/../../../../lib/crt0.o")
    # obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/crtbegin.o")
    # obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/crtend.o")
    #obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/cyglto_plugin.dll") 
    #WinMainCRTStartup
    #obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/collect2.exe") 
    # obj_list.append("/usr/lib/gcc/x86_64-pc-cygwin/7.3.0/lto-wrapper.exe") 
    # obj_list.append("--entry WinMainCRTStartup")
    # obj_list.append("-nodefaultlib")
    link(obj_list)

if __name__ == "__main__":
    main()