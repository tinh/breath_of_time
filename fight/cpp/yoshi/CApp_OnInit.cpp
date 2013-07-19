#include "CApp.h"

/*
**	SDL_SetVideoMode : creats a window. third argument could support some flgas example :
**	SDL_HWSURFACE : use hardware memory for storing images;
** 	SDL_DOUBLEBUF : tells sdl to (not flickering on the scree ?);
** 	SDL_FULLSCREEN : sets fullscreen;
*/

bool	CApp::OnInit(){

	if (SDL_Init(SDL_INIT_EVERYTHING) < 0)
		return (false);
	if (!(Surf_Display = SDL_SetVideoMode(640, 480, 16, SDL_HWSURFACE | SDL_DOUBLEBUF)))
		return (false);
	if (!(Surf_Yoshi = CSurface::OnLoad("yoshi.bmp")))
		return (false);

	CSurface::Transparent(Surf_Yoshi, 255, 0, 255);
	
	Anim_Yoshi.MaxFrames = 8;
	Anim_Yoshi.Oscillate = true;
	return (true);
}