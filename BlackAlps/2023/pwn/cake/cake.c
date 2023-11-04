#include <errno.h>
#include <grp.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <time.h>
#include <unistd.h>

static void reap(int sig) {
    int saved_errno = errno;
    waitpid(-1, NULL, WNOHANG);
    errno = saved_errno;
}

int authenticate(int fd) {
    char *correct_password = "GLaDOS";
    char password[100] = {};

    char *password_pointer = password;
    char input_char;

    while(1){
        ssize_t read_return = read(fd, &input_char, 1);
        if (read_return <= 0 || input_char == '\n') {
            break;
        }
        *password_pointer = input_char;
        password_pointer++;
    }

    return !strcmp(password, correct_password);
}

void welcome(int fd) {
    char *message;

    srand(time(NULL));

    int a = rand();
    int b = rand();
    int c = rand();
    int d = rand();
    int e = rand();

    unsigned int subject_number = (unsigned int) (a+b+c+d+e) % 1000;

    char subject_number_string[100];
    snprintf(subject_number_string, 100, "%d", subject_number);

    message = "Welcome to the Aperture Science Enrichment Center.\nYou are subject number ";
    write(fd, message, strlen(message));
    write(fd, subject_number_string, strlen(subject_number_string));
    message = ".\n";
    write(fd, message, strlen(message));

    message = "Please enter your password to access the cake:";
    write(fd, message, strlen(message));

    int authenticated = authenticate(fd);

    if (authenticated) {
        message = "The cake is a lie!\n";
        write(fd, message, strlen(message));
    } else {
        message = "You are not authorized to access the cake :(\n";
        write(fd, message, strlen(message));
    }
}

void drop_privileges() {
    if (getuid() == 0) {
        if (initgroups("player", 1000) || setgid(1000) || setuid(1000)) {
            printf("Error dropping privileges\n");
            exit(1);
        }
    }
}

int main() {
    puts("This is the cake challenge\n");

    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = reap;
    sa.sa_flags = SA_RESTART | SA_NOCLDSTOP;
    sigaction(SIGCHLD, &sa, NULL);

    int listen_sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (listen_sockfd < 0) {
        printf("Error creating socket\n");
        return 1;
    }

    int option_value = 1;
    setsockopt(listen_sockfd, SOL_SOCKET, SO_REUSEADDR, &option_value, sizeof(option_value));

    struct sockaddr_in server_address = {
        .sin_family = AF_INET,
        .sin_port = htons(4242),
        .sin_addr.s_addr = htonl(INADDR_ANY)
    };

    if(bind(listen_sockfd, (struct sockaddr *) &server_address, sizeof(server_address)) < 0) {
        printf("Error binding socket\n");
        return 1;
    }

    if (listen(listen_sockfd, 100) < 0) {
        printf("Error listening socket\n");
        return 1;
    }

    while(1) {
        int client_sockfd = accept(listen_sockfd, NULL, NULL);
        if (client_sockfd < 0) {
            printf("Error accepting client\n");
            return 1;
        }

        printf("Client connected\n");

        int pid = fork();

        if (pid < 0) {
            printf("Error forking\n");
            return 1;
        } else if (pid == 0) {
            // child process
            close(listen_sockfd);
            drop_privileges();

            welcome(client_sockfd);

            char* message = "Still alive...\n";
            write(client_sockfd, message, strlen(message));
            close(client_sockfd);

            printf("Client disconnected\n");
            return 0;
        } else {
            // parent process
            close(client_sockfd);
        }
    }
}
