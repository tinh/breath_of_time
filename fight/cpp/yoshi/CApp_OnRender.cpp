#include "CApp.h"

void	CApp::OnRender(){
	CSurface::OnDraw(Surf_Display, Surf_Yoshi, 290, 220, 0, Anim_Yoshi.GetCurrentFrame() * 64, 64, 64);

	SDL_Flip(Surf_Display);
}