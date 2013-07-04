SRCS		=	CApp.cpp \
				OnInit.cpp \
				OnEvent.cpp \
				OnLoop.cpp \
				OnRender.cpp \
				OnCleanup.cpp 

OBJ			=	$(SRCS:.cpp=.o)

CC			=	g++

NAME		=	template

CFLAGS		=	-W -Wall -Wextra

RM			=	rm -f

all:			$(NAME)

$(NAME):		$(OBJ)
				$(CC) -o $(NAME) $(OBJ) -lSDLmain -lSDL

clean:
				$(RM) $(OBJ)

fclean:			clean
				$(RM) $(NAME)

re:				fclean all

.PHONY:			all $(NAME) clean fclean re