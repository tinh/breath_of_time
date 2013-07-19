#ifndef 	_CAPP_H_
# define	_CAPP_H_

#include <SDL/SDL.h>

#include "CSurface.h"
#include "CAnimation.h"
#include "CEvent.h"

class CApp : public CEvent {
	private:
		bool		Runing;

		SDL_Surface	*Surf_Display;

		SDL_Surface	*Surf_Yoshi;

	public:
		CApp();
		
		CAnimation	Anim_Yoshi;
		int			OnExecute();

	public:
		bool		OnInit();
		
		void		OnEvent(SDL_Event *Event);
			void		OnExit();
		
		void		OnLoop();
		
		void		OnRender();
		
		void		OnCleanup();
};

#endif		/* !_CAPP_H_ */
