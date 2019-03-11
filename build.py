import sys
import os

def clean():
    files = [
        "*.a",
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
        cmd = "clang -c -x c %s -o %s"%(src_file,obj_name)
        
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
    cmd = "/Library/Developer/CommandLineTools/usr/bin/ld " + link_str
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
    #obj_list.append("-dynamic -dylib -arch x86_64 -macosx_version_min 10.12.0")
    obj_list.append("-demangle")
    obj_list.append("-lto_library /Library/Developer/CommandLineTools/usr/lib/libLTO.dylib")
    obj_list.append("-no_deduplicate -dynamic -arch x86_64 -macosx_version_min 10.12.0")
    obj_list.append("-o out.a")
    obj_list.append("-lSystem /Library/Developer/CommandLineTools/usr/lib/clang/9.0.0/lib/darwin/libclang_rt.osx.a")
    obj_list.append("")
    obj_list.append("")
    obj_list.append("")
    link(obj_list)

if __name__ == "__main__":
    main()