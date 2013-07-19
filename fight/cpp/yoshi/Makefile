SRCS		=	CApp.cpp \
				CApp_OnInit.cpp \
				CApp_OnLoop.cpp \
				CApp_OnRender.cpp \
				CApp_OnCleanup.cpp  \
				CSurface.cpp \
				CApp_OnEvent.cpp \
				CEvent.cpp \
				CAnimation.cpp

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