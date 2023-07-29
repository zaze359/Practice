#include <stdio.h>
#include <unistd.h>

// 需要在Linux中编译运行, windows 无法使用fork()创建子进程
int main() 
{
    pid_t pid = fork();
    if(pid == 0) {
        printf("----- in child\n");
        printf("child pid=%d; retrun %d\n", getpid(), pid);
    } else {
        printf("----- in parent\n");
        printf("parent pid=%d; retrun %d\n", getpid(), pid);
    }
}
