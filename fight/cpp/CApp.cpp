#include "CApp.h"


CApp::CApp(){
	Surf_Display = NULL;

	Runing = true;
}

int			CApp::OnExecute(){

SDL_Event	Event;

	if (OnInit() == false)
		return (-1);

	while (Runing){
		while (SDL_PollEvent(&Event)){
			OnEvent(&Event);
		}
		OnLoop();
		OnRender();
	}
	OnCleanup();

	return (0);
}

int 		main(){
	CApp	theApp;

	return (theApp.OnExecute());
}