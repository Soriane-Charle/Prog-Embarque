/************************************************************************/
/*																		*/
/*	Eight_LED.cpp		--		Definition for 8LED library 	  		*/
/*																		*/
/************************************************************************/
/*	Author:		Eric Marsh												*/
/*	Copyright 2016, Digilent Inc.										*/
/************************************************************************/
/*  File Description:													*/
/*		This file defines functions for the Pmod8LED					*/
/*																		*/
/************************************************************************/
/*  Revision History:													*/
/*																		*/
/*	8/8/2016(EricM): created											*/
/*																		*/
/************************************************************************/


/* ------------------------------------------------------------ */
/*				Include File Definitions						*/
/* ------------------------------------------------------------ */
#include "Eight_LED.h"
#include <WProgram.h>


/* ------------------------------------------------------------ */
/*				Procedure Definitions							*/
/* ------------------------------------------------------------ */


/* ------------------------------------------------------------ */
/*        8LED::8LED
**
**        Synopsis:
**				
**        Parameters:
**
**
**
**        Return Values:
**                void 
**
**        Errors:
**
**
**        Description:
**			Class constructor. Performs variables initialization tasks
**
**
*/
eightLED::eightLED()
{
	LEDArray = {-1, -1, -1, -1, -1, -1, -1, -1};
}

/* ------------------------------------------------------------ */
/*        8LED::begin
**
**        Synopsis:
**				8LED.begin(32);
**        Parameters:
**				int pin1 - the first LED pin number.
**
**        Return Values:
**                void 
**
**        Errors:
**
**
**        Description:
**				This function initializes the LED pins on the Pmod8LED
**
*/
void eightLED::begin(int pin1)
{
		for(int i = 0; i < 8; i++){
			LEDArray[i] = pin1 + i;
			pinMode(LEDArray[i], OUTPUT);
		}
		Clear();
}

/* ------------------------------------------------------------ */
/*        LED::TurnOn
**
**        Synopsis:
**				LED.TurnOn(0);
**        Parameters:
**				- int LED - the LED on PmodLED to light up (0-7)
**        Return Values:
**                void
**
**        Errors:
**
**
**        Description:
**				Turns on LED
**
**
*/
void eightLED::TurnOn(int LED)
{
	digitalWrite(LEDArray[LED], HIGH); 
}

/* ------------------------------------------------------------ */
/*        LED::TurnOff
**
**        Synopsis:
**				LED.TurnOff(0);
**        Parameters:
**				- int LED - the LED on PmodLED to turn off (0-7)
**        Return Values:
**                void
**
**        Errors:
**
**
**        Description:
**				Turns off LED
**
**
*/
void eightLED::TurnOff(int LED)
{
	digitalWrite(LEDArray[LED], LOW); 
}

/* ------------------------------------------------------------ */
/*         8LED::Clear
**
**        Synopsis:
**				 8LED.Clear();
**        Parameters:
**
**        Return Values:
**                void
**
**        Errors:
**
**
**        Description:
**				Turns off all LEDs
**
**
*/
void eightLED::Clear()
{
	for(int i = 0; i < 8; i++){
		digitalWrite(LEDArray[i], LOW); 
	}
}