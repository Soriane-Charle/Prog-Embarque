/************************************************************************/
/*																		*/
/*	Eight_LED.h	--	Declaration for 8LED library 	  			  		*/
/*																		*/
/************************************************************************/
/*	Author:		Eric Marsh												*/
/*	Copyright 2016, Digilent Inc.										*/
/************************************************************************/
/*  File Description:													*/
/*	This file declares the Pmod8LED library functions and the constants	*/
/*	involved.															*/
/*																		*/
/************************************************************************/
/*  Revision History:													*/
/*																		*/
/*	8/8/2016(EricM): created											*/
/*																		*/
/************************************************************************/
#if !defined(Eight_LED_H)
#define Eight_LED_H

/* ------------------------------------------------------------ */
/*					Procedure Declarations						*/
/* ------------------------------------------------------------ */


class eightLED {

	private: 
		int LEDArray[8];
		
	public:
		eightLED ();
		void begin(int pin1);
		void TurnOn(int LED);
		void TurnOff(int LED);
		void Clear();
};

#endif
