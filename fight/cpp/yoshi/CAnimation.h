#ifndef 	_CANIMATION_H_
# define	_CANIMATION_H_

#include <SDL/SDL.h>

class CAnimation
{
	private:
		int		CurrentFrame;
		int		FrameInc;

	private:
		int		FrameRate;
		long	OldTime;

	public:
		int		MaxFrames;
		bool	Oscillate;

	public:
		CAnimation();
		void		OnAnimate();

	public:
		void		SetFrameRate(int Rate);
		void		SetCurrentFrame(int Frame);
		int			GetCurrentFrame();
};

#endif		/* !_CANIMATION_H_ */