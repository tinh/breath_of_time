#ifndef _CSURFACE_H_
# define _CSURFACE_H_

#include <SDL/SDL.h>

class CSurface {

	public:
		CSurface();	

	public:
		static SDL_Surface *OnLoad(char *);
		static bool OnDraw(SDL_Surface *Dest, SDL_Surface *Src, int X, int Y);
		static bool OnDraw(SDL_Surface *Dest, SDL_Surface *Src, int X, int Y, int X2, int Y2, int W, int H);
};

#endif	/* !_CSURFACE_H_ */